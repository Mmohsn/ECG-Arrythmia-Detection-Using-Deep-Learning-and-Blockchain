# ECG-Arrythmia-Detection-Using-Deep-Learning-and-Blockchain
---
This repository contains the code for a project aimed at securing medical data, specifically electrocardiogram (ECG) data, while making predictions using blockchain technology. The MIT-BIH ECG dataset is utilized in this project to demonstrate how blockchain can be leveraged to ensure data integrity and security while performing machine learning predictions.

## Project Overview

The primary objective of this project is to enhance the security of medical data by integrating blockchain technology into the data processing pipeline. The project focuses on securing ECG data from the MIT-BIH Arrhythmia Database and using a prediction model to classify the data.

## Repository Structure

- `block_chain.py`: Contains the implementation of blockchain technology to secure the medical data. This script ensures that the data integrity is maintained throughout the data processing stages.
  
- `prediction.py`: Handles the machine learning aspect of the project, where a model is trained on the MIT-BIH ECG data to predict arrhythmia.
  
- `run.py`: The main script that ties together the blockchain and prediction components, providing an end-to-end solution for securing and analyzing ECG data.

- `Notebook.ipynb`: A Jupyter notebook that provides a step-by-step demonstration of the entire process, from data preprocessing to blockchain integration and prediction. This notebook is intended for those who prefer an interactive approach to understanding the project.

## Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/Mmohsn/ECG-Arrythmia-Detection-Using-Deep-Learning-and-Blockchain.git
    cd ECG-Arrythmia-Detection-Using-Deep-Learning-and-Blockchain
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the project:

    ```bash
    python run.py
    ```

## Dataset

The project uses the MIT-BIH Arrhythmia Database, which is publicly available and widely used for ECG classification tasks. Please ensure that you have the dataset available in the appropriate directory before running the scripts.

## How It Works

1. **Data Preprocessing**: The MIT-BIH ECG data is preprocessed to a format suitable for prediction.
2. **Blockchain Integration**: The preprocessed data is then fed into a blockchain framework to secure the data and ensure its integrity.
3. **Prediction**: A machine learning model is used to predict arrhythmia based on the ECG data. The prediction process is secure, as the data integrity is protected by the blockchain.

## Contributing

Contributions to the project are welcome. If you have any ideas, bug reports, or suggestions, please open an issue or submit a pull request.

## Acknowledgments

- The MIT-BIH Arrhythmia Database is provided by the MIT Laboratory for Computational Physiology.
