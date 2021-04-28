# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 01:25:21 2021

@author: duke.kuo
"""


from skpy import SkypeAuthException
from skpy import Skype
sk = Skype(connect=False)
sk.conn.setTokenFile(".tokens-app")
username="duke_0124@hotmail.com"
password="!QAZXSw20124"
try:
    sk.conn.readToken()
except SkypeAuthException:
     sk.conn.setUserPwd(username, password)
     sk.conn.getSkypeToken()
sk.conn
contact =sk.contacts

#for i in contact:
#     print(i)
     
ch = sk.contacts["live:.cid.4b5d2e83b90120aa"].chat
 
ch.sendMsg("憑證剩下XX天，請記得安排")