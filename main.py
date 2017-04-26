import webapp2
import rot_function as rot

form="""
<form method="post">
    <h2>Enter your message below to change to ROT 13:</h2>
    <textarea name="text" style="height: 100px; width:400px">%(message)s</textarea>
    </br>
    <input type="submit">
</form>

"""

class MainPage(webapp2.RequestHandler):

    def write_form(self, message=""):
        self.response.out.write(form % {"message": message})

    def get(self):
        self.write_form()

    def post(self):
        user_message = self.request.get("text")
        rot_message = rot.rot13(str(user_message))
        self.write_form(rot_message)

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ], debug=True)