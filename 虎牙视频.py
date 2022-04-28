import requests
import re
import time

headers ={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
}
for i in range(1,5):
    url = f'https://v.huya.com/g/Dance?set_id=31&order=hot&page={i}'
    response = requests.get(url, headers=headers)
    zip_data = re.findall('li data-vid="(.*?)">',response.text)
    for index in zip_data:
        time.sleep(0.5)
        index_url = f'https://liveapi.huya.com/moment/getMomentContent?videoId={index}&uid=&_=1636771856063'
        response_1 = requests.get(url = index_url , headers = headers)
        title = response_1.json()['data']['moment']['title']
        video_url = response_1.json()['data']['moment']['videoInfo']['definitions'][0]['url']
        video_content = requests.get(url = video_url , headers = headers).content
        with open('G:\pythonProject\新建文件夹/' + title + '.mp4' , mode='wb') as f:
            f.write(video_content)
        print(title + "保存成功！！！")
