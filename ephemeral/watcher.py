import sys
import time
from kazoo.client import KazooClient

zk = KazooClient(hosts="192.168.56.112:2181,192.168.56.113:2181,192.168.56.112:2181")
zk.start()
if zk.exists("/test"):
    print '/test exists'
else:
    zk.create('/test')

@zk.ChildrenWatch('/test')
def watchChilden(children):
    print children



if __name__ == '__main__':
    while True:
        time.sleep(5)
