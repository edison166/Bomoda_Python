# -*- coding: UTF-8 -*-
#!/usr/bin/python
import codecs
import os
import json
import jieba
import sys;
reload(sys);
sys.setdefaultencoding('utf8');

def WordCount3(rootDir,word,topnum):

    termDict = {}
       
    for root,dirs,files in os.walk(rootDir):
        for filespath in files:
            filename = os.path.join(root,filespath)
            if filename.find('.json') != -1:
                fileobj = open(filename,'r')
                tmp = fileobj.readline()
                line = json.loads(tmp)
                text = line['text']
                # convert to the unique form
                text = text.replace(' ', ''); 
                text = text.lower()
                if text.find(word) != -1:
                    seg_list = list(jieba.cut(text))
                    #term count
                    for term in seg_list:
                        #if term is a chinese word, whose length is at least 2
                        if len(term) >= 2 and len(term) != len(term.encode('utf-8')):
                            if term in termDict:                       
                                termDict[ term ] = termDict[ term ] + 1
                            else:                       
                                termDict[ term ] = 1
                fileobj.close()
                
    sortTerm = get_top(termDict, topnum)
    
    print("The top 10 mentioned Chinese terms associated with brand " + word + " are : ")
  
    for (k, v) in sortTerm:
         print(str(k)+ "     " + str(v) + ' times')
         print('\n')
         


#get the top results
def get_top(myDict,num):

     mylist = sorted(myDict.items(), key=lambda d:d[1], reverse = True)
     return mylist[0 : num]
    


if __name__ == '__main__':
    topnum = 10
    path = '/Users/edisonzhao1/Downloads/weibo/'
    brand = 'michaelkors'
    print('Now processing Michael Kors')
    WordCount3(path, brand, topnum)
    print('\n')
    brand = 'katespade'
    print('Now processing Kate Spade')
    WordCount3(path, brand, topnum)
    
