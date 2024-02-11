### SkySense - Analyzing Sentiment of Tweets about US Airlines

SkySense is a Streamlit application for analyzing the sentiment of tweets about US airlines. It provides interactive visualizations of tweet sentiment distribution, sentiment analysis by airline, and word clouds for different sentiment categories. Additionally, it displays sentiment analysis statistics and an interactive scatter plot for exploring the relationship between numerical features.

#### How to Run the Application

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

#### Functionality Overview

1. **Random Tweets Display**: Displays a random tweet based on selected sentiment (positive, neutral, negative).
2. **Number of Tweets by Sentiment**: Provides visualizations (histogram or pie chart) of tweet distribution by sentiment category.
3. **Total Number of Tweets by Sentiment for Each Airline**: Shows the distribution of tweet sentiment for selected airlines.
4. **Word Cloud**: Generates a word cloud visualization representing the most frequent words in tweets of the selected sentiment category.
5. **Sentiment Analysis Statistics**: Displays statistics about the sentiment analysis results, including the total number of tweets and counts for each sentiment category.
6. **Interactive Scatter Plot**: Allows users to explore the relationship between two numerical features with a scatter plot.
