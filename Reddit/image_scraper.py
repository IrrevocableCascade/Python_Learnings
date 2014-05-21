__author__ = 'Irrevocable Cascade'

from urllib import request
from urllib import parse
from urllib.request import urlretrieve

DOMAIN = 'http://www.reddit.com'
USERNAME = 'IrrevocableCascade'
PASSWORD = 'chaCher6'

def login(uname,pw):
    api_login = '/api/login'
    url = DOMAIN + api_login
    body = {'api_type': 'json', 'user': str(uname), 'passwd': str(pw)}
    headers = {'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8'}
    data = parse.urlencode(body)
    binary_data = data.encode('utf-8')
    req = request.Request(url, binary_data, headers)
    response = request.urlopen(req)
    response_data = response.read()
    return print(response_data)

def get_sub(subname):
    url = DOMAIN + '/r/' + subname
    req = request.Request(url)
    response = request.urlopen(req)
    response_data = response.read().decode('utf-8')
    return response_data

def extract_pattern(page, pattern):

    start_link = page.find("a href")
    if start_link == -1:
        return None, 0
    start_quote = page.find(pattern, start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1: end_quote]
    return url, end_quote


html_string = get_sub('earthporn')

while True:
    url, n = extract_pattern(html_string, '"http://i.imgur')
    html_string = html_string[n:]
    if url:
        filename = url[19:]
        urlretrieve(url, filename)
        print(url)
    else:
        break


