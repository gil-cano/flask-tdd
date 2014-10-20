from flask import flash
from flask import Flask
from flask import render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from wtforms import SubmitField
from wtforms import TextAreaField


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)


@app.route("/", methods=['GET', 'POST'])
def index():
    form = WordForm()
    if form.validate_on_submit():
        text = form.text.data
        characters = len(text)
        words = len(text.split())
        message = '%s palabras %s caracteres' % (words, characters)
        flash(message)
        form.text.data = ''
    return render_template('words.html', form=form)


class WordForm(Form):
    text = TextAreaField('')
    submit = SubmitField('Contar')


if __name__ == "__main__":
    app.run(debug=True)
