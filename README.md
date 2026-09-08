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
Kenya is facing a rapidly worsening diabetes crisis, with health experts warning that the true burden is far higher than current statistics reveal. Years of under diagnosis, outdated national surveys and late presentation continue to mask the real scale of the problem. 

Current estimates suggest 813,300 Kenyan adults (3.1%) live with diabetes, but experts believe the actual prevalence is closer to 3.3–4.5%. Globally, 589 million adults have diabetes, with 252 million undiagnosed—most in low  and middle income countries where access to early testing remains limited. The High Cost of Late Diagnosis In Kenya, many patients only learn they are diabetic after developing serious complications. It is noted that,
- 60–70% of hospital admissions are linked to diabetes complications.
- 80% of dialysis patients suffer from diabetes related kidney failure.

These late presentations place enormous strain on an already overstretched health system. Urbanisation, Diet and Lifestyle Kenya’s diabetes surge is strongly tied to rapid urbanisation, sedentary habits and increased consumption of high sugar and high fat foods. According to KUTRRH endocrinologist Dr. Caroline Mithi: “Sedentary lifestyle, excessive smoking, alcohol intake, lack of exercise, and high-carbohydrate, high-fat diets are the main factors driving diabetes.” Younger adults are increasingly being diagnosed with type 2 diabetes sometimes as early as age 30 prompting experts to recommend baseline screening from age 30, with annual checks thereafter.

---

## Project Goal
Develop a 3-class classification model leveraging the CDC’s BRFSS dataset to detect early-to-advanced metabolic dysfunction.Key Deliverables:
- Multi-Class Prediction: Differentiate between Healthy ($0$), Prediabetic ($1$), and Diabetic ($2$) states using a curated 12-feature subset of non-invasive biological, behavioral, and demographic indicators.
- Early Interception Focus: Optimize classification thresholds and class weights to maximize the detection rate (Recall) of prediabetic individuals, enabling early lifestyle intervention before chronic complications occur.
- Feature Interpretability: Apply feature importance analysis (such as SHAP values) to identify the primary behavioral and clinical metrics driving transitions between metabolic stages.

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
> - DiffWalk (Difficulty Walking): Do you have serious difficulty walking or climbing stairs? 0 = no 1 = yes
> - Sex (0 = female, 1 = male)
> - Age (scale 1 = 18-24, 9 = 60-64, 13 = 80 or older)
> - Education (Education level) (EDUCA see codebook) scale 1-6 1 = Never attended school or only kindergarten 2 = Grades 1 through 8 (Elementary) 3 = Grades 9 through 11 (Some high school) 4 = Grade 12 or GED (High school graduate) 5 = College 1 year to 3 years (Some college or technical school) 6 = College 4 years or more (College graduate)
> - Income (Income scale: scale 1-8, 1 = less than $10,000, 5 = less than $35,000, 8 = $75,000 or more)

---

## Type of Problem
- Classification problem - early detection of Type 2 Diabetes.

1. Target Variable 
- (Diabetes_012) - 0 = no diabetes, 1 = prediabetes, 2 = diabetes

2. Feature variables
Features to use
> - BMI - Primary Driver. Body mass scales continuously, providing a direct gradient that helps differentiate normal, prediabetic, and diabetic ranges.
> - GenHlth - Strong Proxy. Self-reported health drops incrementally as metabolic health worsens from healthy $\rightarrow$ prediabetes $\rightarrow$ diabetes.
> - HighBp - Metabolic Marker. High blood pressure frequently develops in the prediabetic phase, making it crucial for splitting healthy vs. prediabetic rows.
> - HighChol - Metabolic Marker. Lipid imbalances track closely with early-to-late insulin resistance.
> - Age - Risk Gradient. Age provides a strong baseline probability curve for transitioning across metabolic tiers over time.
> - PhysHlth - Functional Metric. Measures physical impairment days, helping separate mild prediabetic discomfort from severe diabetic complications.
> - DiffWalk - Advanced Indicator. Highly effective at isolating class $2$ (Diabetes) due to mobility issues linked to nerve damage and poor circulation.
> - HeartDiseaseorAttack - Vascular Comorbid Marker. Advanced cardiovascular events heavily lean toward class $2$ (Diabetes), preventing false positives in class $1$ (Prediabetes).
> - PhysActivity - Lifestyle Driver. Sedentary behavior helps explain why individuals with similar BMIs might fall into prediabetes vs. non-diabetes.
> - Income - Social Determinant. Captures healthcare access and dietary quality, which strongly correlate with overall disease progression.
> - Eductaion - Social Determinant. Works alongside income to account for health literacy and early preventive habits.
> - Stroke - Severe Complication Flag. Provides a strong boundary marker for long-standing, advanced diabetes (Class $2$).

Features to drop
> - Smoker and HvyAlcoholConsump - While relevant to overall lifestyle, their direct mathematical correlation with distinguishing prediabetes specifically is very noisy in BRFSS survey data.
> - HeartDiseaseorAttack
> - CholCheck - Over $95\%$ of survey participants report having had a cholesterol check in the last 5 years, making this column almost entirely redundant with HighChol.
> - Fruits and Veggies - Binary answers like "eating fruit 1+ times a day" do not contain enough statistical nuance to distinguish prediabetes from diabetes.
> - AnyHealthcare and NoDocbcCost - Extremely low variance across respondents; they add noise rather than useful predictive signals.
> - Sex - Biological sex shows very weak correlation boundaries across the 3 metabolic states compared to BMI, blood pressure, and age.

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
- XGBoost

Imbalanced-learn
- SMOTE - oversampling minority severity classes to address class imbalance..
- class_weight