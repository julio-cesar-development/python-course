#!/bin/bash

kubectl apply -f ./k8s/secrets.yaml \
  -f ./k8s/rabbit.yaml \
  -f ./k8s/deadletter.yaml \
  -f ./k8s/consumer01.yaml \
  -f ./k8s/consumer02.yaml \
  -f ./k8s/publisher.yaml

# kubectl get deploy,statefulset,job,svc,pod -n default

# kubectl get secret env-secrets
# kubectl describe secret env-secrets

# kubectl create secret generic env-secrets \
#   --from-literal=RABBIT_PORT=5672 \
#   --from-literal=RABBIT_USER=dev \
#   --from-literal=RABBIT_PASS=dev
