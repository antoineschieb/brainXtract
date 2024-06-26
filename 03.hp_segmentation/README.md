# Automated 3D Microscopic Volume Analysis for Hippocampus Segmentation in Mouse Brain

## Introduction
This repository contains scripts and utilities for processing and analyzing medical imaging datasets, particularly focusing on the Hippocampus Segmentation. The scripts are primarily aimed at preprocessing tasks such as data conversion, augmentation, and evaluation.

## Requirements
- Python 3.x
- NVIDIA GPU (for accelerated processing)
- Dependencies listed in `requirements.txt`

## Setup Instructions

1. **Create Conda Environment**:
   ```bash
   conda create --name hippocampus_seg_env python=3.x

2. **Activate the Environment**:
   ```bash
   conda activate hippocampus_seg_env

3. **Check GPU Availability**:
   Execute `!nvidia-smi` to ensure that a compatible NVIDIA GPU is available for accelerated processing.

## Dataset Information
- **Training Dataset**: `{BASE_PATH}/dataset/nnUNet_raw_data/{task_name}/imagesTr`
- **Ground Truth Training Dataset**: `{BASE_PATH}/dataset/nnUNet_raw_data/{task_name}/labelsTr`
- **Test Dataset**: `{BASE_PATH}/dataset/nnUNet_raw_data/{task_name}/imagesTs`
- **Ground Truth Test Dataset**: `{BASE_PATH}/dataset/nnUNet_raw_data/{task_name}/labelsTs`

## Usage
- After setup and preprocessing, various utility functions and scripts are available for:
  - Dataset format prepared 
  - Model training and evaluation
  - Evaluation metrics calculation

## Slice Visualisation
- Slice Viewer 
![Slice View](./images/slice_viewer.jpg)
- Slice Viewer 
![Slice View](./images/slice_viewer1.jpg)

## Prediction
![Hippocampus Segmentation](./images/hp.jpg)

## Additional Notes
- This repository is designed to work with the nnUNet framework for medical image segmentation tasks.

For more detailed information, refer to the documentation and source code.
