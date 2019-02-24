#搞一个简单的，看一下口红色号的购买量
import requests

url_begin = "https://rate.tmall.com/list_detail_rate.htm?itemId=574854028364&spuId=1027377153&sellerId=3375170974&order=3&currentPage="
page_num = 1
url_end = "&append=0&content=1&tagId=&posi=&picture=&groupId=&ua=098%23E1hvZpv7vcyvUpCkvvvvvjiPRLsy1jtbP2LyAjYHPmPUAjEmnL5UsjlhRFzwAjn8RLyCvvpvvhCvRphvCvvvphmrvpvEvvHOc4hvvvOHdphvmpmC3Uj7vvm2i4wCvvpvvhHh2QhvCPMMvvvEvpCWvnplnB0xRdItn0vHfw9OdiTAVA5paBJ1nbvAwYV9%2Bu0OV166%2BE7rVXKKNB3r1EKKDfUf8wClHd8rVcvrYE7rVBuKf9033Le9R3pDNdyCvm9vvhCvvvvvvvvvByOvvvHivvCVB9vv9LvvvhXVvvmCjvvvByOvvUhwuphvmvvvpo3yh6zJkphvC9hvpyPwAvhCvvOv9hCvvvvtvpvhvvCvpUwCvvpv9hCvCQhvCli4zYMwzt0rvpvBCUhZhV6vvvlpEBYb3Oy3%2B2ervpvBCvjY%2FohvvEmXEBYb3Oy3%2B2ervpvEvUmoeNZvvEBLdphvhURmYSy4vvvuxdhSpaVxnsuCvpvW7D%2FcZhdw7Di4%2BjsNRphvCvvvphmrvpvEvUhIPg6vv2Lm9phvHHiaKO90zHi47%2BZetss37I34NrGB&needFold=0&_ksTS=1550915536628_1965&callback=jsonp1966"

url = url_begin + str(page_num)
# print(url)
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"}

cookies = {}
# response = requests.get(url,headers = headers)
# response = requests.get("https://detail.tmall.com/item.htm?id=574854028364&ali_trackid=2:mm_28347190_2425761_20458269:1550975363_271_955480656&spm=a231o.7712113/d.1004.11&pvid=200_11.27.109.220_414_1550913849952")
session = requests.session()
session.get("https://detail.tmall.com/item.htm?id=574854028364&ali_trackid=2:mm_28347190_2425761_20458269:1550975363_271_955480656&spm=a231o.7712113/d.1004.11&pvid=200_11.27.109.220_414_1550913849952",headers = headers)
response = session.get(url,headers = headers)
# print(response.request)
# print(response.content)
print(response.text)



