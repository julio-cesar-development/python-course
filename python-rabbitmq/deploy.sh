#!/bin/bash

(kubectl delete -f ./k8s 1> /dev/null 2>&1 && echo "Cleaning pods...") &
wait

# secrets
kubectl apply -f ./k8s/secrets.yaml

# deployment and service rabbit
kubectl apply -f ./k8s/rabbit-statefulset.yaml
kubectl apply -f ./k8s/rabbit-cluster-ip-service.yaml

# deployment and service consumer
kubectl apply -f ./k8s/consumer-deployment.yaml

# deployment and service publisher
kubectl apply -f ./k8s/publisher-deployment.yaml
