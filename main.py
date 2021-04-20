import re
import traceback
import time

from methods import *
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


file_inp = open('db_gleb.txt', encoding='windows-1251')
gleb_phrases = file_inp.readlines()
file_inp.close()

troll_file = open('trolling.txt', encoding='utf-8')
trolls = troll_file.readlines()
troll_file.close()

cfg_file = open('config.txt')
cfg = cfg_file.readlines()
cfg_file.close()

dict_commands = {'/пнуть глеба',
                 'гле',
                 '/затролить',
                 '/анекдот',
                 '/change_prob',
                 '/закончить тролинг'}

token = cfg[0].split(' ')[2][:-1]
vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, group_id=204095550)

while True:
    try:
        for event in longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                file_out = open('db_gleb.txt', 'a', encoding='utf-8')
                if event.from_chat:
                    text = event.object['message']['text']
                    user_id = event.object['message']['from_id']

                    hour = int(time.ctime().split(' ')[3].split(':')[0])
                    if hour < 18:
                        if check_gleb(vk, event.chat_id, text):
                            continue
                    else:
                        cfg[3] = 'is_written = False\n'
                        cfg[4] = 'is_wait = False\n'
                        cfg_file = open('config.txt', 'w', encoding='utf-8')
                        cfg_file.writelines(cfg)
                        cfg_file.close()

                    is_command = False
                    for key in dict_commands:
                        if re.search(key, text.lower()):
                            is_command = True
                    if is_po_desytkam(text):
                        po_desytkam(vk, event.chat_id)
                    elif is_command:
                        command_message(vk, event.chat_id, text, user_id)
                    elif user_id == 144779081 and not gleb_phrases.__contains__(text):
                        gleb_phrases.append(text)
                        file_out.write('\n' + gleb_phrases[-1])
                        common_message(vk, event.chat_id, gleb_phrases, trolls, user_id)
                    else:
                        common_message(vk, event.chat_id, gleb_phrases, trolls, user_id)
                file_out.close()
    except Exception as e:
        print(e)
        traceback.print_exc(limit=None, file=None, chain=True)
