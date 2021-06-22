import requests
from multiprocessing.dummy import Pool
import re
import os
import time

def get_toc(html,start_url):
    toc_url_list=[]
    toc_block=re.findall('正文(.*?)</tbody>',html,re.S)[0]
    toc_url=re.findall('href="(.*?)"',toc_block,re.S)
    for url in toc_url:
        toc_url_list.append(start_url+'/'+url)
    return toc_url_list

def get_article(html):
    chapter_name=re.search('size="4">(.*?)<',html,re.S).group(1)
    text_block=re.search('<p>(.*?)</p>',html,re.S).group(1)
    text_block=text_block.replace('<br/>','')
    save(chapter_name,text_block)

def save(chapter,article):
    os.makedirs('动物农场',exist_ok=True)
    with open(os.path.join('动物农场',chapter+'.txt'),'w',encoding='utf-8') as f:
        f.write(article)

def get_html(sites):
    # 在下面的代码行中使用断点来调试脚本。
    # 按 Ctrl+F8 切换断点。
    # html=requests.get(sites)
    # html_bytes=html.content
    # html_str=html_bytes.decode()
    html_str=requests.get(sites).content.decode('gbk')
    # print(html_str)
    return html_str

def main():
    start_url='http://www.kanunu8.com/book3/6879'
    html=requests.get(start_url).content.decode('GBK')
    pool=Pool(3)
    html_str=pool.map(get_html,get_toc(html, start_url))
    pool2 = Pool(3)
    pool2.map(get_article,html_str)


if __name__ == '__main__':
    main()