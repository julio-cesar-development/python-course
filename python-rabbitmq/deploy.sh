#!/bin/bash

kubectl apply -f ./k8s/secrets.yaml
kubectl apply -f ./k8s/rabbit.yaml
kubectl apply -f ./k8s/consumer01.yaml
kubectl apply -f ./k8s/consumer02.yaml
kubectl apply -f ./k8s/publisher.yaml
