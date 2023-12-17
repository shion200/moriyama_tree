import React, { useState, useEffect } from "react";
import "./Page2.css";
import { useNavigate } from "react-router-dom";
import axios from "axios";


export const Page2 = () => {
  const navigate = useNavigate();
  const [image, setImage] = useState(null); // ステートで受け取った画像を管理

  useEffect(() => {
    // APIから画像データを取得
    const fetchImage = async () => {
      try {
        const response = await axios.get("http://localhost8000/token"); // APIのURLを指定
        setImage(response.data); // 画像データをステートにセット
      } catch (error) {
        console.error("Error fetching image: ", error);
      }
    };

    fetchImage();
  }, []); // コンポーネントがマウントされた時に1度だけ実行

  // 再生成を処理する関数（必要に応じて更新）
  const handleRegenerate = () => {
    // 画像を再生成するロジック
  };

  // Navigate to home page
  const handleGoHome = () => {
    navigate("/"); // Navigate to the home page
  };

  return (
    <div>
      <h2>生成した画像</h2>

      {image && <img src={image.url} alt="生成した画像" />}

      <br />

      <div className="button1">
        <button onClick={handleGoHome}>これにする！</button>
      </div>

      <form onSubmit={handleRegenerate}>
        

        <p>画像生成のPrompt</p>
        <textarea />

        <br />
        <input className="submit-btn" type="submit" value="再生成" />
      </form>
    </div>
  );
};
