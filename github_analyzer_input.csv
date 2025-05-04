import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('district_scores.csv')

# Preview the data
print(df.head())

# Example: Sort by highest average commits
top_commits = df.sort_values(by='avg_commits', ascending=False)

# Plot it
plt.figure(figsize=(10, 6))
plt.bar(top_commits['district'], top_commits['avg_commits'], color='purple')
plt.title('Average Commits per User by District')
plt.xlabel('District')
plt.ylabel('Average Commits')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
