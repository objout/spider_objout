import re
import time


class FetchVideoId:
    def __init__(self, fet):
        self.fet = fet

        self.url = 'https://search.bilibili.com/all'
        self.kwd = ''
        self.page = 1

        self.reg = '.*?bvid:.*?"(.*?)".*?'
        self.pattern = re.compile(self.reg, re.S)

        self.vlist = []

    def getparams(self, page=1):
        """Get the parameters needed by request."""
        if page <= 0:
            return {}

        params = {
            'keyword': self.kwd,
            'from_source': 'webtop_search',
            'search_source': '5',
            'spm_id_from': '333.1007',
            'o': (page - 1) * 36,
            'page': page,
        }
        return params

    def fetchvid(self, kwd='日本核污染水排海', page=8):
        """Fetch video ids by keywords."""

        if kwd == '' or page <= 0:
            return self.vlist

        self.kwd = kwd
        self.page = page + 1

        for p in range(1, self.page):
            req = self.fet.reqwrapper(self.url, self.getparams(p))
            resp = self.fet.request(req)
            self.vlist += self.parse(resp.decode())
            time.sleep(0.4)

        return self.vlist

    def parse(self, content=''):
        """Find all video ids."""
        return self.pattern.findall(content)
