from PyQt5.QtWidgets import QWidget, QApplication, QDialog

from PyQt5.QtCore import pyqtSlot, Qt, pyqtSignal

from UI.Ui_colorDialog import Ui_Dialog

import matplotlib.pyplot as plt


class ColorDialog(QDialog):
    color_sig = pyqtSignal(str)

    def __init__(self, parent=None):
        super(ColorDialog, self).__init__(parent)
        self.UI = Ui_Dialog()
        self.UI.setupUi(self)

    @pyqtSlot()
    def on_btn_cancel_clicked(self):
        self.UI.comboBox.setCurrentIndex(0)

    @pyqtSlot()
    def on_btn_confirm_clicked(self):
        cmap = self.UI.comboBox.currentText()
        self.color_sig.emit(cmap)
        self.close()



if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    win = ColorDialog()
    win.show()
    sys.exit(app.exec())
