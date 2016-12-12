#! /usr/bin/python3
# _encoding:utf-8_
# Written by liuzhaoyang
# wcontact:liu575563079@gmail.com

# 发送大型的udp数据包

import IN,argparse,socket

if not hasattr(IN,'IP_MTU'):
    raise RuntimeError('can not perform MTU discovery on this cmbination of operating system and python distrubution')

def send_big_datagram(host,port):
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.setsockopt(socket.IPPROTO_IP,IN.IP_MTU_DISCOVER,IN.IP_PMTUDISC_DO)
    sock.connect((host,port))

    try:
        sock.send('#',65000)
    except socket.error:
        print('lzy the datagram did not make it')
        max_mtu = sock.getsockopt(socket.IPPROTO_IP,IN.IP_MTU)
        print('mtu  {}'.format(max_mtu))
    else:
        print('the big datagram was send')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='send udp packet to get mtu')
    parser.add_argument()
