# Healthhcare_Analysis

## Objective

In our Django-based website, we transitioned from drug analysis to exploring stroke possibilities using a dataset. After preprocessing, we computed summary statistics showcasing age distribution correlations among factors like hypertension, heart disease, and more. Employing Matplotlib and Seaborn, we crafted visualisations illustrating gender-specific health conditions and factors influencing stroke likelihood. Our pivot included predictive modelling using scikit-learn to estimate stroke occurrence based on attributes like age, gender, BMI, and smoking status. Integrating Plotly for interactive visuals, our site presents probability insights on stroke risk factors. The UI offers user-friendly features for exploring specific factors and understanding the impact on stroke likelihood. This comprehensive analysis aids users in comprehending stroke indicators and risks through a user-friendly web interface.

## About The Data Set

### Dataset 1

Source – Kaggle  
Link: [250k Medicines Usage, Side Effects, and Substitutes](https://www.kaggle.com/datasets/shudhanshusingh/250k-medicines-usage-side-effects-and-substitutes?rvi=1)

This dataset contains information on over 248,000 medical drugs available worldwide. It's a valuable resource for medical researchers, healthcare professionals, and drug manufacturers. Here are some specifics about the dataset:

- **Drug Name**: The name of the drug itself.
- **Adverse Reactions and Side Effects**: Information about the potential negative effects when using the drug.
- **Drug Interactions**: Details about how this drug interacts with other drugs.
- **Drug Class**: Drug classification based on purpose or function.
- **Substitute Drugs**: Alternatives to the drug from different manufacturers with the same compositions.
- **Active Ingredients**: Components used in the drug's formulation.

### Dataset 2

Source: Kaggle  
Link: [AZ Medicine Dataset of India](https://www.kaggle.com/datasets/shudhanshusingh/az-medicine-dataset-of-india)

This dataset contains information on medicines from various pharmaceutical companies, including compositions, types, market availability, pricing, and more. It also includes data on drug side effects, substitutes, and usage. The data gets updated annually.

### Dataset 3

Source - Kaggle  
Link: [11,000 Medicine Details](https://www.kaggle.com/datasets/singhnavjot2062001/11000-medicine-details?rvi=1)

The dataset comprises over 11,826 medicines and includes information on their composition, uses, manufacturers, image URLs, and review percentages (Excellent, Average, Poor). It is valuable for medical professionals, researchers, and healthcare practitioners to study drug interactions, treatment efficacy, quality control, and user satisfaction.

### Dataset 4

Source – Kaggle  
Link: [Healthcare Dataset - Stroke Data](https://www.kaggle.com/code/rishabh057/healthcare-dataset-stroke-data/input)

The dataset contains information about individuals and various health-related attributes:

- **id**: Unique identifier for each individual.
- **gender**: Gender of the individual.
- **age**: Age of the individual.
- **hypertension**: Binary feature indicating whether the individual has hypertension (1 for yes, 0 for no).
- **heart_disease**: Binary feature indicating whether the individual has heart disease (1 for yes, 0 for no).
- **ever_married**: Binary feature indicating whether the individual is married (Yes or No).
- **work_type**: Type of work the individual is engaged in.
- **Residence_type**: Type of residence (Urban or Rural).
- **avg_glucose_level**: Average glucose level in the individual's blood.
- **bmi**: The individual's Body Mass Index (BMI).
- **smoking_status**: Smoking status of the individual (smokes, formerly smoked, never smoked).
- **stroke**: Binary feature indicating whether the individual had a stroke (1 for yes, 0 for no).

The dataset comprises 5110 entries (rows) with 12 columns. It contains a mix of numeric (integers and floats) and categorical (object) data types. Additionally, there are some missing values in the 'bmi' column (4909 non-null values out of 5110 entries). The goal of analysing this dataset could involve understanding factors associated with strokes or building predictive models for stroke occurrence based on various attributes.

## About The Project

#### Project Transition: Drug Analysis to Stroke Investigation

The project embarked on a transition from drug analysis to a profound investigation of stroke possibilities within health-related datasets. Initially, we focused on leveraging Python libraries - Pandas, Matplotlib, NumPy, and Seaborn - to conduct meticulous data analysis and visualisation. These libraries provided a robust foundation for processing and understanding complex datasets. 

#### Utilization of Pandas for Data Profiling

Pandas, a versatile library, played a pivotal role in our data profiling techniques. It empowered us to clean, preprocess, and extract insights from diverse datasets seamlessly. By employing Pandas, we efficiently handled missing data, transformed information, and conducted essential statistical analyses. This step significantly contributed to laying a solid groundwork for subsequent investigations.

#### Matplotlib and Visual Insights

Integrating Matplotlib's pyplot was a game-changer in our quest for insightful visualisations. Its functionalities allowed us to create vivid and meaningful visual representations. These visualisations were crucial in unravelling complex patterns, relationships, and distributions within the datasets. They became essential tools aiding our understanding of the intricate health-related information in the data.

#### Django Web Framework: Transformation to Web Interface

Our journey continued with the adoption of Django, a robust web framework renowned for its versatility and efficiency. Utilising Django, we seamlessly translated our data analyses into an accessible and user-friendly web interface. This transformation expanded the reach of our insights, making them available to a broader audience. Integrating Django facilitated an intuitive platform that simplified the exploration and comprehension of health data nuances.

#### Merging Analytical Methodologies with Web Development

The project's uniqueness lies in seamlessly merging analytical methodologies with web development. This synergy allowed us to create an informative platform that explores and explains health data intricacies. We crafted an insightful and educational platform by interweaving our analytical prowess with web development finesse. This convergence showcased our proficiency in amalgamating diverse skill sets to create a comprehensive solution.

## Summary and Impact

Our project's progression from initial data analysis to developing a user-friendly web interface exemplifies a holistic approach to health-related data exploration. We achieved a cohesive and informative platform through the strategic use of Python libraries, particularly Pandas for data profiling and Matplotlib for visualisations, and the adoption of Django for web development. This project is a testament to our ability to navigate intricate datasets, extract meaningful insights, and present them quickly.

## Screenshots

### 1. Data View
![image](https://github.com/mathewsjoe/Healthhcare_Analysis/assets/118895154/b4130021-540c-457c-a672-d8648349197d)

![image](https://github.com/mathewsjoe/Healthhcare_Analysis/assets/118895154/2df35ed5-0a2f-4cca-a704-03f80352fce3)


### 2. Descriptive Statistics
![image](https://github.com/mathewsjoe/Healthhcare_Analysis/assets/118895154/5b9b2ed7-34ee-496d-a4e5-152a10b1d982)


### Explanatory Analysis
![image](https://github.com/mathewsjoe/Healthhcare_Analysis/assets/118895154/89a28d67-5674-4553-a2ba-a11e6a1b8f42)

![image](https://github.com/mathewsjoe/Healthhcare_Analysis/assets/118895154/ee63a158-9ced-4ec8-97b8-77423fca5c55)

![image](https://github.com/mathewsjoe/Healthhcare_Analysis/assets/118895154/2c989d13-d3bb-4f3a-a781-762d5f4800aa)



## Data Profile

![image](https://github.com/mathewsjoe/Healthhcare_Analysis/assets/118895154/a7814833-28cb-405c-8393-499059ba5430)

![image](https://github.com/mathewsjoe/Healthhcare_Analysis/assets/118895154/098e8358-7cf5-4962-ba4b-2da22fde5541)

![image](https://github.com/mathewsjoe/Healthhcare_Analysis/assets/118895154/2e4bf8ac-dbd5-4cce-a72d-80e43464d731)

![image](https://github.com/mathewsjoe/Healthhcare_Analysis/assets/118895154/063d958a-6bdf-460c-9d3b-babbd2d619d2)

![image](https://github.com/mathewsjoe/Healthhcare_Analysis/assets/118895154/e14c48eb-2737-4b04-8ba1-61f896c301c7)

![image](https://github.com/mathewsjoe/Healthhcare_Analysis/assets/118895154/154bdd81-6f65-43d8-a61a-e874bb1236bf)

![image](https://github.com/mathewsjoe/Healthhcare_Analysis/assets/118895154/4f490c89-3478-4715-a2a6-22edd7469232)

![image](https://github.com/mathewsjoe/Healthhcare_Analysis/assets/118895154/b4a9fe30-288e-491e-afaf-441249b1785e)

![image](https://github.com/mathewsjoe/Healthhcare_Analysis/assets/118895154/b0814ff9-7007-4b57-96ba-9d4ec2a47ffb)

![image](https://github.com/mathewsjoe/Healthhcare_Analysis/assets/118895154/e377fd36-4b6d-432c-9b63-cb671e421466)

![image](https://github.com/mathewsjoe/Healthhcare_Analysis/assets/118895154/62ff74ee-a458-4f8f-9b29-30e3996ae871)
