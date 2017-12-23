from flask import Flask, render_template, request, escape
import mysql.connector

app = Flask(__name__)
dbconfig = {'host':'127.0.0.1','user':'root','password':'','database':'vsearchlogDB'}
conn = mysql.connector.connect(**dbconfig)

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
    cursor = conn.cursor()
    _SQL = """select * from log"""
    cursor.execute(_SQL)
    contents = cursor.fetchall()
    return render_template('viewlog.html',
                            the_title='View Log',
                            the_row_titles=['FormData','Remote_addr','User_agent','Results'],
                            the_data=contents,
                            )        

def log_request(req: 'flask_request', res: str) -> None:
    cursor = conn.cursor()
    _SQL = """insert into log
              (phrase, letters, ip, browser_string, results)
              values
              (%s,%s,%s,%s,%s)"""
    cursor.execute(_SQL, (req.form['phrase'], request.form['letters'],
                        req.remote_addr, req.user_agent.browser, res,))
    conn.commit()
    cursor.close()                              


if __name__ == '__main__':
    app.run(debug=True)