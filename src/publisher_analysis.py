import pandas as pd

def analyze_publisher_contribution(df):
    try:
        # Analyze publisher contribution
        if 'publisher' not in df.columns:
            raise KeyError("Error: 'publisher' column not found in the DataFrame.")

        publisher_counts = df['publisher'].value_counts()
        print("\nPublisher Contribution Analysis:")
        print(publisher_counts.head(10))  # Display top 10 most active publishers

        # If email addresses are used as publisher names, identify unique domains
        if '@' in publisher_counts.index[0]:
            unique_domains = [email.split('@')[-1] for email in publisher_counts.index]
            domain_counts = pd.Series(unique_domains).value_counts()
            print("\nUnique Domains Analysis:")
            print(domain_counts.head(10))  # Display top 10 unique domains
    except KeyError as e:
        print(e)
    except Exception as e:
        print("An error occurred during publisher contribution analysis:", str(e))