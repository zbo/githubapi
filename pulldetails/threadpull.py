import time
import threadpool
import urllib3

in_path = './in'
temp_save = '/Users/zhu/Downloads/cache_details_processed'


def get_changed_files(link):
    http = urllib3.PoolManager()
    r = http.request('GET', link, headers={'Authorization': 'token haha'})
    print(r.status)


def read_all(in_path):
    ret = []
    f = open(in_path, 'r', encoding='UTF-8')
    a = f.readline().strip()
    while a != '':
        ret.append(a)
        a = f.readline()
    return ret


if __name__ == '__main__':
    req_list = read_all(in_path)
    pool = threadpool.ThreadPool(1)
    requests = threadpool.makeRequests(get_changed_files, req_list)
    [pool.putRequest(req) for req in requests]
    pool.wait()
