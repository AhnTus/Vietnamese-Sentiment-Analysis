import pyodbc
from function.User_file import User
class UserDao:
    
    def check_login(self,user:User):
        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=MSI;DATABASE=SalesPhone;Trusted_Connection=yes')
        cursor = conn.cursor()
        cursor.execute("EXEC CheckLogin @Username=?, @Password=?", (user.getUserName,user.getPassWord))
        login_success = cursor.fetchone()[0]  
        conn.close()
        return login_success
    def get_full_name(self,user:User):
        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=MSI;DATABASE=SalesPhone;Trusted_Connection=yes')
        cursor = conn.cursor()
        cursor.execute(f"select full_name From users join comment on comment.user_id=users.id where comment = N'{user.getComment}'")
        user_row = cursor.fetchone()
        conn.close()
        return user_row[0] if user_row else None
    def get_user_id(self,user:User):
        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=MSI;DATABASE=SalesPhone;Trusted_Connection=yes')
        cursor = conn.cursor()
        cursor.execute(f"SELECT DISTINCT(id) FROM users WHERE username = '{user.getUserName}'")
        user_row = cursor.fetchone()
        conn.close()
        return user_row[0] if user_row else None
