#!/usr/bin/python

#import urllib2
import sys
import random
from collections import Counter
from collections import defaultdict
import jieba.posseg as pseg

ngram       = 2
line_num    = 0
line_limit  = 2000
words_list  = []
lan_model   = defaultdict(Counter) 
with open("hapness.txt","r") as src:
#with open("test.txt","r") as src:
    for each_line in src:
        line_num += 1
        if(line_num>line_limit):
            break
        words = pseg.cut(each_line.strip())
#        for word in words:
#            #if(flag != 'x'):
#            lb[word.encode('utf-8')] += 1
        words = [i.word.encode('utf-8') for i in words]
        for i in range(len(words)):
            words_list.append(words[i])
for i in range(ngram,len(words_list)) :
    context = tuple(words_list[i-ngram:i])
    word    = words_list[i]
    lan_model[context][word] += 1

#-----------"""统计词频，并获得条件概率"""------------#
def get_forward_word(start_tuple):
    for context,context_cnt in lan_model.items():
        context_sum = float(sum(context_cnt.values()))
        rand_value = random.random()
        pro = 0.0
        if(start_tuple == context):
            for word,word_cnt in context_cnt.items():
                lan_model[context][word] = word_cnt/context_sum
                pro += word_cnt/context_sum
                if (pro > rand_value):
                    words = []
                    for i in range(1,ngram):
                        words.append(start_tuple[i])
                    words.append(word)
                    return tuple(words)

#------------------采样首词------------------#
sentence =  ''
start_tuple_idx = random.randint(0,len(words_list)-ngram)
start_tuple     = tuple(words_list[start_tuple_idx:start_tuple_idx + ngram])
for i in range(ngram):
    sentence += start_tuple[i] 

#------------------生成语句------------------#
for i in range(300):
    if(i == 0): 
        re_tuple = get_forward_word(start_tuple)
    else :
        re_tuple = get_forward_word(re_tuple)
    sentence += re_tuple[ngram - 1]

print sentence                                                                               
