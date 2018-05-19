import os
import json
from flask import Flask, redirect, render_template, request, flash, url_for

app = Flask(__name__)



if __name__ == "__main__":
    app.run(host= os.environ.get("IP"),
    port= int(os.environ.get("PORT")),
    debug= True)