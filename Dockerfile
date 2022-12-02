FROM grafana/grafana-oss:9.2.6

COPY --chown=grafana ./grafana_mount/data/grafana.db  /var/lib/grafana/grafana.db