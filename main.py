# # string = ("123456", 123)
# # print(string[0][0:3])


# # string = "T-ALI"
# # if string[1] == '-':
# #     string[] = 


fn = ['first', 'rao', 'yusra']
# ln = ['last', 'sharjeel', 'naeem']
# emails = [x + "." + y + "@gmail.com" for x, y in zip(fn, ln)]
# print('emails')
# print(emails)

import requests

r = requests.post('https://stagehrms.transemr.com/api/login', json={'username': "rao.sharjeel", 'password': 'passw'})
# r = requests.get('https://stagehrms.transemr.com/api/login', auth=("rao.sharjeel", 'password'))
print(r.status_code)
print(r.json())

# session = requests.Session()
# response = session.get('https://stagehrms.transemr.com/api/login', auth=('username', 'password'))
# print(response.status_code)
# print(response.json())