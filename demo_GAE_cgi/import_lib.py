import cgi

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app


import PIL
import numpy
'''
from google.appengine.dist import use_library
use_library('django', '1.1')  # could not work , know nothing right now.
#import cv2 # could not, because it did not support
import matplotlib
'''

class MainPage(webapp.RequestHandler):
    def get(self):
        self.response.out.write("""
          <html>
            <body>
              <form action="/sign" method="post">
                <div><textarea name="content" rows="3" cols="60"></textarea></div>
                <div><input type="submit" value="submit"></div>
                <div><input type="file" name="content"></input></div>
                <div><input type="submit" value="upload"></div>
              </form>
            </body>
          </html>""")


class Guestbook(webapp.RequestHandler):
    def post(self):
        self.response.headers['Content-Type'] = 'image/jpeg'
        self.response.out.write('<html><body>You wrote:<pre>')
        self.response.out.write(cgi.escape(self.request.get('content')))
        self.response.out.write('</pre></body></html>')

application = webapp.WSGIApplication(
                                     [('/', MainPage),
                                      ('/sign', Guestbook)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
