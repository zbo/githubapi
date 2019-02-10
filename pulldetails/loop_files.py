import json
import os
import log

output = './out_file'

path = '/Users/zhu/Downloads/cache_details_processed'


def process(cache_path):
    sub_files = log.get_sub_files(cache_path)
    for file in sub_files:
        j = log.loadjson(file)
        if 'message' in j:
            continue
        try:
            log.write(str(j[0]['changes']), output)

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
