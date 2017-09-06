# -*- coding: utf-8 -*-
"""
Created on Wed May 17 2017

@author: lemon
"""

import jieba
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
import os
import PIL.Image as Image
import numpy as np


with open('brief_quanguo.txt', 'rb') as f: # 读取文件内容
    text = f.read()
    f.close()


# 首先使用 jieba 中文分词工具进行分词
wordlist = jieba.cut(text, cut_all=False)      
# cut_all, True为全模式，False为精确模式
     
wordlist_space_split = ' '.join(wordlist)

d = os.path.dirname(__file__)
alice_coloring = np.array(Image.open(os.path.join(d,'colors.png')))
my_wordcloud = WordCloud(background_color='#F0F8FF', max_words=100, mask=alice_coloring,
                         max_font_size=300, random_state=42).generate(wordlist_space_split)

image_colors = ImageColorGenerator(alice_coloring)

plt.show(my_wordcloud.recolor(color_func=image_colors))
plt.imshow(my_wordcloud)            # 以图片的形式显示词云
plt.axis('off')                     # 关闭坐标轴
plt.show()

my_wordcloud.to_file(os.path.join(d, 'brief_quanguo_colors_cloud.png'))