# -*- coding: utf-8 -*-
import requests
from  bs4 import BeautifulSoup
def single(url):

#    send_headers={"User-Agent":" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
#                  "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8",
#                  "Connection":"keep-alive",
#                  "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"}
#    
    html=requests.get(url)
    soup=BeautifulSoup(html.content)
    soup1=soup.find(class_='zf-room')#tag类型
    price=soup.find_all(class_='total')[0].string
    area=soup.find_all(class_='lf')[0].get_text()[3:8:]
    housetype=soup.find_all(class_='lf')[1].get_text()
    floor=soup.find_all(class_='lf')[2].get_text()
    toward=soup.find_all(class_='lf')[3].get_text()
    subline=soup1.find_all("p")[4].get_text()
    local=soup1.find_all("p")[6].get_text()
    print(price,area,housetype,floor,toward,subline,local)
#    for i in soup.find_all("span"):
#        print (i)
#        price.append(i)
    return price,area,housetype,floor,toward,subline,local
def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')
if __name__=="__main__":
    url="https://bj.lianjia.com/zufang/101102936376.html"
    p,a,h,f,t,s,l=single(url)
    #soup.find_all(class_='price')
    #bs4.element.ResultSet返回的是一个列表，通过find——all得到需先取一个值才行，t[0].string
    #find（）得到tag类型
    #链接：https://blog.csdn.net/zjiang1994/article/details/52679174