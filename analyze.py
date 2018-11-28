import re
import os
import string
import glob
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

    file_names = glob.glob("1155*")
    i = 0
    for file_name in file_names:
        analysis = []
        comment_dict = []
        
        with open(file_name) as f:
            print('File ', file_name, ':')
            for line in f:
                t = line.strip().lower();
                t = re.sub(r'[^\w\s]','',t)
                if (isNotNull (t)):
                    comment_dict.append(t)
            f.close()
            
            for i in range(len(comment_dict)):
                tokens = nltk.word_tokenize(comment_dict[i])
                neg_cnt = 0
                pos_cnt = 0

                neg_word=[]
                pos_word=[]
                for neg in neg_dict:
                    if (neg in tokens):
                        neg_cnt = neg_cnt +1
                        neg_word.append(neg)
                for pos in pos_dict:
                    if (pos in tokens):
                        pos_cnt = pos_cnt +1
                        pos_word.append(pos)
                analysis.append(pos_cnt - neg_cnt)     
                print('Comment', i, ' negative words matched: ',  neg_word)
                print('Comment', i, ' positive words matched: ', pos_word)
            print(analysis)
if __name__ == '__main__':
    main()
