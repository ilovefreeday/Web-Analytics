from twython import Twython

APP_KEY = 'l3f60dAw9PVGyNHCk8TJusTOb'
APP_KEY_SECRET = 'hQLR77cquoSYBGr77E38sDTSYnU6milonwYG0p0TqIPIiBUOFp'
ACCESS_TOKEN = '1099720716-F6PE89F1oBxiHA7tKxXS37QT4KFGUKd3fobWs8O'
ACCESS_TOKEN_SECRET = 'TbVwSs9qGY4vX7YJxhBHdtC2KF8a4KNmq3SaGmG1YQR8q'

t = Twython(app_key = APP_KEY, app_secret = APP_KEY_SECRET, oauth_token = ACCESS_TOKEN, oauth_token_secret = ACCESS_TOKEN_SECRET)

search = t.search(q='$tsla', count = 5)

tweets = search['statuses']

for tweet in tweets:
	print tweet['text'],'\n'