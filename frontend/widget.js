;(function(){
  const CHAT_URL = 'https://shiva-bot-7b7a47a4404f.herokuapp.com/';

  // 1) inject widget-only CSS
  const css = `
    /* pulse keyframes */
    @keyframes shiva-flash {
      0%, 100% { transform: scale(1); box-shadow: 0 4px 12px rgba(0,0,0,0.2); }
      50%      { transform: scale(1.2); box-shadow: 0 0 20px rgba(0,123,255,0.8); }
    }

    /* chat label */
    #shiva-chat-label {
      position: fixed;
      bottom: 140px;             /* sits just above the button */
      right: 50px;
      background:rgb(44, 49, 102);
      color: #fff;
      padding: 6px 12px;
      border-radius: 4px;
      font-size: 1.5rem;
      box-shadow: 0 4px 12px rgba(0,0,0,0.2);
      z-index: 9999;
      white-space: nowrap;
      animation: shiva-flash 1s ease-in-out 5;
      pointer-events: none;      /* clicks fall through to the button */
    }
    /* hide once opened */
    #shiva-chat-label.hidden {
      display: none;
    }

    /* chat button */
    #shiva-chat-btn {
      position: fixed;
      bottom: 64px;
      right: 50px;
      width: 66px;
      height: 66px;
      background: #007bff url('https://shiva-bot-7b7a47a4404f.herokuapp.com/static/icons8-chat-64.png') no-repeat center/60% auto;
      border-radius: 50%;
      box-shadow: 0 4px 12px rgba(0,0,0,0.2);
      cursor: pointer;
      z-index: 9999;
      transition: background-color 0.2s ease;
      animation: shiva-flash 1s ease-in-out 5;
    }
    #shiva-chat-btn.open {
      background-color: #0056b3;
    }

    /* chat container */
    #shiva-chat-container {
      position: fixed;
      bottom: 100px;
      right: 24px;
      width: 400px;
      height: 550px;
      display: none;
      box-shadow: 0 8px 24px rgba(0,0,0,0.2);
      border-radius: 8px;
      overflow: hidden;
      z-index: 9998;
      background: #fff;
    }
    #shiva-chat-container.open {
      display: block;
      animation: none !important;
    }
    #shiva-chat-container iframe {
      width: 100%;
      height: 100%;
      border: none;
    }

    /* expand button */
    #shiva-chat-expand {
      position: absolute;
      top: 8px;
      right: 8px;
      width: 24px;
      height: 24px;
      background: url('https://shiva-bot-7b7a47a4404f.herokuapp.com/static/icons8-expand-30.png') no-repeat center/contain;
      cursor: pointer;
      z-index: 10000;
    }
  `;
  const style = document.createElement('style');
  style.textContent = css;
  document.head.appendChild(style);

  // 2) create chat label, button & container
  const label = document.createElement('div');
  label.id = 'shiva-chat-label';
  label.textContent = 'Chat with me';
  document.body.appendChild(label);

  const btn = document.createElement('div');
  btn.id = 'shiva-chat-btn';
  document.body.appendChild(btn);

  const container = document.createElement('div');
  container.id = 'shiva-chat-container';
  container.innerHTML = `
    <div id="shiva-chat-expand" title="Open full chat"></div>
    <iframe src="${CHAT_URL}" frameborder="0"></iframe>
  `;
  document.body.appendChild(container);

  // 3) toggle open/close on click, hide label
  btn.addEventListener('click', () => {
    const isOpen = btn.classList.toggle('open');
    container.classList.toggle('open');
    label.classList.toggle('hidden', isOpen);
  });

  // 4) expand to full screen
  container
    .querySelector('#shiva-chat-expand')
    .addEventListener('click', e => {
      e.stopPropagation();
      window.open(CHAT_URL, '_blank');
    });
})();
