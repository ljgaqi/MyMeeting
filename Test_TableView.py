import sys
from PyQt5.QtSql import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Test_TableView(QWidget):
    def __init__(self, parent=None):
        super(Test_TableView, self).__init__(parent)
        self.setWindowTitle("TableView连接数据库窗口")
        self.resize(800, 600)

        self.connectDB()
        self.searchDB()
        self.createTable()

    def connectDB(self):
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('./meeting.db')
        self.db.open()

    def searchDB(self):
        # self.model = QSqlTableModel()
        # self.model.setTable('DateMeeting')
        # self.model.select()
        self.model = QSqlQueryModel()
        self.model.setQuery("select * from DateMeeting where datetime > '2021-09-28 8:00:00:000' and datetime < '2021-10-22 8:00:00:000' and room = '会议室一' order by datetime")

    def createTable(self):
        self.tableview = QTableView()
        self.tableview.setModel(self.model)
        layout = QVBoxLayout()
        layout.addWidget(self.tableview)
        self.setLayout(layout)




if __name__=="__main__":
    app = QApplication(sys.argv)
    table = Test_TableView()
    table.show()
    sys.exit(app.exec_())