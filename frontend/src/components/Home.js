import React, { useState, useEffect } from "react";
import "./Home.css";
import { useNavigate } from "react-router-dom";
import axios from "axios";


export const Home = () => {
  const navigate = useNavigate();
  const [images, setImages] = useState([]); // 画像を管理
  const [prompt, setPrompt] = useState(""); // 画像生成のプロンプトを管理

  useEffect(() => {
    // APIから画像データを取得
    const fetchImages = async () => {
      try {
        const response = await axios.get("https://myblobstorage434606520.blob.core.windows.net/"); // Azure APIのURLを指定
        setImages(response.data); // 画像データをステートにセット
      } catch (error) {
        console.error("Error fetching images: ", error);
      }
    };

    fetchImages();
  }, []); // コンポーネントがマウントされた時に1度だけ実行

  
  const toPage2 = async (event) => {
    event.preventDefault();
    
    try {
      await axios.post("http://localhost:8000/prompt", {promptTextTemp:prompt});
      navigate("/Page2");
    } catch (error) {
      console.error("Error generating image: ", error);
      if (error.response) {
        // サーバーからの応答をログに出力
        console.error("Server response: ", error.response.data);
      }
    }
  };
  

  return (
    <div>
      <div className="container">
        {images.map((image, index) => (
          <div className={`item${index + 1}`} key={index}>
            <img src={image.url} alt={`絵${index + 1}`} />
          </div>
        ))}
      </div>

      <div className="contact-form">
        <form onSubmit={toPage2}>
          <p>画像生成のPrompt</p>
          <input 
            value={prompt} onChange={(e) => setPrompt(e.target.value)} 
          />

          <br />
          <input className="submit-btn" type="submit" value="送信" />
        </form>
      </div>
    </div>
  );
};

