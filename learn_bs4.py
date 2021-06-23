from bs4 import BeautifulSoup
import requests
import lxml.html

html_source='''
<html>
  <head>
    <title>测试</title>
  </head>
  <body>
    <div class="useful">
      <ul>
        <li class="info">我需要的信息1</li>
        <li class="test">我需要的信息2</li>
        <li class="iamstrange">我需要的信息3</li>
      </ul>
     </div>
     <div class="useless">
       <ul>
         <li class="info">垃圾1</li>
         <li class="info">垃圾2</li>
       </ul>
     </div>
  </body>
</html>
'''

def bs4_example():
    html=requests.get('http://exercise.kingname.info/exercise_bs_1.html').content.decode()
    soup=BeautifulSoup(html,'lxml')
    info_2=soup.find(class_='test')
    print(f'使用find方法，返回对象类型：{type(info_2)}')
    print(info_2.string)

def xpath_example():
    selectors=lxml.html.fromstring(html_source)
    # info=selectors.xpath('//div[@class="useful" or @class="useless"]/ul/li/text()')
    # info=selectors.xpath('//div[starts-with(@class,"use")]/ul/li/text()')
    # info=selectors.xpath('//div[contains(@class,"use")]/ul/li/text()')
    # info=selectors.xpath('//div[@*]/ul/li/text()')
    # info=selectors.xpath('//div[@*]/ul/li[text()="垃圾1"]/text()')
    info=selectors.xpath('//div[@*]/ul/li[contains(text(),"需要")]/text()')
    for each in info:
        print(each)

if __name__ == '__main__':
    xpath_example()
    # bs4_example()