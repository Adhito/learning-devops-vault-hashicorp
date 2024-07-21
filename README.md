# Learning Hashicorp Vault Management 
Learning Hashicorp Vault Management 


### **Start Vault On K8s**


Create Namespace
```
kubectl create namespace vault
```

Install HV

```
helm install vault hashicorp/vault --namespace vault --version 0.28.0
```


### **Start Vault On Docker**

Create Vault Container
```
docker run -p 8200:8200 --cap-add=IPC_LOCK -e 'VAULT_DEV_ROOT_TOKEN_ID=adhito-token' -e 'VAULT_DEV_LISTEN_ADDRESS=0.0.0.0:8200' hashicorp/vault
```


### **Sample Secret Creation and Read w/ Python**

Create Sample Secret 
```
python hv_create_secret.py
```

Read Sample Secret 
```
python hv_read_secret.py
```
