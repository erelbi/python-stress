import glob
import threading,random
import os
import time
import tempfile
import subprocess
import socket
import requests
import wget

def disk(disk):
    bash_command = 'dd if=/dev/zero of=/tmp/test.file bs=1M count=10000'
    timeout = time.time() + 60*float(1)
    while True:
        disk_test = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)
        # output, error = disk_test.communicate()
        print(disk)
        if time.time() > timeout:
            break
def cpu(cpu):
    timeout = time.time() + 60 * float(1)
    bash_command2 = 'stress -c 4 -t 1'
    while True:
        cpu_test = subprocess.Popen(bash_command2.split(), stdout=subprocess.PIPE)
        # output, error = cpu_test.communicate()
        print(cpu)
        if time.time() > timeout:
            break
def memory(memory):
    timeout = time.time() + 60 * float(1)
    bash_command3 =  "stress-ng --vm 2 --vm-bytes 2G -t 1"
    while True:
        mem_test= subprocess.Popen(bash_command3.split(), stdout=subprocess.PIPE)
        # output, error = mem_test.communicate()
        print(memory)
        if time.time() >timeout:
            break


def network(network):
    url = 'http://doc.deney.site/genel_linux_komutlari_kullan%c4%b1mlar%c4%b1.pdf'
    file = requests.get(url, allow_redirects=True)
    timeout = time.time() + 60 * float(1)
    while True:
        open('file.test', 'wb').write(file.content)
        print(network)
        if time.time() > timeout:
                 break

t1 = threading.Thread(target=disk, args =("disk stress work",))
t1.start()
t2 = threading.Thread(target=cpu, args =("cpu stress work",))
t2.start()
t3 = threading.Thread(target=memory, args=("memory stress work",))
t3.start()
t4 = threading.Thread(target=network, args=("network stress work",))
t4.start()
