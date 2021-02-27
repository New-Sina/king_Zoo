import requests
import os
import re
import json
import time
import timeit
import random
import urllib
from datetime import datetime

osenviron={}
djj_bark_cookie=''
djj_sever_jiang=''
result=''


hd={"Accept": "*/*","Accept-Encoding": "br, gzip, deflate","Accept-Language": "zh-Hans-CN;q=1, en-US;q=0.9, zh-Hant-CN;q=0.8","As-Version": "v1","Content-Type": "application/json","User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 qapp","Version": "1211","Version-Name": ""}

def ludingji(i,j,k):
    print('=🔔='*k)
    try:
       response = requests.post(i,headers=hd,data=j)
       #print(response.text)
       if(k==8):
             res=json.dumps(response.text)
             print(res)
             res=re.compile('(\d+.\d+)').findall(res)
             res=res[0]+'|'+res[1]+'|'+res[2]
             loger(res)
    except Exception as e:
      print(str(e))
      pass

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
       return


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
   result +=m+'\n'                
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
   urllist=[]
   tokenlist=[]
   tklist= []
   alllist=[]
   watch('ludingji_url',urllist)
   watch('ludingji_tk',tklist)
   watch('ludingji_token',tokenlist)
   for i in range(8):
     funlist=[]
     watch('ludingji_fun'+str(i),funlist)
     alllist.append(funlist)
   #print(len(alllist))
   for max in range(10):
     result=''
     jj=0
     if(len(urllist)==0):
        break
     if(len(tklist)==0):
        break
     if(len(tokenlist)==0):
        break
     if(len(alllist)==0):
        break
     for j in range(len(tklist)):
       jj+=1
       hd['tk']=tklist[j]
       hd['token']=tokenlist[j]
       print('===='+str(j))
       for k in range(8):
           ludingji(urllist[k],alllist[k][j],(k+1))
           time.sleep(2)
     time.sleep(10)
     print('💎【'+str(max)+'】=======🔔🔔🔔🔔')
   pushmsg('ludingji-二库',result)
if __name__ == '__main__':
       start()
    
