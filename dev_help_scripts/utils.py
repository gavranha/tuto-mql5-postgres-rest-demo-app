import psutil as ps


def gethostip():
    addrs = ps.net_if_addrs()
    eth0 = addrs["eth0"]
    snicaddr = eth0[0]
    ip = snicaddr[1]
    return ip
