
import tornado.web
import tornado.ioloop

import BaseHandler

# from common import config
import common.config

class MainHandler(BaseHandler.BaseHandler):

    def get(self):
        common.config.config.logger.debug('')
        self.render("index.html")
