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
        # self.pushButton1.clicked.connect(self.formate_tableview)

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

        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('./meeting.db')
        self.db.open()

        self.tableView.setModel(self.model)


    def format_datetime(self):
        today=datetime.date.today()
        self.dateEdit1.setDate(today)
        self.dateEdit2.setDate(today+datetime.timedelta(days=1))

        
if __name__=="__main__":
    app=QApplication(sys.argv)
    main=meeting()
    main.show()
    sys.exit(app.exec_())