import flask


app = flask.Flask(__name__)


@app.route('/')
def root():
    return 'front page'

@app.route('/<person>')
def pindex(person):
    # call function to get results to be shared with API
    # format into html
    return 'index'

@app.route('/<person>/<quote_number>')
def quote(person, num):
    # call function to get results
    # format into html
    return 'quote'
