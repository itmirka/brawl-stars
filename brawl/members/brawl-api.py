import requests

headers = {
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImJiYmVhY2E4LWNlMTctNGMyNS1iNWNlLWVmZWQzOGM1OTM5NCIsImlhdCI6MTY1Mjk3ODI5MCwic3ViIjoiZGV2ZWxvcGVyLzBjMGNiMzgyLWVmNTUtYjZmOC00YzU2LWJhNjVhNzk2NWQxZSIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiMy45MS4xNTcuMTk0IiwiNTQuODYuNTAuMTM5Il0sInR5cGUiOiJjbGllbnQifV19.eFDQnzgxIVVMNRBfgx4RM1QrRks0nKx2udm8c9-AFqoguc5gmf4L7BKcVmAOvHmD-aJrLIi7OkZHJZRi15TBEA'
}

def get_user():
	response = requests.get('https://api.brawlstars.com/v1/players/%23GQLGGGUY', headers=headers)
	user_json = response.json()
	print(user_json)


get_user()