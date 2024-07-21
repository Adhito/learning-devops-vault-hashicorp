import hvac
import sys

## Stage : Authentication
client = hvac.Client(
    url='http://127.0.0.1:8200',
    token='adhito-token',
)

## Stage : Writing a secret
create_response = client.secrets.kv.v2.create_or_update_secret(
    path='adhito-secret',
    secret=dict(password='adhito-super-secret-password-12345'),
)

print('LOG : Secret written successfully.')