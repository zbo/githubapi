import json
import os
import log
import operator

output = './out_file'

path = '/Users/zhu/Downloads/cache_details_processed'

file_dict = {}


def extract_all_changed_files(owner_name, repo_name, j):
    for n in j:
        key = '{owner}/{repo}/contents/{file}'.format(owner=owner_name, repo=repo_name, file=n['filename'])
        if not key in file_dict:
            file_dict[key] = 1
        else:
            value = file_dict[key]
            value = value + 1
            file_dict[key] = value


def process(cache_path):
    repo_name = os.path.basename(cache_path)
    sub_files = log.get_sub_files(cache_path)
    for file in sub_files:
        j = log.loadjson(file)
        if len(j) == 0:
            continue
        if 'message' in j:
            continue
        try:
            extract_all_changed_files(owner_name, repo_name, j)
        except:
            print(file)
            raise


if __name__ == '__main__':
    log.clear(output)
    sub = log.get_sub_folder(path)
    for folder in sub:
        owner_name = os.path.basename(folder)
        sub2 = log.get_sub_folder(folder)
        for one in sub2:
            process(one)
    d = sorted(file_dict.items(), key=operator.itemgetter(1), reverse=True)
    for n in d:
        log.write('{0} {1}\n'.format(n[0], n[1]), output)
    pass
