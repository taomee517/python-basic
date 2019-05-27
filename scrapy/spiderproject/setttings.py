BOT_NAME = 'nvshens'

SPIDER_MODULES = ['nvshens.spiders']
NEWSPIDER_MODULE = 'nvshens.spiders'
ROBOTSTXT_OBEY = True

# 延迟请求
DOWNLOAD_DELAY = 1

# 请求带上headers
DEFAULT_REQUEST_HEADERS = {
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Accept-Language': 'en',
}

# 启动pipelines类型为字典
ITEM_PIPELINES = {
    'nvshens.pipelines.NvshensPipeline': 300,
}