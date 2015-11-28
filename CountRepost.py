# -*- coding: UTF-8 -*-
#!/usr/bin/python

import os
import json
import matplotlib.pyplot as plt

def CountReposts(rootDir,word,topnum):

    timeDict = {}
    allTime = set()
    for root,dirs,files in os.walk(rootDir):
        for filespath in files:
            filename = os.path.join(root,filespath)
            if filename.find('.json') != -1 and filename.find('repost') != -1:
                fileobj = open(filename,'r')
                tmp = fileobj.readline()
                line = json.loads(tmp)
                time = line['created_at']
                help = time.split(' ')
                time = help[1] + '-' + help[2]
                time = time_format(time)
                
                allTime.add(time)
                text = line['text']
                # convert to the unique form
                text = text.replace(' ', ''); 
                text = text.lower()
                if text.find(word) != -1:                   
                    #time count
                    if time in timeDict:                       
                        timeDict[ time ] = timeDict[ time ] + 1
                    else:                       
                        timeDict[ time ] = 1
                fileobj.close()
                
    for t in allTime:
        if t not in timeDict:
            timeDict[ t ] = 0

    sortTime = get_top(timeDict)
    print("The number of reposts per day for brand " + word + " are listed as follows : ")

    i = 0
    X_axis = []
    Y_axis = []
    for (k, v) in sortTime:
         X_axis.append(i)
         Y_axis.append(v)
         print(str(k) + "     " + str(v) + ' times')
         i = i + 1
    plt.xlabel('days after 08-29')
    plt.ylabel('Reposts Number')
    plt.plot(X_axis, Y_axis)
    plt.show()


def time_format(myTime):
    myTime = myTime.replace('Oct', '10')
    myTime = myTime.replace('Sep', '09')
    myTime = myTime.replace('Aug', '08')
    return myTime
    
         

#get the top results
def get_top(myDict):

     mylist = sorted(myDict.items(), key=lambda d:d[0], reverse = False)
     return mylist

    
if __name__ == '__main__':
    topnum = 1
    path = '/Users/edisonzhao1/Downloads/weibo/'
    brand = 'michaelkors'
    print('Now processing Michael Kors')
    CountReposts(path, brand, topnum)
    print('\n')
    brand = 'katespade'
    print('Now processing Kate Spade')
    CountReposts(path, brand, topnum)
    
