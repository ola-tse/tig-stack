
![Logo](https://user-images.githubusercontent.com/64506580/159311466-f720a877-6c76-403a-904d-134addbd6a86.png)


# Telegraf, InfluxDB, Grafana (TIG) Stack

Get up and running with your own data in TIG within minutes.

## ⚡️ Getting Started

Clone the project

```bash
git clone https://github.com/huntabyte/tig-stack.git
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
```bash
pip install -r requirements.txt
```

Start data generator
```bash
python dummy_data_pubber.py
```


## Docker Images Tested
Some versions is set to latest i docker compose.

[**Mosquitto**]() / `2.0.15` 

[**Telegraf**](https://hub.docker.com/_/telegraf) / `1.19`

[**InfluxDB**](https://hub.docker.com/_/influxdb) / `2.1.1`

[**Grafana-OSS**](https://hub.docker.com/r/grafana/grafana-oss) / `9.2.6` (set to latest in compose)



## Contributing

Contributions are always welcome!

