- gcloud auth list
- gcloud config list project
- gcloud config set compute/zone ZONE
- gcloud config get-value project
  
- gcloud compute instances create gcelab2 --machine-type e2-medium --zone $ZONE
- gcloud -h
- gcloud compute instances list --filter="name=('gcelab2')"
- gcloud compute firewall-rules list --filter="NETWORK:'default' AND ALLOW:'icmp'"

- gcloud compute firewall-rules list --filter=ALLOW:'80'
- curl http://$(gcloud compute instances list --filter=name:gcelab2 --format='value(EXTERNAL_IP)')

- gcloud compute ssh gcelab2 --zone $ZONE
- gcloud compute instances add-tags gcelab2 --tags http-server,https-server
- gcloud compute firewall-rules create default-allow-http --direction=INGRESS --priority=1000 --network=default --action=ALLOW --rules=tcp:80 --source-ranges=0.0.0.0/0 --target-tags=http-server

- gcloud logging logs list --filter="compute"
- gcloud logging read "resource.type=gce_instance AND labels.instance_name='gcelab2'" --limit 5


```   

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
