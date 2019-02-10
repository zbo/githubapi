import time
import threadpool
import urllib3
import os
import log
import json

in_path = './in'
temp_save = '/Users/zhu/Downloads/cache_details_processed'


def loadjson(file):
    f = open(file, 'r', encoding='UTF-8')
    a = f.read()
    j = json.loads(str(a))
    f.close()
    return j


def verifyjson(filepath):
    try:
        loadjson(filepath)
    except:
        print('invalid json {0}'.format(filepath))

def get_changed_files(link):
    tail = link[link.index('repos'):]
    tail = tail.split('/')
    filepath = '{0}/{1}/{2}/{3}.json'.format(temp_save, tail[1], tail[2], tail[4])
    folderpath = '{0}/{1}/{2}'.format(temp_save, tail[1], tail[2])
    if not os.path.exists(folderpath):
        os.makedirs(folderpath)
    if os.path.exists(filepath):
        verifyjson(filepath)
        return
    else:
        http = urllib3.PoolManager()
        r = http.request('GET', link, headers={'Authorization': 'token u can guess'})
        log.write(bytes.decode(r.data), filepath)


def read_all(in_path):
    ret = []
    f = open(in_path, 'r', encoding='UTF-8')
    a = f.readline().strip()
    while a != '':
        ret.append(a)
        a = f.readline().strip()
    return ret


if __name__ == '__main__':
    req_list = read_all(in_path)
    pool = threadpool.ThreadPool(100)
    requests = threadpool.makeRequests(get_changed_files, req_list)
    [pool.putRequest(req) for req in requests]
    pool.wait()
