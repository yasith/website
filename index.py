import webapp2
import jinja2
import os

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class Home(webapp2.RequestHandler):

  def get(self):

    template_values = {}

    template = jinja_environment.get_template('home.html')
    self.response.out.write(template.render(template_values))



args = [('/', Home),
       ('/blog', Home),
       ('/resume', Home),
       ('/portfolio', Home),
       ('/contact', Home)]

app = webapp2.WSGIApplication(args, debug=True)
