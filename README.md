# Crop Recommendation System Using Machine Learning
# Description
Precision agriculture is an approach that uses information technology and a wide array of items such as GPS, sensors, and data analytics to enhance crop yields and optimize agricultural practices. By integrating machine learning, this project aims to analyze environmental and soil data to predict the optimal crops for specific conditions. This involves using historical data to train models that can understand and predict which crop varieties will thrive under various environmental factors such as soil type, climate conditions, and resource availability.


The primary motivation for this project is to enhance agricultural productivity by enabling farmers to make better-informed decisions about what crops to plant and when. This is increasingly important as agricultural industries face challenges from changing climate conditions, population growth, and the need for sustainable practices. By using data-driven decisions, farmers can optimize the use of resources like water, fertilizers, and pesticides, which in turn contributes to more sustainable agricultural practices. The project aims to minimize waste and maximize efficiency in crop production.

![image](https://github.com/user-attachments/assets/8ff6b6bf-d253-4cbf-9310-4bab141b5695)


# Key Features
Input Data Collection: The system allows users to input relevant data such as soil parameters, climate information, and geographic location.
Data Preprocessing: The input data is preprocessed to handle missing values, normalize or scale features, and transform categorical variables.
Machine Learning Models: Various machine learning algorithms are used Random forest, knn, neural networks, decision trees, support vector machines (SVM), and gradient boosting techniques, etc. to build predictive models.
Model Training and Evaluation: The models are trained on historical data and evaluated using appropriate performance metrics to ensure accuracy and reliability.
Crop Recommendation: We will give top 5  crops and also their probabilities based on the inputs.
User-Friendly Interface: The system provides a user-friendly interface where users can easily input their data, view recommendations.

# Dataset




Source: The dataset is hosted on Kaggle, a popular platform for data science projects and competitions.

Data Size and Structure

Number of Instances/Samples: 2,200            Number of Attributes: 8 raw attributes

Features: 7 ( That we are interested in)

Soil Nutrients: Nitrogen (N), Phosphorus (P), Potassium (K)

Weather Conditions: Temperature, Humidity, Rainfall

Soil pH: pH level of the soil

Target Variable: Crop type recommended (categorical variable) – 22 categories.

The target variable, 'label', represents the type of crop recommended based on the input features. The dataset contains multiple crop categories such as rice, wheat, maize, etc.



# Algorithms

Types of Machine Learning or Data Analysis

Type of Task: Classification (multi)

Goal: The primary goal is to classify which crops are best suited for cultivation based on specific environmental conditions and soil characteristics.

Machine Learning Techniques:

Decision Trees, Random Forest, Gradient Boosting, 
Logistic Regression (multi), Linear Discriminant Analysis (LDA)
Support Vector Machines (SVM), K-Nearest Neighbors (KNN)
Naïve Bayes
 Neural Networks.
 

 # How our model will be different:
 
We are trying to predict top 5 crops instead of one crop and that too with their probabilities.

Also trying better model evaluation techniques like accuracy, precision, recall, and F1-score. Techniques like cross-validation will be used to ensure that the model generalizes well on unseen data.





