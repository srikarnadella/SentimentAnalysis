from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
import nltk
import datetime as dt

url = "https://finviz.com/quote.ashx?t="

tickers = ["TSLA", "AMZN", "META", "AMD", "NVDA"]
news_dict = {}

for ticker in tickers:
    modurl = url + ticker
    req = Request(url=modurl, headers={'user-agent': 'my-app'})
    response = urlopen(req)
    html = BeautifulSoup(response, 'html.parser')  # Use 'html.parser' as the parser
    news_table = html.find(id='news-table')
    
    if news_table:
        news_dict[ticker] = news_table
    else:
        print(f"No news table found for {ticker}")

retrievedData = []
for ticker, news_table in news_dict.items():
    data_rows = news_dict[ticker].findAll('tr')

    for index, row in enumerate(data_rows):
        a_tag = row.find('a')
        if a_tag:
            title = a_tag.text
            timestamp = row.td.text.strip().split(' ')
            date = 'ooga'
            time = 'booga'
            
            # Check if timestamp is empty or has unexpected format
            if len(timestamp) > 1:
                date = timestamp[0]
                time = timestamp[1]
                
                # Parse different date formats
                try:
                    if date.lower() == 'today':
                        date = dt.datetime.now().strftime('%Y-%m-%d')
                    elif date.lower() == 'yesterday':
                        date = (dt.datetime.now() - dt.timedelta(1)).strftime('%Y-%m-%d')
                    else:
                        date = dt.datetime.strptime(date, '%b-%d-%y').strftime('%Y-%m-%d')
                except ValueError as e:
                    print(f"Error parsing date '{date}': {str(e)}")
                    # Handle the error, for example, by setting a default date
                    date = dt.datetime.now().strftime('%Y-%m-%d')  # Default to current date
                
                retrievedData.append([ticker, date, time, title])
            else:
                print(f"Empty or invalid timestamp format: {timestamp}")
        else:
            print(f"No <a> tag found in row {index}")

df = pd.DataFrame(retrievedData, columns=["ticker", 'date', 'time', 'title'])
vader = SentimentIntensityAnalyzer()

# Calculate sentiment compound score for each title
f = lambda title: vader.polarity_scores(title)['compound']
df['compound'] = df['title'].apply(f)

# Convert 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'], errors='coerce').dt.date

# Group by 'date' and 'ticker', calculate mean of 'compound' scores
meandf = df.groupby(['date', 'ticker'])['compound'].mean().unstack()

# Plotting the bar chart
fig, ax = plt.subplots(figsize=(14, 8))

meandf.plot(kind='bar', ax=ax)

plt.title('Sentiment Analysis of Stock News')
plt.xlabel('Date')
plt.ylabel('Average Sentiment (Compound Score)')
plt.legend(title='Ticker')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
