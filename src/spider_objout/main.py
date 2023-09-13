from .persistent.persistent import Persistent
from .spider.utils.fetch import Fetch
from .spider.fetchcid import FetchCid
from .spider.fetchdanmaku import FetchDanmaku
from .spider.fetchvid import FetchVideoId
from .spider.parsedanmaku import ParseDanmaku
from .visualizing.visualize import Visualize


def main():
    try:
        fname = 'danmakumap.xlsx'
        kwd = '日本核污染水排海'
        page = 8

        fet = Fetch()
        fetvid = FetchVideoId(fet)
        fetcid = FetchCid(fet)
        fetdan = FetchDanmaku(fet)
        parsedan = ParseDanmaku()
        per = Persistent(fname)
        vs = Visualize(fname)

        vidlist = fetvid.fetchvid(kwd=kwd, page=page)
        danmakumap = {}

        for vid in vidlist:
            cid = fetcid.fetchcid(vid)
            raw = fetdan.fetchdanmaku(cid)  # type:ignore
            res = parsedan.parse(raw)  # type:ignore
            for item in res:
                k = item.strip()
                danmakumap[k] = danmakumap.get(k, 0) + 1

        danmakumap = sorted(
            zip(danmakumap.values(), danmakumap.keys()),
            reverse=True
        )
        per.write(danmakumap)
        print(danmakumap[:20])
        vs.run()
        return 0
    except Exception as e:
        raise e


if __name__ == "__main__":
    main()
