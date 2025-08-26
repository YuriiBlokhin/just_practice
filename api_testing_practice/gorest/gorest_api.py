# import requests
# import os
# from dotenv import load_dotenv
# load_dotenv()
#
# url = 'https://gorest.co.in/'
#
# def create_user():
#     payload = {"name":"Tenali Ramakrishna",
#                "gender":"male",
#                "email":"tenali.ramakrishna@15ce.com",
#                "status":"active"
#                }
#
#     headers = {'Content-Type': 'application/json',
#
#                }
#
#
#     response = requests.post(f'{url}public/v2/users', auth=os.getenv('TOKEN'), json=payload)
#     print(response.status_code)