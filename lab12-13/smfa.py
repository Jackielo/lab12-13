from flask import Flask, Response, render_template, request
import json
from subprocess import Popen, PIPE
import os
from tempfile import mkdtemp
from werkzeug import secure_filename

app = Flask(__name__)

@app.route("/")
def index():
  return "Hello?"

@app.route('/queues',	methods=['GET'])
def	queues_index():
  """
  List	all	queues
  curl	-s	-X	GET	-H	'Accept:	application/json'	http://localhost:5000/queues	|	python	-mjson.tool
  """
  all	=	[]
  conn	=	get_conn()
  for	q	in	conn.get_all_queues():
  all.append(q.name)
  resp	=	json.dumps(all)
  return	Response(response=resp,	mimetype="application/json")

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080, debug=True)