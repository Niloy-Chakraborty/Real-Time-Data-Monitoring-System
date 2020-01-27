# Pipeline-for-Real-Time-Network-Data-Monitoring-System
Real-time Network Data Monitoring System using RabbitMQ , InfluxDB and Chronograf

# Motivation:
Now-a-days it is very important to monitor the data from various source (Network data, sensor data etc..) to take smart decisions based on the results. Often it becomes a hectic to make a proper pipeline where data will be autoatically flow from source to final DB, without losing it. 
To resolve this problem, this repository has been built that provides a solution for end-to-end data flow pipeline via RabbitMQ and InfluxDB. 
Here the example data is Server Data which contains all the values like, bytes_in , bytes_out etc. But this repository can be used for other data sources also.

# Guidelines:
After installing all the softwares (mentioned below) and packages (from requirements.txt), you need to do the following:
1) Unzip the data (If you need to do so..)
2) Run main file. It will create Json data and publish it to the Message Queue
3) Run consumer. It will consume the data from MQ and insert the data to the InfluDB


# SoftWare Installation Guideline:

Erlang- RabbitMQ Installation: 
-------------------------------


1) Go to https://www.erlang.org/downloads and download the executable.

2) Then Run and install the executable file.

3) Go to https://www.rabbitmq.com/download.html and download the rabbitmq executable file.

4) Now Run and Install the RabbitMQ executable

5) In the Command Prompt, Go to the RabbitMQ Server Location and use the command below:
   "rabbitmq-server start"

6) Install the RabbitMQ Management Console
   "rabbitmq-plugins.bat enable rabbitmq_management"

7) Next go to localhost:15672. The RabbitMQ console will be seen. 
   The default username : guest.
   The default password : guest


InFluxDB and Chronograf:
-------------------------

1) Go to https://portal.influxdata.com/downloads/ and download InfluxDB

2) The InfluxDB Version is : 1.7.9

3) Unzip the downloaded file and run influxd.exe and influx.exe respectively

4) Go to https://portal.influxdata.com/downloads/ and download Chronograf.

5) The used Chronograf version is 1.7.14

6) Unfer Unzipping the file, run chronograf.exe

7) Open chronograf in localhost:8888 and configure to see the dashboard. 

