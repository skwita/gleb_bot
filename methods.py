import random
import re
from vk_api.utils import get_random_id

str_tasks = ['теорвер', 'едсак', 'риск', 'расчетки', 'схемач', 'тесты', 'прогу', 'проект']
str_anek = 'Поймали инопланетяне китайца, француза и русского, и посадили китайца в квадратную комнату,' \
           ' француза - в треугольную, а русского - в круглую.\n \
            И говорят: "кто желание загадает, и мы его выполним,' \
           ' того мы мозги съедим, если не сможем - отпустим." \
            Китаец говорит:\n\
            — наполните комнату рыбой.\n\
            Инопланетяне выполнили...\n\
            Француз говорит:\n\
            — наполните комнату деньгами.\n\
            Инопланетяне выполнили...\n\
            Русский говорит:\n\n\n — насри в угол...'

str_fart = ['пёр', 'пер', 'пук', 'бзд', 'шепт', 'шёпт', 'пшик', 'запустить газовую станцию' ]

def send_nudes(vk, chat_id, message):
    vk.messages.send(chat_id=chat_id, random_id=get_random_id(), message=message)


def command_message(vk, chat_id, message, user_id):
    file_cfg = open('config.txt', encoding='utf-8')
    cfg = file_cfg.readlines()
    file_cfg.close()
    if message.lower() == '/пнуть глеба':
        send_nudes(vk, chat_id, 'Глеб, иди делать ' + str_tasks[random.randint(0, len(str_tasks) - 1)])
    if re.search(r'гле', message):
        send_nudes(vk, chat_id, '@kok_magic')
    if message.lower() == '/затролить':
        cfg[2] = 'is_trolling_on = True\n'
        cfg_file = open('config.txt', 'w', encoding='utf-8')
        cfg_file.writelines(cfg)
        cfg_file.close()
        send_nudes(vk, chat_id, 'Глебу лучше перестать писать, иначе его отхуесосят по полной')
    if message.lower() == '/закончить тролинг' and user_id != 144779081:
        cfg[2] = 'is_trolling_on = False\n'
        cfg_file = open('config.txt', 'w', encoding='utf-8')
        cfg_file.writelines(cfg)
        cfg_file.close()
        send_nudes(vk, chat_id, 'Глеб может расслабиться')
    if message.lower() == '/анекдот':
        send_nudes(vk, chat_id, str_anek)
    msg_split = message.split(' ')
    if msg_split[0].lower() == '/change_prob':
        prob_new = msg_split[1]
        cfg[1] = f'prob = {prob_new}\n'
        cfg_file = open('config.txt', 'w', encoding='utf-8')
        cfg_file.writelines(cfg)
        cfg_file.close()
        send_nudes(vk, chat_id, 'done')


def is_po_desytkam(message):
    for root in str_fart:
        if re.search(fr'{root}', message):
            return True
    return False


def po_desytkam(vk, chat_id):
    send_nudes(vk, chat_id, 'По десяткам!')


def check_gleb(vk, chat_id, message):
    file_cfg = open('config.txt', encoding='utf-8')
    cfg = file_cfg.readlines()
    file_cfg.close()
    if cfg[3].split(' ')[2][:-1] == 'False':
        if cfg[4].split(' ')[2][:-1] == 'True':
            if re.search(r'не', message.lower()):
                send_nudes(vk, chat_id, 'Плохо....')
            elif re.search(r'да', message.lower()) or re.search(r'конечно', message.lower()) or re.search(r'отчислили',
                                                                                                    message.lower()):
                send_nudes(vk, chat_id, 'Харош')
            else:
                send_nudes(vk, chat_id, 'Не понял...')
            cfg[3] = 'is_written = True\n'
            cfg[4] = 'is_wait = False\n'
            cfg_file = open('config.txt', 'w', encoding='utf-8')
            cfg_file.writelines(cfg)
            cfg_file.close()
        else:
            send_nudes(vk, chat_id, 'Кстати, Глеба отчислили?')
            cfg[4] = 'is_wait = True\n'
            cfg_file = open('config.txt', 'w', encoding='utf-8')
            cfg_file.writelines(cfg)
            cfg_file.close()
        return True
    return False

def common_message(vk, chat_id, gleb_phrases, trolls, user_id):
    file_cfg = open('config.txt', encoding='utf-8')
    cfg = file_cfg.readlines()
    file_cfg.close()
    cfg_prob = cfg[1].split(' ')
    prob = int(cfg_prob[2])
    cfg_is_trolling_on = cfg[2].split(' ')
    is_trolling_on = cfg_is_trolling_on[2] == 'True\n'
    if is_trolling_on:
        if user_id == 144779081:
            send_nudes(vk, chat_id, trolls[random.randint(0, len(trolls) - 1)])
    elif random.randint(0, 9) < prob:
        if len(gleb_phrases) != 0:
            rand = random.randint(0, len(gleb_phrases) - 1)
            send_nudes(vk, chat_id, gleb_phrases[rand])
        else:
            send_nudes(vk, chat_id, 'Глеб пуст')
