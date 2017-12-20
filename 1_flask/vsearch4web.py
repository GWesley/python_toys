from flask import Flask, render_template, request, escape
app = Flask(__name__)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                            the_title='Welcome to search4letters on the web!',
                            )


@app.route('/search4', methods=["POST"])
def do_search() -> str:
    phrase = request.form['phrase'] 
    letters = request.form['letters']
    result = 'what ever'
    log_request(request, result)
    return render_template('results.html',
                            the_title='Here are your result',
                            the_phrase=phrase,
                            the_letters=letters,
                            the_results='what ever'
                            )

@app.route('/viewlog')
def view_the_log() -> str:
    with open('vsearch.log') as log :
        contents = log.read()
        return escape(contents)

def log_request(req: 'flask_request', res: str) -> None:
    with open('vsearch.log','a') as log:
        print(req, res, file=log)


if __name__ == '__main__':
    app.run(debug=True)