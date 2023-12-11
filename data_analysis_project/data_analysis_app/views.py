# data_analysis_app/views.py
from django.shortcuts import render
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def data_tab(request):
    # Read Titanic dataset from CSV
    df = pd.read_csv("C:\\Users\\user\\Desktop\\finalcleaned.csv")
    df_first_ten = df.head(10)
    # Convert DataFrame to HTML for rendering in template
    table_html = df_first_ten.to_html(classes='table table-striped')

    return render(request, 'data_tab.html', {'table_html': table_html})

def descriptive_statistics_tab(request):
    # Read Titanic dataset from CSV
    df = pd.read_csv("C:\\Users\\user\\Desktop\\finalcleaned.csv")
    
    # Perform descriptive statistics using pandas
    descriptive_stats = df.describe().to_html(classes='table table-striped')

    return render(request, 'descriptive_statistics_tab.html', {'descriptive_stats': descriptive_stats})

def exploratory_data_analysis_tab(request):
    # Set a non-interactive backend for matplotlib
    plt.switch_backend('agg')

    # Read Titanic dataset from CSV
    df = pd.read_csv("C:\\Users\\user\\Desktop\\finalcleaned.csv")
    
    # Perform exploratory data analysis using seaborn and matplotlib
    # Create plots, convert them to base64, and pass to template

    # Example: Countplot of 'Sex'
    plot1 = plt.hist(df['Review'], bins=20, color='skyblue', edgecolor='black')
    plt.title('Distribution of Reviews')
    plt.xlabel('Review Score')
    plt.ylabel('Frequency')
    
    # Save plot to BytesIO
    plot1_image = BytesIO()
    plot1.figure.savefig(plot1_image, format='png')
    plot1_base64 = base64.b64encode(plot1_image.getvalue()).decode('utf-8')

    # Example: Age distribution
    plot2 = sns.boxplot(x='Therapeutic Class', y='Review', data=df)
    plt.title('Box Plot of Reviews by Therapeutic Class')
    plt.xlabel('Therapeutic Class')
    plt.ylabel('Review Score')
    plt.xticks(rotation=45, ha='right')
    # Save plot to BytesIO
    plot2_image = BytesIO()
    plot2.figure.savefig(plot2_image, format='png')
    plot2_base64 = base64.b64encode(plot2_image.getvalue()).decode('utf-8')

    return render(request, 'exploratory_data_analysis_tab.html', {'plot1': plot1_base64, 'plot2': plot2_base64})