# Early Type 2 Diabetes Risk Classifier. 

---

## What is type 2 diabetes?!
Type 2 diabetes, the most common type of diabetes, is a disease that occurs when your blood glucose, also called blood sugar, is too high. Blood glucose is your main source of energy and comes mainly from the food you eat. Insulin, a hormone made by the pancreas, helps glucose get into your cells to be used for energy. In type 2 diabetes, your body doesn’t make enough insulin or doesn’t use insulin well. Too much glucose then stays in your blood and not enough reaches your cells.

You can develop type 2 diabetes at any age, even during childhood. However, type 2 diabetes occurs most often in middle-aged and older people. You are more likely to develop type 2 diabetes if you are age 45 or older, have a family history of diabetes, or are overweight or have obesity. Diabetes is more common in people who are African American, Hispanic/Latino, American Indian, Asian American, or Pacific Islander.

---

## Project Description.
Type 2 diabetes often develops quietly over several years. By the time symptoms appear, high blood sugar levels may have already impacted heart, kidney or eye health. While blood tests are the definitive way to diagnose diabetes, universal screening is difficult to scale—especially in communities with limited access to affordable healthcare clinics. This project addresses that challenge by building a machine learning model that estimates diabetes risk using simple, non-invasive health metrics and lifestyle survey responses.

While there is no permanent cure, early detection allows individuals to manage or even reverse prediabetes through targeted lifestyle interventions—such as weight loss, dietary adjustments, increased physical activity and medical therapy. Predictive machine learning models offer public health officials and healthcare providers a scalable way to flag high-risk individuals early, paving the way for proactive, preventative care.

Using a pre-balanced dataset of over 250,000 records from the CDC’s Behavioral Risk Factor Surveillance System (BRFSS), this pipeline analyzes 21 distinct factors, including BMI, blood pressure history, physical activity, daily diet, and age. The model maps these everyday inputs into a continuous risk probability score, identifying individuals who are at high risk before they step foot inside a laboratory.

---

## Problem Statement.
Despite affecting hundreds of millions of people worldwide and causing severe complications like heart disease, vision loss and kidney failure, the vast majority of individuals living with prediabetes and diabetes remain completely unaware of their condition until irreversible damage has already occurred. 

While early lifestyle modifications can effectively halt disease progression, traditional clinical screening relies on invasive, facility-based blood tests that leave under-resourced populations severely underserved. How can we accurately predict an individual's risk of having or developing Type 2 diabetes using easily collectable, non-invasive demographic, behavioral, and self-reported health indicators—enabling early, scalable intervention before formal clinical testing is conducted? By tapping into large-scale health survey data, this project builds a non-invasive machine learning model to decode complex patterns across daily lifestyle habits, socioeconomic factors and comorbid health indicators (having two or more health conditions at the same time), creating a low-cost, digital early-warning system that bridges the gap between population health data and proactive clinical care.

---

## Dataset
- Remote source: Diabetes Health Indictaors Dataset - https://www.kaggle.com/alexteboul/diabetes-health-indicators-dataset
- Size: 253,680 survey responses, 22 columns
Columns:-
> - Diabetes_012 (0 = no diabetes, 1 = prediabetes, 2 = diabetes)
> - HighBP (0 = no high BP, 1 = high BP)
> - HighChol (0 = no high cholesterol, 1 = high cholesterol)
> - CholCheck (0 = no cholesterol check in 5 years, 1 = yes cholesterol check in 5 years)
> - BMI (Body Mass Index) 
> - Smoker (Have you smoked at least 100 cigarettes in your entire life? [Note: 5 packs = 100 cigarettes] 0 = no, 1 = yes)
> - Stroke ((Ever told) you had a stroke. 0 = no 1 = yes)
> - HeartDiseaseorAttack (coronary heart disease (CHD) or myocardial infarction (MI) 0 = no, 1 = yes)
> - PhysActivity (physical activity in past 30 days - not including job 0 = no, 1 = yes)
> - Fruits (Consume Fruit 1 or more times per day 0 = no, 1 = yes)
> - Veggies (Consume Vegetables 1 or more times per day 0 = no 1 = yes)
> - HvyAlcoholConsump (Heavy drinkers (adult men having more than 14 drinks per week and adult women having more than 7 drinks per week) 0 = no, 1 = yes)
> - AnyHealthcare (Have any kind of health care coverage, including health insurance, prepaid plans such as HMO, etc. 0 = no, 1 = yes)
> - NoDocbcCost (Was there a time in the past 12 months when you needed to see a doctor but could not because of cost? 0 = no 1 = yes)
> - GenHlth (Would you say that in general your health is: scale 1-5: 1 = excellent, 2 = very good, 3 = good, 4 = fair, 5 = poor)
> - MentHlth (mental health: scale 1-30 days, for how many days during the past 30 days was your mental health not good?)
> - PhysHlth (Physical health: scale 1-30 days, for how many days during the past 30 days was your physical health not good?)
> - Sex (0 = female, 1 = male)
> - Age (scale 1 = 18-24, 9 = 60-64, 13 = 80 or older)
> - Income (Income scale: scale 1-8, 1 = less than $10,000, 5 = less than $35,000, 8 = $75,000 or more)

---

## ML Workflow
i) Problem Definition.

ii) Data Collection

iii) Data Cleaning and Preprocessing.

iv) Exploratory Data Analysis

v) Feature Engineering and Selection.

vi) Model Selction.

vii) Model Training.

viii) Model Evaluation and Tuning.

ix) Model Deployment.

x) Model Monitoring and Maintenanace.

---

## Tools.
Python
- pandas 
- numpy
- matplolib and seaborn
- scikit-learn

Models
- Logistic Regression
- SVM
- KNN
- Random Forest
- xgboost

Imbalanced-learn
- SMOTE - oversampling minority severity classes to address class imbalance.