import gzip
import re


class FetchCid:
    def __init__(self, fet):
        self.fet = fet

        self.urltpl = 'https://www.bilibili.com/video/{}/'
        self.params = {
            'spm_id_from': '333.337.search-card.all.click'
        }

        self.reg = '.*?__INITIAL_STATE__.*?"cid":(.*?),".*?'
        self.pattern = re.compile(self.reg, re.S)

        self.vid = ''

    def parse(self, resp=b''):
        res = gzip.decompress(resp).decode()
        return res

    def fetchvdpage(self):
        """Fetch video page by video id."""
        url = self.urltpl.format(self.vid)
        req = self.fet.reqwrapper(url, self.params)
        resp = self.fet.request(req)
        return self.parse(resp)

    def extractcid(self, content=''):
        """Extract cid of the video page."""
        ret = self.pattern.match(content)
        if ret is not None:
            return ret.group(1)
        else:
            return -1

    def fetchcid(self, vid=''):
        self.vid = vid

        html = self.fetchvdpage()
        return self.extractcid(html)
