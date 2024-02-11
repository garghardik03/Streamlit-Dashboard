# SkySense - Analyzing Sentiment of Tweets about US Airlines

SkySense is a Streamlit application for analyzing the sentiment of tweets about US airlines. It provides interactive visualizations of tweet sentiment distribution, sentiment analysis by airline, and word clouds for different sentiment categories.

## How to Run the Application

1. Clone this repository to your local machine.
2. Install the required Python packages listed in `requirements.txt` by running:
   ```
   pip install -r requirements.txt
   ```
3. Ensure you have the `Tweets.csv` file containing the tweet data in the project directory.
4. Run the Streamlit application using the following command:
   ```
   streamlit run app.py
   ```


## Functionality Overview

### Random Tweets Display

- Use the sidebar radio button to select a sentiment category (positive, neutral, negative).
- View a random tweet belonging to the selected sentiment category.

### Number of Tweets by Sentiment

- Choose between a histogram or pie chart visualization of the tweet distribution by sentiment category.
- Toggle the visibility of this section using the "Hide" checkbox.

### Total Number of Tweets by Sentiment for Each Airline

- Select one or more airlines from the multiselect dropdown to filter the tweet data.
- Visualize the distribution of tweet sentiment for each selected airline using a facetted histogram.
- Toggle the visibility of this section using the "Hide" checkbox.

### Word Cloud

- Choose the sentiment category (positive, neutral, negative) for which you want to display the word cloud.
- View the word cloud visualization representing the most frequent words in tweets of the selected sentiment category.
- Toggle the visibility of this section using the "Close" checkbox.