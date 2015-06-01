import falcon
from datetime import datetime


class Resource(object):
    messages = {"uno": "dos"}

    def on_get(self, req, resp, to):
        if not self.messages.has_key(to):
            resp.status = falcon.HTTP_NOT_FOUND
        else:
            resp.status = falcon.HTTP_200
            resp.body = self.messages[to]

    def on_post(self, req, resp, to):
        content = req.get_param("message")
        self.messages[to] = content
        resp.status = falcon.HTTP_200
        resp.body = content  # self.messages[to]

	