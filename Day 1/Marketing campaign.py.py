
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from colorama import Fore, Style, init
init(autoreset=True)
df = pd.read_csv("marketing_campaign.csv", sep='\t')
print(Fore.CYAN + "✅ Dataset Loaded Successfully!")
print(Fore.YELLOW + f"Shape of Data: {df.shape}")
print(Fore.CYAN + "\n Cleaning Data...")

df.columns = df.columns.str.strip().str.replace(' ', '_')
df.drop_duplicates(inplace=True)
df.fillna(df.mean(numeric_only=True), inplace=True)

if 'Dt_Customer' in df.columns:
    df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'], errors='coerce')

print(Fore.GREEN + " Data Cleaning Done!")
sns.set(style="whitegrid")
plt.rcParams.update({
    'figure.figsize': (9, 5),
    'axes.titlesize': 14,
    'axes.labelsize': 12,
    'axes.titlepad': 12,
    'axes.labelpad': 10,
    'font.weight': 'bold',
})
if 'Year_Birth' in df.columns:
    df['Age'] = 2025 - df['Year_Birth']
    plt.figure(figsize=(8,5))
    sns.histplot(df['Age'], bins=20, color="#FF69B4", edgecolor='white', alpha=0.9)
    plt.title(" Distribution of Customer Age")
    plt.xlabel("Age")
    plt.ylabel("Count")
    plt.show()

if 'Marital_Status' in df.columns:
    plt.figure(figsize=(7,5))
    sns.countplot(x='Marital_Status', data=df, palette=['#FF5C8A', '#FFA6C1', '#FFC2D1'])
    plt.title(" Distribution of Marital Status")
    plt.xlabel("Marital Status")
    plt.ylabel("Count")
    plt.show()

if 'Income' in df.columns:
    plt.figure(figsize=(8,5))
    sns.histplot(df['Income'], kde=True, color='#FF6699', alpha=0.8)
    plt.title(" Income Distribution")
    plt.xlabel("Income")
    plt.ylabel("Count")
    plt.show()

if 'Response' in df.columns:
    response_counts = df['Response'].value_counts()
    plt.figure(figsize=(6,5))
    sns.barplot(x=response_counts.index, y=response_counts.values, palette=['#FF66A3', '#FFC0CB'])
    plt.title(" Campaign Response (Accepted vs Rejected)")
    plt.xlabel("Response")
    plt.ylabel("Count")
    plt.show()

if 'Education' in df.columns:
    if {'MntWines', 'MntMeatProducts'}.issubset(df.columns):
        df['MntTotal'] = df[['MntWines','MntFruits','MntMeatProducts','MntFishProducts',
                             'MntSweetProducts','MntGoldProds']].sum(axis=1)
        plt.figure(figsize=(8,5))
        sns.boxplot(x='Education', y='MntTotal', data=df, palette='pastel')
        plt.title(" Education Level vs Total Spending")
        plt.xlabel("Education Level")
        plt.ylabel("Total Amount Spent")
        plt.show()
print(Fore.MAGENTA + "\n Dashboard Ready — Beautiful Interactive-Style Output Created!")
