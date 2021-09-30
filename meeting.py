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
        self.pushButton1.clicked.connect(self.SearchMeeting)
        self.pushButton2.clicked.connect(self.insertDB)

        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('./meeting.db')
        self.db.open()

        # self.model = QSqlTableModel()
        # self.model.setTable('DateMeeting')
        # self.model.select()
        # self.model.setEditStrategy(QSqlTableModel.OnFieldChange)

        self.model = QSqlQueryModel()
        self.model.setQuery("select * from DateMeeting")

        self.model.setHeaderData(0, Qt.Horizontal, '序号')
        self.model.setHeaderData(1, Qt.Horizontal, '会议名称')
        self.model.setHeaderData(2, Qt.Horizontal, '会议时间')
        self.model.setHeaderData(3, Qt.Horizontal, '会议室')
        self.model.setHeaderData(4, Qt.Horizontal, '中介名称')
        self.model.setHeaderData(5, Qt.Horizontal, '项目类型')

        self.tableView.setModel(self.model)


        self.tableView.setColumnWidth(0, 140)
        self.tableView.setColumnWidth(1, 400)
        self.tableView.setColumnWidth(2, 200)
        self.tableView.setColumnWidth(3, 80)
        self.tableView.setColumnWidth(4, 80)
        self.tableView.setColumnWidth(5, 80)

    def SearchMeeting(self):
        begindate = self.dateEdit1.date().toString(Qt.ISODate)
        begintime = self.timeEdit1.time().toString()
        enddate = self.dateEdit2.date().toString(Qt.ISODate)
        endtime = self.timeEdit2.time().toString()
        begin = begindate + " " + begintime
        end = enddate + " " + endtime

        print(begin, end)

    def format_datetime(self):
        today = datetime.date.today()
        self.dateEdit1.setDate(today)
        self.dateEdit2.setDate(today + datetime.timedelta(days=1))

    def insertDB(self):
        self.insertDialog = insertDialog()
        self.insertDialog.signalAddMeeting.connect(self.Insert_Date_DB)
        self.insertDialog.show()

    def Insert_Date_DB(self, date_list):
        print(date_list)
        quary = QSqlQuery()
        quary.prepare("Insert into DateMeeting (no,name,datetime,room,company,type) values (?,?,?,?,?,?)")

        for list in date_list:
            quary.addBindValue(list)

        quary.exec()
        self.db.commit()

        QMessageBox.about(self, "注意", "会议日程添加成功")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = meeting()
    main.show()
    sys.exit(app.exec_())
