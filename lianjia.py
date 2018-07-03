# -*- coding: utf-8 -*-
import requests
from  bs4 import BeautifulSoup
import time
import single
import pandas as pd
#dataframe=pd.DataFrame({"title":timu,"urls":lianjie})
#dataframe.to_csv(r"C:\Users\Administrator\Desktop\lianjie.csv",index=False,sep=',')
import numpy as np
#将主页面上的网页链接爬取下来
def frist(firsturl):
    time.sleep(3)
    title=[]
    l=[]
    html=requests.get(firsturl)
    #html可能乱码，soup会转码
    soup = BeautifulSoup(html.content)
    for link in soup.find_all('h2'):
        if len(str(link))>84:
    #        href=link.get('href')
            li=link.a['href']
            t= link.a["title"]
            title.append(t)
            l.append(li)
    return title,l

if __name__=="__main__":
#    p=[]
#    a=[]
#    h=[]
#    floor=[]
#    t=[]
#    s=[]
#    l=[]
    f=pd.read_csv(r"C:\Users\Administrator\Desktop\lianjie.csv",encoding='ISO-8859-1', sep=',', header=None)
    #断了之后直接将后面的值改一下，跟着断点之后继续下载
    for link in f[1][1098:]:
         p1,a1,h1,f1,t1,s1,l1=single.single(link)
         print (link)
         p.append(p1)
         a.append(a1)
         h.append(h1)
         floor.append(f1)
         t.append(t1)
         s.append(s1)
         l.append(l1)
    
#    lianjie=[]
#    timu=[]
#    for i in range(1,101):
#        firsturl=r"https://bj.lianjia.com/zufang/pg%d/"%i
##        list.append(firsturl)
#        title,l=frist(firsturl)
#        
#        lianjie=lianjie+l
#        
#        timu=timu+title
