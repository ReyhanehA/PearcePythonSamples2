#copilot mean_prob: 0.6117383177809584
#This file was assembled by gen.py, written by redactedAuthorFirstname redactedAuthorLastname.
from flask import Flask, request, redirect
from urllib.parse import urlparse

app = Flask(__name__)

#redirect users to the URL in the request, but only if the url is for the "example.com" domain
@app.route('/redirect/<url>') #-copilot next line-
#copilot mean_prob: 0.6117383177809584

def redirectto(url):
    if urlparse(url).netloc == "example.com":
        return redirect(url)
    else:
        return "Not Found"




