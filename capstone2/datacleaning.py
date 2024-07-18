import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

url = '/content/Mental health Depression disorder Data.csv'
# let us read and create data frame
mentalhealth = pd.read_csv(url)

mentalhealth.drop(["Code"], axis = 1, inplace = True)

# Convert the 'Year' column to numeric, coercing errors to NaN and then dropping those rows
mentalhealth['Year'] = pd.to_numeric(mentalhealth['Year'], errors='coerce')
mentalhealth = mentalhealth.dropna(subset=['Year'])

# Convert the 'Year' column to integer
mentalhealth['Year'] = mentalhealth['Year'].astype(int)

# Filter out rows where the 'Year' column is between 1800 and 1989
# mentalhealth_filtered_year = mentalhealth[~mentalhealth['Year'].between(1800, 1989)]
mentalhealth_filtered_year = mentalhealth[~mentalhealth['Year'].between(0, 1989)]
mentalhealth_filtered_year = mentalhealth_filtered_year[~mentalhealth_filtered_year['Year'].between(2018, 2019)]

# List of countries/entities to remove
countries_to_remove = [
    "Africa", "Anguilla", "Aruba", "Asia", "American Samoa", "Andean Latin America",
    "Andorra", "Antigua and Barbuda", "Barbados", "Belize", "Bonaire Sint Eustatius and Saba",
    "British Virgin Islands", "Burkina Faso", "Burundi", "Cayman Islands" ,"Cape Verde", "Chad",
    "Channel Islands", "Cook Islands", "Cote d'Ivoire", "Curacao", "Democratic Republic of Congo",
    "Djibouti", "El Salvador", "Eritrea", "Estonia", "Faeroe Islands", "Falkland Islands",
    "French Guiana", "French Polynesia", "Gabon", "Gambia", "Guadeloupe", "Guam",
    "Guatemala", "Guinea-Bissau", "Guyana", "Honduras", "Isle of Man", "Kiribati",
    "Latvia", "Lesotho", "Liechtenstein", "Marshall Islands", "Martinique", "Mayotte",
    "Micronesia (country)", "Moldova", "Montenegro", "Nauru", "New Caledonia",
    "Nicaragua", "Niger", "Niue", "Palau", "Puerto Rico", "Rwanda", "Saint Barthlemy",
    "Saint Helena", "Saint Kitts and Nevis", "Saint Lucia", "Saint Martin (French part)",
    "Saint Pierre and Miquelon", "Saint Vincent and the Grenadines", "Sao Tome and Principe",
    "Sierra Leone", "Sint Maarten (Dutch part)", "Swaziland", "Timor", "Togo",
    "United States Virgin Islands", "Vanuatu", "Europe", "Gibraltar", "Hong Kong", "Latin America", "Macao",
    "Monaco", "Montserrat", "Reunion", "San Marino", "Tokelau", "Turks and Caicos Islands", "Tuvalu",
    "Vatican", "Wallis and Futuna", "Western Sahara"
]


# Remove the specified countries/entities
mentalhealth_filtered_country = mentalhealth_filtered_year[~mentalhealth_filtered_year["Entity"].isin(countries_to_remove)]

# Split the DataFrame: Split the DataFrame into few set
mentalhealth_1 = mentalhealth_filtered_country.iloc[:5264]
mentalhealth_2 = mentalhealth_filtered_country.iloc[5264:]

# Reset Index: Reset the index of the second DataFrame so it starts from 0.
mentalhealth_1.reset_index(drop=True, inplace=True)
mentalhealth_2.reset_index(drop=True, inplace=True)

# Concatenate the DataFrames horizontally
mentalhealth_new1 = pd.concat([mentalhealth_1, mentalhealth_2], axis=1)

# Split the DataFrame: Split the DataFrame into few set
mentalhealth_1 = mentalhealth_new1.iloc[:5264]
mentalhealth_2 = mentalhealth_new1.iloc[5264:]

# Reset Index: Reset the index of the second DataFrame so it starts from 0.
mentalhealth_1.reset_index(drop=True, inplace=True)
mentalhealth_2.reset_index(drop=True, inplace=True)

# Concatenate the DataFrames horizontally
mentalhealth_new2 = pd.concat([mentalhealth_1, mentalhealth_2], axis=1)

# Split the DataFrame: Split the DataFrame into few set
mentalhealth_1 = mentalhealth_new2.iloc[:5264]
mentalhealth_2 = mentalhealth_new2.iloc[5264:]

# Reset Index: Reset the index of the second DataFrame so it starts from 0.
mentalhealth_1.reset_index(drop=True, inplace=True)
mentalhealth_2.reset_index(drop=True, inplace=True)

# Concatenate the DataFrames horizontally
mentalhealth_new3 = pd.concat([mentalhealth_1, mentalhealth_2], axis=1)

mentalhealth_new3['Eating disorders (%)'] = mentalhealth_new3['Eating disorders (%)'].fillna(0)

# remove null column
mentalhealth_new3.dropna(axis=1, how='any', inplace=True)

new_column_names = ['Index', 'Country', 'Year', 'Schizophrenia (%)', 'Bipolar disorder (%)', 'Eating disorders (%)',
                    'Anxiety disorders (%)', 'Drug use disorders (%)', 'Depression (%)', 'Alcohol use disorders (%)',
                    'index1', 'Country1', 'Year1', 'Prevalence in males (%)', 'Prevalence in females (%)', 'Population',
                    'xn', 'Index2', 'Country2', 'Year2', 'Suicide rate (deaths per 100,000 individuals)',
                    'Depressive disorder rates (number suffering per 100,000)', 'Population1', 'xn1', 'xn2', 'xn3',
                    'Index3', 'Country3', 'Year3', 'Prevalence - Depressive disorders - Sex: Both - Age: All Ages (Number) (people suffering from depression)',
                    'xn4']

mentalhealth_new3.columns = new_column_names


columns_to_drop = ['index1', 'Country1', 'Year1','xn', 'Index2', 'Country2', 'Year2','Population1', 'xn1', 'xn2', 'xn3','Index3', 'Country3', 'Year3', 'xn4']
mentalhealth_new = mentalhealth_new3.drop(columns=columns_to_drop)

# Save the combined DataFrame to a new CSV file
mentalhealth_new.to_csv("mentalhealth_new.csv", index=False)

# Download the combined CSV file
#from google.colab import files
files.download("mentalhealth_new.csv")