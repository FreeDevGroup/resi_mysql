#!/bin/sh

ssh -o StrictHostKeyChecking=no ubuntu@$AWS_IP_ADDRESS << 'ENDSSH'
  cd /home/ubuntu/resiapi
  export $(cat .env | xargs)
  docker stop $(docker ps -a -q)
  docker rm $(docker ps -a -q)
  docker system prune -af --volumes
  # docker login -u $CI_REGISTRY_USER -p $CI_JOB_TOKEN $CI_REGISTRY
  # docker pull $IMAGE:web
  # docker pull $IMAGE:nginx
  docker-compose down -v
  docker-compose -f docker-compose-test.yml up -d
  # docker-compose -f docker-compose-prod.yml up -d
ENDSSH


