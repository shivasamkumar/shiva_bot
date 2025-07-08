# Personal Assistant

A Retrieval-Augmented Generation (RAG) powered personal Assistant , which answer's anything about background, experience, education and projects. Combines OpenAI's LLM with a Chroma vector store to retrieve and generate accurate answers from your knowledge base.

**Website Live Demo:** https://shivasamkumar.github.io/
**Chatbot Live Demo:** https://shiva-bot-7b7a47a4404f.herokuapp.com/

- **Streaming Responses**  
 RealbySent Events (SSE).
- **Embeddable Widget**  
 Flashing chat icon widget for easy embedding into any website.
- **Local & Cloud-Ready**  
 Configurable for local development or deployment (Heroku, Docker, etc.).

## Getting Started

### Prerequisites
- Python 3.8+  
- `git`  
- An OpenAI API key

### Installation and Usage

1. **Clone the repo**  
  ```bash
  git clone https://github.com/shivasamkumar/shiva_bot.git
  cd shiva_bot
  ```

2. **Create a virtual environment & install dependencies**
  ```bash
  python -m venv .venv
  source .venv/bin/activate   # on Windows: .venv\Scripts\activate
  pip install --upgrade pip
  pip install -r requirements.txt
  ```

3. **Configure environment variables**  
  Create a `.env` in the `api/` folder (or set in your environment):
  ```
  OPENAI_API_KEY=your_openai_api_key
  VECTORDB_PATH=vector_db
  KB_ROOT=knowledge_base
  ```

4. **Ingest your knowledge base**
  ```bash
  cd api
  % Create your own knowledge base
  python ingest.py
  cd ..
  ```

5. **Run the API locally**
  ```bash
  uvicorn api.app:app --reload --host 0.0.0.0 --port 8000
  ```

6. **Embed the widget**
  - Copy `widget.js` and `widget.css` into your frontend.
  - Add the snippet to your site's HTML just before `</body>`:
    ```html
    <link rel="stylesheet" href="widget.css">
    <script src="widget.js"></script>
    ```

## Deployment

Chatbot can be deployed on Heroku, AWS Elastic Beanstalk, DigitalOcean App Platform, or any container service:

```bash
heroku create bot
git push heroku main
heroku config:set OPENAI_API_KEY=your_key VECTORDB_PATH=vector_db KB_ROOT=knowledge_base
```

## Usage

1. Click the chat icon on your page to launch the bot widget.
2. Ask Shiva about his education, experience, projects, or future plans.
3. Optionally click "Expand" to open the full-screen chat in a new tab.

## Future Development

- **AI Agents**: Automate email drafting, job applications, and scheduling.
- **Multimodal Inputs**: Support image and document uploads.
- **User Profiles**: Personalized conversation flows.
- **Analytics Dashboard**: Track frequently asked questions and improve the knowledge base.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m "Add SomeFeature"`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

Please follow the existing code style and include tests where applicable.

## License

This project is licensed under the MIT License. See [LICENSE](License.md) for details.