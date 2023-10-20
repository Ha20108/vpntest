import routeros_api 
import random

name = str(random.randint(10**(8-1), 10**8-1))
password = str(random.randint(10**(8-1), 10**8-1))
ip = f'172.30.0.{str(random.randint( 00,99 ))}'
try:
    connection = routeros_api.RouterOsApiPool(
            host='467a02f5d0ea.sn.mynetname.net',
            username='admin',
            password='131990',
            port=8728,
            use_ssl=False,
            ssl_verify=False,
            ssl_verify_hostname=True,
            ssl_context=None,
            plaintext_login=True
        )
    api = connection.get_api()
    test = api.get_resource('/ppp/secret').get()

    for i in test:
        if i ['name'] == name or ['remote_address'] == f'172.30.1.{ip}' :
            name = f'{name}{ip}'
            ip = f'172.30.1.{str(random.randint( 0,254 ))}'
        else:
            name = name
            #api.get_resource('/ppp/secret').add( name = name , password= password ,service='sstp',profile='sstp',remote_address=f'172.30.0.{ip}')
    api.get_resource('/ppp/secret').add( name = name , password= password ,service='sstp',profile='sstp',remote_address= ip )
    print(name)
    print(ip)

except Exception as e:
    print(e)
    
