import urllib.parse
import urllib.request

from .getheaders import getheaders


class Fetch:
    def __init__(self):
        self.headers = getheaders()

    def reqwrapper(self, url, params):
        """Request wrapper."""
        params = urllib.parse.urlencode(params)
        url = f'{url}?{params}'
        return urllib.request.Request(url=url, headers=self.headers)

    def request(self, req):
        """Open request."""
        return urllib.request.urlopen(req).read()
