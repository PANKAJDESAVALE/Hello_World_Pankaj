import sqlite3

con=sqlite3.connect("mydb.db")

cur=con.cursor()

#cur.execute("create table student(id  INT,name  TEXT)")

#cur.execute("insert into student(id,name)values(101,'pankaj')")

#cur.execute("insert into student(id,name)values(?,?)",(199,"XYZ"))

#list=[(103,"pqr"),(104,"SWERD"),(105,"qwerty")]

#cur.executemany("insert into student(id,name)values(?,?)",list)

#data=cur.execute("select * from student")
#print(data)
#for i in data:
    #print(i[0],i[1])

#cur.execute("select * from student")
#data=cur.fetchall()

#for i in data:
    #print(i[0],i[1])

#cur.execute("select * from student where id=101")
#data=cur.fetchone()
#print(data)

#cur.execute("update student set name='DESAVALE' where id=101")

#cur.execute("delete from student where id=104")

#cur.execute("delete from student where id=?",[199])

cur.execute("update student set name=? where id=?",("TATA",105))

con.commit()

con.close()