from flask import Flask, jsonify, request

app = Flask(__name__)
hearts = [
    {
        "heart_id" : 1,
        "date" : "1/2/2022",
        "heart_rate" : "135"
    },
    {
        "heart_id" : 2,
        "date" : "8/2/2022",
        "heart_rate" : "126"
    }
]
@app.route ('/hearts', methods=['GET'])
def heartInfo():
    return jsonify(hearts)

@app.route('/hearts', methods=['POST'])
def addHeartInfo():
    heart = request.get_json()
    hearts.append(heart)
    return {'id': len(hearts)},200

@app.route('/hearts/<int:index>', methods=['DELETE'])
def deleteHeartInfo(index):
    hearts.pop(index)
    return 'Heart information was successfully deleted', 200

if __name__ == '__main__':
    app.run()