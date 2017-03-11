#!/usr/bin/python
#-+- coding: utf-8 -+-

import urllib2
import jieba
#import sys

str_lst = []
word_dic = {}

try:
    s = urllib2.urlopen("https://raw.githubusercontent.com/OpenMindClub/DeepLearningStartUp/master/happiness_seg.txt").read()
except urllib2.HTTPError,e:
    print e.code
except urllib2.URLError,e:
    print str(e)

#txt文件input，for test
#s  = open(sys.argv[1],"r").read().strip()

seg_list = jieba.cut(s,cut_all=True) 

for word in seg_list :
    str_lst.append(word)
    word_dic[word] = 0

token = " 。！？：；、，》《（） \n".decode('utf-8')
filter_seg = [fil for fil in str_lst if fil not in token]
for word in filter_seg:
    word_dic[word] = word_dic[word] + 1

word_lst = sorted(word_dic.iteritems(),key=lambda d:d[1],reverse=True)
for i in range(10):
    print word_lst[i][0],":",word_lst[i][1]
