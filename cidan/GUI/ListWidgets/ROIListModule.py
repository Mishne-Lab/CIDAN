from qtpy import QtCore
from qtpy.QtGui import *
from qtpy.QtWidgets import *

from cidan.GUI.ListWidgets.ROIItemModule import ROIItemModule
from cidan.GUI.ListWidgets.ROIItemWidget import ROIItemWidget


class ROIListModule(QFrame):
    """
    Its the roi list in the ROI modification tab
    """

    def __init__(self, data_handler, roi_tab, select_multiple=False, display_time=True):
        super().__init__()
        self.current_selected_roi = 0
        self.select_multiple = select_multiple
        self.display_time = display_time
        self.roi_tab = roi_tab
        self.color_list = data_handler.color_list
        self.list = QListView()

        self.setStyleSheet("QListView::item { border-bottom: 1px solid rgb(50, 65, " +
                           "75); } " + """QListView::item::pressed,
 {
  background-color: #19232D;
  border: 1px solid #32414B;
  color: #F0F0F0;
  gridline-color: #32414B;
  border-radius: 4px;
}""")
        self.top_labels_layout = QHBoxLayout()
        self.top_labels_layout.setContentsMargins(0, 0, 0, 0)
        label1 = QLabel(text="ROI Selected")
        label1.setMaximumWidth(170 * ((self.logicalDpiX() / 96.0)))
        self.top_labels_layout.addWidget(label1, alignment=QtCore.Qt.AlignRight)
        label2 = QLabel(text="ROI Num")
        label2.setMaximumWidth(140 * ((self.logicalDpiX() / 96.0)))
        self.top_labels_layout.addWidget(label2, alignment=QtCore.Qt.AlignLeft)
        self.top_labels_layout.addWidget(QLabel(), alignment=QtCore.Qt.AlignRight)
        self.top_labels_layout.addWidget(QLabel(), alignment=QtCore.Qt.AlignRight)
        self.top_labels_layout.addWidget(QLabel(), alignment=QtCore.Qt.AlignRight)
        self.top_labels_layout.addWidget(QLabel(), alignment=QtCore.Qt.AlignRight)
        if display_time:
            label3 = QLabel(text="Time Trace On")
            label3.setMaximumWidth(100*((self.logicalDpiX() / 96.0-1)/2+1))
            self.top_labels_layout.addWidget(label3, alignment=QtCore.Qt.AlignRight)
        self.setMinimumHeight(200 * ((self.logicalDpiX() / 96.0 - 1) / 2 + 1))
        self.model = QStandardItemModel(self.list)
        self.list.setModel(self.model)
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addLayout(self.top_labels_layout)
        self.layout.addWidget(self.list)
        self.roi_item_list = []
        self.setLayout(self.layout)

    def keyPressEvent(self, event):
        self.roi_tab.keyPressEvent(event)
    def set_current_select(self, num):
        self.list.setCurrentIndex(self.model.index(int(num - 1), 0))
        self.roi_time_check_list[num - 1] = not self.roi_time_check_list[num - 1]
        self.roi_item_list[num - 1].select_check_box()
        # self.roi_module_list[num-1].
        if self.display_time:
            self.roi_item_list[num - 1].select_time_check_box()

    def set_list_items(self, rois):
        self.roi_list = rois
        for x in range(self.model.rowCount()):
            self.model.removeRow(0)
        self.roi_item_list = []
        self.roi_module_list = []
        for num in range(len(self.roi_list)):
            item = ROIItemWidget(self.roi_tab,
                                 self.color_list[num % len(self.color_list)], self,
                                 num + 1, display_time=self.display_time
                                 )
            item1 = ROIItemModule(self.color_list[num % len(self.color_list)], num + 1,
                                  self.roi_tab)
            item1.setSelectable(False)
            self.roi_item_list.append(item)
            self.model.appendRow(item1)
            self.roi_module_list.append(item1)
            self.list.setIndexWidget(item1.index(), item)
        self.roi_time_check_list = [False] * len(self.roi_item_list)
        if hasattr(self.roi_tab, "tab_selector_roi"):
            self.roi_tab.tab_selector_roi.setCurrentIndex(1)
        # self.roi_item_list[0].select_check_box()
        # self.roi_item_list[0].select_time_check_box()
    # def change(self):
    #     # This is a way of running the select roi function when a checkbox is clicked there
    #     # needed to be a work around because can't just connect a signal to it
    #     for num, item, check_val in zip(range(1,len(self.roi_time_check_list)+1),self.roi_item_list,self.roi_time_check_list):
    #         if item.checkState() != check_val:
    #             self.roi_time_check_list[num-1] = item.checkState()
    #             if item.checkState():
    #                 self.roi_tab.selectRoi(num)
    #             else:
    #                 self.roi_tab.deselectRoi(num)
