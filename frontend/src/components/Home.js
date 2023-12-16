import "./Home.css";

export const Home = () => {
  return (
    <div>
      <div className="a">
        
        <img src="./images/christmasTree.png" alt="クリスマスツリー" />
      </div>

      <div className='contact-form'>
        <form>
          <p>出来事の内容</p>
          <input />
          
          <p>画像生成の要素</p>
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

  
  