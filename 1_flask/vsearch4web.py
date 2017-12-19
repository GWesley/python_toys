from flask import Flask, render_template, request, redirect 
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
    return render_template('results.html',
                            the_title='Here are your result',
                            the_phrase=phrase,
                            the_letters=letters,
                            the_result='what ever'
                            )
if __name__ == '__main__':
    app.run(debug=True)