from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from flask_jwt import JWT, jwt_required
from security import authenticate, identity
import datetime

app = Flask(__name__)
app.secret_key = 'test'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=1)

jwt = JWT(app, authenticate, identity)

@app.route('/')
@cross_origin()
@jwt_required()
def hello_world():
    return jsonify('Hello World!')

if __name__ == '__main__':
    app.debug = True
    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'
    app.run()