from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

def perform_sentiment_analysis(df):
    try:
        # Perform sentiment analysis on headlines using VADER
        analyzer = SentimentIntensityAnalyzer()
        df['sentiment'] = df['headline'].apply(lambda x: analyzer.polarity_scores(x)['compound'])
    except Exception as e:
        print("Error occurred during sentiment analysis:", str(e))

def identify_common_keywords(df):
    try:
        # Tokenize and remove stop words
        vectorizer = CountVectorizer(stop_words='english', lowercase=True)
        X = vectorizer.fit_transform(df['headline'])

        # Apply Latent Dirichlet Allocation for topic modeling
        lda = LatentDirichletAllocation(n_components=5, random_state=42)
        lda.fit(X)

        # Get the most common keywords for each topic
        feature_names = vectorizer.get_feature_names_out()
        keywords_per_topic = []
        for topic_idx, topic in enumerate(lda.components_):
            top_keywords_idx = topic.argsort()[:-10 - 1:-1]  # Top 10 keywords
            keywords_per_topic.append([feature_names[i] for i in top_keywords_idx])

        # Print common keywords for each topic
        print("Common Keywords for Each Topic:")
        for idx, keywords in enumerate(keywords_per_topic):
            print(f"Topic {idx+1}: {', '.join(keywords)}")
    except Exception as e:
        print("Error occurred during keyword identification:", str(e))