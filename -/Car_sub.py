import requests
import os
import re
import json
import time
import timeit
import random
import urllib
from datetime import datetime
result=''


osenviron={}

msg=''
urllist=[]
hdlist=[]
btlist=[]

def Av(i,hd,k,key):
   print(str(k)+'=🔔='*k)
   try:
     response = requests.post(i,headers=hd,data=key,timeout=10)
     #print(response.text)
   except Exception as e:
      print(str(e))

def watch(flag,list):
   vip=''
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
def hand(bd):
   rp1=bd.find('ceId')+5
   St=bd[rp1:rp1+9]
   rp2=bd.find('erId')+5
   Mst=bd[rp2:rp2+5]
   newbd=Mst+str(random.randint(1111,8888))
   bd=bd.replace(St,newbd)
   return bd
   
def pushmsg(title,txt,bflag=1,wflag=1):
   txt=urllib.parse.quote(txt)
   title=urllib.parse.quote(title)
   if bflag==1 and djj_bark_cookie.strip():
      print("\n【通知汇总】")
      purl = f'''https://api.day.app/{djj_bark_cookie}/{title}/{txt}'''
      response = requests.post(purl)
      #print(response.text)
   if wflag==1 and djj_sever_jiang.strip():
      print("\n【微信消息】")
      purl = f'''http://sc.ftqq.com/{djj_sever_jiang}.send'''
      headers={
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'
    }
      body=f'''text={txt})&desp={title}'''
      response = requests.post(purl,headers=headers,data=body)
    #print(response.text)
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
   watch('car_subhd',hdlist)
   watch('car_subbt',btlist)
   watch('car_suburl',urllist)
   for j in range(len(btlist)):
       print(f'''===={str(j)}({len(btlist)})''')
       hd=eval(hdlist[0])
       for k in range(5):
           
           Av(urllist[0],hd,(k+1),hand(btlist[j]))
       print(str(j)+'💎'*15+'干就完了')
       result+='\n'

if __name__ == '__main__':
       start()
    
