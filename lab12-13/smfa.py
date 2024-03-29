from flask import Flask, Response, render_template, request
import json
from subprocess import Popen, PIPE
import os
from tempfile import mkdtemp
from werkzeug import secure_filename

app = Flask(__name__)

@app.route("/")
def index():
  return """
  Create: curl	-X	POST	-H	'Content-Type:	application/json'	http://localhost:5000/queues	-d	'{"name":	"my-queue"}'
  Delete: curl	-X	DELETE	-H	'Accept:	application/json'	http://localhost:5000/queues/<mytestqueue>
  Get number of messages: curl	-X	GET	-H	'Accept:	application/json'	http://localhost:5000/queues/<mytestqueue>/msgs/count
  Write a message: curl	-s	-X	POST	-H	'Accept:	application/json'	http://localhost:5000/queues/<mytestqueue>/msgs	-d
  '{"content":	"this	is	the	message	I	want	to	put	on	the	queue"}'
  Read a message: curl	-X	GET	-H	'Accept:	application/json'	http://localhost:5000/queues/<mytestqueue>/msgs
  Read and erase a message: curl	-X	DELETE	-H	'Accept:	application/json'	http://localhost:5000/queues/<mytestqueue>/msgs
  """

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

def	get_conn():
  key_id,	secret_access_key	=	urllib2.urlopen("http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key").read().split(':')
  return	boto.sqs.connect_to_region("eu-west-1",	aws_access_key_id=key_id,	aws_secret_access_key=secret_access_key)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000, debug=True)