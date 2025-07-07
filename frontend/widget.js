// frontend/widget.js
;(function(){
  const CHAT_URL = 'https://shiva-bot-7b7a47a4404f.herokuapp.com/';  // ← your Heroku URL

  // 1) toggle button
  const btn = document.createElement('div');
  btn.id = 'shiva-chat-btn';
  btn.title = 'Chat with Shiva';
  document.body.appendChild(btn);

  // 2) hidden container + iframe
  const container = document.createElement('div');
  container.id = 'shiva-chat-container';
  container.innerHTML = `<iframe src="${CHAT_URL}" frameborder="0"></iframe>`;
  document.body.appendChild(container);

  // 3) click handler
  btn.addEventListener('click', ()=> {
    btn.classList.toggle('open');
    container.classList.toggle('open');
  });
})();
