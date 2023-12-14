import React from "react";
import "./Page1.css";

export const Page1 = () => {
    return (
      <div>
        <h1>ログインページ</h1>

        <h2>ユーザーID</h2>
        <input type="text" placeholder="ユーザーIDを入力してください" />
        <h2>パスワード</h2>
        <input type="text" placeholder="パスワードを入力してください" />
        <button>ログイン</button>
      </div>
    );
  };

