"""
Before you start, please install necessary libraries:
use the "pip install" command
"""

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# ========== PANDAS ==========

# Create a Series
s = pd.Series([1, 3, 5, 8, 10])
print("Series:\n", s)

# Create a DataFrame
data = {
    'Name': ['Eric', 'Cameron', 'Drew', 'James'],
    'Age': [18, 20, 20, 21],
    'Score': [85, 63, 77, 90]
}
df = pd.DataFrame(data)
print("\nDataFrame:\n", df)

# Access a column
print("\nAge column:\n", df['Age'])

# Filter rows where score > 80
print("\nRows where score > 80:\n", df[df['Score'] > 80])

# Basic statistics
print("\nDataFrame Description:\n", df.describe())

# Group by and aggregate
grouped = df.groupby('Age').sum()
print("\nGrouped by Age:\n", grouped)

# Sorting by Score
sorted_df = df.sort_values(by='Score', ascending=False)
print("\nSorted by Score:\n", sorted_df)

# DATA CLEANSING - THIS TAKES UP 90% OF THE TIME IN DATA SCIENCE!
# df.dropna() function -> drops all rows with missing values
# df.fillna() function -> fills in NA values with something
# df.drop_duplicates() function -> drops duplicate rows

# THIS IS KEY FOR THIS WEEK'S DATA CHALLENGE! If you had a CSV, you'd read it like:
# df_from_csv = pd.read_csv('path_to_file.csv')

# You can also read data from other types of files or sources
# df = pd.read_excel()
# df = pd.read_json()
# df = pd.read_clipboard()
# df = pd.read_html()
# df = pd.read_sql()
# print(df_from_csv)

# ========== MATPLOTLIB ==========

# Basic Line Chart
plt.plot(df['Age'], df['Score'])
plt.xlabel('Age')
plt.ylabel('Score')
plt.title('Score by Age')
plt.show()

# Scatter Plot
plt.scatter(df['Age'], df['Score'], color='red', marker='o')
plt.xlabel('Age')
plt.ylabel('Score')
plt.title('Score Distribution by Age')
plt.show()

# Bar Chart
plt.bar(df['Name'], df['Score'], color=['blue', 'green', 'yellow', 'red'])
plt.xlabel('Name')
plt.ylabel('Score')
plt.title('Scores of Names')
plt.show()

# ========== PROBLEMS - WORK THROUGH TOGETHER ==========

"""
1. Add another column 'Country' to the DataFrame with values ['US', 'CA', 'UK', 'AU']. Then, group the data by 'Country' and sum up the scores.
2. Filter the data to display only those whose names start with the letter 'A'.
3. Create a new DataFrame with columns 'Product' and 'Sales'. Generate a pie chart using Matplotlib.
4. Using the same 'Product and Sales' DataFrame, sort the data based on sales, and then generate a horizontal bar chart.
5. Combine the Age and Score columns from the original DataFrame into a single column called 'Info' in the format 'Age-Score'. (E.g., '25-85')
"""

# DATA CHALLENGE:
# Please download this data set:
# https://www.kaggle.com/datasets/maxhorowitz/nflplaybyplay2009to2016/

# Learn something cool about the NFL

# --- NFL Data Challenge Ideas ---
# THESE ARE JUST IDEAS, YOU CAN DO THESE OR YOU CAN DO SOMETHING ON YOUR OWN!
# THE WINNER WILL PROBABLY TAKE SOMETHING IN HERE A STEP FURTHER!
# PRESENT VISUALIZATIONS AT OUR NEXT MEETING! VOTE ON WINNER!

# Basic Exploration:
# 1. How many unique games are in the dataset?
# 2. Which quarterbacks have thrown the most passes?
# 3. On average, how many seconds remain in a game when a touchdown is scored?

# Time Analysis:
# 4. How are touchdowns distributed across different quarters?
# 5. What's the average score differential in the last 5 minutes of the 4th quarter?

# Play Analysis:
# 6. How often do teams attempt plays on 4th down?
# 7. In which field zone (left, center, or right) do most interceptions occur?

# Player Analysis:
# 8. Who are the top 5 players by total yards gained (combining rushing and passing)?
# 9. Which player has been involved in the most tackles for a loss?

# Team Analysis:
# 10. Which team, when playing at home, has the highest average score differential?
# 11. Which team has scored the most touchdowns overall?

# Game Situations:
# 12. In situations where there are less than 2 minutes left in the game and the score differential is 7 or less, how often do teams pass versus run?
# 13. Which team has used the most timeouts in the 4th quarter?

# Advanced Analysis:
# 14. Is there a correlation between 'air_yards' and 'yards_after_catch'?
# 15. What are the top 3 game dates with the most number of touchdowns?

# Field Goals and Kicks:
# 16. Which team has the highest success rate in field goals?
# 17. Which player has attempted the longest field goal?

# Penalties:
# 18. Which team has been penalized the most in terms of total yardage?
# 19. Which game had the highest number of penalties?

# Explore and Visualize:
# 20. Create a visualization of touchdowns over time (e.g., across different game dates or years).
# 21. Visualize the distribution of score differentials. Are most games close or are there a lot of blowouts?