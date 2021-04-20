import random
import re
from config import token
from methodes import *
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id

vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, group_id=204095550)

file_inp = open('db_gleb.txt', encoding='utf-8')
temp = file_inp.readlines()
file_inp.close()


def send_nudes(chat_id, message):
    vk.messages.send(chat_id=chat_id, random_id=get_random_id(), message=message)


while True:
    try:
        for event in longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                file_out = open('db_gleb.txt', 'a', encoding='utf-8')
                if event.from_chat:
                    text = event.object['message']['text']
                    user_id = event.object['message']['from_id']
                    result = re.search(r'гле', text.lower())
                    if result:
                        send_nudes(event.chat_id, '@kok_magic')
                    result = re.search(r'анек', text.lower())
                    str_anek = 'Поймали инопланетяне китайца, француза и русского, и посадили китайца в квадратную комнату, француза - в треугольную, а русского - в круглую.\n \
                            И говорят: "кто желание загадает, и мы его выполним, того мы мозги съедим, если не сможем - отпустим." \
                            Китаец говорит:\n\
                            — наполните комнату рыбой.\n\
                            Инопланетяне выполнили...\n\
                            Француз говорит:\n\
                            — наполните комнату деньгами.\n\
                            Инопланетяне выполнили...\n\
                            Русский говорит:\n\n\n — насри в угол...'
                    if result:
                        vk.messages.send(
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message=str_anek
                        )
                    if (user_id == 144779081 or user_id == 54849868) and not temp.__contains__(text):
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
                file_out.close()
    except Exception as e:
        print(e)
