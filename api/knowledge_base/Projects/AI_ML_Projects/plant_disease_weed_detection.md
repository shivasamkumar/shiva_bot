# YOLOv12 Plant Disease & Weed Detection

## Introduction
Modern agriculture increasingly relies on automated, AI-driven systems to monitor crop health and manage weeds—two critical factors directly impacting yield, quality, and sustainability. This project delivers a comprehensive pipeline combining dual YOLOv12 detectors and a GPT-enabled advisory system. First, plant-disease and weed datasets are downloaded from Roboflow, merged under a unified `data.yaml`, and used to train specialist Ultralytics YOLOv12 models. During inference, both models run on each input image, fusing outputs with clear `D_` and `W_` prefixes for disease and weed classes. Detected disease labels and confidence scores feed into OpenAI’s GPT-4o API to generate actionable agronomic advice and treatment recommendations. 

## Features

1. **Assembling & Preparing Custom Datasets**  
   - Downloads a **plant‑disease** dataset (scab, blight, mildew, viral spots, etc.) and a **weed** dataset from two Roboflow workspaces.  
   - Merges them under a unified `data.yaml` to maintain consistent class mappings and streamline training across both domains.
   - Cover key concepts like , data merzing and **model zoo** aproach , working with two multiple models for the same problem. 

2. **Trains & Fine‑Tunes Specialist YOLOv12 Models**  
   - Uses Ultralytics’ YOLOv12 architecture to build two separate detectors:  
     - **Plant Disease Model** — sensitive to subtle lesion patterns and leaf deformations for early disease detection. I used two unique datsets from robo flow , for the plant disease detection and merged them together.
     - **Weed Detection Model** — optimized for identifying common weed species against crop backdrops.  
   - Training hyperparameters (epochs, batch size, learning rate schedules) are fully configurable in the notebook.  
   - Tracks performance via precision, recall, and mAP metrics.

3. **Performs Dual‑Model Inference via Model Zoo**  
   - Implements a “two‑specialist” inference strategy rather than a single all‑in‑one model, reducing class overlap errors.  
   - Runs both models on each image and fuses their outputs with clear annotations:  
     - **D\_** prefixes for disease classes (e.g., `D_Powdery_mildew`)  
     - **W\_** prefixes for weed classes (e.g., `W_Johnson_grass`)  

4. **Integrates GPT‑4o for Natural‑Language Disease Analysis**  
   - Feeds detected disease names and confidence scores into OpenAI’s GPT‑4o API.  
   - Generates actionable agronomic advice and best‑practice treatment suggestions.
   - Fine tuning the gpt model according to the use case by giving it a .json file to learn on.
   - Transforms raw detection boxes into an intuitive “field report".


## Challenges Faced

- **Dataset Merging Complexity**  
  Harmonizing class labels and annotation formats across two distinct Roboflow workspaces and ensuring balanced representation during training.  
- **Model Differentiation & Overlap**  
  Designing dual specialist detectors to reduce misclassification between disease and weed classes and to optimize inference pipelines under a “model zoo” strategy.  
- **Training & Resource Management**  
  Tuning training hyperparameters (epochs, batch size, learning rate schedules) to maximize mAP on both datasets without overfitting, given compute constraints in a Colab environment.  
- **Real-Time GPT Integration**  
  Orchestrating low-latency calls to the GPT-4o API for field-report generation while managing API rate limits and maintaining a responsive user interface.  

## Results
- **Plant Disease Detector Fine-Tuning**  
  - mAP @ 0.50 increased from 0.7697 to 0.7930  
  - mAP @ 0.75 increased from 0.7060 to 0.7248  
  - mAP @ 0.50–95 increased from 0.5962 to 0.6216  
- **Weed Detector Performance**  
  - mAP @ 0.50 = 0.7535  
  - mAP @ 0.75 = 0.9756  
  - mAP @ 0.50–95 = 0.87997  
- **Integrated Field Reporting**  
  Demonstrated seamless fusion of detection outputs with GPT-4o to generate actionable agronomic advice and structured field reports, validating the end-to-end multimodal pipeline. 
