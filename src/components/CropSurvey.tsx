import React from "react"
import "./cropSurveyStyle.css"

const cropSurvey = () => {


    return (
    <body>
    <h1>Select a Crop:</h1>
    <form method="POST" action="/">
        <label htmlFor="crop">Choose a crop:</label>
        <select id="crop" name="crop">
            <option value="rice">Rice</option>
            <option value="maize">Maize</option>
            <option value="chickpea">Chickpea</option>
            <option value="kidneybeans">Kidney Beans</option>
            <option value="pigeonpeas">Pigeon Peas</option>
            <option value="mothbeans">Moth Beans</option>
            <option value="mungbean">Mung Bean</option>
            <option value="blackgram">Black Gram</option>
            <option value="lentil">Lentil</option>
            <option value="pomegranate">Pomegranate</option>
            <option value="banana">Banana</option>
            <option value="mango">Mango</option>
            <option value="grapes">Grapes</option>
            <option value="watermelon">Watermelon</option>
            <option value="muskmelon">Muskmelon</option>
            <option value="apple">Apple</option>
            <option value="orange">Orange</option>
            <option value="papaya">Papaya</option>
            <option value="coconut">Coconut</option>
            <option value="cotton">Cotton</option>
            <option value="jute">Jute</option>
            <option value="coffee">Coffee</option>
        </select>
        <div className="submit-button">
            <input type="submit" value="Submit" />
        </div>
    </form>
</body>
    )
}

export default cropSurvey;