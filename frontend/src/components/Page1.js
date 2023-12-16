import React, { useState } from "react";
import axios from "axios"; // Import axios for API calls
import { useNavigate } from "react-router-dom";
import "./Page1.css";

export const Page1 = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      // Replace 'http://localhost:8000' with your FastAPI server URL
      const response = await axios.post('http://localhost:8000/token', {
        username: username,
        password: password,
      });

      // Assuming the response includes an authentication token
      if (response.data && response.data.access_token) {
        // You might want to store the token in local storage or context for further requests
        localStorage.setItem('token', response.data.access_token);
        navigate("/"); // Navigate to the home page on successful login
      }
    } catch (error) {
      if (error.response && error.response.status === 400) {
        alert("名前かパスワードが間違えています");
      } else {
        alert("エラーが発生しました");
      }
    }
  };

  return (
    <div className="Page1">
      <h1>ログインページ</h1>
      <form onSubmit={handleSubmit}>
        <p>名前</p>
        <input 
          type="text"
          placeholder="ユーザーIDを入力してください"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
        <p>パスワード</p>
        <input 
          type="password"
          placeholder="パスワードを入力してください"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <br />
        <input className="submit-btn" type="submit" value="ログイン" />
      </form>
    </div>
  );
};
