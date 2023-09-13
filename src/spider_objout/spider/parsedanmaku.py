import re

from google.protobuf import text_format

from .utils import bili_pb2


class ParseDanmaku:
    def __init__(self):
        self.reg = '.*?content:.*?"(.*?)".*?ctime.*?'
        self.pattern = re.compile(self.reg, re.S)

    def parse(self, data=''):
        """Parse the protobuf data."""
        try:
            danmakulist = []
            my_seg = bili_pb2.DmSegMobileReply()  # type: ignore
            my_seg.ParseFromString(data)
            for j in my_seg.elems:
                res = text_format.MessageToString(j, as_utf8=True)
                content = self.pattern.match(res).group(1)  # type: ignore
                danmakulist.append(content)
            return danmakulist
        except Exception as e:
            raise e
