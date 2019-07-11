# 配置文件

# 豆瓣搜索接口
DOUBAN_SEARCH = "https://www.douban.com/search?q="

# 请求头
CRAWLER_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'Referer': 'https://www.douban.com/',
}

# beautifulsoup解析器
PARSER = 'html.parser'