import pandas as pd
import nltk
import re

nltk.download('punkt')


def preprocess_tweets(csv_files):
    # Create an empty DataFrame to store the preprocessed data
    preprocessed_data = pd.DataFrame()

    for csv_file in csv_files:
        # Load one CSV file into a pandas DataFrame
        df = pd.read_csv(csv_file)
        df = df[~df['content'].str.contains('http|pic.twitter.com')]

        # Remove unnecessary columns and rename the 'content' column to 'tweet'
        df = df[['content']]
        df = df.rename(columns={'content': 'tweet'})

        # Remove non-alphanumeric characters using regex
        df['tweet'] = df['tweet'].apply(lambda x: re.sub(r'[^a-zA-Z0-9\s]', '', x))

        # Tokenize the text using NLTK
        df['tweet'] = df['tweet'].apply(nltk.word_tokenize)

        # Join the tokens back into sentences
        df['tweet'] = df['tweet'].apply(lambda x: ' '.join(x))

        # Concatenate the preprocessed DataFrame to the preprocessed_data DataFrame
        preprocessed_data = pd.concat([preprocessed_data, df], ignore_index=True)
        '''
            # Append the preprocessed DataFrame to the preprocessed_data DataFrame
            preprocessed_data = preprocessed_data.append(df, ignore_index=True)
        '''
        return preprocessed_data
