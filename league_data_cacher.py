import arrow
import requests


URL = 'https://2fjfpxrbb3.execute-api.ap-southeast-1.amazonaws.com/production/leagueapi/getleaguemembers?leagueId={}'

def get_league_url(league_id):
	return URL.format(league_id)


def get_penn_fantasy_league_data():
	url = get_league_url('ip3NjxML')
	r = requests.get(url, headers={'userid': 'tarunreddy.bethi@gmail.com'})
	return r.json()['data']


def cache_league_data(event, context):
