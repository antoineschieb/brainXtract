# Hippocampus Segmentation 

## Introduction
This repository contains scripts and utilities for processing and analyzing medical imaging datasets, particularly focusing on the Hippocampus Segmentation. The scripts are primarily aimed at preprocessing tasks such as data conversion, augmentation, and evaluation.

## Requirements
- Python 3.x
- NVIDIA GPU (for accelerated processing)
- Dependencies listed in `requirements.txt`

## Setup Instructions
1. Execute `!nvidia-smi` to check GPU availability.
2. Import necessary libraries:
3. Define dataset paths:
4. Setup environment variables:
5. Install dependencies:
6. Preprocess dataset:
## Dataset Information
- **Training Dataset**: `{BASE_PATH}/dataset/nnUNet_raw_data/{task_name}/imagesTr`
- **Ground Truth Training Dataset**: `{BASE_PATH}/dataset/nnUNet_raw_data/{task_name}/labelsTr`
- **Test Dataset**: `{BASE_PATH}/dataset/nnUNet_raw_data/{task_name}/imagesTs`
- **Ground Truth Test Dataset**: `{BASE_PATH}/dataset/nnUNet_raw_data/{task_name}/labelsTs`

## Usage
- After setup and preprocessing, various utility functions and scripts are available for:
  - Data visualization
  - Evaluation metrics calculation
  - Model training and evaluation

## Slice Visualisation
![Slice View](./03.hp_segmentation/images/slice_viewer.jpg)
![Slice View](./03.hp_segmentation/images/slice_viewer1.jpg)

## Prediction
![Hippocampus Segmentation](./03.hp_segmentation/images/hp.jpg)

## Additional Notes
- This repository is designed to work with the nnUNet framework for medical image segmentation tasks.

For more detailed information, refer to the documentation and source code.
