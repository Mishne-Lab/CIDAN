from PySide2.QtWidgets import *
import sys
import qdarkstyle
from GUI.SettingBlockModule import *

class SettingsModule(QFrame):
    def __init__(self, name, *args, show_name=True):
        super().__init__()

        self.setStyleSheet("SettingsModule { border:1px solid rgb(50, 65, "
                           "75);} ")
        self.setting_block_list = args
        self.layout = QVBoxLayout()
        if show_name:
            self.header = QLabel()
            self.header.setText(name)
            self.header.setStyleSheet("font-size: 20px")
            self.layout.addWidget(self.header)
        self.setting_block_layout = QToolBox()
        for block in self.setting_block_list:
            self.setting_block_layout.addItem(block, block.name)
        self.layout.addWidget(self.setting_block_layout)
        self.setLayout(self.layout)
def preprocessing_settings(main_widget):
    return SettingsModule( "Preprocessing Settings", dataset_setting_block(main_widget),
                          filter_setting_block(main_widget))
def roi_extraction_settings(main_widget):
    return SettingsModule( "ROI Extraction Settings", multiprocessing_settings_block(main_widget), roi_extraction_settings_block(main_widget), show_name=False)
if __name__ == "__main__":
    app = QApplication([])

    widget = preprocessing_settings()
    widget.setStyleSheet(qdarkstyle.load_stylesheet())
    widget.show()


    sys.exit(app.exec_())