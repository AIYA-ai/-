# 本程序用于绘制网络连接图
import json
import networkx as nx
import matplotlib.pyplot as plt


def calc_color(c: float):  # 自动匹配颜色
    # 红 - 绿 - 蓝
    # 大 - 中 - 小
    c = 1 - c
    r = 0x0
    b = 0x0
    if c < 0.5:
        c *= 2
        g = 0xFF * c
        r = 0xFF - g

    else:
        c = (c - 0.5) * 2
        b = 0xFF * c
        g = 0xFF - b
    r = int(r)
    g = int(g)
    b = int(b)
    return "#%02X%02X%02X" % (r, g, b)


with open('occurrence.song.times.json', 'r', encoding='utf8')as fp:  # 读取数据
    json_song_ev = json.load(fp)
    json_song_ev1 = json_song_ev[0:100:2]
with open('occurrence.tang.times.json', 'r', encoding='utf8')as fp:  # 读取数据
    json_tang_ev = json.load(fp)
    json_tang_ev1 = json_tang_ev[0:100:2]


def draw_network(json_ev, x):
    print('运行中...')
    G = nx.Graph()
    plt.subplots(figsize=(9, 9))
    zhh = []
    a_size = 0
    for i in json_ev:
        zh = i
        a_size += zh[2]
    for i in json_ev:
        zh = i
        zh1 = zh[0:2]
        if zh1[0] not in zhh:
            zhh.append(zh1[0])
            G.add_node(zh1[0])
        if zh1[1] not in zhh:
            zhh.append(zh1[1])
            G.add_node(zh1[1])
    pos = nx.circular_layout(G)
    for i in json_ev:
        zh = i
        size = zh[2] / a_size * 10
        options = {
            "node_color": calc_color(size * 2),
            "nodelist": [zh[0]],
            "node_size": size * 5000,
            'with_labels': True
        }
        options1 = {
            "node_color": calc_color(size * 2),
            "nodelist": [zh[1]],
            "node_size": size * 5000,
            'with_labels': True
        }
        if zh[0] in zhh:
            nx.draw_networkx(G, pos=pos, **options)
            js = 0
            for j in zhh:
                if j == zh[0]:
                    zhh[js] = ''
                js += 1
        if zh[1] in zhh:
            nx.draw_networkx(G, pos=pos, **options1)
            js = 0
            for j in zhh:
                if j == zh[1]:
                    zhh[js] = ''
                js += 1
        nx.draw_networkx_edges(
            G,
            pos,
            edgelist=[(zh[0], zh[1])],
            width=size * 10,
            alpha=0.5,
            edge_color=calc_color(size),
        )
    if x == 1:
        plt.title('唐代词共现图')  # 绘制标题
        plt.savefig('唐代词共现图')  # 保存图片
    else:
        plt.title('宋代词共现图')  # 绘制标题
        plt.savefig('宋代词共现图')  # 保存图片
    plt.show()
    print('运行成功')


draw_network(json_tang_ev1, 1)
draw_network(json_song_ev1, 2)
