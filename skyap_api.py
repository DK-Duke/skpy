# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 01:25:21 2021

@author: duke.kuo
"""


from skpy import SkypeAuthException
from skpy import Skype
sk = Skype(connect=False)
sk.conn.setTokenFile(".tokens-app")
username="your account name"
password="password"
try:
    sk.conn.readToken()
except SkypeAuthException:
     sk.conn.setUserPwd(username, password)
     sk.conn.getSkypeToken()
sk.conn
contact =sk.contacts

#for i in contact:
#     print(i)
     
ch = sk.contacts["live:對象ID"].chat
 
ch.sendMsg("憑證剩下XX天，請記得安排")
