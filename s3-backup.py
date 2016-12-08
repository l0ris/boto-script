from boto.s3.connection import S3Connection
from boto.s3.key import Key
import boto
#create connection
conn = S3Connection(aws_access_key_id=’YOUR_ACCESS_KEY’,aws_secret_access_key=’YOUR_SECRET_ACCESS_KEY’)

#create S3 bucket
b = conn.create_bucket(‘new-bucket-name’)
k = Key(b)

#choose destination object name
dest = raw_input (“destination file name in s3?”)

dest2 = “%s” % dest
k.key = dest2

# put local file name you want to backup to S3
source = raw_input (“source file name which you want to backup?”)
source2 = “%s” % source
k.set_contents_from_filename(source2)
