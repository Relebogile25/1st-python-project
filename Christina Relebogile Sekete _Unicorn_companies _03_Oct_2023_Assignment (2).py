#!/usr/bin/env python
# coding: utf-8

# ## import Modules 

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# # Load your dataset 

# In[3]:


unicorn_companies = pd.read_csv(r'C:\Users\reles\OneDrive\Desktop\Quantam\week 4\Unicorn_Companies.csv')


# # Display basic information about the dataset

# In[4]:


print("Dataset Information:")
print(unicorn_companies.info())


# # Display the first few rows of the dataset

# In[5]:


print("\nFirst Few Rows of the Dataset:")
print(unicorn_companies.head())


# # Summary statistics for numeric columns

# In[7]:


print("\nSummary Statistics for Numeric Columns:")
print(unicorn_companies.describe())


# # Data cleaning and conversion of string columns to float

# In[16]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your 'unicorn_companies' dataset (replace 'your_data.csv' with the actual file path)
unicorn_companies = pd.read_csv( r'C:\Users\reles\OneDrive\Desktop\Quantam\week 4\Unicorn_Companies.csv')

# Check the data types of 'Valuation' and 'Funding' columns
print(unicorn_companies['Valuation'].dtype)
print(unicorn_companies['Funding'].dtype)

# If they are not recognized as strings, convert them to strings first
unicorn_companies['Valuation'] = unicorn_companies['Valuation'].astype(str)
unicorn_companies['Funding'] = unicorn_companies['Funding'].astype(str)

# Clean and convert the 'Valuation' and 'Funding' columns to float, handling both 'M' and 'B' suffixes
def clean_and_convert_valuation(valuation_str):
    valuation_str = valuation_str.replace('$', '').replace(',', '')
    if 'M' in valuation_str:
        return float(valuation_str.replace('M', '')) / 1000  # Convert 'M' to 'B' (divide by 1000)
    elif 'B' in valuation_str:
        return float(valuation_str.replace('B', ''))
    elif 'Unknown' in valuation_str:
        return None  # Handle 'Unknown' values as missing data
    else:
        return float(valuation_str)

unicorn_companies['Valuation'] = unicorn_companies['Valuation'].apply(clean_and_convert_valuation)
unicorn_companies['Funding'] = unicorn_companies['Funding'].apply(clean_and_convert_valuation)


plt.tight_layout()
plt.show()



#  # Data visualization

# In[17]:


plt.figure(figsize=(16, 16))


# # Countplot of industries

# In[20]:


plt.subplot(4, 2, 1)
sns.countplot(data=unicorn_companies, x='Industry')
plt.title('Count of Companies by Industry')
plt.xticks(rotation=90)


# # Boxplot of valuations

# In[21]:


plt.subplot(4, 2, 2)
sns.boxplot(data=unicorn_companies, y='Valuation')
plt.title('Distribution of Valuations')


# # Countplot of countries

# In[23]:


plt.subplot(4, 2, 3)
sns.countplot(data=unicorn_companies, x='Country')
plt.title('Count of Companies by Country')
plt.xticks(rotation=90)


# # Histogram of funding amounts

# In[24]:


plt.subplot(4, 2, 4)
sns.histplot(data=unicorn_companies, x='Funding', bins=20, kde=True)
plt.title('Distribution of Funding Amounts')


# 
# # Countplot of select investors 

# In[26]:


plt.subplot(4, 2, 5)
sns.countplot(data=unicorn_companies, x='Select Investors')
plt.title('Count of Companies by Select Investor')
plt.xticks(rotation=90)


# # Line plot for trends in company count by year 

# In[31]:


print("Column Names:")
print(unicorn_companies.columns)


# In[72]:


# Ensure 'date joined' is in datetime format
unicorn_companies['Date Joined'] = pd.to_datetime(unicorn_companies['Date Joined'])

# Extract the year from the 'date joined' column
unicorn_companies['Year_Founded'] = unicorn_companies['Date Joined'].dt.year

# Count the number of companies founded each year
company_count_by_year = unicorn_companies['Year_Founded'].value_counts().sort_index()

# Create a line plot
plt.figure(figsize=(10, 6))
sns.lineplot(data=company_count_by_year, x=company_count_by_year.index, y=company_count_by_year.values)
plt.title('Company Count by Year')
plt.xlabel('Year')
plt.ylabel('Count')

plt.show()







# # Create a pie chart

# In[11]:


import pandas as pd
import matplotlib.pyplot as plt
# Load your 'unicorn_companies' dataset (replace 'your_data.csv' with the actual file path)
unicorn_companies = pd.read_csv( r'C:\Users\reles\OneDrive\Desktop\Quantam\week 4\Unicorn_Companies.csv')
# Assuming you have loaded your data into a DataFrame called 'data'

# Select the column for which you want to create a pie chart (e.g., 'Industry')
selected_column = 'Industry'

# Count the frequency of each category in the selected column
category_counts = unicorn_companies[selected_column].value_counts()

# Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=140)
plt.title(f'Distribution of Companies by {selected_column.capitalize()}')

plt.axis('equal')

plt.show()


# In[8]:


# Count the frequency of each category in the selected column
category_counts = unicorn_companies[selected_column].value_counts()

# Select the top 5 categories
top_5_categories = category_counts.head(5)

# Create a pie chart for the top 5 categories
plt.figure(figsize=(8, 8))
plt.pie(top_5_categories, labels=top_5_categories.index, autopct='%1.1f%%', startangle=140)
plt.title(f'Top 5 Industries by Company Count')

plt.axis('equal')  # Equal aspect ratio ensures that the pie chart is drawn as a circle.

plt.show()




# # 1. Which unicorn companies have had the biggest return on investment?

# In[53]:


import pandas as pd

# Assuming 'df' is your DataFrame
numeric_columns =unicorn_companies.select_dtypes(include=['number'])

# List of column names that are numeric
numeric_column_names = numeric_columns.columns.tolist()

# Print the numeric column names
print(numeric_column_names)






# In[55]:


unicorn_companies['Valuation'] = pd.to_numeric(unicorn_companies['Valuation'], errors='coerce')


# In[59]:


# Calculate ROI as (Valuation / Funding) and store it in a new 'ROI' column
unicorn_companies['ROI'] = unicorn_companies['Valuation'] / unicorn_companies['Funding']

# Sort the DataFrame by ROI in descending order and select the top 10
top_roi_companies = unicorn_companies.sort_values(by='ROI', ascending=False).head(10)

# Display the top 10 companies with the biggest ROI along with the selected columns
selected_columns = ['Company', 'Date Joined', 'Industry', 'City', 'Country', 'Funding', 'Select Investors', 'ROI']
print("\nTop 10 Companies with the Biggest ROI:")
print(top_roi_companies[selected_columns])


# In[61]:


import matplotlib.pyplot as plt

# Data for the top 10 companies with the biggest ROI
companies = ["Otto Bock HealthCare", "Zapier", "Dunamu", "Workhuman", "CFGI", "Manner", "DJI Innovations", "GalaxySpace", "Canva", "Il Makiage"]
roi_values = [float('inf'), 4000.0, 126.76, 111.11, 105.26, 100.0, 76.19, 71.43, 69.93, 68.97]

# Create a bar chart to visualize ROI for the top 10 companies
plt.figure(figsize=(12, 6))
plt.barh(companies, roi_values, color='skyblue')
plt.xlabel('ROI')
plt.ylabel('Company')
plt.title('Top 10 Companies with the Biggest ROI')
plt.gca().invert_yaxis()  # Invert the y-axis to display the highest ROI at the top

# Show the plot
plt.show()


# # 2. How long does it usually take for a company to become a unicorn? Has it always been this way?

# In[67]:


# Calculate the cumulative percentage of companies that became unicorns over the years
average_time_to_unicorn = unicorn_companies.groupby('Year Founded')['Company'].count().cumsum() / unicorn_companies['Company'].count()

# Create a plot to visualize the average time to become a unicorn
plt.figure(figsize=(8, 4))
plt.plot(average_time_to_unicorn.index, average_time_to_unicorn.values)
plt.title('Average Time to Become a Unicorn')
plt.xlabel('Year')
plt.ylabel('Cumulative Percentage')

# Show the plot
plt.show()


# # 3. Which countries have the most unicorns? Are there any cities that appear to be industry hubs?

# In[68]:


country_unicorn_count = unicorn_companies['Country'].value_counts().head(10)
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
sns.barplot(x=country_unicorn_count.values, y=country_unicorn_count.index)
plt.title('Countries with the Most Unicorns')
plt.xlabel('Count')
plt.ylabel('Country')


# # You can also analyze cities as industry hubs

# In[69]:


city_unicorn_count = unicorn_companies['City'].value_counts().head(10)
plt.subplot(2, 1, 2)
sns.barplot(x=city_unicorn_count.values, y=city_unicorn_count.index)
plt.title('Cities with the Most Unicorns')
plt.xlabel('Count')
plt.ylabel('City')


# # 4. Which investors have funded the most unicorns?

# In[71]:


top_investors = unicorn_companies['Select Investors'].value_counts().head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=top_investors.values, y=top_investors.index)
plt.title('Top Investors Funding the Most Unicorns')
plt.xlabel('Count')
plt.ylabel('Investor')

# Show the plots
plt.tight_layout()
plt.show()


# In[80]:


# Count the frequency of each category in the selected column
category_counts = unicorn_companies[selected_column].value_counts()

# Select the top 10 categories
top_10_categories = category_counts.head(10)

# Create a pie chart for the top 10 categories
plt.figure(figsize=(8, 8))
plt.pie(top_10_categories, labels=top_10_categories.index, autopct='%1.1f%%', startangle=140)
plt.title(f'Top 10 Industries by Company Count')

plt.axis('equal')  # Equal aspect ratio ensures that the pie chart is drawn as a circle.

plt.show()


# # Univariate Analysis # Explore individual features # Numerical Features

# In[75]:


plt.figure(figsize=(8, 6))
sns.scatterplot(data=data, x='Valuation', y='Funding')
plt.title('Scatter Plot: Valuation vs. Funding')
plt.xlabel('Valuation')
plt.ylabel('Funding')
plt.show()


# # Calculate correlation matrix

# In[76]:


# Categorical Features
categorical_features = ['Industry', 'Country']

# Plot bar plots for categorical features
plt.figure(figsize=(12, 5))
for i, feature in enumerate(categorical_features, 1):
    plt.subplot(1, len(categorical_features), i)
    sns.countplot(data=data, x=feature)
    plt.title(f'Frequency of {feature}')
    plt.xlabel(feature)
    plt.ylabel('Count')
    plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# ## Bivariate Analysis ## Explore relationships between pairs of variables

# In[78]:


# Numerical-Numerical Relationships
plt.figure(figsize=(8, 6))
sns.scatterplot(data=data, x='Valuation', y='Funding')
plt.title('Scatter Plot: Valuation vs. Funding')
plt.xlabel('Valuation')
plt.ylabel('Funding')
plt.show()


# # Calculate correlation matrix

# In[79]:


correlation_matrix = unicorn_companies[numerical_features].corr()

# Plot a heatmap of the correlation matrix
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')
plt.show()


# In[81]:


# Select the column for which you want to create a bar chart (e.g., 'City')
selected_column = 'City'

# Count the frequency of each category in the selected column
category_counts = unicorn_companies[selected_column].value_counts()

# Select the top 10 categories
top_10_categories = category_counts.head(10)

# Create a bar chart for the top 10 categories
plt.figure(figsize=(12, 6))  # Adjust the figure size if needed
top_10_categories.plot(kind='bar')
plt.title(f'Top 10 Cities by Company Count')
plt.xlabel('City')
plt.ylabel('Company Count')

plt.show()


# In[12]:


import pandas as pd
import matplotlib.pyplot as plt
# Load your 'unicorn_companies' dataset (replace 'your_data.csv' with the actual file path)
unicorn_companies = pd.read_csv( r'C:\Users\reles\OneDrive\Desktop\Quantam\week 4\Unicorn_Companies.csv')
# Assuming you have loaded your data into a DataFrame called 'data'

# Select the column for which you want to create a pie chart (e.g., 'Industry')
selected_column = 'Industry'

# Count the frequency of each category in the selected column
category_counts = unicorn_companies[selected_column].value_counts()

# Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=140)
plt.title(f'Distribution of Companies by {selected_column.capitalize()}')

plt.axis('equal')

plt.show()


# In[ ]:




