import logging, os, time
from ZookeeperLock import ZookeeperLock

def main():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    sh = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s -%(module)s:%(filename)s-L%(lineno)d-%(levelname)s: %(message)s')
    sh.setFormatter(formatter)
    logger.addHandler(sh)

    zookeeperHosts = "192.168.56.112:2181,192.168.56.113:2181,192.168.56.112:2181"
    lockName = "test"

    lock = ZookeeperLock(zookeeperHosts, lockName, logger=logger)

    ret = lock.acquire(False)

    if not ret:
        logging.info("Can't get lock! Ret: %s", ret)
        return

    logging.info("Get lock! Do something! Sleep 10 secs!")
    for i in range(1, 11):
        time.sleep(1)
        print str(i)

    lock.release()

if __name__ == "__main__":
    try:
        main()
    except Exception, ex:
        print "Ocurred Exception: %s" % str(ex)
        quit()
