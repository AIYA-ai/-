# 该程序用于测试高频词特征判断分类唐宋诗准确度
import json
import os
import jieba

path = './json/'
files = os.listdir(path)

s_name_list = []    # 宋名字列表
t_name_list = []    # 唐名字列表
error_t = 0     # 唐错误得分
error_s = 0     # 宋错误得分
t_core = 0      # 唐得分
s_core = 0      # 宋得分
unknown = 0     # 未知分类
s_t_all_score = 0  # 宋唐总分正确数
score_all_t = 0     # 唐正确分类数
score_all_s = 0     # 宋正确分类数

with open('evaluate.song.json', 'r', encoding='utf8')as fp:  # 读取宋高频词权值数据
    json_song_ev = json.load(fp)
with open('evaluate.tang.json', 'r', encoding='utf8')as fp:  # 读取唐高频词权值数据
    json_tang_ev = json.load(fp)
with open('authors.song.json', 'r', encoding='utf8')as fp:  # 读取作者数据
    json_song_au = json.load(fp)
with open('authors.tang.json', 'r', encoding='utf8')as fp:  # 读取作者数据
    json_tang_au = json.load(fp)
for i in range(len(json_song_au)):
    reply_name = json_song_au[i]['name']
    s_name_list.append(reply_name)    # 只获取作者名，根据作者所在朝代判断对诗的分类是否正确
for i in range(len(json_tang_au)):
    reply_name = json_tang_au[i]['name']
    t_name_list.append(reply_name)
print(s_name_list)
print(t_name_list)
for file in files:
    s_name = 'song'
    t_name = 'tang'
    if t_name in file or s_name in file:
        new_name = path + file
        with open(new_name, 'r', encoding='utf8')as fp:  # 读取诗词数据
            json_data = json.load(fp)
        for i in range(len(json_data)):
            reply_number = json_data[i]['paragraphs']   # 获取诗词
            reply_name = json_data[i]['author']    # 获取作者名
            words2 = str(reply_number)      # 转成字符串型，不转无法识别
            words1 = jieba.lcut(words2)     # 使用结巴工具进行分词
            t_core = 0    # 唐得分重置
            s_core = 0    # 宋得分重置
            for chara in words1:    # words是当前的分好段的诗，chara为其中的字或词
                if chara in json_tang_ev:   # 如果chara在唐高频词中
                    t_core += json_tang_ev[chara]  # 唐得分加上该数的权重值
                if chara in json_song_ev:   # 如果chara在宋高频词中
                    s_core += json_song_ev[chara]  # 宋得分加上该数的权重值
            if t_core > s_core:  # 如果唐得分高

                if reply_name in t_name_list:  # 如果作者在唐作者中
                    score_all_t += 1          # 正确值+1
                elif reply_name in s_name_list:
                    score_all_s += 1        # 反之错误值+1
            elif t_core < s_core:            # 如果宋得分高
                if reply_name in s_name_list:  # 如果作者在宋作者中
                    error_s += 1 # 正确值+1
                elif reply_name in t_name_list:
                    error_t += 1            # 错误值+1
            else:
                unknown += 1             # 当唐得分和宋得分一样高时，unknown+1
    print('唐诗正确个数：', score_all_t, '宋词正确个数：', score_all_s,  '唐诗错误个数：', error_t, '宋词错误个数：', error_s, '未知错误个数：', unknown)
    if (score_all_s + score_all_t) != 0:
        print('总正确率', (score_all_s + score_all_t) / (score_all_s + score_all_t + error_t + error_s + unknown))
        print('宋正确率', (score_all_s) / (score_all_s + error_s ))
        print('唐正确率', (score_all_t) / (score_all_t + error_t))
