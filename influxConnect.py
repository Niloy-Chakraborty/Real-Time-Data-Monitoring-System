#!/usr/bin/env python
"""
Script Name: influxConnect
Functionality: This script takes data from Consumer and insert data into InfluxDB
Author: Niloy Chakraborty
"""

import influxdb
from influxdb import InfluxDBClient
import json

"""
Function Name: push_data
Parameters: user_id, password,data,j,timestamp
Functionality: --This script takes data from Consumer
               -- Connect to InfluxDB
               -- Create New DB
               -- Convert the data into Line Protocol
               -- Write the data into the InfluxDB
Return: 
"""


def push_data(data):

    db_name= 'Smart_Datacenter_Final'
    data= eval(data)
    # print(type(data))

    # Convert Timestamp to UNIX standard for InfluxDB
    from datetime import datetime,timedelta
    utc_time = datetime.strptime(data["timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
    # print(utc_time)
    milliseconds = int(utc_time.timestamp() * 1000)

    # print("json Data is", data)
    val_dict= data["value"]
    # print(val_dict)
    client = InfluxDBClient(host='localhost', port=8086)
    client.create_database(db_name)
    client.switch_database(db_name)

    # Line Protocol
    # Measurement: servers, host: node0.., field name: bytes_in, bytes_out etc.., field value: ytes_in, bytes_out etc..
    # Timestamp: in influxdb standard

    line_new= "servers,host="+data["instanceId"]+" bytes_in="+str(val_dict["bytes_in"])+",bytes_out="+str(val_dict["bytes_out"])+",Exhaust_Temp="+str(val_dict["Exhaust_Temp"])+",Temp="+str(val_dict["Temp"])+",proc_run="+str(val_dict["proc_run"])+",ib_port_xmit_data_mlx4_0_port1="+str(val_dict["ib_port_xmit_data_mlx4_0_port1"])+",cpu_system="+str(val_dict["cpu_system"])+",ib_port_rcv_data_mlx4_0_port1="+str(val_dict["ib_port_rcv_data_mlx4_0_port1"])+",mem_free="+str(val_dict["mem_free"])+",powerconsumption_in_watts="+str(val_dict["powerconsumption_in_watts"])+",Inlet_Temp="+str(val_dict["Inlet_Temp"])+",cpu_user="+str(val_dict["cpu_user"])+",proc_total="+str(val_dict["proc_total"])+" "+str(milliseconds)
    # print(line_new)

    if client.write_points(line_new, database=db_name, time_precision='ms', protocol='line'):
        print("data inserted into DB successfully!")

    # close http session
    client.close()
