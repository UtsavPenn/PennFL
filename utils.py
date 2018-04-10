import json

import arrow


def get_todays_date():
	return str(arrow.now().date())


def jsonify(data):
	return json.dumps(data)