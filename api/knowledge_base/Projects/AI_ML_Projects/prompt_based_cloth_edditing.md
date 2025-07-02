# Prompt Driven Cloth Editor

## Introduction
The Prompt Driven Cloth Editor is a Python-based pipeline for interactive, prompt-guided garment editing that combines state-of-the-art semantic segmentation with generative inpainting. In **Version 1**, NVIDIA’s SegFormer model is fine-tuned on a custom multi-class clothing dataset to produce high-quality semantic masks for regions like sleeves, collars, and patterns. These masks are then fed into Stable Diffusion’s inpainting pipeline, allowing users to specify natural-language design prompts (e.g. “floral pattern on sleeves”) and instantly visualize realistic garment modifications. In **Version 2**, CLIPSeg is integrated for free-form, prompt-based mask generation—enabling on-the-fly semantic segmentation without retraining. A pair of Jupyter notebooks (`Semantic_segmentation_training.ipynb` and `Prompt_based_Generative_cloth_editting.ipynb`) orchestrates the full workflow from dataset preprocessing through mask generation and diffusion-based editing. 

## Features
- **Fine-Tuned SegFormer**  
  Trains a custom SegFormer model on a multi-class clothing dataset (sleeves, collar, torso, hem, etc.) to output precise semantic masks.  
- **Stable Diffusion Inpainting**  
  Applies text-prompted inpainting to masked regions, generating high-fidelity garment edits directly from natural-language descriptions.  
- **CLIPSeg Prompt Masking**  
  Offers a zero-shot segmentation mode where CLIPSeg produces masks from arbitrary text prompts (e.g. “add polka dots to collar”), eliminating the need for retraining.  
- **Modular Notebook Pipeline**  
  Two Colab-ready notebooks—one for segmentation training and one for generative editing—auto-install dependencies and support batch-mode operations.  
- **Interactive Outputs**  
  Saves edited garment variants under `outputs/`, provides visualizations of original vs. edited images, and logs intermediate mask overlays for debugging. 

## Challenges Faced
- **Dataset Annotation & Balance**  
  Curating and labeling a sufficiently large, balanced dataset of garment regions to train SegFormer without overfitting to dominant classes.  
- **Model Generalization**  
  Ensuring the fine-tuned SegFormer produced accurate masks across diverse clothing types, colors, and textures.  
- **Inpainting Consistency**  
  Tuning Stable Diffusion prompts and mask padding to avoid artifacts at mask boundaries and maintain realistic fabric continuity.  
- **Latency & Resource Constraints**  
  Managing GPU memory and inference speed for both segmentation and diffusion steps within the Colab environment’s limits.

## Results
- **Segmentation Accuracy**  
  Achieved a mean Intersection-over-Union (mIoU) of 0.82 across five garment classes on a held-out validation set.  
- **Prompt-Driven Edits**  
  Demonstrated seamless transformations—e.g., “striped sleeves,” “lace collar,” “floral hem”—with high visual fidelity and minimal artifacts.  
- **Zero-Shot Masking**  
  CLIPSeg integration enabled accurate mask generation for unseen prompts with an average precision of 0.76 on test prompts.  
- **End-to-End Workflow**  
  Validated the complete pipeline from segmentation training to generative editing in live demos, showcasing rapid design exploration with natural-language control. 
