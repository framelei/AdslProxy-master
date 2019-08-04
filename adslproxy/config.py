# coding=utf-8
# 拨号间隔
ADSL_CYCLE = 100

# 拨号出错重试间隔
ADSL_ERROR_CYCLE = 5

# ADSL命令
ADSL_BASH = 'adsl-stop;adsl-start'

# 代理运行端口
PROXY_PORT = 8888

# 客户端唯一标识
CLIENT_NAME = 'adsl.01'

# 拨号网卡
ADSL_IFNAME = 'ppp0'

# Redis数据库IP
REDIS_HOST = '129.28.200.147'

# Redis数据库密码, 如无则填None
REDIS_PASSWORD = 'Re_Lei'

# Redis数据库端口
REDIS_PORT = 6379

# 代理池键名
PROXY_KEY = 'ADSL'

# 测试URL
TEST_URL = 'https://www.fang.com/SoufunFamily.htm'

# 根据站点配置请求头，eg：不加请求头房天下会报403
REQUEST_HEADERS = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
}
# 测试超时时间
TEST_TIMEOUT = 20

# API端口
API_PORT = 8000