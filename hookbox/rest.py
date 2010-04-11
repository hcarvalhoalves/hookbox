import cgi
import logging

try:
    import json
except:
    import simplejson as json
    
class HookboxRest(object):
    logger = logging.getLogger('HookboxRest')
    def __init__(self, server):
      
        self.server = server
        self.user = None # hack to make channel implementation simpler
        
    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']
        handler = getattr(self, 'render_' + path[1:], None)
        if not handler:
            start_response('404 Not Found', ())
            return "Not Found"
        try:
            return handler(environ, start_response)
        except Exception, e:
            self.logger.warn('REST Error: %s', path, exc_info=True)
            start_response('500 Internal server error', [])
            return str(e)
    
    def render_publish(self, environ, start_response):
        form = get_form(environ)
        channel_name = form.get('channel_name', None)
        if not channel_name:
            raise Exception("Missing channel_name")
        payload = form.get('payload', 'null')
        originator = form.get('originator', None)
        channel = self.server.get_channel(None, channel_name)
        channel.publish(self, payload, needs_auth=False, originator=originator)
        start_response('200 Ok', [])
        return json.dumps([True, {}])

    def render_disconnect(self, environ, start_response):
        form = get_form(environ)
        identifier = form.get('identifier', None)
        if not channel:
            raise Exception("Missing channel_name")
        payload = form.get('payload', None)
        self.server.publish(self, channel, payload, pre_auth=True)
        start_response('200 Ok', [])
        return json.dumps([True, {}])

    def render_set_channel_options(self, environ, start_response):
        form = get_form(environ)
        channel_name = form.get('channel_name', None)
        if not channel_name:
            raise Exception("Missing channel_name")
        del form['channel_name']
        channel = self.server.get_channel(None, channel_name)
        channel.update_options(**form)
        start_response('200 Ok', [])
        return json.dumps([True, {}])
        
    def render_channel_info(self, environ, start_response):
        start_response('200 Ok', [])
        return json.dumps([True, {}])

def get_form(environ):
    form = {}
    if environ['REQUEST_METHOD'].upper() == 'POST':
        qs = environ['wsgi.input'].read()
    else:
        qs = environ['QUERY_STRING']
    for key, val in cgi.parse_qs(qs).items():
        form[key] = val[0]
    return form