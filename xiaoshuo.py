import requests
import re

for num in range(2,900):
    url = f'https://www.biquge7.com/book/8263/{num}.html'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 Edg/96.0.1054.29'
    }
    response = requests.get(url=url,headers=headers)
    title = re.findall('<h1 class="wap_none">(.*?)</h1>',response.text)
    zip_data = re.findall('>(.*?)<br /',response.text)
    file = open(f'G:\pythonProject\练习数据/{title[0]}.txt','a',encoding='utf-8')
    for i in zip_data:
        s = i +'\n'
        file.write(s)
    file.close()
    print(str(num) + "保存成功")

