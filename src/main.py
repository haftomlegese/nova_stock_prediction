import pandas as pd
import descriptive_statistics

def main():
    try:
        # Load the dataset
        df = pd.read_csv('data/raw_analyst_ratings.csv')

        # Perform exploratory data analysis
        descriptive_statistics.analyze_headline_lengths(df)
        descriptive_statistics.count_articles_per_publisher(df)
        descriptive_statistics.analyze_publication_dates(df)
        

    except FileNotFoundError:
        print("Error: The dataset file 'raw_analyst_ratings.csv' was not found.")
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    main()