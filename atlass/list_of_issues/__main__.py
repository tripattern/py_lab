import sys
from atlassian import Jira

user = sys.argv[1]
api_token = sys.argv[2]
server = sys.argv[3]

jira = Jira(
    url=server,
    username=user,
    password=api_token,
    cloud=True)

key = 'SALES-201'
issue = jira.issue(key)  # full description
field = 'issuetype'
summary = jira.issue_field_value(key, field)

print('ticket: ', key, summary)
