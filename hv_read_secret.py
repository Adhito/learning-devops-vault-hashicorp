import hvac
import sys

## Stage : Authentication
client = hvac.Client(
    url='http://127.0.0.1:8200',
    token='adhito-token',
)

## Stage : Reading a secret
read_response = client.secrets.kv.read_secret_version(path='adhito-secret')
password = read_response['data']['data']['password']
print('LOG : Password is = ' + password)


## Stage : Checking a secret
if password != 'not-adhito-super-secret-password-12345':
    sys.exit('LOG : Password Is Incorrect !')

print('LOG : Password Is Correct, Access granted!')