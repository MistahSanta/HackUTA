
import React, { useEffect } from 'react';
import { Streamlit, withStreamlitConnection } from 'streamlit-component-lib';

const Text = () => {

  useEffect( () => Streamlit.setFrameHeight() );

  return (
    <>
      <h2>Hello BOBBBOBOB!</h2>
      <p>Nice to meet you!!</p>
    </>
  )
}

export default withStreamlitConnection(Text);