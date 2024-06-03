This is an untested example of to demo an on-premise deployment of the EMQX, Telegraf, InfluxDB, and Grafana stack.

THe TIG stack is partly credited to HuntaByte (https://youtu.be/QGG_76OmRnA?si=txcPj_jqzjeHmeee).  Please browse through their short 13-minute video.

**Prerequsite:**
You will neeed Docker compose properly running.
I ran this with Ubuntu, but I think it should work on any environment

**Key Steps**
1. Start by opening docker-compose.yml; read through it and make appriopriate changes (primarily to USERNAME and Passwords)
2. Next goto config/telegraf/telegraf.conf file which will 'bridge' EMQX with InfluxDB.  This is a long file, but we really have two parts:
3.   Inputs:
       From telegraf plugins, configured after line 3137, to feed some inputs from telegraf to InfluxDB.  Nothing needs editing here.
       From EMQX, is configured on line 8527.  Make sure the topic and url is correct.
     Outputs:
       To InfluxDB, is configured on line 999.  Make sure the token and organization matches the docker-compose file
4. Then run docker-compose up -d
5. I suggest you to start configuring & troubleshooting from telegraf (docker logs -f [telegraf container name]).
6. Then to influxdb make sure your bucket is collecting data
7. Then to Grafana, you need to configure the connection with influxdb (I refer you to HuntaByte's youtube to get started)
8. Then finally back to MQTT using the attached python mqtt-consumer & publisher.

Good luck.
