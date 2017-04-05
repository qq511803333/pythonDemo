import pymysql

con = pymysql.connect(
    user='root',
    password='guang888',
    host='localhost',
    database='mydatabase'
)
db = con.cursor()
sql = "insert into train (data) VALUES ('1111')";
db.execute(sql)
# result = db.fetchall();
# print(result)
con.commit()
con.close()
