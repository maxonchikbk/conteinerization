![Screenshot](index.jpg)

## Features:
1) Prometheus, cAdvisor and Alertmanager
2) Karma alert dashboard for Prometheus Alertmanager
3) Alerts to TelegramBot
4) Monitoring containers in Docker for Windows with Grafana. 
5) Node Exporter Full in Grafana
6) VM and host monitoring in Zabbix: Ubuntu, Archlinux, CentOS, FreeBSD
7) Performance tests from RabbitMQ 
8) Monitoring services in Elastic
9) Sentry with Flask test-app on http://mon.local:4567/
10) Elastic APM test-apps: 
    - FlaskApp http://mon.local:808/ 
    - GoApp http://mon.local:801/ 
    - jsApp http://mon.local:803/ 
11) Jaeger with test web-app
12) Zipkin with kafka test-app on http://mon.local:8881/

# Steps:

1) Add to hosts:
```
127.0.0.1 mon.local
127.0.0.1 prom.local
127.0.0.1 grafana.local
127.0.0.1 zabbix.local
127.0.0.1 alertmanager.local
127.0.0.1 karma.local
127.0.0.1 cadvisor.local
127.0.0.1 sentry.local
127.0.0.1 rabbit.local
127.0.0.1 elastic.local
127.0.0.1 jaeger.local
127.0.0.1 zipkin.local
```
2) Run install.cmd
3) Go to http://mon.local/ 

## Credentials:
1) Main: Admin/password
2) Grafana: Admin/grafana
3) Zabbix: Admin/zabbix
4) Sentry: max@mail.local/sentry
5) RabbitMQ: Admin/rabbit