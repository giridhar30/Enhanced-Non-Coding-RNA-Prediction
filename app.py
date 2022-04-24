from flask import Flask, request
from prediction import predict_family
app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def rna():
    if request.method == 'POST':
        data = request.json
        if not data:
            return {'error': 'data not found'}
        if 'rna' not in data:
            return {'error': 'RNA sequence not found'}
        rna = data['rna']
        if not rna:
                return {'error': 'empty sequence not allowed'}
        return {'family': predict_family(rna)}

if __name__ == '__main__':
    app.run(debug = True)
