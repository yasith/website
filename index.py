import webapp2
import jinja2
import os
import cgi

from google.appengine.api import mail

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class Home(webapp2.RequestHandler):

  def get(self):

    template_values = {}

    template = jinja_environment.get_template('index.html')
    self.response.out.write(template.render(template_values))

class SendMail(webapp2.RequestHandler):

  def post(self):
    name = cgi.escape(self.request.get('name'))
    email = cgi.escape(self.request.get('email'))
    content = cgi.escape(self.request.get('content'))

    message = mail.EmailMessage(sender= "Tuxv.Net <tuxv@tuxv.net>",
                                    subject="Email from tuxv.net contact form")

    message.to = "Yasith Vidanaarachchi <yasith@tuxv.net>"
    message.reply_to = name + " <" + email + ">"
    message.body = content

    message.send()


args = [('/', Home),
       ('/sendmail', SendMail)]

app = webapp2.WSGIApplication(args, debug=True)
