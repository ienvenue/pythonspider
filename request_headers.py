import requests

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    html_str = requests.get('https://api.help.bj.cn/apis/weather/?id=101060101', headers=headers)
    html_json = html_str.json()
    print(html_json)
