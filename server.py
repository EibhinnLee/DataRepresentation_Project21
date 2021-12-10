from flask import Flask, url_for, request, redirect, abort, jsonify
from werkzeug.exceptions import HTTPVersionNotSupported
from RacingDao import racingDAO

app = Flask(__name__, static_url_path='', static_folder='staticpages')

# testing the server 127.0.0.1:5000
@app.route('/')
def index():
    return "Hope this works!!!!!!"
#get all

# retrieving all in the database
@app.route('/horses')
def getAll():
    return jsonify(racingDAO.getAll())


# find By id
@app.route('/horses/<int:Racenumber>')
def findById(Racenumber):
    return jsonify(racingDAO.findById(Racenumber))

# creating a new row into the database
@app.route('/horses', methods=['POST'])
def create():
   
    if not request.json:
        abort(400)

    horse = {
        "Horse": request.json["Horse"],
        "Jockey": request.json["Jockey"],
        "Trainer": request.json["Trainer"],
        "Age": request.json["Age"]
    }
    return jsonify(racingDAO.create(horse))
    

    return "served by Create "


# update
@app.route('/horses/<int:Racenumber>', methods=['PUT'])
def update(Racenumber):
    foundBook=racingDAO.findById(Racenumber)
    print (foundBook)
    if foundBook == {}:
        return jsonify({}), 404
    currentBook = foundBook
    if 'Horse' in request.json:
        currentBook['Horse'] = request.json['Horse']
    if 'Jockey' in request.json:
        currentBook['Jockey'] = request.json['Jockey']
    if 'Trainer' in request.json:
        currentBook['Trainer'] = request.json['Trainer']
    if 'Age' in request.json:
        currentBook['Age'] = request.json['Age']
    racingDAO.update(currentBook)

    return jsonify(currentBook)

# delete
# curl -X DELETE http://127.0.0.1:5000/horses/1


@app.route('/books/<int:Racenumber>', methods=['DELETE'])
def delete(Racenumber):
    racingDAO.delete(Racenumber)

    return jsonify({"Non-Runner Confirmed": True})


if __name__ == "__main__":
    app.run(debug=True)