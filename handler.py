import os
import json
import logging
import random
import requests

log = logging.getLogger()
log.setLevel(logging.DEBUG)

def push(event, context):
    commits = [commit['message'] for commit in json.loads(event['body'])['commits']]

    body = 'Commits: ' + ', '.join(commits)
    log.debug('Commits: {}'.format(body))

    payload = {'text': body}

    r = requests.post(os.getenv('SLACK_WEBHOOK'), data=str(payload))

    log.debug('{}'.format(r.text))

    return {
        'statusCode': 200,
        'body': 'received'
    }
