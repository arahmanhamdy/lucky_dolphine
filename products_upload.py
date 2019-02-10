import xmlrpc

url = "http://localhost:8069"
db = "luck_test1"
username = 'admin'
password = 'iti'

common = xmlrpc.('{}/xmlrpc/2/common'.format(url))
common.version()
