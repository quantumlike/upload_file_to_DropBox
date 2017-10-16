import dropbox 
import sys
# from time import sleep

#Using DropBox API v2.

# This will fail if use an invalid authorization code
access_token = '<your access token>' # Put the access token obtained from previous file here
print ("Your access token is:", access_token)
dbx = dropbox.Dropbox(access_token)
# sleep(3)
dbx.users_get_current_account()
print (dbx.users_get_current_account())


file_from = '/home/0012.jpg'
dest_path = '/test/0012.jpg'
with open(file_from, 'rb') as f:
    dbx.files_upload(f.read(), dest_path)
    print ('uploaded to DropBox')
