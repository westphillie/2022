import logo from './logo.svg';
import React from 'react';
import { useState, useEffect, setState } from "react";
import './App.css';
import { Marker, Popup, MapContainer, TileLayer, useMap } from 'react-leaflet'
import 'leaflet/dist/leaflet.css';
import L from 'leaflet';

delete L.Icon.Default.prototype._getIconUrl;

L.Icon.Default.mergeOptions({
    iconRetinaUrl: require('leaflet/dist/images/marker-icon-2x.png'),
    iconUrl: require('leaflet/dist/images/marker-icon.png'),
    shadowUrl: require('leaflet/dist/images/marker-shadow.png')
});

function Player(props) {
  return (
    <Marker position={props.locations}>
          <Popup>
            <span>{props.obj[5]}</span>
          </Popup>
    </Marker>
  );
}

function PlayerMarkers(props) {
  return (
    <div>
      {props.players.map(function(object, i){
        return <Player obj={object} locations={props.locations[i]} key={i} />;
      })}
    </div>
  );
}

function App(props) {
    return (

      <div>
      <MapContainer center={[38.000, -98.000]} zoom={4}>
      
        <TileLayer
          attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
          url='http://{s}.tile.osm.org/{z}/{x}/{y}.png'
        />
        
        <PlayerMarkers players={props.prospects} locations={props.locations}/>
      </MapContainer>
      </div>

    );
};


export default App;
