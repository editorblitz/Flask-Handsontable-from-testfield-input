from flask import Flask, request, render_template
import re
import json
import numpy as np
import pandas as pd

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/convert", methods=["POST"])
def convert():
    data = request.form.get("inputText").split("\n")
    data = [re.sub('\r', '', line) for line in data]
    data = [line.split("\t") for line in data]

    df = pd.DataFrame(data)

    content = f"""
    {data}
    """
# https://stackoverflow.com/questions/15321431/how-to-pass-a-list-from-python-by-jinja2-to-javascript

    return render_template("result.html", content=content, the_data=data, tables=[df.to_html(classes='data', header="true")])
   # return render_template("result.html", content=content, the_data=json.dumps(data))


if __name__ == "__main__":
    app.run(debug=True)
