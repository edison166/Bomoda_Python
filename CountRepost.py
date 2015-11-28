# -*- coding: UTF-8 -*-
#!/usr/bin/python

import os
import json

def CountRepost(rootDir,word,topnum):

    timeDict = {}
       
    for root,dirs,files in os.walk(rootDir):
        for filespath in files:
            filename = os.path.join(root,filespath)
            if filename.find('.json') != -1 and filename.find('repost') != -1:
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
                
  
    print("The number of reposts per day for brand " + word + " are listed as follows : ")
  
    for (k, v) in timeDict.items():
         print(str(k) + "     " + str(v) + ' times')

         


if __name__ == '__main__':
    topnum = 1
    path = '/Users/edisonzhao1/Downloads/weibo/'
    brand = 'michaelkors'
    CountRepost(path, brand, topnum)
    print('\n')
    brand = 'katespade'
    CountRepost(path, brand, topnum)
    
