import json
import os
import re
from io import BytesIO
from pprint import pformat, pprint

import boto3
import requests
from PIL import Image
from requests.exceptions import HTTPError

s3 = boto3.client('s3')

image_url = os.environ.get('IMAGE_URL') or 'https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png'
target_file = os.environ.get('TARGET_FILE') or 'header.txt'
filename = None

print('Attempting a request against \n   %s' % image_url)

regex_pattern = 'https:\/\/.*\/(.*)\.(jpg|gif|png)'
regex_search = re.match(regex_pattern, image_url)
if regex_search:
    filename = '%s.%s' % (regex_search.group(1), regex_search.group(2))
    print('URL is Valid')
else:
    print('URL is invalid... exiting')
    exit(1)

try:
    response = requests.get(image_url)
    response.raise_for_status()
except HTTPError as err:
    print('HTTPError : %s' % err)
except Exception as err:
    print('Misc Exception : %s' % err)
else:
    print('Request Successfull for %s' % filename)
    
    # Print Headers to Console
    print('Headers for \n   %s\n' % image_url)
    json_string = json.dumps(response.headers.__dict__['_store'])
    headers_json = json.loads(json_string)
    pprint(headers_json)

    # Save Header content to header.txt
    print('Writing to %s' % target_file)
    f = open(target_file,"w+")
    f.write(pformat(headers_json))
    f.close()
    print('Finished Writing %s' % target_file)

    # Save Image to file
    print('Writing image to %s' % filename)
    image = Image.open(BytesIO(response.content))
    image.save(filename)

    # Upload both to s3
    print('Uploading to image and headers to s3')
    bucket_name = os.environ.get('BUCKET_NAME') or 'python-png-info'
    s3.upload_file(filename, bucket_name, filename)
    s3.upload_file(target_file, bucket_name, target_file)

    # Upload this script!
    print('Uploading this very script to s3')
    s3.upload_file('main.py', bucket_name, 'main.py')
    print('Finished Uploading to s3')


