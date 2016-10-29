import sys
import time
from kazoo.client import KazooClient


if __name__ == '__main__':
    nodeName = sys.argv[1]
    print "Connector Start" + nodeName
    zk = KazooClient(hosts="192.168.56.112:2181,192.168.56.113:2181,192.168.56.112:2181")
    zk.start()
    stat = zk.create("/test/"+nodeName, b"example", ephemeral=True)
    time.sleep(20)
    print "Connector Closed"
    zk.stop()
