# -*- coding: UTF-8 -*-
#!/usr/bin/python

import os
import json

def WordCount2_a(rootDir,word,topnum):

    timeDict = {}
       
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
                    time = line['created_at']
                    help = time.split(' ')
                    time = help[0] + ' ' + help[1] + ' ' + help[2]
                    #time count
                    if time in timeDict:                       
                        timeDict[ time ] = timeDict[ time ] + 1
                    else:                       
                        timeDict[ time ] = 1
                fileobj.close()
                
    sortTime = get_top(timeDict, topnum)
    
    print("The date that has the highest number of posts for brand " + word + " is : ")
  
    for (k, v) in sortTime:
         print(str(k) + "     " + str(v) + ' times')
         print('\n')
         


#get the top results
def get_top(myDict,num):

     mylist = sorted(myDict.items(), key=lambda d:d[1], reverse = True)
     return mylist[0 : num]
    


if __name__ == '__main__':
    topnum = 1
    path = '/Users/edisonzhao1/Downloads/weibo/'
    brand = 'michaelkors'
    WordCount2_a(path, brand, topnum)
    brand = 'katespade'
    WordCount2_a(path, brand, topnum)
    
