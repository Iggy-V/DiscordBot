import pandas as pd
import random

# Load the CSV file
def load_csv(filepath):
    return pd.read_csv(filepath)

# Save the CSV file
def save_csv(df, filepath):
    df.to_csv(filepath, index=False)

# Select a random easy problem that hasn't been used
def select_random_problem(df):
    # Filter for unused and easy problems
    available_problems = df[(df['Difficulty'] == 'Easy') & (df['Used'].isna())]
    if available_problems.empty:
        return None, None
    random_problem = available_problems.sample()
    return random_problem.index[0], random_problem

# Generate the link and mark as used
def generate_link_and_update(df, index, problem):
    if problem is None:
        return None
    title = problem['Title'].values[0].lower().replace(' ', '-')
    link = f"https://leetcode.com/problems/{title}/"
    # Mark as used
    df.at[index, 'Used'] = 'Yes'
    return link

def LeetCodeRandom():
    filepath = r"C:\Users\ignas\OneDrive\Desktop\Coding\Python Projects\DiscordBot\all-leetcode-questions.csv"  # Modify with the actual path to your CSV file
    df = load_csv(filepath)

    # Ensure there's a 'Used' column
    if 'Used' not in df.columns:
        df['Used'] = pd.NA

    index, problem = select_random_problem(df)
    link = generate_link_and_update(df, index, problem)
    
    save_csv(df, filepath)
    
    if link:
        answer = f"LeetCode link: {link}"
    else:
        answer = "No more unused easy problems available."
    
    return answer

