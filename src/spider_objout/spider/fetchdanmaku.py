class FetchDanmaku:
    def __init__(self, fet):
        self.fet = fet

        self.url = 'https://api.bilibili.com/x/v2/dm/wbi/web/seg.so'
        self.cid = '1196257131'
        self.params = {
            'type': '1',
            'oid': self.cid,
            'segment_index': '1',
            'pull_mode': '1',
            'ps': '0',
            'pe': '120000',
        }

    def fetchdanmaku(self, cid=''):
        if cid == '':
            return
        self.params["oid"] = cid
        req = self.fet.reqwrapper(self.url, self.params)
        resp = self.fet.request(req)
        return resp
