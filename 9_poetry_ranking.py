# 本程序用于评判前五十首特征诗
import json
import os
import jieba

path = './json/'
files = os.listdir(path)

s_name = []
t_name = []
forward = 0

file1 = open('p.txt', 'r', encoding='utf-8')  # 正向感情词典
happy_list = file1.read().splitlines()

file1 = open('n.txt', 'r', encoding='utf-8')  # 负向感情词典
sad_list = file1.read().splitlines()

with open('evaluate.song.json', 'r', encoding='utf8')as fp:  # 读取数据
    json_song_ev = json.load(fp)
with open('evaluate.tang.json', 'r', encoding='utf8')as fp:  # 读取数据
    json_tang_ev = json.load(fp)
poetry = []
tang_ranking = []
song_ranking = []
rows = 0
for file in files:
    name_s = 'song'
    name_t = 'tang'
    new_name = path + file
    if name_s in file:
        with open(new_name, 'r', encoding='utf8')as fp:  # 读取数据
            json_data = json.load(fp)
        for i in range(len(json_data)):
            reply_number = ''.join(json_data[i]['paragraphs'])
            reply_name = json_data[i]['author']
            reply_title = json_data[i]['title']
            words2 = str(reply_number)
            words1 = jieba.lcut(words2)
            fuxiang = 0
            poetry = []
            t_core = 0
            if len(words1) > 150:
                continue
            for chara in words1:
                if chara in json_tang_ev:
                    t_core += json_tang_ev[chara]
                if chara in sad_list:
                    fuxiang += 1
            poetry.append(reply_title)
            poetry.append(reply_name)
            poetry.append(reply_number)
            poetry.append(t_core + forward)
            song_ranking.append(poetry)
    elif name_t in file:
        with open(new_name, 'r', encoding='utf8')as fp:  # 如果不是json的文件读取会报错
            json_data = json.load(fp)
        for i in range(len(json_data)):
            reply_number = ''.join(json_data[i]['paragraphs'])
            reply_name = json_data[i]['author']
            reply_title = json_data[i]['title']
            words2 = str(reply_number)
            words1 = jieba.lcut(words2)
            t_core = 0
            poetry = []
            if len(words1) > 150:
                continue
            for chara in words1:
                if chara in json_tang_ev:
                    t_core += json_tang_ev[chara]
                if chara in happy_list:
                    forward += 1
            poetry.append(reply_title)
            poetry.append(reply_name)
            poetry.append(reply_number)
            poetry.append(t_core + forward)
            tang_ranking.append(poetry)
    rows += 1
    print('已运行至第' + str(rows) + '个文件')     # 输出第多少个文件
data1 = sorted(song_ranking, key=lambda x: x[3], reverse=True)  # 排序
data2 = sorted(tang_ranking, key=lambda x: x[3], reverse=True)  # 排序
data1 = data1[0:50]
data2 = data2[0:50]
with open('songTop50.txt', 'w+', encoding='utf8') as fp:
    for i in range(50):
        a = data1[i]
        fp.write('第'+str(i+1)+'名'+' '+'词名:'+'《'+str(a[0])+'》'+' '+'作者:'+str(a[1])+' '+'词句:'+str(a[2]))
        fp.write('\n')
with open('tangTop50.txt', 'w+', encoding='utf8') as fp:
    for i in range(50):
        a = data2[i]
        fp.write('第'+str(i+1)+'名'+' '+'诗名:'+'《'+str(a[0])+'》'+' '+'作者:'+str(a[1])+' '+'词句:'+str(a[2]))
        fp.write('\n')
