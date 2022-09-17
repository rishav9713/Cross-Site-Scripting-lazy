from flask import Flask, abort, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app, supports_credentials=True)
#cors = CORS(app)
#app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
def helloWorld():
  return {
	  "title" : "lazy ctf",
	  "desc" : "Real world CTF 2.0",
	  "challenge" : "Dont trust anyone",
   	  "total time" : "24 hrs",
	  "hint" : "/api/v1/users"
	 }


@app.route("/.well-known/security.txt")
def security():
  return '''
Contact: mailto:hacktekers@gmail.com <br>
Acknowledgements: https://hacktekers.org <br>
<br>
# Do not disclose any security vulnerability until its fixed ! <br>
'''

@app.route("/api/v1/users")
def apicall():
  if request.headers.get('Origin'):
   return {"message" : "well done ! you have exploited cors ! report this vulnerability to security team to get rewards !"}
  else:
   abort(403, "You are not allowed to access this resource, you are untrusted, i will send data only if you originate from trusted place !")

if __name__ == "__main__":
  app.run(port=5000)
