


import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    '''
    '''
    # def __init__(self):
    #     super(self.__class__, self).__init__()
    #     '''
    #         init logging stuff
    #     '''


    '''
    '''
    def get_current_user(self):
        user_json = self.get_secure_cookie("strapUser")

        if not user_json:
            return None

        return tornado.escape.json_decode(user_json)
