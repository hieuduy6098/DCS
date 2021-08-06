import time
import random
import json
from paho.mqtt import client as mqtt_client
import mysql.connector
import queue
import threading
q=queue.Queue(maxsize=0)

def generateData(id) :
  lineData = {
    "id": "L" + str(id),
    "time" : time.time(),
    "data" : [
      {"idmay": "M1","tocDo":random.randrange(0,100), "hieuSuat" : random.randrange(0,100), "sanLuong" : random.randrange(0,100), "soGoiBiCan" : random.randrange(0,100), "ptgoiBiCan" : random.randrange(0,100), "soGoiRong" : random.randrange(0,100), "ptgoiRong" : random.randrange(0,100),},
      {"idmay": "M2","tocDo":random.randrange(0,100), "hieuSuat" : random.randrange(0,100), "sanLuong" : random.randrange(0,100), "soGoiBiCan" : random.randrange(0,100), "ptgoiBiCan" : random.randrange(0,100), "soGoiRong" : random.randrange(0,100), "ptgoiRong" : random.randrange(0,100),},
      {"idmay": "M3","tocDo":random.randrange(0,100), "hieuSuat" : random.randrange(0,100), "sanLuong" : random.randrange(0,100), "soGoiBiCan" : random.randrange(0,100), "ptgoiBiCan" : random.randrange(0,100), "soGoiRong" : random.randrange(0,100), "ptgoiRong" : random.randrange(0,100),},
    ],
  }
  lineDataJson = json.dumps(lineData)
  #print(lineDataJson)

  return str(lineDataJson)
broker = '27.71.227.145'
port = 1883
topic = "dcsData"
# generate client ID with pub prefix randomly
client_id = 'publicDcs'
username = ''
password = ''

def connect_mqtt():
  def on_connect(client, userdata, flags, rc):
    if rc == 0:
      print("Connected to MQTT Broker!")
    else:
      print("Failed to connect, return code %d\n", rc)

  client = mqtt_client.Client(client_id)
  client.username_pw_set(username, password)
  client.on_connect = on_connect
  client.connect(broker, port)
  return client

def publish(client):
  while True:
    msg1=generateData(1)
    client.publish(topic, msg1)
    #msg1 = json.dumps(msg1)
    q.put(msg1)
    time.sleep(3)
    msg2=generateData(2)
    client.publish(topic, msg2)
    #msg2 = json.dumps(msg2)
    q.put(msg2)
    #print(msg1)
    print("finish public")
    time.sleep(3)

def connectSql():
  while True:
    conn = mysql.connector.connect(host='localhost', user='root', password='',database='localdcsdata')
    cur = conn.cursor()
    sql = ("INSERT INTO datamaylocal (idmay, idline, time, tocdo, hieusuat, sanluong, sogoibican, ptgoibican, sogoirong, ptgoirong)" + "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
    
    data=q.get()
    data = json.loads(data)
    print(data)
    
    value1=(
      data["data"][0]["idmay"],
      data["id"],
      data["time"],
      data["data"][0]["tocDo"],
      data["data"][0]["hieuSuat"],
      data["data"][0]["sanLuong"],
      data["data"][0]["soGoiBiCan"],
      data["data"][0]["ptgoiBiCan"],
      data["data"][0]["soGoiRong"],
      data["data"][0]["ptgoiRong"]
    )
    value2=(
      data["data"][1]["idmay"],
      data["id"],
      data["time"],
      data["data"][1]["tocDo"],
      data["data"][1]["hieuSuat"],
      data["data"][1]["sanLuong"],
      data["data"][1]["soGoiBiCan"],
      data["data"][1]["ptgoiBiCan"],
      data["data"][1]["soGoiRong"],
      data["data"][1]["ptgoiRong"]
    )
    value3=(
      data["data"][2]["idmay"],
      data["id"],
      data["time"],
      data["data"][2]["tocDo"],
      data["data"][2]["hieuSuat"],
      data["data"][2]["sanLuong"],
      data["data"][2]["soGoiBiCan"],
      data["data"][2]["ptgoiBiCan"],
      data["data"][2]["soGoiRong"],
      data["data"][2]["ptgoiRong"]
    )
    
    #print(value)
    cur.execute(sql, value1)
    cur.execute(sql, value2)
    cur.execute(sql, value3)

    conn.commit()
    print("finish insert")
    #time.sleep(2)
    
    conn.close()

def contactMQTT():
  client=connect_mqtt()
  publish(client)

if __name__ == '__main__':
  t1=threading.Thread(target=contactMQTT).start()
  t2=threading.Thread(target=connectSql).start()

