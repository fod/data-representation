from flask import Flask, render_template, send_file


app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('APP_CONFIG_FILE', silent=True)
MAPBOX_ACCESS_KEY = app.config['MAPBOX_ACCESS_KEY']

if __name__== '__main__':
    app.run(debug=True)

@app.route('/mapbox_js')
def mapbox_js():
    return render_template(
        'mapbox_js.html', 
        ACCESS_KEY=MAPBOX_ACCESS_KEY,
        MAP_LONGITUDE=app.config['MAP_LONGITUDE'],
        MAP_LATITUDE=app.config['MAP_LATITUDE'],
        MAP_ZOOM=app.config['MAP_ZOOM'],
    )

@app.route('/eds')
def get_eds():
    return send_file('static/electoral_divisions.geojson')
   