import React, { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import "./Page1.css";

export const Page1 = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      // FormDataオブジェクトを使用してリクエストデータを準備
      const formData = new FormData();
      formData.append('username', username);
      formData.append('password', password);

      // FastAPIサーバーにPOSTリクエストを送信
      const response = await axios.post('http://localhost:8000/token', formData);
      // レスポンスに認証トークンが含まれている場合
      if (response.data && response.data.access_token) {
        // トークンをローカルストレージに保存し、ホームページにリダイレクト
        localStorage.setItem('token', response.data.access_token);
        console.log(response.data)
        navigate("/");
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
