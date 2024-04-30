import pandas as pd
import descriptive_statistics
import text_analysis
import time_series_analysis
import publisher_analysis

def main():
    try:
        # Load the dataset
        df = pd.read_csv('data/raw_analyst_ratings.csv')

        # Perform exploratory data analysis
        descriptive_statistics.analyze_headline_lengths(df)
        descriptive_statistics.count_articles_per_publisher(df)
        descriptive_statistics.analyze_publication_dates(df)
        
        text_analysis.perform_sentiment_analysis(df)
        text_analysis.identify_common_keywords(df)

        time_series_analysis.analyze_publication_frequency(df)
        time_series_analysis.analyze_publishing_times(df)
        
        publisher_analysis.analyze_publisher_contribution(df)
        
    except FileNotFoundError:
        print("Error: The dataset file 'raw_analyst_ratings.csv' was not found.")
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    main()