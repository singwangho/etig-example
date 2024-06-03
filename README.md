This is an untested example to demo an on-premise deployment of the EMQX, Telegraf, InfluxDB, and Grafana stack (EMQX+TIG).

The TIG stack is based on HuntaByte's youtube video (https://youtu.be/QGG_76OmRnA?si=txcPj_jqzjeHmeee).  Please browse through this fantastic short 13-minute video demonstrating how to get started on TIG.

**Prerequsite:**
You will neeed Docker compose properly running.
I ran this with Ubuntu, but as it runs on docker, it should run on any environment?

**Key Steps**
1. Start by reading through the short docker-compose.yml; making appriopriate changes to the main configuration settings (primarily to USERNAME and Passwords)
2. Next goto config/telegraf/telegraf.conf file which will 'bridge' EMQX with InfluxDB.  This is a long file, but we really have two parts:
     Inputs:
       From telegraf plugins, configured after line 3137, to feed some inputs from telegraf to InfluxDB.  Nothing needs editing here.
       From EMQX, is configured on line 8527.  Make sure the topic and url is correct.
     Outputs:
       To InfluxDB, is configured on line 999.  Make sure the token and organization matches the docker-compose file
3. Run docker-compose up -d
4. Now start configuring and troubleshooting.  I suggest to start at telegraf (docker logs -f [telegraf container name]).
5. Then goto influxdb make sure your bucket is collecting data (see Huntabyte's youtube video...)
6. Then to Grafana, you need to configure the connection with influxdb (again see HuntaByte's video)
7. Then finally visit EMQX, you should see telegraf connected to EMQX.  I have attached a python based mqtt-consumer & publisher to help you do MQTT debugging.

Good luck.
