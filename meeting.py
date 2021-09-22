import sys
import datetime
import time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtSql import *
from Meeting_Main import Ui_MainWindow

from insertDialog import insertDialog

class meeting(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(meeting, self).__init__(parent)
        self.setupUi(self)
        self.format_datetime()

        self.pushButton2.clicked.connect(self.insertDB)

        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('./meeting.db')
        self.db.open()

        self.model = QSqlTableModel()
        self.model.setTable('DateMeeting')
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.select()
        self.model.setHeaderData(0, Qt.Horizontal, '序号')
        self.model.setHeaderData(1, Qt.Horizontal, '会议名称')
        self.model.setHeaderData(2, Qt.Horizontal, '会议时间')
        self.model.setHeaderData(3, Qt.Horizontal, '会议室')
        self.model.setHeaderData(4, Qt.Horizontal, '中介名称')
        self.model.setHeaderData(5, Qt.Horizontal, '项目类型')

        self.tableView.setModel(self.model)

        self.tableView.setColumnWidth(0, 40)
        self.tableView.setColumnWidth(1, 400)
        self.tableView.setColumnWidth(2, 200)
        self.tableView.setColumnWidth(3, 100)
        self.tableView.setColumnWidth(4, 100)
        self.tableView.setColumnWidth(4, 100)


    def format_datetime(self):
        today = datetime.date.today()
        self.dateEdit1.setDate(today)
        self.dateEdit2.setDate(today + datetime.timedelta(days=1))

    def insertDB(self):
        self.insertDialog=insertDialog()
        self.insertDialog.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = meeting()
    main.show()
    sys.exit(app.exec_())
