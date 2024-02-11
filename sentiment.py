import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

# Set the title
st.title("SkySense")
st.sidebar.title("SkySense")
st.markdown("Analyzing the sentiment of tweets about the US airlines.")
st.sidebar.markdown("Analyzing the sentiment of tweets about the US airlines.")


@st.cache_data(persist=True)
def load_data():
    data = pd.read_csv("Tweets.csv")
    data['tweet_created'] = pd.to_datetime(data['tweet_created'])
    return data


data = load_data()

# display tweets in sidebar with radio button of choice
st.sidebar.subheader("Show random tweets")
random_tweet = st.sidebar.radio(
    'Sentiment', ('positive', 'neutral', 'negative'))
st.sidebar.markdown(data.query(
    'airline_sentiment == @random_tweet')[["text"]].sample(n=1).iat[0, 0])

# plot interactive bar chart and pie chart
st.sidebar.subheader("Number of tweets by sentiment")
select = st.sidebar.selectbox(
    'Visualization type', ['Histogram', 'Pie chart'], key='1')
sentiment_count = data['airline_sentiment'].value_counts()
sentiment_count = pd.DataFrame(
    {'Sentiment': sentiment_count.index, 'Tweets': sentiment_count.values})
if not st.sidebar.checkbox("Hide", True):
    st.markdown("### Number of tweets by sentiment")
    if select == 'Histogram':
        fig = px.bar(sentiment_count, x='Sentiment', y='Tweets',
                     color='Tweets', height=500)
        st.plotly_chart(fig)
    else:
        fig = px.pie(sentiment_count, values='Tweets', names='Sentiment')
        st.plotly_chart(fig)

# plotting the number of tweets by sentiment for each airline
st.sidebar.subheader("Total number of tweets by sentiment for each airline")
airline = st.sidebar.multiselect(
    "Pick airlines", ('US Airways', 'United', 'American', 'Southwest', 'Delta', 'Virgin America'), key='0')
if len(airline) > 0:
    data = data[data.airline.isin(airline)]
    fig_2 = px.histogram(data, x='airline', y='airline_sentiment', histfunc='count',
                         color='airline_sentiment', facet_col='airline_sentiment', labels={'airline_sentiment': 'tweets'}, height=600, width=800)
    st.plotly_chart(fig_2)


# plotting word cloud
st.sidebar.subheader("Word Cloud")
word_sentiment = st.sidebar.radio(
    'Display word cloud for what sentiment?', ('positive', 'neutral', 'negative'))
if not st.sidebar.checkbox("Close", True, key='3'):
    st.subheader("Word cloud for %s sentiment" % (word_sentiment))
    df = data[data['airline_sentiment'] == word_sentiment]
    words = ' '.join(df['text'])
    processed_words = ' '.join([word for word in words.split(
    ) if 'http' not in word and not word.startswith('@') and word != 'RT'])
    wordcloud = WordCloud(stopwords=STOPWORDS, background_color='white',
                          width=800, height=640).generate(processed_words)
    plt.imshow(wordcloud)
    plt.xticks([])
    plt.yticks([])
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()

# Display sentiment analysis statistics
st.subheader("Sentiment Analysis Statistics")
st.write("Total Tweets:", len(data))
st.write("Positive Tweets:", len(
    data[data['airline_sentiment'] == 'positive']))
st.write("Neutral Tweets:", len(data[data['airline_sentiment'] == 'neutral']))
st.write("Negative Tweets:", len(
    data[data['airline_sentiment'] == 'negative']))

# Interactive scatter plot
st.sidebar.subheader("Interactive Scatter Plot")
x_feature = st.sidebar.selectbox(
    "X-axis feature", data.select_dtypes(include=np.number).columns, key='x_feature')
y_feature = st.sidebar.selectbox(
    "Y-axis feature", data.select_dtypes(include=np.number).columns, key='y_feature')
if not st.sidebar.checkbox("Hide", True, key='scatter_checkbox'):
    st.markdown("### Interactive Scatter Plot")
    fig_scatter = px.scatter(
        data, x=x_feature, y=y_feature, color='airline_sentiment')
    st.plotly_chart(fig_scatter)
