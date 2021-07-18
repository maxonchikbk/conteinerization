docker-compose -f ./nginx/docker-compose.yml down
docker-compose -f ./prom/docker-compose.yml down    
docker-compose -f ./zabbix/docker-compose.yml down
docker-compose --env-file ./sentry/.env -f ./sentry/docker-compose.yml down