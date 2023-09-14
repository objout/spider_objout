import threading
from .persistent.persistent import Persistent
from .spider.utils.fetch import Fetch
from .spider.fetchcid import FetchCid
from .spider.fetchdanmaku import FetchDanmaku
from .spider.fetchvid import FetchVideoId
from .spider.parsedanmaku import ParseDanmaku
from .visualizing.visualize import Visualize

fet = Fetch()
fetcid = FetchCid(fet)
fetdan = FetchDanmaku(fet)
parsedan = ParseDanmaku()
fetvid = FetchVideoId(fet)

danmakumap = {}


def fetchDanmakuContent(vidl=[]):
    for vid in vidl:
        cid = fetcid.fetchcid(vid)
        raw = fetdan.fetchdanmaku(cid)  # type:ignore
        res = []
        try:
            res = parsedan.parse(raw)  # type:ignore
        except Exception:
            continue
        for item in res:
            k = item.strip()
            danmakumap[k] = danmakumap.get(k, 0) + 1  # type:ignore


def create_thread(vl):
    ret = threading.Thread(
            target=fetchDanmakuContent,
            args=(vl,))
    return ret


def main():
    try:
        fname = 'danmakumap.xlsx'
        kwd = '日本核污染水排海'
        page = 8

        per = Persistent(fname)
        vs = Visualize(fname)

        vidlist = fetvid.fetchvid(kwd=kwd, page=page)
        p1 = len(vidlist) >> 2
        p2 = p1 << 1
        p3 = p1 * 3

        threads = []
        threads.append(create_thread(vidlist[:p1]))
        threads.append(create_thread(vidlist[p1:p2]))
        threads.append(create_thread(vidlist[p2:p3]))
        threads.append(create_thread(vidlist[p3:]))
        for t in threads:
            t.start()
        for t in threads:
            t.join()

        global danmakumap
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
