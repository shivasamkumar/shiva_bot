# Multimodal Plant Disease QA & Detection Pipeline

## Introduction
The Multimodal Plant Disease QA & Detection Pipeline is an end-to-end, retrieval-augmented Gradio application that fuses web-scraped knowledge and computer-vision to deliver interactive plant disease diagnosis. It begins by using the Google Search API in a helper notebook to scrape and preprocess a corpus of plant-disease articles, which are then chunked, embedded via OpenAI’s embedding API, and stored in a ChromaDB vector store. In parallel, a custom YOLO model is trained to detect and crop diseased regions from uploaded leaf images. Both the vector-based retrieval QA and the vision-based detector are wrapped as LangChain tools and orchestrated by an LLM agent, enabling users to upload a leaf photo, immediately see the highlighted disease area, and ask follow-up questions—powered by GPT API calls and tool-invocation logic. 

## Features
- **Automated Web Scraping** of plant-disease articles via Google Search API to build a raw text knowledge base.  
- **Preprocessing & Visualization** of scraped documents for cleaning, inspection, and exploratory analysis.  
- **Embeddings & Vector Store**: Text chunking, OpenAI embedding generation, and persistence in ChromaDB for fast, semantic retrieval.  
- **Custom YOLO Model**: Loadable `best.pt` weights to detect and crop disease-affected regions in leaf images.  
- **LangChain Tools**: Wrappers for both detection and retrieval-QA pipelines, enabling the LLM agent to invoke vision and text tools seamlessly.  
- **Interactive Gradio App**: A user-friendly web interface to upload images, view disease detections, and engage in natural-language QA about symptoms, causes, and treatments. 

## Challenges Faced
- **Data Collection & Quality**  
  Ensuring comprehensive coverage and consistency in scraped articles, handling rate limits, and cleaning heterogeneous HTML/text content.  
- **Vector-Store Scalability**  
  Chunking long documents while maintaining semantic coherence and optimizing ChromaDB performance for rapid vector lookups.  
- **Model Training & Integration**  
  Training a YOLO model that generalizes across varied leaf images and seamlessly integrating its outputs into the LLM toolchain.  
- **Latency & Resource Management**  
  Balancing real-time inference demands in Gradio (both vision and retrieval) with API rate limits, GPU constraints, and user experience.  

## Results
- **3D Embedding Visualization**  
  Generated interactive 3D plots of document embeddings, demonstrating clear clustering of disease categories and validating semantic retrieval.  
- **High-Accuracy Detection**  
  Deployed the custom YOLO model in demo inferences, accurately localizing and cropping diseased leaf areas across multiple plant species.  
- **Seamless Multimodal QA**  
  Delivered an integrated Gradio chatbot UI where users upload leaf images, receive immediate visual feedback, and pose follow-up questions—answered via the RAG pipeline.  
- **End-to-End Validation**  
  Verified the full workflow from scraping through QA in live demos, showcasing robust disease inference, treatment recommendations, and tool-based follow-up capabilities. 
