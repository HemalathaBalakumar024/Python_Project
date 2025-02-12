# Autism Spectrum Disorder Prediction using Deep Neural Network (DNN)
This repository contains a deep learning project aimed at predicting Autism Spectrum Disorder (ASD) using a Deep Neural Network (DNN). The objective is to develop a model that can classify individuals based on relevant features, providing an early indication of potential ASD.
🧑‍🏫 Introduction
Autism Spectrum Disorder (ASD) is a developmental disorder characterized by difficulties with social interaction and communication. Early diagnosis and intervention can greatly improve outcomes. This project leverages a Deep Neural Network (DNN) to classify individuals based on features related to ASD diagnosis.

📊 Dataset
The dataset used for this project contains various features related to behavioral patterns and demographic information.

Source: Publicly available ASD dataset (replace with actual link if applicable)
Features: Includes behavioral screening questions, age, gender, and other demographic information.
Preprocessing: Missing values were handled, and categorical variables were encoded. The data was normalized for training the DNN model.
🏗️ Model Architecture
The DNN model consists of the following layers:

Input Layer: Takes in 21 features (example, adjust if necessary)
Hidden Layers: Three fully connected layers with ReLU activation
Dropout layers to prevent overfitting
Output Layer: Single neuron with a sigmoid activation for binary classification
