docker-compose -f ./nginx/docker-compose.yml up -d  
docker-compose -f ./prom/docker-compose.yml up -d    
docker-compose -f ./elastic/docker-compose.yml up -d
docker-compose -f ./jaeger/docker-compose.yml up -d
docker-compose --env-file ./zipkin/.env -f ./zipkin/docker-compose.yml -f ./zipkin/docker-compose-kafka.yml up -d
docker-compose -f ./zabbix/docker-compose.yml up -d
bash ./sentry/install.sh
docker-compose --env-file ./sentry/.env -f ./sentry/docker-compose.yml -f ./sentry/docker-test.yml up -d