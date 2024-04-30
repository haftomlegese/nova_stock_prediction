import pandas as pd
import matplotlib.pyplot as plt

def analyze_publication_frequency(df):
    try:
        # Analyze publication frequency over time
        df['date'] = pd.to_datetime(df['date'])
        publication_frequency = df.groupby(df['date'].dt.date).size()

        # Plot publication frequency over time
        plt.plot(publication_frequency.index, publication_frequency.values)
        plt.xlabel('Date')
        plt.ylabel('Number of Articles')
        plt.title('Publication Frequency Over Time')
        plt.show()
    except KeyError:
        print("Error: 'date' column not found in the DataFrame.")
    except Exception as e:
        print("An error occurred during publication frequency analysis:", str(e))

def analyze_publishing_times(df):
    try:
        # Analyze publishing times
        df['date'] = pd.to_datetime(df['date'])
        df['hour'] = df['date'].dt.hour

        # Count the number of articles published at each hour
        publishing_times = df.groupby('hour').size()

        # Plot publishing times
        plt.bar(publishing_times.index, publishing_times.values)
        plt.xlabel('Hour of the Day')
        plt.ylabel('Number of Articles')
        plt.title('Publishing Times')
        plt.show()
    except KeyError:
        print("Error: 'date' column not found in the DataFrame.")
    except Exception as e:
        print("An error occurred during publishing times analysis:", str(e))
