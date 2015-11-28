# -*- coding: UTF-8 -*-
#!/usr/bin/python

import os
import json

def WordCount1_a(rootDir,word):

    usersDict = {}
    userCount = 0; #total user count
    f=open("WordCount1_a_" + word,"w")
       
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
                    userCount = userCount + 1
                    uid = line['user']['id']
                    uname = line['user']['name']
                    #users count
                    if uid in usersDict:                       
                        usersDict[ uid ] = usersDict[ uid ] + 1
                    else:                       
                        usersDict[ uid ] = 1
                fileobj.close()

    f.write("Total number for brand " + word + " is : ")
    f.write(str(userCount))
    f.write('\n')
    f.write('\n')
    f.write(' UserId' + "      " + 'Number')
    f.write('\n')
    f.write('-------------------')
    f.write('\n')
    for (k, v) in usersDict.items():
         f.write(str(k) + "     " + str(v))
         f.write('\n')
    f.close()




if __name__ == '__main__':
    path = '/Users/edisonzhao1/Downloads/weibo/'
#    brand = 'michaelkors'
    brand = 'katespade'
    WordCount1_a(path, brand)
