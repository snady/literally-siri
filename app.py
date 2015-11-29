from flask import Flask, render_template, session, request
from flask import redirect, url_for
import util
import re

app = Flask(__name__)

@app.route("/", methods = ['GET','POST'])
def index():
        if request.method == 'GET':
                try:
                        error = request.args.get('error')
                        if error != None:
                                return render_template("main.html",error = error)
                except:
                        pass
        return render_template("main.html")
        
        
@app.route("/answers", methods = ['GET','POST'])
def answer():
        if request.method == 'GET':
                if request.args.get('optbtn') == 'who':
                        #This is a who query: construct ans accordingly
                        query = request.args.get('query')
                        result = util.getNames(query)
                        ans = util.getAnswer(result)
                        
                elif request.args.get('optbtn') == 'when':
                        #this is a when quer: construct ans accordingly
                        query = request.args.get('query')
                        result = util.getDates(query)
                        ans = util.getAnswer(result)
                else:
                        #someone tried to get to answers direct url, redirects to error
                        return redirect("/?error=%s" % "ERROR: INVALID QUERY")
        else:
                return redirect("/")

        return render_template("answers.html", ans=ans)

if __name__ == "__main__":
        app.secret_key = "hello"
        app.run(host='0.0.0.0', port=8000)
