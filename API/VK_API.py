import requests
import os

from pprint import pprint
from dotenv import load_dotenv
load_dotenv()

'''vk_response = requests.get('https://oauth.vk.com/authorize?scope=friends&response_type=token&v=5.92&client_id=7803468')
pprint(vk_response.text)'''

auth_token = os.getenv("TOKEN")
vk_api = requests.get(f'https://api.vk.com/method/users.get?user_ids=USER_ID&v=5.92&access_token={auth_token}')
#print(vk_api.text)


def get_friends(user_id):
    data = {
        # ваш код здесь
    }
    friends_list = requests.post(f'https://api.vk.com/method/friends.get?user_id=531301803&v=5.92&access_token={auth_token}')
    return friends_list.json()['response']


print(get_friends(531301803))
# запрашиваем список друзей пользователя с ID 531301803