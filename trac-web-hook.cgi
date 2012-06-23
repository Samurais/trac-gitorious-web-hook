#!/usr/bin/env python

import cgi
import json
from operator import itemgetter
from subprocess import call

BRANCHES = ['master']
REPO_NAME = '(default)'
TRAC_ENV = '/var/www/trac'

def process():
	payload = cgi.parse().get('payload')

	if not payload:
		return

	try:
		data = json.loads(payload[0])
	except ValueError:
		return

	if data.get('ref') not in BRANCHES:
		return

	pending_commits = map(itemgetter('id'), data.get('commits', []))
	call(["trac-admin", TRAC_ENV, "changeset", "added", REPO_NAME] + pending_commits)

print 'Content-Type: text/plain'
print

process()
