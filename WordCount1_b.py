# -*- coding: UTF-8 -*-
#!/usr/bin/python

import os
import json
import sys;
reload(sys);
sys.setdefaultencoding('utf8');

def WordCount1_b(rootDir, topnum):

    usersDict = {}
    locationDict = {}
    userCount = 0; #total user count
    f=open("WordCount1_b", "w")
       
    for root,dirs,files in os.walk(rootDir):
        for filespath in files:
            filename = os.path.join(root,filespath)
            if filename.find('.json') != -1:
                fileobj = open(filename,'r')
                tmp = fileobj.readline()
                line = json.loads(tmp)
                uid = line['user']['id']
                loc = line['user']['location']
                help = loc.split(' ')
                if len(help) == 2:
                    loc = help[1]
               
                #users count
                if uid in usersDict :
                    usersDict[ uid ] = usersDict[ uid ] + 1
                else:
                    usersDict[ uid ] = 1
                    
                 #location count
                if loc in locationDict :
                     locationDict[ loc ] = locationDict[ loc ] + 1
                else:
                     locationDict[ loc ] = 1
                fileobj.close()

    sortUsers = get_top(usersDict, topnum)               
    print('The top ' + str(topnum) + ' users ' + ' are : ')
    print('\n')
    print(' UserId' + '           ' + 'Post Number')
    print('--------------------------------')
    for (k, v) in sortUsers:
         print(str(k) + '          ' + str(v))
         print('\n')
    print('\n')

    sortUsers = get_top(locationDict, topnum)               
    print('The top ' + str(topnum) + ' locations ' + ' are : ')
    print('\n')
    print(' Location' + '        ' + 'Post Number')
    print('-------------------------------')
    for (k, v) in sortUsers:
         print(('    ' + str(k) + '            ' + str(v)))
         print('\n')
    f.close()


#get the top results
def get_top(myDict,num):

     mylist = sorted(myDict.items(), key=lambda d:d[1], reverse = True)
     return mylist[0 : num]

if __name__ == '__main__':
    topnum = 10
    path = '/Users/edisonzhao1/Downloads/weibo/'
    WordCount1_b(path, topnum)
