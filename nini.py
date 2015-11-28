#!/usr/bin/python
# -*- coding: UTF-8 -*-


import os
import json
from datetime import datetime
import time

    
    
def top(rootDir,word):
    #top related vars
    usersDict = {}
    locsDict = {}
    topNum = 10
    postCount = 0 #total post count
    userCount = 0; #total user count

    for root,dirs,files in os.walk(rootDir):

        for filespath in files:
            if filespath[0]=='.':
                break
            
            filename = os.path.join(root,filespath)
            #if filespath.find('.json') == -1 :
            #    print "in Dir:[",filespath,"]"

            if filename.find('.json')  != -1 :
                fileobj = open(filename,'r')
                line = fileobj.readline()

                dictData = json.loads(line) 

                if  dictData['text'].find(word):
                    uid = dictData['user']['id']
                    loc = dictData['user']['location']
                   
                    #users count
                    if usersDict.get(uid) :
                        usersDict[ uid ] = usersDict[ uid ] + 1
                        userCount += 1
                    else:
                        usersDict.setdefault(uid,1)
                     
                    #location count    
                    if locsDict.get(loc) :
                        locsDict[ loc ] = locsDict[ loc ] + 1
                    else:
                        locsDict.setdefault(loc,1)
                        
                    postCount += 1 
                    
                fileobj.close()
                
            #break
            
    topUsers = get_top(usersDict,topNum)
    topLocs = get_top(locsDict,topNum)
    print ("User count: ",userCount)
    print ("Post count: ",postCount)
    print ("Top users:")
    print (topUsers)
    print ("Top Locations:")
    print (topLocs)
    print ("-----------------END-----------------")
    
            
def get_top(myDict,num):

     kvlist = sorted(myDict.items(), key=lambda d:d[1], reverse = True)
     resDict = {}
     for item in kvlist:
         k = item[0]
         v = item[1]
         if num > 0:
             resDict[k] = v
             num = num-1
     return resDict
     #return dict_slice(tmpdict,0,num-1)
     
     
     
     
     
def dict_slice(adict, start, end):
    keys = adict.keys()
    slice = {}
    for k in keys[start:end]:
        slice[k] = adict[k]
    return slice
                




if __name__ == '__main__':

    top('/Users/edisonzhao1/Downloads/weibo/', 'Michael Kors')    
 #   test1()
