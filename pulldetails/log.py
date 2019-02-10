import json
import os


def write(content, out):
    f = open(out, 'a', encoding='UTF-8')
    f.writelines(content)
    f.flush()
    f.close()


def clear(out):
    if os.path.exists(out):
        os.remove(out)


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