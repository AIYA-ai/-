# 该程序用于对词频计算权值
import json

tangs = {}
songs = {}
s_score = 0
t_score = 0
weight_s = 0
weight_t = 0
all_num = 0
high_word = 1000
out_s = {}
out_t = {}
with open('poet.tang.times.json', 'r', encoding='utf8')as fp:  # 读取词频数据
    json_data = json.load(fp)
json_tang = json_data[0:high_word]   # 取前2000的高频词
with open('poet.song.times.json', 'r', encoding='utf8')as fp:  # 读取词频数据
    json_data = json.load(fp)
json_song = json_data[0:high_word]

for i in json_song:
    s_score += i[1]     # 宋词高频词总频次
for i in json_tang:
    t_score += i[1]     # 唐诗高频词总频次
for i in range(high_word+1):
    all_num += i
weight1 = 1    # 用于设置两个指标的权重
weight2 = 1    # 用于设置两个指标的权重
ranking = 0       # 用于记录当前的高频词排名

for i, j in json_tang:  # i为 字名，j为出现次数
    ranking += 1
    json_song1 = dict(json_song)  # 需要将读取的数据转换为字典才能进行匹配判断
    if i not in json_song1:
        weight_s = (high_word - ranking) / all_num     # 归一化操作，根据字的排名
        tangs[i] = weight1 * weight_s + weight2 * (j / t_score)
        out_t[i] = j
    else:
        weight_s = (high_word - ranking) / all_num    # 归一化操作，根据字的排名，减轻两个数据中相同字的权值
        tangs[i] = weight1 * weight_s
ranking = 0
for i, j in json_song:
    ranking += 1
    json_tang1 = dict(json_tang)
    if i not in json_tang1:         # 在宋高频词里的，不在唐高频词里的
        weight_t = (high_word - ranking) / all_num /10
        songs[i] = weight1 * weight_t  # 第二指标为字出现的频率/总频率
        out_s[i] = j
    else:
        weight_t = (high_word - ranking) / all_num
        songs[i] = weight1 * weight_t + weight2 * j / s_score      # 第二指标为字出现的频率/总频率，同样要减轻两个数据中相同字的权值
print('唐高频词权值：', tangs)
print('宋高频词权值：', songs)
file_w = open('evaluate.song.json', 'w')  # 存储数据
json_str = json.dumps(songs)
file_w.write(json_str)
file_w.close()
file_w = open('evaluate.tang.json', 'w')
json_str = json.dumps(tangs)
file_w.write(json_str)
file_w.close()
file_w = open('evaluate.out.song.json', 'w')
json_str = json.dumps(out_s)
file_w.write(json_str)
file_w.close()
file_w = open('evaluate.out.tang.json', 'w')
json_str = json.dumps(out_t)
file_w.write(json_str)
file_w.close()
