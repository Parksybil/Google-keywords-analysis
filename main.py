from pytrends.request import TrendReq
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, timedelta

# Set up pytrends
pytrends = TrendReq(hl='vi', tz=420)

# Prompt for keyword and timeframe
keyword = input("Enter the keyword: ")
days = int(input("Enter the number of days: "))

# Calculate the start and end dates
end_date = datetime.now()
start_date = end_date - timedelta(days=days)

# Format the dates
end_date = end_date.strftime('%Y-%m-%d')
start_date = start_date.strftime('%Y-%m-%d')

# Define the keyword list
kw_list = [keyword]

# Build the payload
pytrends.build_payload(kw_list, timeframe=f'{start_date} {end_date}', geo='VN')

# Fetch the interest over time
interest_over_time_df = pytrends.interest_over_time()

# Plot the data
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(interest_over_time_df.index, interest_over_time_df[keyword])
plt.title(f'Google Trends: {keyword}')

# Get related queries
related_queries = pytrends.related_queries()

# Plot related queries
ax = plt.subplot(1, 2, 2)
related_queries[keyword]['top']['value'].plot(kind='barh', ax=ax)
ax.invert_yaxis()
plt.title('Related queries')
plt.yticks(range(len(related_queries[keyword]['top'])), related_queries[keyword]['top']['query'])

plt.tight_layout()
plt.show()
