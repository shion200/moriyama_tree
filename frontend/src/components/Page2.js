import React from "react";
import "./Page2.css";
import { useNavigate } from "react-router-dom"; // Import useNavigate

export const Page2 = () => {
  const navigate = useNavigate(); // Initialize the navigate function

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

      <img src="./images/a_man_drinking_beer.png" alt="絵1" />
      
      <br />

      <div className="button1">
        <button onClick={handleGoHome}>これにする！</button> {/* Updated this line */}
      </div>
      
      <form onSubmit={handleRegenerate}>
        <p>出来事の内容</p>
        <input />
          
        <p>画像生成のPrompt</p>
        <textarea />
      
        <br />
        <input className="submit-btn"
          type="submit" 
          value="再生成" 
        />
      </form>
    </div>
  );
};
