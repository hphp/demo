import cgi
import datetime
import logging

from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import images
from PIL import Image
from cStringIO import StringIO
logging.getLogger().setLevel(logging.DEBUG)


class Greeting(db.Model):
    author = db.UserProperty()
    content = db.StringProperty(multiline=True)
    avatar = db.BlobProperty()
    date = db.DateTimeProperty(auto_now_add=True)

class MainPage(webapp.RequestHandler):
    def get(self):
        self.response.out.write('<html><body>')
        self.response.out.write("""
              <form action="/sign" enctype="multipart/form-data" method="post">
                <div><label>Message:</label></div>
                <div><textarea name="content" rows="3" cols="60"></textarea></div>
                <div><label>Avatar:</label></div>
                <div><input type="file" name="img"/></div>
                <div><input type="submit" value="Sign Guestbook"></div>
              </form>
            </body>
          </html>""")

class Guestbook(webapp.RequestHandler):
    def post(self):
        imgfile = StringIO(self.request.get('img')) # to some type
        img = Image.open(imgfile) # img --> instance
        img = img.resize((100,100)) # support resize
        self.response.out.write(type(img)) # instance
        self.response.out.write(dir(img)) # many attributes
        #img.save("/home/hphp/temp.png") # could not , because have no writing rights.
        '''
        #below comes true , this str could get transformed to img , and show by the browser.
        output = StringIO()
        img.save(output, format='png')
        contents = output.getvalue()
        output.close()
        self.response.headers['Content-Type'] = "image/png"
        self.response.out.write(contents)
        '''

application = webapp.WSGIApplication([
    ('/', MainPage),
    ('/sign', Guestbook)
], debug=True)


def main():
    run_wsgi_app(application)


if __name__ == '__main__':
    main()
