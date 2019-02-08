import os
import log
import json

path = './cache'
output = './out'
nocomments = './out_no_comments'
allpull = './result'


class codereview:
    def __init__(self):
        self.comments = []
        self.issue_comments = []
        self.review_comments = []
        self.pull_num = -1
        self.pull_link = ''
        self.reviewer = ''
        self.submit_at = ''


def loadjson(file):
    f = open(file, 'r', encoding='UTF-8')
    a = f.read()
    j = json.loads(str(a))
    f.close()
    return j


def get_sub_folder(path):
    ret = []
    children = os.listdir(path)
    for child in children:
        child = os.path.join(path, child)
        if os.path.isdir(child):
            ret.append(child)
    return ret


def find_review(file):
    a = file.split('/')
    a[1] = 'cache_review'
    a = '/'.join(a) + '.json'
    return a


def find_comment(file):
    a = file.split('/')
    a[1] = 'cache_comments'
    a = '/'.join(a) + '.json'
    return a


def find_issue(file):
    a = file.split('/')
    a[1] = 'cache_issue'
    a = '/'.join(a) + '.json'
    return a


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


def process_review(file, code_review):
    j = loadjson(file)
    if len(j) == 0:
        pass
    elif 'message' in j:
        pass
    else:
        for c in j:
            if len(c['body'].strip()) > 0:
                code_review.reviewer = c['user']['login']
                code_review.review_comments.append(c['body'])
                code_review.submit_at = c['submitted_at']

    return code_review


def process_comments(file, code_review):
    j = loadjson(file)
    if len(j) == 0:
        pass
    elif 'message' in j:
        pass
    else:
        for c in j:
            if len(c['body'].strip())>0:
                code_review.comments.append(c['body'])
    return code_review


def process_issue(file, code_review):
    j = loadjson(file)
    if len(j) == 0:
        pass
    elif 'message' in j:
        pass
    else:
        for c in j:
            if len(c['body'].strip()) > 0:
                code_review.issue_comments.append(c['body'])
    return code_review


def process(cache_path):
    sub_files = get_sub_files(cache_path)
    for file in sub_files:
        print(file)
        log.write(file+'\n', allpull)
        cache_review_path = find_review(file)
        cache_issue_path = find_issue(file)
        cache_comment_path = find_comment(file)
        c = codereview()
        c.pull_link = file
        c = process_review(cache_review_path, c)
        c = process_comments(cache_comment_path, c)
        c = process_issue(cache_issue_path, c)
        log_record(c)


def log_record(c):
    if len(c.review_comments) == 0 and len(c.comments) == 0 and len(c.issue_comments) == 0:
        log.write('=== ' + c.reviewer + ' ===' + c.submit_at + '\n', nocomments)
        log.write(c.pull_link + '\n', nocomments)
    else:
        log.write('=== ' + c.reviewer + ' ===' + c.submit_at + '\n', output)
        log.write(c.pull_link + '\n', output)
        log.write(str(c.comments) + '\n', output)
        log.write(str(c.issue_comments) + '\n', output)
        log.write(str(c.review_comments) + '\n', output)


if __name__ == '__main__':
    log.clear(output)
    log.clear(nocomments)
    sub = get_sub_folder(path)
    for folder in sub:
        sub2 = get_sub_folder(folder)
        for one in sub2:
            process(one)
