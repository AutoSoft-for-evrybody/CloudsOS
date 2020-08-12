try:
    from PyQt5 import QtWidgets, QtSql
except ModuleNotFoundError:
    raise UserWarning("PyQt5 not installed")
from hashlib import sha1
from webbrowser import open
try:
    import pymysql
    from pymysql.cursors import DictCursor
except ModuleNotFoundError:
    raise UserWarning("pymysql not installed")
import sys
try:
    app = QtWidgets.QApplication(sys.argv)
except:
    pass

class QtConnection:
    def __init__(self, host, database="mydatabase", table="toolsid", user="root", password=""):
        
        self.connection = QtSql.QSqlDatabase.addDatabase("QMYSQL")
        self.connection.setHostName(host)
        self.connection.setDatabaseName(database)
        self.connection.setUserName(user)
        self.connection.setPassword(password)

        self.host = host
        self.database = database
        self.table = table
        self.user = user
        self.password = password
    def login(self, user, password, web_reg=True):
        password = sha1(password.encode())
        try:
            if (not self.connection.open()):
                raise ConnectionError(self.connection.lastError().text())
            query = QtSql.QSqlQuery()
            query.exec("SELECT * FROM " + self.table)
            if not query.first():
                raise UserWarning("указатель не может быть позиционирован")
            while True:
                if (not query.next()):
                    break
                arr = []
                for i in query.size():
                    arr.append(query.value(i))
                print(*arr)
            
        except:
            self.connection.close()
            raise
        finally:
            self.connection.close()
    
class PyMySqlConnection:
    def __init__(self, host, database="mydatabase", table="toolsid", user="root", password=""):
        
        

        self.host = host
        self.database = database
        self.table = table
        self.user = user
        self.password = password
    def login(self, username, password, web_reg=True):
        orig_p = password
        password = sha1(password.encode()).hexdigest()
        try:
            self.connection = pymysql.connect(database=self.database, host=self.host, user=self.user, password=self.password, cursorclass=DictCursor, charset='utf8mb4')
            self.cursor = self.connection.cursor()
            self.cursor.execute("SELECT * FROM " + self.table)
            answer = [dict([(key, str(text).replace("\r\n", "\n")) for key, text in row.items()]) for row in self.cursor]

            for i in answer:
                if i["login"] == username and i["password"] == password:
                    if (web_reg):
                        open(f"https://{self.host}/toolsid/scripts/login.php?login={username}&password={orig_p}")
                    if (i["admin"] in ["0", 0]):
                        return True
                    else:
                        return "admin"
            return False
            
        except:
            self.connection.close()
            raise
        finally:
            self.connection.close()
    def register(self, username, password, admin=False, web_reg=True):
        orig_p = password
        password = sha1(password.encode()).hexdigest()
        try:
            self.connection = pymysql.connect(database=self.database, host=self.host, user=self.user, password=self.password, cursorclass=DictCursor, charset='utf8mb4')
            self.cursor = self.connection.cursor()
            self.connection2 = pymysql.connect(database=self.database, host=self.host, user=self.user, password=self.password, cursorclass=DictCursor, charset='utf8mb4')
            self.cursor2 = self.connection2.cursor()
            self.cursor.execute("SELECT * FROM " + self.table)
            answer = [dict([(key, str(text).replace("\r\n", "\n")) for key, text in row.items()]) for row in self.cursor]

            for i in answer:
                if i["login"] == username:
                    return False
            self.cursor2.execute("INSERT INTO `"+self.table+"`(`login`, `password`, `admin`) VALUES (\""+username+"\",\""+password+"\","+("1" if admin else "0")+")")
            self.connection2.commit()
            if (web_reg):
                open(f"https://{self.host}/toolsid/scripts/login.php?login={username}&password={orig_p}")
            return True
            
        except:
            self.connection.close()
            self.connection2.close()
            raise
        finally:
            self.connection.close()
            self.connection2.close()
