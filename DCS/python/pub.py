import paho.mqtt.client as mqttClient
import time
import random 
import json
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        global Connected                #Use global variable
        Connected = True                #Signal connection 
    else:
        print("Connection failed")
Connected = False   #global variable for the state of the connection
broker_address= "127.0.0.1"
port = 1883
#user = "hieu98"
#password = "100998"
client = mqttClient.Client("Python")
#client.username_pw_set(user, password=password)    #set username and password
client.on_connect= on_connect                      #attach function to callback
client.connect(broker_address, port=port)          #connect to broker
client.loop_start()        #start the loop
if Connected != True:    #Wait for connection
    time.sleep(0.1)
    while True:
        """
        message = {
            "barnId": "",	# id chuồng
            "nodeId": "",			#	
            "time": "",		# thời gian
            "status": random.randint(0,3),			# trạng thái chuồng -> cảnh báo
            "data": 					# dữ liệu
            [{"temp1": random.randint(0,100),"temp2": random.randint(0,100),"temp3": random.randint(0,100)},	# "xxxtemp":id cảm biến, xxx: giá trị cảm biến 
            {"conc1": random.randint(0,100),"conc2": random.randint(0,100),"conc3": random.randint(0,100)},	# "xxxconc":id cảm biến, xxx: giá trị cảm biến 
            {"light1": random.randint(0,1),"light2": random.randint(0,1),"light3": random.randint(0,1)},	# "xxxlight":id cảm biến, xxx: giá trị cảm biến 
            {"humi1": random.randint(0,100),"humi2": random.randint(0,100),"humi3": random.randint(0,100)},	# "xxxhumi":id cảm biến, xxx: giá trị cảm biến 	
            ]
        }
        """
        message = {
            "rpi": "g04",	# id chuồng
            "type": "electrical",			#	
            "data": 					# dữ liệu
            [{"id": "g04eleia","v": random.randint(0,100)},	
             {"id": "g04eleib","v": random.randint(0,100)},
             {"id": "g04eleic","v": random.randint(0,100)},
             {"id": "g04elevab","v": random.randint(0,100)},
             {"id": "g04eles","v": random.randint(2490,2500)},
             {"id": "g04elef","v": random.randint(58,62)},
            ]
        }
        message2 = {
            "rpi": "g04",	# id chuồng
            "type": "environment",			#	
            "data": 					# dữ liệu
            [{"id": "g01envtw","v": random.randint(0,100)},	
             {"id": "g01envpo","v": random.randint(0,100)},
             {"id": "g01envo2","v": random.randint(0,100)},
             {"id": "g01envh2s","v": random.randint(0,100)},
            ]
        }
        #json.dumps(message)
        #print(message)
        time.sleep(1)
        client.publish("test", json.dumps(message))
        client.publish("test", json.dumps(message2))
        #print(message)
