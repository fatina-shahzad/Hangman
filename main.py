from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/hangman_final'
db = SQLAlchemy(app)


class Player_table(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player = db.Column(db.String(50))
    word = db.Column(db.String(50))
    no_of_tries = db.Column(db.Integer)


@app.route('/Guess_word', methods=['POST'])
def player():
    word = Player_table(word=request.form['word'], no_of_tries=request.form['no_of_tries'],
                        player=request.form['player'])
    db.session.add(word)
    db.session.commit()
    return{'word': 'database updated with the guess word'}


@app.route('/play', methods=['Get'])
def play():
    guess_word = Player_table.query.filter(Player_table.word == Player_table.word).first()
    no_guess_tries = Player_table.query.filter(Player_table.no_of_tries == Player_table.no_of_tries).first()
    word_guess = guess_word.word
    print(word_guess)
    length_word = len(word_guess)
    print(length_word)
    tries = no_guess_tries.no_of_tries
    print(tries)
    letters_guessed = ""
    while tries > 0:
        guess_char = input("enter the guess")
        if guess_char in word_guess:
            print(f"you guessed{guess_char}right! ")
        else:
            tries -= 1
            print("Wrong! no of tries left", tries)

        letters_guessed = letters_guessed + guess_char
        wrong_guess = 0
        print(wrong_guess, "shy!!")
        for letters in word_guess:
            if letters in letters_guessed:
                print(f"{letters}", end="")

            else:
                print("_", end="")
                wrong_guess += 1

        if wrong_guess == 0:
            print('congo, you won')
            break

    else:
        print('you loose')

    return {'message': 'its working'}



@app.route('/')
def index():
    return 'hey'


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
