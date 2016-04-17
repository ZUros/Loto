#!/usr/bin/env python
import os
import jinja2
import webapp2
import random


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):

        return self.render_template("index.html")

class MainHandler_loto(BaseHandler):
    def get(self):

        import random

        glavne_stevilke =[]
        dodatna_stevilka =[]
        glavne_stevilke_koliko = 0
        dodatna_stevilka_koliko = 0

        while glavne_stevilke_koliko<6:
            stevilka=random.randint(1,40)
            if stevilka not in glavne_stevilke:
                glavne_stevilke.append(stevilka)
                glavne_stevilke_koliko+=1

        while dodatna_stevilka_koliko<1:
            stevilka=random.randint(1,40)
            if stevilka not in dodatna_stevilka:
                dodatna_stevilka.append(stevilka)
                dodatna_stevilka_koliko+=1

        glavne_stevilke.sort()
        dodatna_stevilka.sort()

        print (glavne_stevilke,dodatna_stevilka)

        return self.render_template("loto.html")

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/loto', MainHandler_loto),
], debug=True)
