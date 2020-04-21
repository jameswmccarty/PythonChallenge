"""
http://www.pythonchallenge.com/pc/return/disproportional.html
"""

import xmlrpc.client

# Create an object to represent our server.
server_url = "http://www.pythonchallenge.com/pc/phonebook.php"
proxy = xmlrpc.client.ServerProxy(server_url)

try:
    #print(proxy.system.listMethods())
	#['phone', 'system.listMethods', 'system.methodHelp', 'system.methodSignature', 'system.multicall', 'system.getCapabilities']
	print(proxy.phone('Bert')) #555-ITALY
except xmlrpc.client.ProtocolError as err:
    print("A protocol error occurred")
    print("URL: %s" % err.url)
    print("HTTP/HTTPS headers: %s" % err.headers)
    print("Error code: %d" % err.errcode)
    print("Error message: %s" % err.errmsg)
