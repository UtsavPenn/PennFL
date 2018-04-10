import setup

import requests
import boto3

from utils import get_todays_date


URL = 'https://2fjfpxrbb3.execute-api.ap-southeast-1.amazonaws.com/production/leagueapi/getleaguemembers?leagueId={}'
S3_BUCKET_NAME = "com.pennfl.storage"
S3_KEY = "league_data.json"

def get_league_url(league_id):
	return URL.format(league_id)


def get_penn_fantasy_league_data():
	url = get_league_url('ip3NjxML')
	r = requests.get(url, headers={'userid': 'tarunreddy.bethi@gmail.com'})
	return r.json()['data']



def get_s3_client():
	return boto3.client('s3')

def get_data_from_s3(bucket, key):
	client = get_s3_client()
	
	pass

def upload_data_to_s3(bucket, key):
	pass

def cache_league_data(event, context):
	s3_client = get_s3_client()
	league_data = get_penn_fantasy_league_data()

	if not s3_client.


	

