__author__ = 'Irrevocable Cascade'

from urllib import request
import json

token = 'd2a24187877cdc2cbf070a2e01757c30343b31ab'
api_adress = 'https://api-ssl.bitly.com'
long_url = input('Enter URL to shorten: \n')
get = '/v3/shorten?access_token='+token+'&longUrl='+long_url
url = api_adress + get

#  rq = request.Request(url)
response = request.urlopen(url)
data = json.loads(response.read().decode('utf-8'))
print(data['status_code'])

