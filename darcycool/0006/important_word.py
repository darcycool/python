# -*- coding: utf-8 -*-
# 第 0006 题： 你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。
import operator
import os
import re

rootDir = 'diary/'


def count_words(filename, words):
    wordDict = dict()
    for word in words:
        if word.lower() in wordDict:
            wordDict[word.lower()] += 1
        else:
            wordDict[word.lower()] = 1
    print('%s word:%s' % (filename, max(wordDict.items(), key=operator.itemgetter(1))[0]))


for top, dirnames, filenames in os.walk(rootDir):
    for filename in filenames:
        file = open(rootDir + filename, 'r')
        str = file.read()
        reObj = re.compile('\b?(\w+)\b?')
        words = reObj.findall(str)
        count_words(filename, words)

from collections import Counter

for top, dirnames, filenames in os.walk(rootDir):
    for filename in filenames:
        file = open(rootDir + filename, 'r')
        str = file.read()
        reObj = re.compile('\b?(\w+)\b?')
        words = reObj.findall(str)
        words = map(lambda w: w.lower(), words)
        print(filename, Counter(words).most_common(1))
