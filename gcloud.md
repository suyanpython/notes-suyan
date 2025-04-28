# K8s's struture  
├── cleanup.sh
├── deployments
│   ├── auth.yaml
│   ├── frontend.yaml
│   ├── hello-canary.yaml
│   ├── hello-green.yaml
│   └── hello.yaml
├── nginx
│   ├── frontend.conf
│   └── proxy.conf
├── pods
│   ├── healthy-monolith.yaml
│   ├── monolith.yaml
│   └── secure-monolith.yaml
├── services
│   ├── auth.yaml
│   ├── frontend.yaml
│   ├── hello-blue.yaml
│   ├── hello-green.yaml
│   ├── hello.yaml
│   └── monolith.yaml
└── tls
    ├── ca-key.pem
    ├── ca.pem
    ├── cert.pem
    └── key.pem

# shortcuts 
- kube ctl get po

- kubectl get deploy → for deployments

- kubectl get svc → for services

- kubectl get ns → for namespaces

# Create a pod 
    - kubectl create deployment nginx --image=nginx:1.10.0 # create pod with deployment of image 
    - kubectl create -f pods/monolith.yaml    # create pod from yml
    - kubectl get pods
    - kubectl describe pods monolith
    
# Expose as ALB  # get external IP 
    - kubectl expose deployment nginx --port 80 --type LoadBalancer
    - kubectl get services
  
# Check locally # & detached mode
  - kubectl port-forward monolith 10080:80 &

  - TOKEN=$(curl http://127.0.0.1:10080/login -u user|jq -r '.token')
  - curl -H "Authorization: Bearer $TOKEN" http://127.0.0.1:10080/secure

# Check history # -f for tream
- kubectl logs monolith

# it exec of the pod 
- kubectl exec monolith --stdin --tty -c monolith -- /bin/sh
- printenv, echo $PATH, touch, mkdir, vi, hostname -i, ip, ls -R

# https 
- kubectl create secret generic tls-certs --from-file tls/
- kubectl create configmap nginx-proxy-conf --from-file nginx/proxy.conf
- kubectl create -f pods/secure-monolith.yaml
- gcloud compute firewall-rules create allow-monolith-nodeport --allow=tcp:31000
- gcloud compute instances list

# get ALB IP
- kubectl get services monolith
- kubectl describe services monolith
- kubectl describe services monolith | grep Endpoints 
  
# add label and search by label 
- kubectl label pods secure-monolith 'secure=enabled'
- kubectl get pods secure-monolith --show-labels
- kubectl get pods -l "app=monolith,secure=enabled"

# Create the target Docker repository

- gcloud auth configure-docker  us-central1-docker.pkg.dev
-  check with: cat ~/.docker/config.json
- gcloud artifacts repositories create my-repository --repository-format=docker --location="us-central1" --description="Docker repository"
- docker build -t us-central1-docker.pkg.dev/"PROJECT_ID"/my-repository/node-app:0.2 .
- docker push us-central1-docker.pkg.dev/"PROJECT_ID"/my-repository/node-app:0.2
- docker stop $(docker ps -q)
- docker rm $(docker ps -aq)
- docker rmi -f $(docker images -aq) # remove remaining images
- docker run -p 4000:80 -d  us-central1-docker.pkg.dev/"PROJECT_ID"/my-repository/node-app:0.2

# Deploy 
- kubectl create configmap nginx-frontend-conf --from-file=nginx/frontend.conf
- kubectl create -f deployments/frontend.yaml
- kubectl create -f services/frontend.yaml


- gcloud auth list
- gcloud config list project
- gcloud config set compute/region us-east5
- gcloud config set compute/zone ZONE
- gcloud config get-value project
  
- gcloud compute instances create gcelab2 --machine-type e2-medium --zone $ZONE
-   gcloud compute instances create www3 \
    --zone=us-central1-c  \
    --tags=network-lb-tag \
    --machine-type=e2-small \
    --image-family=debian-11 \
    --image-project=debian-cloud \
    --metadata=startup-script='#!/bin/bash
      apt-get update
      apt-get install apache2 -y
      service apache2 restart
      echo "
<h3>Web Server: www3</h3>" | tee /var/www/html/index.html'
  
- gcloud container clusters create --machine-type=e2-medium --zone=us-east5-b lab-cluster
- gcloud container clusters get-credentials lab-cluster
- kubectl create deployment hello-server --image=gcr.io/google-samples/hello-app:1.0
- kubectl expose deployment hello-server --type=LoadBalancer --port 8080
- kubectl get service
- curl http://[EXTERNAL-IP]:8080
  
- gcloud -h
- gcloud compute instances list --filter="name=('gcelab2')"
- gcloud compute firewall-rules list --filter="NETWORK:'default' AND ALLOW:'icmp'"

- gcloud compute firewall-rules list --filter=ALLOW:'80'
- curl http://$(gcloud compute instances list --filter=name:gcelab2 --format='value(EXTERNAL_IP)')

- gcloud compute ssh gcelab2 --zone $ZONE
- gcloud compute instances add-tags gcelab2 --tags http-server,https-server
- gcloud compute firewall-rules create default-allow-http --direction=INGRESS --priority=1000 --network=default --action=ALLOW --rules=tcp:80 --source-ranges=0.0.0.0/0 --target-tags=http-server
- 
- gcloud compute firewall-rules create www-firewall-network-lb --target-tags network-lb-tag --allow tcp:80
- gcloud compute addresses create network-lb-ip-1 --region us-central1
- gcloud compute http-health-checks create basic-check
- 

- gcloud logging logs list --filter="compute"
- gcloud logging read "resource.type=gce_instance AND labels.instance_name='gcelab2'" --limit 5


```   
gcloud compute forwarding-rules describe www-rule --region us-central1
IPAddress: 34.31.93.13
IPProtocol: TCP
creationTimestamp: '2025-04-25T07:54:29.989-07:00'
description: ''
fingerprint: 5TwZHYzzb2Y=
id: '7830275268335246538'
kind: compute#forwardingRule
labelFingerprint: 42WmSpB8rSM=
loadBalancingScheme: EXTERNAL
name: www-rule
networkTier: PREMIUM
portRange: 80-80
region: https://www.googleapis.com/compute/v1/projects/qwiklabs-gcp-02-170058fdaa94/regions/us-central1
selfLink: https://www.googleapis.com/compute/v1/projects/qwiklabs-gcp-02-170058fdaa94/regions/us-central1/forwardingRules/www-rule
target: https://www.googleapis.com/compute/v1/projects/qwiklabs-gcp-02-170058fdaa94/regions/us-central1/targetPools/www-pool

$ gcloud compute firewall-rules list --format=json
[
  {
    "allowed": [
      {
        "IPProtocol": "tcp",
        "ports": [
          "80"
        ]
      }
    ],
    "creationTimestamp": "2025-04-25T00:49:07.820-07:00",
    "description": "",
    "direction": "INGRESS",
    "disabled": false,
    "id": "4386262455348002972",
    "kind": "compute#firewall",
    "logConfig": {
      "enable": false
    },
    "name": "default-allow-http",
    "network": "https://www.googleapis.com/compute/v1/projects/qwiklabs-gcp-02-286bd1e64a0d/global/networks/default",
    "priority": 1000,
    "selfLink": "https://www.googleapis.com/compute/v1/projects/qwiklabs-gcp-02-286bd1e64a0d/global/firewalls/default-allow-http",
    "sourceRanges": [
      "0.0.0.0/0"
    ],
    "targetTags": [
      "http-server"
    ]
  },
  {
    "allowed": [
      {
        "IPProtocol": "icmp"
      }
    ],
    "creationTimestamp": "2025-04-21T09:16:12.731-07:00",
    "description": "Allow ICMP from anywhere",
    "direction": "INGRESS",
    "disabled": false,
    "id": "606606984789873059",
    "kind": "compute#firewall",
    "logConfig": {
      "enable": false
    },
    "name": "default-allow-icmp",
    "network": "https://www.googleapis.com/compute/v1/projects/qwiklabs-gcp-02-286bd1e64a0d/global/networks/default",
    "priority": 65534,
    "selfLink": "https://www.googleapis.com/compute/v1/projects/qwiklabs-gcp-02-286bd1e64a0d/global/firewalls/default-allow-icmp",
    "sourceRanges": [
      "0.0.0.0/0"
    ]
  },
  {
    "allowed": [
      {
        "IPProtocol": "tcp",
        "ports": [
          "0-65535"
        ]
      },
      {
        "IPProtocol": "udp",
        "ports": [
          "0-65535"
        ]
      },
      {
        "IPProtocol": "icmp"
      }
    ],
    "creationTimestamp": "2025-04-21T09:16:12.482-07:00",
    "description": "Allow internal traffic on the default network",
    "direction": "INGRESS",
    "disabled": false,
    "id": "1077236783687389603",
    "kind": "compute#firewall",
    "logConfig": {
      "enable": false
    },
    "name": "default-allow-internal",
    "network": "https://www.googleapis.com/compute/v1/projects/qwiklabs-gcp-02-286bd1e64a0d/global/networks/default",
    "priority": 65534,
    "selfLink": "https://www.googleapis.com/compute/v1/projects/qwiklabs-gcp-02-286bd1e64a0d/global/firewalls/default-allow-internal",
    "sourceRanges": [
      "10.128.0.0/9"
    ]
  },
  {
    "allowed": [
      {
        "IPProtocol": "tcp",
        "ports": [
          "3389"
        ]
      }
    ],
    "creationTimestamp": "2025-04-21T09:16:12.648-07:00",
    "description": "Allow RDP from anywhere",
    "direction": "INGRESS",
    "disabled": false,
    "id": "4495729124340126115",
    "kind": "compute#firewall",
    "logConfig": {
      "enable": false
    },
    "name": "default-allow-rdp",
    "network": "https://www.googleapis.com/compute/v1/projects/qwiklabs-gcp-02-286bd1e64a0d/global/networks/default",
    "priority": 65534,
    "selfLink": "https://www.googleapis.com/compute/v1/projects/qwiklabs-gcp-02-286bd1e64a0d/global/firewalls/default-allow-rdp",
    "sourceRanges": [
      "0.0.0.0/0"
    ]
  },
  {
    "allowed": [
      {
        "IPProtocol": "tcp",
        "ports": [
          "22"
        ]
      }
    ],
    "creationTimestamp": "2025-04-21T09:16:12.564-07:00",
    "description": "Allow SSH from anywhere",
    "direction": "INGRESS",
    "disabled": false,
    "id": "4994714739707466147",
    "kind": "compute#firewall",
    "logConfig": {
      "enable": false
    },
    "name": "default-allow-ssh",
    "network": "https://www.googleapis.com/compute/v1/projects/qwiklabs-gcp-02-286bd1e64a0d/global/networks/default",
    "priority": 65534,
    "selfLink": "https://www.googleapis.com/compute/v1/projects/qwiklabs-gcp-02-286bd1e64a0d/global/firewalls/default-allow-ssh",
    "sourceRanges": [
      "0.0.0.0/0"
    ]
  }
]

```
