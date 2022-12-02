# Telegraf, InfluxDB, Grafana (TIG) Stack + MQTT broker and data generator

Get up and running with your own data in TIG within minutes.

## ⚡️ Getting Started

### Prereqs: 
* Docker 
* Python

Clone the project

```bash
git clone https://github.com/ola-tse/tig-stack.git
```

Navigate to the project directory

```bash
cd tig-stack
```

build the services
```bash
docker-compose build
```

Run the services
```bash
docker-compose up
```


[**Grafana dashboard**](http://localhost:3000)

[**InfluxDB Dashboard**](http://localhost:8086) 


## Docker Images Tested
Some versions is set to latest i docker compose.

[**Mosquitto**]() / `2.0.15` 

[**Telegraf**](http://hub.docker.com/_/telegraf) / `1.19`

[**InfluxDB**](http://hub.docker.com/_/influxdb) / `2.1.1`

[**Grafana-OSS**](https://hub.docker.com/r/grafana/grafana-oss) / `9.2.6` 



## Contributing

Contributions are always welcome!

