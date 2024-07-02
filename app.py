from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/", methods=["GET","POST"])
def index():
  return(render_template("index.html"))

@app.route("/main",methods=["GET","POST"])
def main():
  r= request.form.get("q")
  print(r)
  return(render_template("main.html",))      
if __name__ == "__main__":
  app.run()
