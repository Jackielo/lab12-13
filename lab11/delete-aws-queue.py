import boto.sqs
import boto.sqs.queue
from boto.sqs.message import Message
from boto.sqs.connection import SQSConnection
from boto.exception import SQSError
import sys
import urllib2

# Get the keys from a specific url and then use them to connect to AWS Service
req = urllib2.Request('http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key')
f = urllib2.urlopen(req)
code = f.read()
access, key = code.split(":")
access_key_id = access
secret_access_key = key


# Set up a connection to the AWS service.
conn = boto.sqs.connect_to_region("eu-west-1", aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)


#rs = conn.delete_queue(sys.argv[1])
rs = conn.get_all_queues()
print sys.argv[1]
for q in rs:
  if q.id == sys.argv[1]:
    print q.id
    conn.delete_queue(q)
