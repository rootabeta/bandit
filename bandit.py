import sys
from flask import Flask,redirect, url_for, request
import base64 #base64.b64decode(data)
from os import path,mkdir
import hashlib

app = Flask(__name__)

@app.route("/",methods=['POST'])
def upload():
    response = "Manifest: \r\n"
    for fname in request.form:
        try:
            content = request.form[fname]
            if "/" in fname:
                fname = fname.split("/")[-1] #no path traversal for youuuu
            fname = "uploads/" + fname
            contentd = base64.b64decode(content)
            assert(not path.exists(fname))
            with open(fname,"wb") as f:
                f.write(contentd)
            md5_hash = hashlib.md5()
            with open(fname, "rb") as h:
                content = h.read()
            md5_hash.update(content)
            digest = md5_hash.hexdigest()     
            response += "{} -> Successfully uploaded ({})\r\n".format(fname,digest)
        except AssertionError:
            response += "{} -> FAILED: File exists\r\n".format(fname)
    
    return response
            
@app.route("/overwrite",methods=['POST'])
def overwrite():
    response = "Manifest: \r\n"
    for fname in request.form:
        try:
            exists = False
            content = request.form[fname]
            if "/" in fname:
                fname = fname.split("/")[-1] #no path traversal for youuuu
            fname = "uploads/" + fname
            contentd = base64.b64decode(content)
            if(path.exists(fname)):
                exists = True
            with open(fname,"wb") as f:
                f.write(contentd)
            md5_hash = hashlib.md5()
            with open(fname, "rb") as h:
                content = h.read()
            md5_hash.update(content)
            digest = md5_hash.hexdigest()     
            if exists:
                response += "{} -> Successfully overwritten ({})\r\n".format(fname,digest)
            else: 
                response += "{} -> Successfully uploaded ({})\r\n".format(fname,digest)
        except:
            response += "{} -> FAILED: Unknown\r\n".format(fname)

    return response
    
if __name__ == "__main__":
    if not path.exists("uploads"):
        mkdir("uploads")
    if len(sys.argv) == 1:
        port = 8080
    else:
        port = int(sys.argv[1])
    app.run(host="0.0.0.0",port=port)
