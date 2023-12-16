import React from "react";
import { BrowserRouter, Link, Routes, Route } from "react-router-dom";
import "./App.css";

import { Home } from "./components/Home";
import { Page1 } from "./components/Page1";
import { Page2 } from "./components/Page2";

function App() {
  return (
    <BrowserRouter>
      <div className="App">
        <header>
          <h1>クリスマスツリーをつくろう！</h1>
        </header>

        
        
        <div className="link">
          <Link to="/">Home</Link>
          <br />
          <Link to="/page1">ログインページ</Link>
          <br />
          <Link to="/page2">絵を選ぶページ</Link>
          <br />
          <p>ユーザーID: 1</p>
        </div>

        

        

        <div className="content">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/page1" element={<Page1 />} />
            <Route path="/page2" element={<Page2 />} />
          </Routes>
        </div>

        
      </div>
    </BrowserRouter>
  );
}

export default App;

