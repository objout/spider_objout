import os
import sys


def parsecookie(filename):
    """Parse the cookie from wget."""
    try:
        res = ''
        f = open(filename, 'r')
        lines = f.readlines()
        for line in lines:
            if line == '' or line[0] == '#' or line[0] == '\n':
                continue
            arr = line.split('\t')
            key = arr[5]
            val = arr[6].strip()
            res += f'{key}={val}; '
        res += 'nostalgia_conf=-1; path=/; domain=.bilibili.com'
        f.close()
        return res
    except Exception as err:
        raise err


def getcookie():
    """Use the shell script to get cookie."""
    try:
        dir = os.path.dirname(__file__)
        script_path = f'{dir}/get-cookies.sh'
        cookie_path = f'{dir}/cookies.txt'

        if os.path.exists(script_path):
            command = f'/bin/bash {script_path} {cookie_path}'
            os.system(command)
        else:
            sys.exit(1)
    except Exception as e:
        raise e

    return parsecookie(cookie_path)


def getheaders(referer='https://search.bilibili.com/all?'):
    """Get the headers needed by requesting."""
    headers = {
        'User-Agent': '''Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
(KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.54''',
        'Cookie': getcookie(),
        'Referer': referer,
        'Accept': """text/html,application/xhtml+xml,application/xml;q=0.9,\
image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7""",
    }
    return headers
