import sys
import datetime
import time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtSql import *
from Meeting_Main import Ui_MainWindow
from datebase import database


class meeting(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super(meeting,self).__init__(parent)
        self.setupUi(self)
        self.format_datetime()
        # self.tableView.horizontalHeader().setStretchLastSection(True)    # 充满整个表格框
        # self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)   #根据需要，分配各行长度
        self.pushButton1.clicked.connect(self.meeting_search)
        self.connect_datebase()
        self.formate_tableview()

    def format_datetime(self):
        today=datetime.date.today()
        self.dateEdit1.setDate(today)
        self.dateEdit2.setDate(today+datetime.timedelta(days=1))

    def connect_datebase(self):
        self.meetingdb=QSqlDatabase.addDatabase('SQLITE')
        self.meetingdb.setDatabaseName('./meeting.db')
        self.meetingdb.open()


    def formate_tableview(self):
        headtitle=['序号','会议名称','会议时间','会议室名称','中介名称','项目类型']
        self.Girdmodel=QStandardItemModel(6,6)
        self.Girdmodel.setHorizontalHeaderLabels(headtitle)
        self.Girdmodel.setTable('DateMeeting')

        
if __name__=="__main__":
    app=QApplication(sys.argv)
    main=meeting()
    main.show()
    sys.exit(app.exec_())