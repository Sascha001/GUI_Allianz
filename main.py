import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtCore import pyqtSlot, QFile, QTextStream

from UI_ui import Ui_MainWindow


class MaindWindow(QMainWindow):
    def __init__(self):
        super(MaindWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.icon_menu.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.mainDashboard_2.setChecked(True)

    # function for searching
    def on_search_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(4)
        search_text = self.ui.search_input.text().strip()
        if search_text:
            self.ui.label_8.setText(search_text)

    # function for changing page to user page
    def on_profile_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(5)

    # change button checkable status when stackedWidget index changed
    def on_stackedWidget_currentChanged(self, index):
        btn_list = self.ui.icon_menu.findChildren(QPushButton) \
                    + self.ui.full_menu.findChildren(QPushButton)
        for btn in btn_list:
            if index in [4,5]:
                btn.setAutoExclusive(False)
                btn.setChecked(False)
            else:
                btn.setAutoExclusive(True)

    # functions for changing menu pages
    def on_mainDashboard_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_mainDashboard_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_orderOverview_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_orderOverview_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_recommendation_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_recommendation_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_history_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_history_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(3)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # loading style file
    with open("style.css", "r") as style_file:
        style_str = style_file.read()

    app.setStyleSheet(style_str)

    window = MaindWindow()
    window.show()

    sys.exit(app.exec())