from flask import Flask, jsonify
from bs4 import BeautifulSoup
import requests
import pandas as pd

app = Flask(__name__)
URL = 'https://data.finanzas.cdmx.gob.mx/sma/Consultaciudadana/'

@app.route('/')
def hello_world():
    return jsonify({"Everything is Awesome": "Everything is cool when you are part of a team"})

@app.route('/cdmx')
def searchCDMX():
    plates = pd.read_csv("vehiculos.csv").values.tolist()
    
    req = requests.get(URL)
    statusCode = req.status_code

    info = []
    
    if statusCode == 200:
        html = BeautifulSoup(req.text, "html.parser")
        form = html.find('form', attrs={'method': 'POST'})
        postUrl = form['action']
        for plate in plates:
            data = {'placa': plate, 'envia': 'Consulta'}
            res = requests.post(postUrl, data)
            _plate = {'plate': plate, 'violations': []}

            if res.status_code == 200:
                html2 = BeautifulSoup(res.text, "html.parser")
                tables = html2.find_all('table', attrs={'id': 'tablaDatos'})
                if len(tables) > 1:
                    for table in tables:
                        rows = table.find_all('tr')
                        general = rows[1].find_all('td')
                        folio = general[0].getText()
                        date = general[1].getText()
                        status = general[2].find('span').getText().strip()
                        description = rows[2].find('font').getText()
                        _plate['violations'].append({
                            'folio': folio,
                            'date': date,
                            'status': status,
                            'description': description
                        })
                else:
                    pass
            print(_plate)
            info.append(_plate)

    return jsonify(info)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)

