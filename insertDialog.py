import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from InserMeeting import Ui_Dialog

class insertDialog(QDialog,Ui_Dialog):

    signalAddMeeting = pyqtSignal(list)

    def __init__(self, parent=None):
        super(insertDialog, self).__init__(parent)
        self.setupUi(self)
        self.buttonBox.button(QDialogButtonBox.Ok).setText('确定')
        self.buttonBox.button(QDialogButtonBox.Cancel).setText('取消')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = insertDialog()
    form.show()
    sys.exit(app.exec_())