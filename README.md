xivo-dird-client
================

A python library to connect to xivo-auth.

Usage:

```python
from xivo_auth_client import Client

c = Client('localhost', username='alice', password='alice')

token_data = c.token.new('xivo_user', expiration=3600)  # Creates a new token expiring in 3600 seconds

token_data
{u'expires_at': u'2015-06-04T09:49:30.449625',
 u'issued_at': u'2015-06-04T08:49:30.449607',
 u'token': u'3d95d849-94e5-fc72-4ff8-93b597e6acf6',
 u'uuid': u'5cdff4a3-24a3-494f-8d32-9c8695e868f9'}

c.token.is_valid(token_data['token'])
True

c.token.get(token_data['token'])
{u'expires_at': u'2015-06-04T09:49:30.449625',
 u'issued_at': u'2015-06-04T08:49:30.449607',
 u'token': u'3d95d849-94e5-fc72-4ff8-93b597e6acf6',
 u'uuid': u'5cdff4a3-24a3-494f-8d32-9c8695e868f9'}

c.token.revoke(token_data['token'])

c.token.is_valid(token_data['token'])
False

c.backends.list()
['xivo_user']
```


## Tests

to run the tests

```sh
cd integration_tests
docker pull xivo/xivo-auth
docker build -t xivo/xivo-auth-client-test-data -f Dockerfile-data .
nosetests
```
