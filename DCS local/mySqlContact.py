import json
import mysql.connector

def contactSql(q1,q2):
  dataQuece1 = json.loads(q1.get())
  dataQuece2 = json.loads(q2.get())
  print(dataQuece1)
  print(type(dataQuece1))
  data1 = (
    dataQuece1.data.idmay,
    dataQuece1.id,
    dataQuece1.time,
    dataQuece1.data.hieusuat,
    dataQuece1.data.sanluong,
    dataQuece1.data.sogoibican,
    dataQuece1.data.ptgoibican,
    dataQuece1.data.sogoirong,
    dataQuece1.data.ptgoirong
  )
  data2 = (
    dataQuece2.data.idmay,
    dataQuece2.id,
    dataQuece2.time,
    dataQuece2.data.hieusuat,
    dataQuece2.data.sanluong,
    dataQuece2.data.sogoibican,
    dataQuece2.data.ptgoibican,
    dataQuece2.data.sogoirong,
    dataQuece2.data.ptgoirong
  )
  #establishing the connection
  conn = mysql.connector.connect(host='localhost', user='root', password='' , database='dcsdata')

  #Creating a cursor object using the cursor() method
  cursor = conn.cursor()

  # Preparing SQL query to INSERT a record into the database.
  sql = """INSERT INTO datamay (idmay, idline, time, hieusuat, sanluong, sogoibican, ptgoibican, sogoirong, ptgoirong) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
  try:
    # Executing the SQL command
    cursor.execute(sql,data1)
    cursor.execute(sql,data2)

    # Commit your changes in the database
    conn.commit()
    print("finish insert data to database")

  except:
    # Rolling back in case of error
    conn.rollback()

  # Closing the connection
  conn.close()


if __name__ == '__main__':
  contactSql()