import random
import re
import traceback

from config import token
from methods import *
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id

vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, group_id=204095550)

file_inp = open('db_gleb.txt', encoding='utf-8')
gleb_phrases = file_inp.readlines()
file_inp.close()

troll_file = open('trolling.txt', encoding='utf-8')
trolls = troll_file.readlines()
troll_file.close()

cfg_file = open('config.py')
cfg = cfg_file.readlines()
cfg_file.close()


dict_commands = {'/пнуть глеба',
                 '/глеб',
                 '/затролить',
                 '/анекдот',
                 '/change_prob'}


while True:
    try:
        for event in longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                file_out = open('db_gleb.txt', 'a', encoding='utf-8')
                if event.from_chat:
                    text = event.object['message']['text']
                    user_id = event.object['message']['from_id']

                    is_command = False
                    for key in dict_commands:
                        if re.search(key, text.lower()):
                            is_command = True

                    if is_command:
                        command_message(vk, event.chat_id, text, trolls, cfg)
                    else:
                        if (user_id == 144779081 or user_id == 54849868) and not gleb_phrases.__contains__(text):
                            gleb_phrases.append(text)
                            file_out.write('\n' + gleb_phrases[-1])
                        common_message(vk, event.chat_id, gleb_phrases)
                file_out.close()
    except Exception as e:
        print(e)
        traceback.print_exc(limit=None, file=None, chain=True)
