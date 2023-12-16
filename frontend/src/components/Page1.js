import React from "react";
import "./Page1.css";

export const Page1 = () => {
    return (
      <div>
        <h1>ログインページ</h1>

        <p>名前</p>
        <input type="text" placeholder="ユーザーIDを入力してください" />
        <p>パスワード</p>
        <input type="text" placeholder="パスワードを入力してください" />
        <br />
        <input className="submit-btn"
            type='submit'
            value='ログイン'
          />
      </div>
    );
  };

