import asyncio
from proxybroker import Broker,Proxy
import grab


async def show(proxies):
    while True:
        proxy = await proxies.get()
        if proxy is None: break
        print('Found proxy: %s' % proxy)
        print(proxies)
        print(proxy.host)
        print(proxy.port)
        #print(type(proxy))


async def prx_srv(proxies):
    while True:
        proxy_for_parser = await proxies.get()
        print('start_proxy_for_parser')
        print('Found proxy: %s' % proxy_for_parser)
        g = grab.Grab()
        print('1')
        g.setup(proxy=proxy_for_parser.host+':'+str(proxy_for_parser.port),proxy_type='http')
        print('2')
        try:

            g.go('http://www.google.com/search?q=Spam')
        except:
            pass
        print('2.1')
        print(g.doc.url)
        print('3')
        proxy_for_parser = await proxies.get()


    #async def test_my_server():
    #proxy_server = Proxy('94.177.175.232', '3128')




proxies = asyncio.Queue()
broker = Broker(proxies)
tasks = asyncio.gather(
    broker.find(types={'HTTP':'High'}, limit=50, countries='CA'),prx_srv(proxies))


loop = asyncio.get_event_loop()
loop.run_until_complete(tasks)
#loop.run_until_complete(test_my_server())

#proxy_server = Proxy('94.177.175.232','3128')
#print(proxy_server.geo)
#print(proxy_server.is_working)
#help(asyncio.gather())