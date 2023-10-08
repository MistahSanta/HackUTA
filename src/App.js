import React from 'react';
import logo from './logo.svg'; // Make sure to import your logo file if you have one
import Text from './components/Text.tsx';
import CropSurvey from './components/CropSurvey.tsx';


function App() {
  return (
    <div className="App">
      <CropSurvey />
      <Text />
    </div>
  );
}

export default App;