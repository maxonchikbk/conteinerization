docker-compose -f ./nginx/docker-compose.yml up -d  
docker-compose -f ./prom/docker-compose.yml up -d    
docker-compose -f ./zabbix/docker-compose.yml up -d
bash ./sentry/install.sh
docker-compose --env-file ./sentry/.env -f ./sentry/docker-compose.yml up -d