import React, { useState, useEffect, useRouter } from "react";
import "./Page2.css";
import { useNavigate } from "react-router-dom";
import axios from "axios";

export const Page2 = () => {
  const navigate = useNavigate();
  const [image, setImage] = useState(null);

  useEffect(() => {
    // APIから画像データを取得
    const fetchImage = async () => {
      try {
        // Azure Blob Storageから画像を取得
          const response = await axios.get(
           // 今私はここにいる
          
           "https://myblobstorage434606520.blob.core.windows.net/" // 画像のパスを指定 
          );
        

        console.log(response.data);

        // 画像データをステートにセット
        setImage(response.data);
      } catch (error) {
        console.error("Error fetching image: ", error);
      }
    };

    fetchImage();
  }, []);

  const handleRegenerate = () => {
    // 画像を再生成するロジックを実装（必要に応じて）
  };

  const handleGoHome = () => {
    navigate("/");
  };

  return (
    <div>
      <h2>生成した画像</h2>

      {/* 画像を表示 */}
      {image && <img src={image} alt="生成した画像" />}

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
