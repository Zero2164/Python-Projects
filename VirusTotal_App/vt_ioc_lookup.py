# ---------IMPORTED COMPONENTS---------
import requests
import os
import sys
from swimlane import Swimlane
# ---------VARIABLES---------

VT_API_KEY = os.environ.get('VT_API_KEY', '')
assert VT_API_KEY, 'Env variable VT_API_KEY not set!'

SWIMLANE_PAT = os.environ.get('SWIMLANE_PAT', '')
assert SWIMLANE_PAT, 'Env variable SWIMLANE_PAT not set!'

IOC = str(sys.argv[1])
url = 'https://www.virustotal.com/api/v3/search?'
headers = {'x-apikey': VT_API_KEY}
params = {'query': IOC}
results = {}
swimlane = Swimlane(
    'http://kyle-lamont-scsd-ilt.training.saocli.com', SWIMLANE_PAT, verify_ssl=False)
app = swimlane.apps.get(name='Virus Total Lookup')
# ---------MAIN APP FUNCTION--------


response = requests.get(url, headers=headers, params=params)
assert 200 <= response.status_code < 400, 'Failed to GET from /search, ERROR: ' + response.text

json_data = response.json()['data']
for item in json_data:
    for key, value in item['attributes']['last_analysis_stats'].items():
        results.update({key: value})


print('---Virus Total Results for: ' + IOC + '---\n\n', results, '\n\n')
