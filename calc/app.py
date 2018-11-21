from flask import Flask, request
from operations import ops_dict

app = Flask(__name__)


@app.route("/<operation>")
@app.route("/math/<operation>")
def do_math(operation):
    return str(ops_dict[operation](float(request.args['a']),
                                   float(request.args['b'])))
