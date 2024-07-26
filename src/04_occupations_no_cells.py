
# # Occupations Introduction
# 
# For this part of the HW, we will practice Pandas using a practice dataset regarding the occupations, location, age, and gender of users of an app.
# 
# ### Two points for each section

# Run the cell below to add section numbering

# ## Import the necessary libraries
import pandas as pd
import numpy as np

# ## Import the dataset
# 
# Import the dataset from here: https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user
# 
# Assign it to a variable called `users` and use the `user_id` as index. (Hint: Use `pd.read_csv(url, sep='|')`)
url = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user"
df = pd.read_csv(url, sep='|')
df
print(df.info())
# ## Print the first 25 entries
# 
# Use `head` to do this.



# ## View the last 10 entries
# 
# Use `tail`



# ## What is the number of observations in the dataset?



# ## What is the number of columns in the dataset?



# ## Print the name of all the columns.



# ## How is the dataset indexed?
# 
# Print the DataFrame index and describe it.



# ## What is the data type of each column?



# ## Print only the occupation column
# 
# Show two ways to do this.



# ## How many unique occupations there are in this dataset?



# ## What are the 5 most common occupations in this dataset?



# ## Summarize the DataFrame.
# 
# Use a single function (method) to describe the data (to show the mean, standard deviation, various quintiles, etc). This method should only work on one of the columns by default, but can be called on the whole dataset (a method of the DataFrame).



# ## Summarize all the columns
# 
# Run `users.describe(include = "all")` and see how it compares to what we did before.



# ## Run `describe` only on the `occupation` column



# ## What is the mean age of users?



# ## What is the age with fewest occurrences?




