YAML files for the various tasks


YAML TO DEPLOY CLUSTER

---
apiVersion: "apps/v1"
kind: "Deployment"
metadata:
  name: "nginx-2"
  namespace: "default"
  labels:
    app: "nginx-2"
spec:
  replicas: 3
  selector:
    matchLabels:
      app: "nginx-2"
  template:
    metadata:
      labels:
        app: "nginx-2"
    spec:
      containers:
      - name: "shriram-q1-a1-sha256"
        image: "asia.gcr.io/pe-training/shriram-q1-a1@sha256:3b64ee57140187030296ef1d67760482f7551dd62c35fc9dd566d219d96c3900"
---
apiVersion: "autoscaling/v2beta1"
kind: "HorizontalPodAutoscaler"
metadata:
  name: "nginx-2-hpa"
  namespace: "default"
  labels:
    app: "nginx-2"
spec:
  scaleTargetRef:
    kind: "Deployment"
    name: "nginx-2"
    apiVersion: "apps/v1"
  minReplicas: 1
  maxReplicas: 5
  metrics:
  - type: "Resource"
    resource:
      name: "cpu"
      targetAverageUtilization: 8




YAML TO EXPOSE NODE PORT

apiVersion: v1
kind: Service
metadata:
  creationTimestamp: 2019-07-31T11:23:16Z
  generateName: nginx-2-
  labels:
    app: nginx-2
  name: nginx-2-9pf6j
  namespace: default
  resourceVersion: "1708"
  selfLink: /api/v1/namespaces/default/services/nginx-2-9pf6j
  uid: 97c58bf6-b385-11e9-b107-42010a8000d3
spec:
  clusterIP: 10.126.4.212
  externalTrafficPolicy: Cluster
  ports:
  - nodePort: 32687
    port: 80
    protocol: TCP
    targetPort: 80
  selector:
    app: nginx-2
  sessionAffinity: None
  type: NodePort
status:
  loadBalancer: {}

YAML FOR CLUSTER IP

apiVersion: v1
kind: Service
metadata:
  creationTimestamp: 2019-07-31T11:22:52Z
  generateName: nginx-2-
  labels:
    app: nginx-2
  name: nginx-2-4szgx
  namespace: default
  resourceVersion: "1635"
  selfLink: /api/v1/namespaces/default/services/nginx-2-4szgx
  uid: 88e9c0a8-b385-11e9-b107-42010a8000d3
spec:
  clusterIP: 10.126.5.246
  ports:
  - port: 80
    protocol: TCP
    targetPort: 80
  selector:
    app: nginx-2
  sessionAffinity: None
  type: ClusterIP
status:
  loadBalancer: {}

YAML FOR LOAD BALANCER

apiVersion: v1
kind: Service
metadata:
  creationTimestamp: 2019-07-31T11:33:01Z
  generateName: nginx-2-
  labels:
    app: nginx-2
  name: nginx-2-gbb5b
  namespace: default
  resourceVersion: "3600"
  selfLink: /api/v1/namespaces/default/services/nginx-2-gbb5b
  uid: f44225a2-b386-11e9-b107-42010a8000d3
spec:
  clusterIP: 10.126.7.246
  externalTrafficPolicy: Cluster
  ports:
  - nodePort: 31206
    port: 80
    protocol: TCP
    targetPort: 80
  selector:
    app: nginx-2
  sessionAffinity: None
  type: LoadBalancer
status:
  loadBalancer:
    ingress:
    - ip: 34.67.110.27
