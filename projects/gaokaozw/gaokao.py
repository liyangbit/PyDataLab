# -*- coding: utf-8 -*-
"""
@author: lemon
"""

import jieba
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS
import matplotlib.pyplot as plt
import os
import PIL.Image as Image
import numpy as np

# 读取文本内容

with open('gaokao.txt', 'rb') as f:
    text = f.read()
    f.close()


# with open('2007-2016.txt', 'rb') as f:
#     text = f.read()
#     f.close()
#
# with open('1997-2006.txt', 'rb') as f:
#     text = f.read()
#     f.close()

# with open('1987-1996.txt', 'rb') as f:
#     text = f.read()
#     f.close()

# with open('1977-1986.txt', 'rb') as f:
#     text = f.read()
#     f.close()

# 加载自定义词典
# jieba.load_userdict(r"C:\Users\Administrator\AppData\Roaming\Python\Python35\site-packages\jieba\userdict.txt")


# 首先使用 jieba 中文分词工具进行分词
wordlist = jieba.cut(text, cut_all=False)      
# cut_all, True为全模式，False为精确模式
     
wordlist_space_split = ' '.join(wordlist)

d = os.path.dirname(__file__)
alice_coloring = np.array(Image.open(os.path.join(d,'orange.jpg')))
# my_wordcloud = WordCloud(background_color='#000000', max_words=300, mask=alice_coloring,
#                          max_font_size=300, random_state=42).generate(wordlist_space_split)


# 加载常用停用词
stopwords1 = [line.rstrip() for line in open('./中文停用词库.txt', 'r', encoding='utf-8')]
stopwords2 = [line.rstrip() for line in open('./哈工大停用词表.txt', 'r', encoding='utf-8')]
stopwords3 = [line.rstrip() for line in open('./四川大学机器智能实验室停用词库.txt', 'r', encoding='utf-8')]

# 添加自定义停用词
stopwords_user1 = set([x.strip() for x in open(
    os.path.join(os.path.dirname(__file__), 'stopwords_user')).read().split('\n')])

stopwords_user = set(stopwords1) | set(stopwords2) | set(stopwords3) | set(stopwords_user1)


# 对分词后的文本生成词云
my_wordcloud = WordCloud(background_color='#000000',
                         max_words=100,
                         font_step=1,
                         mask=alice_coloring,
                         random_state= 30, # 设置有多少种随机生成状态，即有多少种配色方案
                         max_font_size=300,
                         stopwords=stopwords_user, # 停用词的类型为set
                         )

# Generate word cloud
my_wordcloud.generate(wordlist_space_split)

image_colors = ImageColorGenerator(alice_coloring)

plt.show(my_wordcloud.recolor(color_func=image_colors))
plt.imshow(my_wordcloud)            # 以图片的形式显示词云
plt.axis('off')                     # 关闭坐标轴
plt.show()

# my_wordcloud.to_file(os.path.join(d, 'gaokao_1977_1986_colors_cloud.jpg'))
# my_wordcloud.to_file(os.path.join(d, 'gaokao_1987_1996_colors_cloud.jpg'))
# my_wordcloud.to_file(os.path.join(d, 'gaokao_1997_2006_colors_cloud.jpg'))
my_wordcloud.to_file(os.path.join(d, 'gaokao_orange_cloud.jpg'))