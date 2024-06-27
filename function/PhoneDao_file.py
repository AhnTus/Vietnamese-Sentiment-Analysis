import pyodbc
from function.Phone_file import Phone
from function.Comment_file import Comment
import pyodbc
class PhoneDao:
    def get_list_phone(self):
        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=MSI;DATABASE=SalesPhone;Trusted_Connection=yes')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM phone")
        phone_row = cursor.fetchall()
        conn.close()
        return phone_row
    def get_phone(self, phone_id):
        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=MSI;DATABASE=SalesPhone;Trusted_Connection=yes')
        cursor = conn.cursor()
        cursor.execute("SELECT id, phone_name, specifications, photo FROM phone WHERE id = ?", (phone_id))
        phone_row = cursor.fetchone()
        conn.close()
        return phone_row
    def get_id_by_phone(self,phone:Phone):
        conn=pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER=MSI;DATABASE=SalesPhone;Trusted_Connection=yes")
        cursor=conn.cursor()
        cursor.execute(f"select id From Phone where phone_name= '{phone.getPhoneName}'")
        id_phone=cursor.fetchone
        conn.close()
        return id_phone [0] if id_phone else None
    def insert_comment_phone(self,phone:Phone,comment:Comment):
            if  phone !=None:
                conn=pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER=MSI;DATABASE=SalesPhone;Trusted_Connection=yes")
                cursor=conn.cursor()
                cursor.execute("insert comment_phone(id_phone,id_comment) values (?,?)",(phone.getId,comment.getId))
                cursor.commit()
                cursor.close()
            else: 
                print("User not found")
