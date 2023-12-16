import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import "./Page1.css";

export const Page1 = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const handleSubmit = (event) => {
    event.preventDefault();
    // ここにハードコーディングされたユーザー名とパスワードを設定
    const correctUsername = "user123"; 
    const correctPassword = "password123";

    if (username === correctUsername && password === correctPassword) {
      navigate("/App"); // 正しい場合、Homeページにリダイレクト
    } else {
      alert("名前かパスワードが間違えています"); // 間違いがある場合、警告を表示
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
          type="password" // パスワード入力のためのタイプを設定
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
