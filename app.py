import pymongo
from flask import *

client = pymongo.MongoClient(
    "mongodb+srv://ziv:nm123456@ziv.ljfz9lq.mongodb.net/?retryWrites=true&w=majority&appName=ziv")
print("success")
app = Flask(
    __name__,
    static_folder="public",
    static_url_path="/"
)
app.secret_key = "key22"

db = client.lunch


@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/user", methods=["POST"])
def user():
    name = request.form.get("username")
    session["username"] = name
    passwd = request.form.get("password")
    collection = db.user

    collection.insert_one({
        "username": name,
        "password": passwd
    })

    return render_template("user.html", username=name)


@app.route("/yc")
def yc():

    return "沒ㄐㄐ"


app.run(port=5000, debug=True)
