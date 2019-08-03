# coding=utf-8
# import json
# import tornado.ioloop
# import tornado.web
# from tornado.web import RequestHandler, Application
# from adslproxy.config import *
#
#
# class MainHandler(RequestHandler):
#     def initialize(self, redis):
#         self.redis = redis
#
#     def get(self, api=''):
#         if not api:
#             links = ['random', 'proxies', 'names', 'all', 'count']
#             self.write('<h4>Welcome to ADSL Proxy API</h4>')
#             for link in links:
#                 self.write('<a href=' + link + '>' + link + '</a><br>')
#
#         if api == 'random':
#             result = self.redis.random()
#             if result:
#                 self.write(result)
#
#         if api == 'names':
#             result = self.redis.names()
#             if result:
#                 self.write(json.dumps(result))
#
#         if api == 'proxies':
#             result = self.redis.proxies()
#             if result:
#                 self.write(json.dumps(result))
#
#         if api == 'all':
#             result = self.redis.all()
#             if result:
#                 self.write(json.dumps(result))
#
#         if api == 'count':
#             self.write(str(self.redis.count()))
#
#
# def server(redis, port=API_PORT, address=''):
#     application = Application([
#         (r'/', MainHandler, dict(redis=redis)),
#         (r'/(.*)', MainHandler, dict(redis=redis)),
#     ])
#     application.listen(port, address=address)
#     print('ADSL API Listening on', port)
#     tornado.ioloop.IOLoop.instance().start()


from flask import Flask, g

from .db import RedisClient

__all__ = ['app']

app = Flask(__name__)


def get_conn():
    if not hasattr(g, 'redis'):
        g.redis = RedisClient()
    return g.redis


@app.route('/')
def index():
    return '<h2>Welcome to Proxy Pool System</h2>'


@app.route('/random')
def get_proxy():
    """
    Get a proxy
    :return: 随机代理
    """
    conn = get_conn()
    return conn.random()


@app.route('/count')
def get_counts():
    """
    Get the count of proxies
    :return: 代理池总量
    """
    conn = get_conn()
    return str(conn.count())


if __name__ == '__main__':
    app.run()
