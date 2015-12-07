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
Available API endpoints:

GET /containers                     List all containers
GET /containers?state=running      List running containers (only)
GET /containers/<id>                Inspect a specific container
GET /containers/<id>/logs           Dump specific container logs
GET /images                         List all images


POST /images                        Create a new image
POST /containers                    Create a new container

PATCH /containers/<id>              Change a container's state
PATCH /images/<id>                  Change a specific image's attributes

DELETE /containers/<id>             Delete a specific container
DELETE /containers                  Delete all containers (including running)
DELETE /images/<id>                 Delete a specific image
DELETE /images                      Delete all images

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

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080, debug=True)