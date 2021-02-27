import requests
import json
import time
import timeit
import os
import urllib
import random
from datetime import datetime
from dateutil import tz


result=''
djj_bark_cookie=''
djj_sever_jiang=''
btlist=[]
urllist=[]
hdlist=[]
osenviron={}

def Av(i,hd,key,k):
   print(str(k)+'=🔔='*k)
   try:
     userRes = requests.post(i,headers=hd,data=key,timeout=10).json()
     print(userRes)
     hand(userRes,k)
   except Exception as e:
     print(str(e))
      
def hand(data,k):
   try:
    msg=''
    if(k==len(btlist)):
      msg=str(data['data']['data']['balance'])+'|'+str(data['data']['data']['today'])+'|'
    if(k==2):
      msg+=str(data['data']['data']['data']['days'])+'|'
    
    time.sleep(5)
    
    loger(msg)
   except Exception as e:
     print(str(e))
   
    
def watch(flag,list):
   vip=''
   global djj_bark_cookie
   global djj_sever_jiang
   if "DJJ_BARK_COOKIE" in os.environ:
     djj_bark_cookie = os.environ["DJJ_BARK_COOKIE"]
   if "DJJ_SEVER_JIANG" in os.environ:
      djj_sever_jiang = os.environ["DJJ_SEVER_JIANG"]
   if flag in osenviron:
      vip = osenviron[flag]
   if flag in os.environ:
      vip = os.environ[flag]
   if vip:
       for line in vip.split('\n'):
         if not line:
            continue 
         list.append(line.strip())
       return list
   else:
       print(f'''【{flag}】 is empty,DTask is over.''')
       exit()


def pushmsg(title,txt,bflag=1,wflag=1):
   txt=urllib.parse.quote(txt)
   title=urllib.parse.quote(title)
   if bflag==1 and djj_bark_cookie.strip():
      print("\n【通知汇总】")
      purl = f'''https://api.day.app/{djj_bark_cookie}/{title}/{txt}'''
      response = requests.post(purl)
   if wflag==1 and djj_sever_jiang.strip():
      print("\n【微信消息】")
      purl = f'''http://sc.ftqq.com/{djj_sever_jiang}.send'''
      headers={
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'
    }
      body=f'''text={txt})&desp={title}'''
      response = requests.post(purl,headers=headers,data=body)
 
def loger(m):
   print(m)
   global result
   result +=m                
def notice(b,e):
    ll=False
    start_time = datetime.strptime(str(datetime.now().date())+b, '%Y-%m-%d%H:%M')
    end_time =  datetime.strptime(str(datetime.now().date())+e, '%Y-%m-%d%H:%M')
    now_time = datetime.now()
    if now_time > start_time and now_time<end_time:
       ll=True
    else:
    	ll=False
    return ll
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
     global result
     
     watch('Dd_hd',hdlist)
     watch('Dd_url',urllist)
     hd=eval(hdlist[0])
     for i in range(5):
       print(f'''>>>>>>>>>【账号{str(i)}开始''')
       btlist=[]
       watch('Dd_bt'+str(i),btlist)
       if(len(btlist)==0):
            break
       for k in range(len(btlist)):
          print('====='+str(k)+'======')
          Av(urllist[0],hd,btlist[k],(k+1))
       print('【'+str(i)+'】💎'+'干就完了')
       result+='\n'
     pushmsg('Dd',result)
     

if __name__ == '__main__':
       start()
  
