from datetime import datetime
from .page_fetcher import *
from .scheduler import *
import timeit

if __name__ == "__main__":
    arr_urls_seeds = [
        "https://www.uol.com.br/",
        # "https://www.globo.com/",
        # "https://www.terra.com.br/",
        # "https://www.msn.com/pt-br",
        # "https://www.techtudo.com.br/",
        # "https://canaltech.com.br/",
        # "https://github.com/",
        # "https://pt.stackoverflow.com/",
        # "https://pt.wix.com/",
        # "https://br.wordpress.com/",
        # "https://www.pathofexile.com/",
        # "https://www.reddit.com",
        # "https://www.r7.com/",
        # "https://www.twitch.tv",
        # "https://www.estadao.com.br/",
        # "https://www.ig.com.br/",
        # "https://www.portaldoholanda.com.br/",
        # "https://www.gazetadopovo.com.br/",
        # "https://www.naosalvo.com.br/",
        # "https://www.Facebook.com",
        # "https://www.Baidu.com",
        # "https://www.Wikipedia.org",
        # "https://www.Yahoo.com",
        # "https://www.Qq.com",
        # "https://www.Taobao.com",
        # "https://www.Twitter.com",
        # "https://www.Amazon.com",
        # "https://www.Google.co.jp",
        # "https://www.Tmall.com",
        # "https://www.Vk.com",
        # "https://www.Sohu.com",
        # "https://www.Weibo.com"
    ]


    arr_urls_seeds = [urlparse(str_url) for str_url in arr_urls_seeds]
    
    scheduler = Scheduler(str_usr_agent="vinigorbot",
                                int_page_limit=30,
                                int_depth_limit=3,
                                arr_urls_seeds=arr_urls_seeds)
   
    fetchers = []

    d_initial_time = datetime.now()
    
    for index in range(10):
        fetchers.append(PageFetcher(scheduler))
        fetchers[index].start()
        
    for fetcher in fetchers:
        fetcher.join()
    
    print("Tempo final de execução: {} mS".format((datetime.now() - d_initial_time).seconds))