import falcon
import msg

api = application = falcon.API()

msg = msg.Resource()
api.add_route('/msg/{to}',msg)