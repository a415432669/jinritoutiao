import requests

header = {
    'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4620.400 QQBrowser/9.7.13014.400'
}
res = requests.get('http://toutiao.com/group/6530061224237859331/',headers=header)

print('123')
print(res.content)