import pyodbc
from function.Comment_file import Comment
from function.User_file import User
class CommentDao:
    def insert_comment(self,user:User,comment:Comment):
            if user.getUserId !=None:
                conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=MSI;DATABASE=SalesPhone;Trusted_Connection=yes')
                cursor = conn.cursor()
                cursor.execute("INSERT INTO comment (user_id, comment) VALUES (?, ?)",(user.getUserId,comment.getComment))
                conn.commit() 
                conn.close()
            else:
                print("User not found.")
    def get_comment_by_user(self):
        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=MSI;DATABASE=SalesPhone;Trusted_Connection=yes')
        cursor = conn.cursor()
        cursor.execute("SELECT id,comment FROM comment")
        comments = cursor.fetchall()
        return comments
    def get_comment_id_by_user(self):
        conn=pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=MSI;DATABASE=SalesPhone;Trusted_Connection=yes')
        cursor=conn.cursor()
        cursor.execute(f"select top 1 id From comment order by id desc")
        comment_id=cursor.fetchone()
        return comment_id [0] if comment_id else None
    def statistical(self):
        conn=pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=MSI;DATABASE=SalesPhone;Trusted_Connection=yes')
        cursor=conn.cursor()
        cursor.execute(f"""SELECT 
                        phone.phone_name,
                        COUNT(CASE WHEN comment.predict = 'Positive' THEN 1 END) AS number_of_positives,
                        COUNT(CASE WHEN comment.predict = 'Negative' THEN 1 END) AS number_of_negatives,
                        COUNT(CASE WHEN comment.predict = 'Neutral' THEN 1 END) AS number_of_neutrals
                    FROM 
                        phone 
                    JOIN 
                        comment_phone ON phone.id = comment_phone.id_phone 
                    JOIN 
                        comment ON comment.id = comment_phone.id_comment
                    GROUP BY 
                        phone.phone_name;
                    """)
        result = cursor.fetchall()
        return result
    def update_comment(self,comment:Comment):
        if comment !=None:
            conn=pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER=MSI;DATABASE=SalesPhone;Trusted_Connection=yes")
            cursor=conn.cursor()
            cursor.execute("Update Comment set predict = ? where id= ?",(comment.getPredict,comment.getId))
            conn.commit()
            conn.close()
        else: 
            print("Comment not found")