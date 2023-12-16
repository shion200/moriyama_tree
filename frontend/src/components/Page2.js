import React from "react";
import "./Page2.css";

export const Page2 = () => {
  // 再生成を処理する関数（必要に応じて更新）
  const handleRegenerate = () => {
    // 画像を再生成するロジック
  };

  return (
    <div>
      <h2>生成した画像</h2>

      <img src="./images/a_man_drinking_beer.png" alt="絵1" />
      
      <br />

      <div className="button008">
        <button onClick={()=>{handleRegenerate()}}>再生成</button>
      </div>
    </div>
  );
};
