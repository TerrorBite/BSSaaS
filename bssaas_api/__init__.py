import flask


app = flask.Flask(__name__)


@app.route('/')
def root():
    return flask.redirect('/')

@app.route('/<person>')
def pindex(person):
    # call function to get results to be shared with HTML thingo
    return flask.jsonify({'stuff': 'index'})

@app.route('/<person>/<quote_number>')
def quote(person, num):
    # call function to get results
    return flask.jsonify({'stuff': 'quote'})
