import sys
import datetime
import time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtSql import *
from Meeting_Main import Ui_MainWindow


class meeting(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super(meeting,self).__init__(parent)
        self.setupUi(self)
        self.format_datetime()
        # self.tableView.horizontalHeader().setStretchLastSection(True)    # 充满整个表格框
        # self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)   #根据需要，分配各行长度
        self.pushButton1.clicked.connect(self.formate_tableview)
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

    def meeting_search(self):
        pass

    def formate_tableview(self):
        # headtitle=['序号','会议名称','会议时间','会议室名称','中介名称','项目类型']
        # self.Girdmodel=QStandardItemModel(6,6)
        # self.Girdmodel.setHorizontalHeaderLabels(headtitle)
        self.model=QSqlTableModel()
        self.tableView.setModel(self.model)
        self.model.setTable('DateMeeting')
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.select()


        # self.model.setHeaderData(0, '序号')
        # self.model.setHeaderData(1,'会议名称')
        # self.model.setHeaderData(2,'会议时间')
        # self.model.setHeaderData(3,'会议室名称')
        # self.model.setHeaderData(4,'中介名称')
        # self.model.setHeaderData(5, '项目类型')


        
if __name__=="__main__":
    app=QApplication(sys.argv)
    main=meeting()
    main.show()
    sys.exit(app.exec_())