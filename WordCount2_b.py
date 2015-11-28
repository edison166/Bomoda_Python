# -*- coding: UTF-8 -*-
#!/usr/bin/python

import os
import json

def WordCount2_b(rootDir,topnum):

    timeDict = {}
       
    for root,dirs,files in os.walk(rootDir):
        for filespath in files:
            filename = os.path.join(root,filespath)
            if filename.find('.json') != -1:
                fileobj = open(filename,'r')
                tmp = fileobj.readline()
                line = json.loads(tmp)
                time = line['created_at']
                help = time.split(' ')
                help2 = help[3];
                help = help2.split(':')                   
                time = help[0]
                #time count
                if time in timeDict:                       
                    timeDict[ time ] = timeDict[ time ] + 1
                else:
                    timeDict[ time ] = 1
                fileobj.close()
                
    sortTime = get_top(timeDict, topnum)
    
    print('The peak hour with the most posts' + ' is : ') 
    for (k, v) in sortTime:
         print(str(k) + "\nand there are " + str(v) + ' posts at that time.')
         print('\n')
         


#get the top results
def get_top(myDict,num):

     mylist = sorted(myDict.items(), key=lambda d:d[1], reverse = True)
     return mylist[0 : num]
    


if __name__ == '__main__':
    topnum = 1
    path = '/Users/edisonzhao1/Downloads/weibo/'
    WordCount2_b(path, topnum)
 
    
