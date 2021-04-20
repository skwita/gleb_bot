import random

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


def send_nudes(vk, chat_id, message):
    vk.messages.send(chat_id=chat_id, random_id=get_random_id(), message=message)


def command_message(vk, chat_id, message, trolls, cfg):
    if message.lower() == '/пнуть глеба':
        send_nudes(vk, chat_id, 'Глеб, иди делать ' + str_tasks[random.randint(0, len(str_tasks) - 1)])
    if message.lower() == '/глеб':
        send_nudes(vk, chat_id, '@kok_magic')
    if message.lower() == '/затролить':
        send_nudes(vk, chat_id, trolls[random.randint(0, len(trolls) - 1)])
    if message.lower() == '/анекдот':
        send_nudes(vk, chat_id, str_anek)
    msg_split = message.split(' ')
    if msg_split[0].lower() == '/change_prob':
        prob_new = msg_split[1]
        cfg[1] = 'prob = ' + prob_new
        cfg_file = open('config.py', 'w', encoding='utf-8')
        cfg_file.writelines(cfg)
        cfg_file.close()
        send_nudes(vk, chat_id, 'done')


def common_message(vk, chat_id, gleb_phrases):
    file_cfg = open('config.py', encoding='utf-8')
    cfg = file_cfg.readlines()
    file_cfg.close()
    cfg_prob = cfg[1].split(' ')
    prob = int(cfg_prob[2])
    if random.randint(0, 9) < prob:
        if len(gleb_phrases) != 0:
            rand = random.randint(0, len(gleb_phrases) - 1)
            send_nudes(vk, chat_id, gleb_phrases[rand])
        else:
            send_nudes(vk, chat_id, 'Глеб пуст')
