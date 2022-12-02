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

Start the services
```bash
docker-compose up -d
```

Install python dependencies
(You might need sudo before "pip" and/or "pip3" insted of "pip" depending of your installation)
```bash
pip install -r requirements.txt
```

Start data generator
(You might need sudo before "python" and/or "python3" insted of "python" depending of your installation)
```bash
python dummy_data_pubber.py
```


[**Grafana dashboard**](https://localhost:3000)

[**InfluxDB Dashboard**](https://localhost:8086) 


## Docker Images Tested
Some versions is set to latest i docker compose.

[**Mosquitto**]() / `2.0.15` 

[**Telegraf**](http://hub.docker.com/_/telegraf) / `1.19`

[**InfluxDB**](http://hub.docker.com/_/influxdb) / `2.1.1`

[**Grafana-OSS**](https://hub.docker.com/r/grafana/grafana-oss) / `9.2.6` (set to latest in compose)



## Contributing

Contributions are always welcome!

