docker-compose -f ./nginx/docker-compose.yml down
docker-compose -f ./prom/docker-compose.yml down    
docker-compose -f ./elastic/docker-compose.yml down
docker-compose -f ./jaeger/docker-compose.yml down
docker-compose --env-file ./zipkin/.env -f ./zipkin/docker-compose.yml -f ./zipkin/docker-compose-kafka.yml down
docker-compose -f ./zabbix/docker-compose.yml down
docker-compose --env-file ./sentry/.env -f ./sentry/docker-compose.yml down