# 本程序的作用是区分统计唐宋的悲喜诗
import json
import os
import jieba

file1 = open('p.txt', 'r', encoding='utf-8')  # 正向词典
happy_list = file1.read().splitlines()
# print(happy_list)

file1 = open('n.txt', 'r', encoding='utf-8')  # 负向词典
sad_list = file1.read().splitlines()
# print(sad_list)

path = './json/'
files = os.listdir(path)

tangs = []
songs = []
rows = 0

forward = 0
happy_song = 0
happy_tang = 0
sad_tang = 0
sad_song = 0
for file in files:
    s_name = 'song'
    t_name = 'tang'
    if s_name in file:
        new_name = path+file
        with open(new_name, 'r', encoding='utf8')as fp:  # 读取宋数据
            json_data = json.load(fp)
        for i in range(len(json_data)):
            reply_number = json_data[i]['paragraphs']
            words2 = str(reply_number)
            words1 = jieba.lcut(words2)
            forward = 0
            negative = 0
            for chara in words1:
                if len(chara) > 2:
                    continue
                if chara in happy_list:
                    forward += 1
                if chara in sad_list:
                    negative += 1
            if forward > negative:
                happy_song += 1
            else:
                sad_song += 1
    elif t_name in file:
        new_name = path + file
        with open(new_name, 'r', encoding='utf8')as fp:  # 读取唐数据
            json_data = json.load(fp)
        for i in range(len(json_data)):
            reply_number = json_data[i]['paragraphs']
            words2 = str(reply_number)
            words1 = jieba.lcut(words2)
            forward = 0
            negative = 0
            for chara in words1:
                if len(chara) > 2:
                    continue
                if chara in happy_list:     # chara 在 正向中
                    forward += 1            # 正向+1
                if chara in sad_list:       # chara 在 正向中
                    negative += 1           # 负向+1
            if forward > negative:          # 比较大小
                happy_tang += 1             # 总唐喜类型的诗的数量
            elif forward < negative:
                sad_tang += 1               # 总唐悲类型的诗的数量
    rows += 1
    print('已运行至第' + str(rows) + '个文件')     # 输出第多少个文件
print('喜类型诗数量：', happy_song, '喜类型诗数量：', happy_tang)
print('悲类型诗数量：', sad_song, '悲类型诗数量：', sad_tang)
