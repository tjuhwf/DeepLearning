#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

word_dic   = {}
word2_list = []
file_hande = open(sys.argv[1],"r")
word_list  = file_hande.read().replace('\n',' ').split(' ')
#
for i in range(len(word_list)-2):
    if(len(word_list[i]) == 4 and len(word_list[i+1]) == 4):
        tmp_list  = []
        tmp_list.append(word_list[i])
        tmp_list.append(' ')
        tmp_list.append(word_list[i+1])
        tmp  =  word_list[i]+' '+word_list[i+1]
        word2_list.append(tmp)
        word_dic[tmp] = 0	
#		
for word in word2_list:
    word_dic[word] = word_dic[word] + 1
#	
new_word_list = sorted(word_dic.iteritems(), key=lambda d:d[1],reverse=True)
#
for i in range(10):
    print new_word_list[i][0],":",new_word_list[i][1]