import re
import os
import string
import nltk


def isNotNull(value):
    return value is not None and len(value)>0

def main():

    pos_dict = []
    neg_dict = []
    comment_dict = []
    
    f = open('./positive-words.txt', 'r')

    for line in f:
        if not re.match(";", line):
            t = line.strip().lower();
            if (isNotNull(t)):
                pos_dict.append(t)
    f.close()

    f = open('./negative-words.txt', 'r')
    
    for line in f:
        if not re.match(";", line):
            t = line.strip().lower();
            if (isNotNull(t)):
                neg_dict.append(t)
    f.close()
    
    f = open('./1155123051.txt', encoding="utf8")
    
    for line in f:
        t = line.strip().lower();
        t = re.sub(r'[^\w\s]','',t)
        if (isNotNull (t)):
            comment_dict.append(t)
    f.close()

    #analysis_for_pos = []
    #for i in range(len(Bing_senti)):
    #    tokens = nltk.word_tokenize(pos_content[i])
    #    neg_cnt = 0
    #   pos_cnt = 0
    #    for neg in dict_neg:
    #        if (neg in tokens):
    #            neg_cnt = neg_cnt +1
    #    for pos in dict_pos:
    #        if (pos in tokens):
    #            pos_cnt = pos_cnt +1
    #    analysis_for_pos.append(pos_cnt - neg_cnt)     
    #   Bing_senti['Bing_analysis_for_pos'] = analysis_for_pos
    
if __name__ == '__main__':
    main()
