import datetime
import sys
import time
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
        self.dateEdit.setDate(datetime.date.today())
    def format_date(self):
        datestr = self.dateEdit.date().toString(Qt.ISODate)
        roomstr = self.comboBox.currentText()
        namestr = self.lineEdit.text()
        timestr = self.comboBox_3.currentText()
        typestr = self.comboBox_2.currentText()
        comestr = self.lineEdit_2.text()
        self.datelist = [datestr+" "+timestr+":00:000", namestr, roomstr, comestr, typestr]
        # print(datelist)
    def accept(self):
        if self.lineEdit.text() == "":
            QMessageBox.about(self, "注意", "项目名称不能为空！")
        elif self.lineEdit_2.text() == "":
            QMessageBox.about(self, "注意", "中介机构名称不能为空！")
        else:
            self.format_date()
            self.signalAddMeeting.emit(self.datelist)
            self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = insertDialog()
    form.show()
    sys.exit(app.exec_())