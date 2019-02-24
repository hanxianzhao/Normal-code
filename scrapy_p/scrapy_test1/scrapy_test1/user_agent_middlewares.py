import random
from builtins import object
from scrapy import signals
from scrapy_test1.settings import USER_AGENTS
from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware


class RandomUserAgent(UserAgentMiddleware):
    def process_requests(self,request,spider):
        print("222")
        user_agent = random.choice(USER_AGENTS)
        print(user_agent)
        print("111")
        request.headers.setdefault('User-Agent',user_agent)