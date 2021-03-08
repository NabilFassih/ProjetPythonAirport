from flask import Flask, render_template, request, redirect, url_for, session, jsonify, send_file
import folium
from helpers import dataAirports, lowAndTopDestination, nbDestinationsByCompagnie, getAllAirports, getAllFightsByMonth, getAirlinesDepDelay, getAirlinesArrDelay

app = Flask(__name__)
app.run(debug=True)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

@app.route('/', methods=['POST', 'GET'])
def home():
    nbAeroports, nbCompagnies, nbDestinations, nbAvions, nbFuseauxHoraires, nbZone = dataAirports()
    topAeroportDepart, topDestination, lowDestination = lowAndTopDestination()
    nbDestinationsByComp = nbDestinationsByCompagnie()
    flightsByMonth = getAllFightsByMonth()
    airlinesDepDelay = getAirlinesDepDelay()
    airlinesArrDelay = getAirlinesArrDelay()
    
    return render_template('index.html', nbAeroports=nbAeroports, nbCompagnies=nbCompagnies, nbDestinations=nbDestinations, nbAvions=nbAvions, nbFuseauxHoraires=nbFuseauxHoraires, nbZone=nbZone, nbDestinationsByComp=nbDestinationsByComp, topAeroportDepart=topAeroportDepart, topDestination=topDestination, lowDestination=lowDestination, flightsByMonth=flightsByMonth, airlinesDepDelay=airlinesDepDelay, airlinesArrDelay=airlinesArrDelay)


@app.route('/folium')
def map():
    airports = getAllAirports()
    start_coords = (41.045867, -102.081191)
    folium_map = folium.Map(location=start_coords, zoom_start=5)

    for airport in airports:
        folium.Marker([airport['lat'], airport['lon']], popup='<i>'+airport['name']+'</i>').add_to(folium_map)

    folium_map.save('templates/map.html')
    return send_file('templates/map.html')
