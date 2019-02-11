import csv
import log

filename = './result.csv'
output = './test'


def process(line_num, row):
    arr = row[2].split('/')
    owner = arr[0]
    repo = arr[1]
    url = 'https://github.microstrategy.com/{owner}/{repo}/tree/next/{tail}'.format(owner=owner, repo=repo, tail='')
    log.write('{0},{1},{2},{3}\n'.format(str(line_num), row[0], row[1], str(url)), output)


if __name__ == '__main__':
    log.clear(output)
    with open(filename) as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == '0':
                process(reader.line_num, row)
