import json
import matplotlib.pyplot as plt
from wordcloud import WordCloud


def create_word_cloud(name):
    path = 'evaluate.out.' + name + '.json'
    with open(path, encoding='utf-8') as f:
        data = json.load(f)
    wc = WordCloud(
        font_path="simsun.ttc",
        background_color='white',
        width=800,
        height=800
    )
    wc.generate_from_frequencies(data)
    plt.figure()
    plt.imshow(wc)
    plt.axis('off')
    plt.show()
    wc.to_file(name + '_draw_word_cloud.png')


create_word_cloud('tang')
create_word_cloud('song')
