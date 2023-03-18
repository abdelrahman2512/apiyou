import flask
from flask import Flask , request

from youtubesearchpython import VideosSearch

app = Flask(__name__)

@app.route("/search")
def se():
	title = request.args.get("Title")
	yt = VideosSearch(title,limit=10)
	r = (yt.result()).get("result")
	return r
	
if __name__ == "__main__":
	app.run(debug=True)
	
	
