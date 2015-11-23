# This script created a queue
#
# Author - Paul Doyle Nov 2015
#
#
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
access_key_id = code[0:20]
secret_access_key = code[21:-1]

print(access_key_id)
print(secret_acess_key)

# Set up a connection to the AWS service.
conn = boto.sqs.connect_to_region("eu-west-1", aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)

# Get a list of the queues that exists and then print the list out
rs = conn.get_all_queues()
for q in rs:
	print q.id
