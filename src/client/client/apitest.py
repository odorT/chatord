import requests

reg_url = 'http://localhost/api/v1/register'
user_url = 'http://localhost/api/v1/user'

data1 = {
    'username': 'kamran4',
    'password': 'kamran'
}

data2 = {
    'username': 'kamran4',
    'password': 'kamran',
    'conn_details': "{'ip': '192.168.100.10', 'port': '1234'}"
}

# for registration
# r = requests.post(url=reg_url, data=data1)

# for getting token
# r = requests.post(url=user_url, data=data2)

# token = eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzOTMxNzM5NSwianRpIjoiNGQ5M2FhYjYtNzBjOC00ZGExLWJmN2ItMThlOTNjM2ZjMDQzIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IntcImNoZWNrX3Bhc3N3b3JkXCI6IG51bGwsIFwiZmluZF9ieV9pZFwiOiBudWxsLCBcImZpbmRfYnlfdXNlcm5hbWVcIjogbnVsbCwgXCJpZFwiOiA4LCBcInBhc3N3b3JkXCI6IFwia2FtcmFuXCIsIFwicXVlcnlcIjogbnVsbCwgXCJxdWVyeV9jbGFzc1wiOiBudWxsLCBcInJlZ2lzdHJ5XCI6IG51bGwsIFwic2F2ZV90b19kYlwiOiBudWxsLCBcInVzZXJuYW1lXCI6IFwia2FtcmFuNFwifSIsIm5iZiI6MTYzOTMxNzM5NSwiZXhwIjoxNjM5MzE4Mjk1fQ.1xTWnNLBnDdV72BcMrpFYmcXW2hxQcuu3sJ1lQVRneY

# getting all online users
r = requests.get(url=user_url, headers={'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzOTMxNzM5NSwianRpIjoiNGQ5M2FhYjYtNzBjOC00ZGExLWJmN2ItMThlOTNjM2ZjMDQzIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IntcImNoZWNrX3Bhc3N3b3JkXCI6IG51bGwsIFwiZmluZF9ieV9pZFwiOiBudWxsLCBcImZpbmRfYnlfdXNlcm5hbWVcIjogbnVsbCwgXCJpZFwiOiA4LCBcInBhc3N3b3JkXCI6IFwia2FtcmFuXCIsIFwicXVlcnlcIjogbnVsbCwgXCJxdWVyeV9jbGFzc1wiOiBudWxsLCBcInJlZ2lzdHJ5XCI6IG51bGwsIFwic2F2ZV90b19kYlwiOiBudWxsLCBcInVzZXJuYW1lXCI6IFwia2FtcmFuNFwifSIsIm5iZiI6MTYzOTMxNzM5NSwiZXhwIjoxNjM5MzE4Mjk1fQ.1xTWnNLBnDdV72BcMrpFYmcXW2hxQcuu3sJ1lQVRneY'})


# log out
# r = requests.patch(url=user_url, headers={'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzOTMxNzM5NSwianRpIjoiNGQ5M2FhYjYtNzBjOC00ZGExLWJmN2ItMThlOTNjM2ZjMDQzIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IntcImNoZWNrX3Bhc3N3b3JkXCI6IG51bGwsIFwiZmluZF9ieV9pZFwiOiBudWxsLCBcImZpbmRfYnlfdXNlcm5hbWVcIjogbnVsbCwgXCJpZFwiOiA4LCBcInBhc3N3b3JkXCI6IFwia2FtcmFuXCIsIFwicXVlcnlcIjogbnVsbCwgXCJxdWVyeV9jbGFzc1wiOiBudWxsLCBcInJlZ2lzdHJ5XCI6IG51bGwsIFwic2F2ZV90b19kYlwiOiBudWxsLCBcInVzZXJuYW1lXCI6IFwia2FtcmFuNFwifSIsIm5iZiI6MTYzOTMxNzM5NSwiZXhwIjoxNjM5MzE4Mjk1fQ.1xTWnNLBnDdV72BcMrpFYmcXW2hxQcuu3sJ1lQVRneY'})


print(r.json())
