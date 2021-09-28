import sys
from PyQt5.QtSql import *

db = QSqlDatabase.addDatabase('QSQLITE')
db.setDatabaseName('./meeting.db')
db.open()

datelist = ['testname','2021-09-28 9:00:00:000' ,'会议室一', 'test', '政府采购']
query = QSqlQuery()
query.prepare("Insert Into DateMeeting (name,datetime,room,company,type) values (?,?,?,?,?)")

for list in datelist:
    query.addBindValue(list)

query.exec()

db.commit()
db.close()