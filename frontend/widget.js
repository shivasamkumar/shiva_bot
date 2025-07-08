;(function(){
  // ← 1. your Heroku-hosted chat
  const CHAT_URL = 'https://shiva-bot-7b7a47a4404f.herokuapp.com/';

  // ← 2. inject widget-only CSS, scoped by ID so it never touches the rest of your site
  const css = `
    #shiva-chat-btn {
      position: fixed;
      bottom: 24px;
      right: 34px;
      width: 56px;
      height: 56px;
      background: #007bff url('/static/icons8-chat-64.png') no-repeat center/60% auto;
      border-radius: 50%;
      box-shadow: 0 4px 12px rgba(0,0,0,0.2);
      cursor: pointer;
      z-index: 9999;
      transition: transform 0.2s ease, background-color 0.2s ease;
    }
    #shiva-chat-btn.open {
      transform: rotate(45deg);
      background-color: #0056b3;
    }
    #shiva-chat-container {
      position: fixed;
      bottom: 100px;
      right: 24px;
      width: 360px;
      height: 500px;
      display: none;
      box-shadow: 0 8px 24px rgba(0,0,0,0.2);
      border-radius: 8px;
      overflow: hidden;
      z-index: 9998;
      background: #fff;
    }
    #shiva-chat-container.open {
      display: block;
    }
    #shiva-chat-container iframe {
      width: 100%;
      height: 100%;
      border: none;
    }
  `;
  const style = document.createElement('style');
  style.textContent = css;
  document.head.appendChild(style);

  // ← 3. then the original “toggle” logic
  const btn = document.createElement('div');
  btn.id = 'shiva-chat-btn';
  btn.title = 'Chat with Shiva';
  document.body.appendChild(btn);

  const container = document.createElement('div');
  container.id = 'shiva-chat-container';
  container.innerHTML = `<iframe src="${CHAT_URL}" frameborder="0"></iframe>`;
  document.body.appendChild(container);

  btn.addEventListener('click', () => {
    btn.classList.toggle('open');
    container.classList.toggle('open');
  });
})();