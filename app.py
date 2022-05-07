from flask import Flask, request, render_template
from prediction import predict_family
from flask_cors import cross_origin

app = Flask(__name__, template_folder='UI')

@app.route('/', methods = ['GET'])
def index():
   return render_template('index.html')

@app.route('/', methods = ['POST'])
@cross_origin()
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
