from random import random, randrange
import time
from mysql.connector.errors import Error
from paho.mqtt import client as mqtt_client
import json
import mysql.connector
import queue
import threading
#creat queue
q=queue.Queue(maxsize=0)

#infor mqtt broker
broker = '27.71.227.145'
port = 1883
topic = "dcsData"
client_id = 'publicDcs1'
username = ''
password = ''
#connect mqtt
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
# sub from mqtt
def subscribe(client: mqtt_client,q):
  def on_message(client, userdata, msg):
    message = json.loads(msg.payload.decode())
    q.put(message)
    #print(message)
  client.subscribe(topic)
  client.on_message = on_message
# function connect and get data from topic
def contactMqtt():
  client = connect_mqtt()
  subscribe(client,q)
  client.loop_forever()
#connect sql
def connectSql():
  while True:
    conn = mysql.connector.connect(host='localhost', user='root', password='',database='dcsdata')
    cur = conn.cursor()
    sql = ("INSERT INTO datamay (idmay, idline, time, tocdo, hieusuat, sanluong, sogoibican, ptgoibican, sogoirong, ptgoirong)" + "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
  
    data=q.get()
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
    time.sleep(2)
    conn.close()

if __name__ == '__main__':
  t1=threading.Thread(target=contactMqtt).start()
  t2=threading.Thread(target=connectSql).start()