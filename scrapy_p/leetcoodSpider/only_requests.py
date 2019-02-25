# 搞一个简单的，看一下口红色号的购买量
import requests
import time
import json
#已经可以爬取出来了，开始没加时间间隔，爬了十多页直接返回"rgv587_flag": "sm"
#要加上cookie，不加不会出来的
#下次爬取网页首先要对网页参数进行分析，附带相应的参数，pagram
#做了个简单的颜色统计{'201 蜜桃恋歌': 21, '207 暮色迷失': 290, '206 沙漠玫瑰': 114, '102 枫糖梦境': 22, '208 佳人绝色': 196, '001': 36, '107 新年限定': 5, '002': 34, '202 不期而遇': 31, '101 玫香赤茶': 41, '210 暗夜迷醉': 31, '104 酒心可可': 6, '205 夜风低吟': 19, '105': 36, '209 盛宴之夜': 38, '103 醉情玫瑰': 25, '106': 27, '203 春日呢喃': 8, '003': 26, '204 沐日清晨': 9, '401': 4}


url = "https://rate.tmall.com/list_detail_rate.htm?itemId=574854028364&spuId=1027377153&sellerId=3375170974&order=3&append=0&content=1&tagId=&posi=&picture=&groupId=&ua=098%23E1hvwQvPvBvvUvCkvvvvvjiPRLzhQjEbPFsp0jnEPmPygjlRRFL9Aj3UnL5OgjlPRphvCvvvvvmrvpvEvv1vk9%2BbvUp6dphvmpvU1pb%2BqvvW0TwCvvpvvUmmmphvLvFvj9vjn%2BBlYE7rejh%2BdUFBAfpzOyTxfwLhdigDN%2BLha4QB%2B0ERD7zhz8TJEcqOa70xdX31bj7QD76fd56OfwLwaBJ1UZ01IExr58TivpvUvvmvrVZ%2F7HJEvpvVmvvC9jaHKphv8vvvvvCvpvvvvvv2vhCvmE9vvvWvphvW9pvvvQCvpvs9vvv2vhCv2RvCvpvVvmvvvhCv2QhvCvvvMMGtvpvhvvvvvUwCvvpvCvvvdphvmpvWjID479vIJT6Cvvyvhv883IOvoC7CvpvZz2s%2FfsbNznswpHYfYgswbYAv7Ih%3D&needFold=0"


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36",
    "Connection": "keep-alive",
    #自己电脑的Cookie
    "Cookie": "#############",
    "Referer" : "https://detail.tmall.com/item.htm?id=574854028364&ali_trackid=2:mm_28347190_2425761_20458269:1551108967_262_1732980112&spm=a231o.7712113/d.1004.1&pvid=200_11.186.129.238_488_1551107494646"
}
colour_dict = {}
for i in range(99):
    times = str(time.time()).split(".")
    times[0] = times[0] + times[1][:3]
    times[1] = times[1][3:]
    pagram = {
        "currentPage": i + 1,
        "_ksTS": "%s_%s" % (times[0], times[1]),
        "callback": "jsonp%s" % (int(times[1]) + 1)
    }
    response = requests.get(url, headers=headers, params=pagram)
    print(response.text)
    content = response.text
    a = content.find("(")
    content1 = json.loads(content[a+1:-1])
    comment_list = content1["rateDetail"]["rateList"]
    for j in comment_list:
        colour = j["auctionSku"].split(":")[1]
        if colour not in colour_dict:
            colour_dict[colour] = 0
        else:
            colour_dict[colour] += 1
    time.sleep(5)
    print(colour_dict)

