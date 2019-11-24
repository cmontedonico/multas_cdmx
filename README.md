# Multas CDMX
# Flask / Python3 

This project is a WebScrapping for CDMX Violations

## Getting Started

git clone git@github.com:cmontedonico/multas_cdmx.git


### PREREQ
Use a machine with Python3 Installed

### Installing

Create the VirtualEnv and install dependencies
```
$ python3 -m venv venv
$ . venv/bin/activate
$ pip3 install -r requirements.txt
```


### CONFIG
Change the file vehiculos.csv for your own fleet information

### RUN 
Run the project
```
$ python3 placas.py
```
this should start the server on
http://0.0.0.0:8080

Open The browser to 
http://0.0.0.0:8080/cdmx

### RESPONSE 
Json with this structure

````
{
    "plate": [
      "798RJ2"
    ], 
    "violations": [
      {
        "date": "2018-09-18", 
        "description": "LOS CONDUCTORES Y OCUPANTES DE LOS VEH\u00d6CULOS DEBEN DE CUMPLIR CON LAS DISPOSICIONES DE SEGURIDAD INDICADAS EN EL PRESENTE ART\u00d6CULO DE ACUERDO A LA NATURALEZA PROPIA DE CADA VEH\u00d6CULO. LOS CONDUCTORES DE VEH\u00d6CULOS MOTORIZADOS DEBEN: ENCENDER LAS LUCES CUANDO DISMINUYA SENSIBLEMENTE LA VISIBILIDAD POR CUALQUIER FACTOR AMBIENTAL O POR LAS CARACTER\u00d6STICAS DE LA INFRAESTRUCTURA VIAL, EVITANDO DESLUMBRAR A QUIENES TRANSITAN EN SENTIDO OPUESTO; Y", 
        "folio": "04185812014", 
        "status": "No pagada"
      }, 
      {
        "date": "2017-10-06", 
        "description": "QUEDA PROHIBIDO A LOS CONDUCTORES DE VEH\u00d6CULOS DE TRANSPORTE DE CARGA: CIRCULAR POR CARRILES CENTRALES Y SEGUNDOS NIVELES DE LAS V\u00d6AS DE ACCESO CONTROLADO CUANDO SE TRATE DE VEH\u00d6CULOS DE PESO BRUTO VEHICULAR DE DISE\u00a5O SUPERIOR A 3,857 KG O DONDE EL SE\u00a5ALAMIENTO RESTRICTIVO AS\u00d6 LO INDIQUE, Y", 
        "folio": "04175916654", 
        "status": "Pagada"
      }, 
      {
        "date": "2015-06-29", 
        "description": "POR CIRCULAR EN CARRILES DE CONTRAFLUJO Y CARRILES CONFINADOS", 
        "folio": "04153352306", 
        "status": "No pagada"
      }
    ]
  }, 
````


## Built With

* [Flask](http://flask.pocoo.org/)
* [Pandas]
* [BS4]

## Authors
* **Alejandro Hernandez** - *Initial work* 
* **Cesare Montedonico** - *Initial work* - [Twitter](https://www.twitter.com/cmontedonico)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
