import os
import log
import json
import shutil

output = './out'
inputfile = './in'
path = '/Users/zhu/Downloads/cache_details'
defect_path = './defects'
non_defects_path = './non_defects'
count = 0


def get_sub_folder(path):
    ret = []
    children = os.listdir(path)
    for child in children:
        child = os.path.join(path, child)
        if os.path.isdir(child):
            ret.append(child)
    return ret


def get_sub_files(path):
    ret = []
    if not os.path.exists(path):
        return ret
    children = os.listdir(path)
    for child in children:
        child = os.path.join(path, child)
        if not os.path.isdir(child):
            ret.append(child)
    return ret


def loadjson(file):
    f = open(file, 'r', encoding='UTF-8')
    a = f.read()
    j = json.loads(str(a))
    f.close()
    return j


def MoveFileToDefects(file,de):
    log.write('{0}|{1}\n'.format(de,file),output)


def MoveFileToNonDefects(file):
    # shutil.copy(file, non_defects_path)
    print(file)

def GetChangedFilesLink(j):
    log.write('{0}/files\n'.format(j['url']), inputfile)


def JudgeDefect(file):
    j = loadjson(file)
    if len(j) == 0:
        pass
    elif 'DE' in j['head']['ref']:
        MoveFileToDefects(file, j['head']['ref'])
        GetChangedFilesLink(j)
    else:
        MoveFileToNonDefects(file)


def process(cache_path):
    sub_files = get_sub_files(cache_path)
    for file in sub_files:
        JudgeDefect(file)


def clear_path(clear_path):
    if os.path.exists(clear_path):
        os.rmdir(clear_path)


if __name__ == '__main__':
    log.clear(output)
    # clear_path(defect_path)
    # clear_path(non_defects_path)
    # os.mkdir(defect_path)
    # os.mkdir(non_defects_path)
    sub = get_sub_folder(path)
    for folder in sub:
        sub2 = get_sub_folder(folder)
        for one in sub2:
            process(one)
