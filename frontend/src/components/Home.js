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
      <div class="container">
        <div class="item1">
          <img src="./images/item1.png" alt="絵1" />
        </div>
        <div class="item2">
          <img src="./images/item2.png" alt="絵2" />
        </div>
        <div class="item3">
          <img src="./images/item3.png" alt="絵3" />
        </div>
        <div class="item4">
          <img src="./images/item4.png" alt="絵4" />
        </div>
        <div class="item5">
          <img src="./images/item5.png" alt="絵5" />
        </div>
        <div class="item6">
          <img src="./images/item6.png" alt="絵6" />
        </div>
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
