
import os

import tornado.web
import tornado.ioloop

from tornado.options import define, options, parse_command_line

import MainHandler
import LoginHandler
from common import config

define("port", default=8989, help="run on the given port", type=int)
define("debug", default=False, help="run in debug mode")

#https://github.com/futurechallenger/pytornado.git
#git@github.com:futurechallenger/pytornado.git

def main():
    parse_command_line()
    application = tornado.web.Application(
                    [(r"/", MainHandler.MainHandler)
                    , (r"/login", LoginHandler.LoginHandler)]
                    , cookie_secret="61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo="
                    , template_path=os.path.join(os.path.dirname(__file__), "templates")
                    , static_path=os.path.join(os.path.dirname(__file__), "static")
                    , xsrf_cookies=True
                    , debug=options.debug)
    application.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()

    print 'prepare logger'

    '''parepare logger
    '''
    config.config.configurations = {
                "current_path": os.path.dirname(__file__)
                }
