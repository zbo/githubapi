import json
import os
import log

output = './out_file'

path = '/Users/zhu/Downloads/cache_details_processed'


def extract_all_changed_files(j):
    for n in j:
        print(n)


def process(cache_path):
    sub_files = log.get_sub_files(cache_path)
    for file in sub_files:
        j = log.loadjson(file)
        if len(j) == 0:
            continue
        if 'message' in j:
            continue
        try:
            extract_all_changed_files(j)
        except:
            print(file)


if __name__ == '__main__':
    log.clear(output)
    sub = log.get_sub_folder(path)
    for folder in sub:
        sub2 = log.get_sub_folder(folder)
        for one in sub2:
            process(one)
            log.write('\n', output)
