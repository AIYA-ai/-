# 该程序用于统计词频数
import json
import os
import jieba

path = './json/'
files = os.listdir(path)
data1 = {}
data2 = {}
exclude = ['[', ']', ' ', ',', "'", '。', '，', '《', '》', '）', '（', '「', '」', '：', '', '？', '□', '、', '：', '〖',
           '〗', '？', '“', '”', '『', '』', '']  # 无效字符排除
file1 = open('stop_words.txt', 'r', encoding='utf-8')  # 停用词
stop_list = file1.read().splitlines()
tangs = []
songs = []
rows = 0
s_name = 'song'
t_name = 'tang'

for file in files:
    if s_name in file:  # 读取宋朝的数据
        new_name = path+file
        with open(new_name, 'r', encoding='utf8')as fp:  # 读取数据
            json_data = json.load(fp)
        for i in range(len(json_data)):     # 依次读取字典中数据
            reply_number = json_data[i]['paragraphs']  # 获取诗词
            words2 = str(reply_number)      # 转成字符串型，不转无法识别
            words1 = jieba.lcut(words2)     # 使用结巴工具进行分词
            for chara in words1:            # words是当前的分好段的诗，chara为其中的字或词
                if chara in stop_list:        # 如果是无效字符跳过处理
                    continue
                if chara in exclude:        # 如果是无效字符跳过处理
                    continue
                if len(chara) > 2:          # 只取长度小于等于2的字词
                    continue
                if chara in data1:          # 如果该词已经存储过，则对其进行+1操作
                    data1[chara] += 1
                else:
                    data1[chara] = 1        # 没有就添加该词
    elif t_name in file:    # 读取唐朝的数据
        new_name = path + file      # 文件路径
        with open(new_name, 'r', encoding='utf8')as fp:  # 读取数据
            json_data = json.load(fp)
        for i in range(len(json_data)):
            reply_number = json_data[i]['paragraphs']
            words2 = str(reply_number)
            words1 = jieba.lcut(words2)
            for chara in words1:
                if chara in exclude:
                    continue
                if len(chara) > 2:
                    continue
                if chara in data2:
                    data2[chara] += 1
                else:
                    data2[chara] = 1
    rows += 1
    print('已运行至第' + str(rows) + '个文件')     # 输出第多少个文件
data_z = sorted(data1.items(), key=lambda x: x[1], reverse=True)  # 排序
filed = 'poet.' + s_name + '.times.json'  # 保存文件路径
file_w = open(filed, 'w')   # 打开文件
json_str = json.dumps(data_z)   # 保存的数据
file_w.write(json_str)
file_w.close()
data_z = sorted(data2.items(), key=lambda x: x[1], reverse=True)  # 排序
filed = 'poet.' + t_name + '.times.json'  # 保存文件路径
file_w = open(filed, 'w')   # 打开文件
json_str = json.dumps(data_z)  # 保存的数据
file_w.write(json_str)
file_w.close()
