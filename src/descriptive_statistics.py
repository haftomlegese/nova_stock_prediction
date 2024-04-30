import pandas as pd
import matplotlib.pyplot as plt

def analyze_headline_lengths(df):
    # Obtain basic statistics for headline lengths
    df['headline_length'] = df['headline'].apply(len)
    headline_stats = df['headline_length'].describe()
    print("Descriptive Statistics for Headline Lengths:")
    print(headline_stats)

def count_articles_per_publisher(df):
    # Count the number of articles per publisher
    publisher_counts = df['publisher'].value_counts()
    print("\nNumber of Articles per Publisher:")
    print(publisher_counts.head(10))  # Display top 10 most active publishers

def analyze_publication_dates(df):
    try:
        # Attempt to convert 'date' column to datetime format
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
        
        # Analyze publication frequency over time
        publication_frequency = df.groupby(df['date'].dt.date).size()

        # Plot publication frequency over time
        plt.plot(publication_frequency.index, publication_frequency.values)
        plt.xlabel('Date')
        plt.ylabel('Number of Articles')
        plt.title('Publication Frequency Over Time')
        plt.show()
        
    except KeyError:
        print("Error: 'date' column not found in the DataFrame.")
    except ValueError:
        print("Error: Unable to convert 'date' column to datetime format.")
    except Exception as e:
        print("An error occurred:", str(e))