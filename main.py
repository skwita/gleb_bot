import random
import re
from config import token
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id

vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, group_id=204095550)

file_inp = open('db_gleb.txt', encoding='utf-8')
temp = file_inp.readlines()
file_inp.close()

file_out = open('db_gleb.txt', 'a')
try:
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            if event.from_chat:
                text = event.object['message']['text']
                user_id = event.object['message']['from_id']
                result = re.search(r'гле', text.lower())
                if result:
                    vk.messages.send(
                        chat_id=event.chat_id,
                        random_id=get_random_id(),
                        message='@kok_magic'
                    )
                if user_id == 144779081 and not temp.__contains__(text):
                    temp.append(text)
                    file_out.write('\n' + temp[-1])
                if random.randint(0, 9) < 10:
                    if len(temp) != 0:
                        rand = random.randint(0, len(temp))
                        vk.messages.send(
                            random_id=get_random_id(),
                            message=temp[rand],
                            chat_id=event.chat_id
                        )
                    else:
                        vk.messages.send(
                            random_id=get_random_id(),
                            message='Глеб пуст',
                            chat_id=event.chat_id
                        )
except Exception as e:
    print(e)
