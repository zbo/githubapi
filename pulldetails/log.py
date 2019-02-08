import os


def write(content, out):
    f = open(out, 'a',  encoding='UTF-8')
    f.writelines(content)
    f.flush()
    f.close()


def clear(out):
    if os.path.exists(out):
        os.remove(out)
