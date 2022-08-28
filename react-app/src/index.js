import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

const root = ReactDOM.createRoot(document.getElementById('root'));

// function player() {
//   return fetch('http://127.0.0.1:5000').then(res => res.json());
// }

// function coords() {
//   return fetch('http://127.0.0.1:5000/coords').then(res=>res.json());
// }

Promise.all([
  fetch("http://127.0.0.1:5000").then(data=>data.json()),
  fetch("http://127.0.0.1:5000/coords").then(data=>data.json())
]).then(([playerdata, coordsdata]) => {
  root.render(
    <React.StrictMode>
      <App prospects={playerdata} locations={coordsdata['locations']}/>
    </React.StrictMode>
  );
}).catch((err) => {
    console.log(err);
});

// var player_data = player();
// var coords_data = coords();

// home(player_data, coords_data['locations']);

// function home(array, coords) {
//   root.render(
//     <React.StrictMode>
//       <App prospects={array} locations={coords}/>
//     </React.StrictMode>
//   );
// }

reportWebVitals();
