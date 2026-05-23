import { useState } from "react";
import { FiUploadCloud } from "react-icons/fi";
import { BsStars } from "react-icons/bs";

function Upload() {

    const [image, setImage] = useState(null);

    const [imageFile, setImageFile] = useState(null);

    const [result, setResult] = useState(null);


    const handleImage = (e) => {

        const file = e.target.files[0];

        if(file){

            setImage(URL.createObjectURL(file));

            setImageFile(file);
        }
    };


    const handleAnalyze = async () => {

        console.log("Analyze clicked");

        if(!imageFile){

            alert("Please upload image");

            return;
        }

        const formData = new FormData();

        formData.append("image", imageFile);


        const response = await fetch(

            "http://127.0.0.1:5000/predict",

            {
                method:"POST",
                body:formData
            }
        );

        const data = await response.json();

        console.log(data);

        setResult(data);
    };


    return (

        <div className="container">

            <div className="background-grid"></div>

            <div className="card">

                <div className="badge">

                    <BsStars />

                    <span>AI READY</span>

                </div>

                <h1 className="title">
                    AgroMind AI
                </h1>

                <p className="subtitle">
                    AI-powered crop disease detection,
                    weather forecasting and intelligent
                    risk prediction for smart farming.
                </p>

                <label className="upload-area">

                    <input
                        type="file"
                        hidden
                        accept="image/*"
                        onChange={handleImage}
                    />

                    <div className="upload-content">

                        <FiUploadCloud className="upload-icon" />

                        <h3>
                            Upload Leaf Image
                        </h3>

                        <p>
                            JPG, PNG supported
                        </p>

                    </div>

                </label>

                {image && (

                    <img
                        src={image}
                        alt="preview"
                        className="preview-image"
                    />
                )}

                <button
                    className="analyze-btn"
                    onClick={handleAnalyze}
                >

                    Analyze Crop

                </button>


                {result && (

                    <div className="result-card">

                        <h2>
                            Disease: {result.disease}
                        </h2>

                        <p>
                            Confidence: {result.confidence}%
                        </p>

                        <p>
                            Temperature: {result.temperature}°C
                        </p>

                        <p>
                            Rainfall: {result.rainfall}
                        </p>

                        <p>
                            Wind: {result.wind}
                        </p>

                        <p>
                            Risk: {result.risk}
                        </p>

                        <p>
                            {result.message}
                        </p>

                    </div>
                )}

            </div>

        </div>
    );
}

export default Upload;