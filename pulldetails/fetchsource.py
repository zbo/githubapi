import urllib3
import log
import threadpool
import threading

in_path = './out_file'
git_address = 'https://github.microstrategy.com/api/v3/repos'
final_store = []
lock = threading.Lock()
output = './out_count_lines_defects'
error_lock = threading.Lock()


class FileAna:
    def __init__(self, l, d, s):
        self.lines = l
        self.defects = d
        self.source = s


def write_to_file(file_ana):
    f = open(output, 'a', encoding='UTF-8')
    for fa in file_ana:
        f.writelines('{0},{1},{2}\n'.format(fa.lines, fa.defects, fa.source))
    f.flush()
    f.close()


def get_source_files(line):
    try:
        arr = line.split()
        last = len(arr) - 1
        de = int(arr[last])
        tail = line[:line.index(str(de))]
        url = '{git}/{tail}'.format(git=git_address, tail=tail)
        http = urllib3.PoolManager()
        r = http.request('GET', url,
                         headers={'Authorization': 'token {0}'.format(t), 'Accept': 'application/vnd.github.v3.raw'})
        total_lines = bytes.decode(r.data).count('\n')
        file_ana = FileAna(l=total_lines, d=de, s=tail)
        final_store.append(file_ana)
        lock.acquire()
        if len(final_store) > 500:
            write_to_file(final_store)
            final_store.clear()
        lock.release()
    except:
        error_lock.acquire()
        log.write(url + '\n', './error')
        error_lock.release()


if __name__ == '__main__':
    log.clear(output)
    t = log.read_token()
    req_list = log.read_all(in_path)
    pool = threadpool.ThreadPool(50)
    requests = threadpool.makeRequests(get_source_files, req_list)
    [pool.putRequest(req) for req in requests]
    pool.wait()
