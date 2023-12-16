import React from "react";
import "./Home.css";
import { useNavigate } from "react-router-dom";

export const Home = () => {
  const navigate = useNavigate();

  const toPage2 = (event) => {
    event.preventDefault(); 
    navigate("/React");     
  };

  return (
    <div>
      <div className="a">
        <img src="./images/christmasTree.png" alt="クリスマスツリー" />
      </div>

      <div className='contact-form'>
        <form onSubmit={toPage2}>
          <p>出来事の内容</p>
          <input />
          
          <p>画像生成のPrompt</p>
          <textarea />
          
          <br />
          <input className="submit-btn"
            type='submit'
            value='送信'
          />
        </form>
      </div>
    </div>
  );
};
