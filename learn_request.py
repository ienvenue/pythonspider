# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import requests
import re

def get_html(sites):
    # 在下面的代码行中使用断点来调试脚本。
    # 按 Ctrl+F8 切换断点。
    # html=requests.get(sites)
    # html_bytes=html.content
    # html_str=html_bytes.decode()
    html_str=requests.get(sites).content.decode()
    # print(html_str)
    return html_str

def post_html(sites):
    data={'name':'value1','password':'value2'}
    # html_formdata=requests.post(sites,data=data).content.decode()
    html_json=requests.post(sites,json=data).content.decode()
    print(html_json)

def get_re_html(sites):
    html=get_html(sites)
    title=re.search('title>(.*?)<',html,re.S).group(1)
    content_list=re.findall('p>(.*?)<',html,re.S)
    content_str='\n'.join(content_list)
    print('title:'+title)
    print(f'content:\n{content_str}')

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    # get_html('http://exercise.kingname.info/exercise_requests_get.html')
    # post_html('http://exercise.kingname.info/exercise_requests_post')
    get_re_html('http://exercise.kingname.info/exercise_requests_get.html')

