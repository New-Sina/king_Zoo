import requests
import os
import re
import json
import time
import random
import timeit
import urllib
from datetime import datetime
from dateutil import tz


djj_bark_cookie=''
djj_sever_jiang=''
djj_tele_cookie=''
   
myid='1986045594'
   
result=''
osenviron={}
msg=''
hd={}
urllist=[]
hdlist=[]
btlist=[]
bdlist=[]




def ufo(st):
   return st.replace('1986045594',myid)
def Av(i,hd,k,key='',flag=0):
   print(str(k)+'=🔔='*k)
   try:
      i=ufo(i)
      if flag==0:
         response = requests.get(f'''{i}{key}''',headers=hd,timeout=10)
      else:
         
         response = requests.post(f'''{i}''',headers=hd,data=key,timeout=10)
        
         
      userRes=json.loads(response.text)
      
      hand(userRes,k)
   except Exception as e:
      print(str(e))

def watch(flag,list):
   vip=''
   global djj_bark_cookie
   global djj_sever_jiang
   global djj_tele_cookie
   if "DJJ_BARK_COOKIE" in os.environ:
      djj_bark_cookie = os.environ["DJJ_BARK_COOKIE"]
   if "DJJ_TELE_COOKIE" in os.environ:
      djj_tele_cookie = os.environ["DJJ_TELE_COOKIE"]
   if "DJJ_SEVER_JIANG" in os.environ:
      djj_sever_jiang = os.environ["DJJ_SEVER_JIANG"]
   if flag in os.environ:
      vip = os.environ[flag]
   if flag in osenviron:
      vip = osenviron[flag]
   if vip:
       for line in vip.split('\n'):
         if not line:
            continue 
         list.append(line.strip())
       return list
   else:
       print(f'''【{flag}】 is empty,DTask is over.''')
       exit()
def hand(userRes,k):
   msg=''
   try:
       if(k==1):
          msg+=str(userRes['result']['money']/100)+'|'+str(userRes['result']['points'])+'|'
          for it in userRes['result']['points_gift_list']:
            if it['id']==52:
              msg+=it['limit_desc'][4:len(it['limit_desc'])]+'|'
            if it['id']==200:
              tmp=it['limit_desc'][4:len(it['limit_desc'])-3]
              print(tmp)
              msg+=it['limit_desc'][4:len(it['limit_desc'])]+'|'
              if int(tmp)<10:
                for n in range(10-int(tmp)):
                    hd['Cookie']=btlist[0]
                    Av(urllist[5],hd,6)
                    time.sleep(2)
               

       elif(k==2):
          for it in userRes['tasks']:
             tmp=it['name']+'-'+str(it['status'])
             
             if it['status']==1:
                url=urllist[k][0:urllist[k].find('name=')+5]+it['name']+urllist[k][urllist[k].find('&b'):len(urllist[k])]
                Av(url,hd,(k+1))
                time.sleep(1)

       elif(k==3):
         print('333')
         print(userRes)
       elif(k==4):
          print('4444')
          if userRes['result'][0]['isSign']==0:
              hd['Cookie']=btlist[0]
              hd['Content-Type']='application/x-www-form-urlencoded'
              msg+='signing......'
              Av(urllist[k],hd,(k+1),bdlist[1],1)
          elif userRes['result'][0]['isSign']==1:
              msg+='signed'
       
       elif(k==5):
         print('555')
         print(userRes['retmsg'])
       
       elif(k==6):
          print('66666')
          print(str(userRes['result']['amount']/100))
       elif(k==7):
          print(userRes['retmsg'])
          hd['Cookie']=btlist[0]
          Av(urllist[k],hd,(k+1))
          
          
          hd['Cookie']=btlist[0]
          Av(urllist[k+1],hd,(k+2))
       elif(k==8):
          print(userRes['retmsg'])
       elif(k==9):
          print(userRes['retmsg'])
       loger(msg)
   except Exception as e:
      print(str(e))
      
      
      


def pushmsg(title,txt,bflag=1,wflag=1,tflag=1):
   try:
     txt=urllib.parse.quote(txt)
     title=urllib.parse.quote(title)
     if bflag==1 and djj_bark_cookie.strip():
         print("\n【Bark通知】")
         purl = f'''https://api.day.app/{djj_bark_cookie}/{title}/{txt}'''
         response = requests.post(purl)
   except Exception as e:
      print(str(e))
   try:
     if tflag==1 and djj_tele_cookie.strip():
         print("\n【Telegram消息】")
         id=djj_tele_cookie[djj_tele_cookie.find('@')+1:len(djj_tele_cookie)]
         botid=djj_tele_cookie[0:djj_tele_cookie.find('@')]

         turl=f'''https://api.telegram.org/bot{botid}/sendMessage?chat_id={id}&text={title}\n{txt}'''

         response = requests.get(turl,timeout=5)
   except Exception as e:
      print(str(e))
   try:
     if wflag==1 and djj_sever_jiang.strip():
        print("\n【微信消息】")
        purl = f'''http://sc.ftqq.com/{djj_sever_jiang}.send'''
        headers={'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'}
        body=f'''text={txt})&desp={title}'''
        response = requests.post(purl,headers=headers,data=body)
   except Exception as e:
      print(str(e))
def loger(m):
   global result
   result +=m     

    

def clock(func):
    def clocked(*args, **kwargs):
        t0 = timeit.default_timer()
        result = func(*args, **kwargs)
        elapsed = timeit.default_timer() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[🔔运行完毕用时%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked
    
    
    
    
@clock
def start():
   global result,hd,btlist,urllist,hdlist,bdlist
   print('Localtime',datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S", ))
   watch('wowo_naitang_hd',hdlist)
   hd=eval(hdlist[0])
   for j in range(1):
       print(f'''===={str(j+1)}''')
       urllist=[]
       btlist=[]
       tmbdlist=[]
       bdlist=[]
       watch('wowo_naitang_url'+str(j),urllist)
       watch('wowo_naitang_ck'+str(j),btlist)
       watch('wowo_naitang_bd'+str(j),tmbdlist)
       for d in tmbdlist:
          bdlist.append(ufo(d))
       for k in range(len(urllist)):
          print('【'+str(k)+'】>>>>>>>>>')
          if k==2 or k==4 or k==5 or k==7 or k==8:
              continue
          else:
            
           if(k==3):
              hd['Cookie']=btlist[0]
              hd['Content-Type']='application/json'
              Av(urllist[k],hd,(k+1),bdlist[0],1)
           elif(k==6):
              hd['Cookie']=btlist[0]
              hd['Content-Type']='application/json'
              Av(urllist[k],hd,(k+1),bdlist[2],1)
           else:
            hd['Cookie']=btlist[0]
            Av(urllist[k],hd,(k+1))
   print('🏆🏆🏆🏆运行完毕')
   pushmsg('喔喔奶糖三库2021129',result)
    
    
   
     
if __name__ == '__main__':
       start()
    
