# Directions:
* Pass a list in the Sentiment_Analyzer.py file, be sure to indicate the timeframe by changing the N value
* Run financials.py file to gather the lastest data from the DJI, SPX, and NDX
* Pass the resulting CSV files from Sentiment_Analyzer.py as a list into the merger.py file, which will join the finanicial data and sentiment analysis data and produce new csv files.
* Pass the merger.py files into the plotter.py to plot.  You need to change the c value in the ax.scatter parameters to either vader or textblob depending on what sentiment to plot.

## Stock Price Movement vs. Social Media Sentiment (Twitter)

## Project Description/Outline:
*Use financial data of 10 stocks from 10 different sectors to track the relationship between Social Media volume/sentiment and stock price movement five days prior to Social Media news volume

## Research Questions to Answer
* Patterns in stock price movement (up or down) relative to social media posts, particularly Twitter sentiment and volume
* Does tweet volume change when there are large price movements?
* Is there a relationship between sentiment and price change direction?

## Data sources or Data Sets to be Used /APIs to be consumed (if any):	
* Alpha Advantage API
* FINRA API
* Twitter
* News API - Wall Street Journal, NY Times, Google News
* VADER library 
* Google trends
