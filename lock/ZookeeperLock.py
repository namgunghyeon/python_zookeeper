import logging, os
from kazoo.client import KazooClient
from kazoo.recipe.lock import Lock

class ZookeeperLock(object):
    def __init__(self, hosts, name, logger=None, timeout=1):
         #hosts="192.168.56.112:2181,192.168.56.113:2181,192.168.56.112:2181"
         self.hosts = hosts
         self.zkClient = None
         self.timeout = timeout
         self.logger = logger
         self.name = name
         self.createLock()

    def createLock(self):
        try:
            self.zkClient = KazooClient(hosts=self.hosts, logger=self.logger, timeout=self.timeout)
            self.zkClient.start(timeout=self.timeout)
        except Exception, ex:
            print "Create KazooClient failed! Exception: %s" % str(ex)

        try:
            lockPath = os.path.join("/", "locks", self.name)
            self.lockHandle = Lock(self.zkClient, lockPath)
        except Exception, ex:
            self.err_str = "Create lock failed! Exception: %s" % str(ex)

    def destroyLock(self):
        if self.zkClient != None:
            self.zkClient.stop()
            self.zkClient = None

    def acquire(self, blocking=True, timeout=None):
        if self.lockHandle == None:
            return None

        try:
            return self.lockHandle.acquire(blocking=blocking, timeout=timeout)
        except Exception as e:
            self.err_str = "Acquire lock failed! Exception: %s" % str(ex)
            return None

    def release(self):
        if self.lockHandle == None:
            return None

        return self.lockHandle.release()
