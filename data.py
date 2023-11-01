# Download the files from the following link and save them in the Data folder
# https://twitter.com/i/communitynotes/download-data
# The files are named as follows: Notes data (1), Ratings data (1 & 2), Note status history data (1)

# From these files, make a new data frame with the nessary columns for training the Rater model.

# Make a function that uses pandas to import the files in the the Data folder
# and returns a data frame with the necessary columns for training the model.

import pandas as pd
import os
import requests


notes_file_path = './Data/notes-00000.tsv'
ratings_1_file_path = './Data/ratings-00000.tsv'
ratings_2_file_path = './Data/ratings-00000.tsv'
note_status_history_file_path = './Data/noteStatusHistory-00000.tsv'
user_enrollment_file_path = './Data/userEnrollment-00000.tsv'



def import_and_combine_data_Rater_Model(necessary_columns):

    notes_df = pd.read_csv(notes_file_path, sep='\t', usecols=necessary_columns)

def download_datasets_into_data_folder():
    links = [
    'https://ton.twimg.com/birdwatch-public-data/2023/11/01/notes/notes-00000.tsv',
    'https://ton.twimg.com/birdwatch-public-data/2023/11/01/noteRatings/ratings-00001.tsv',
    'https://ton.twimg.com/birdwatch-public-data/2023/11/01/noteRatings/ratings-00000.tsv',
    'https://ton.twimg.com/birdwatch-public-data/2023/11/01/noteStatusHistory/noteStatusHistory-00000.tsv',
    'https://ton.twimg.com/birdwatch-public-data/2023/11/01/userEnrollment/userEnrollment-00000.tsv'
    ]
    data_directory = 'Data'
    # Create the directory if it doesn't exist
    if not os.path.exists(data_directory):
        os.makedirs(data_directory)

    # Nested function to download and save a file
    def download_file(url, folder):
        local_filename = url.split('/')[-1]
        local_filepath = os.path.join(folder, local_filename)

        # Stream the download (for large files)
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(local_filepath, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)

        return local_filepath

    # Download each file
    for link in links:
        try:
            filepath = download_file(link, data_directory)
            print(f"Downloaded {link} to {filepath}")
        except requests.exceptions.HTTPError as err:
            print(f"Failed to download {link}: {err}")




# notes_df = pd.read_csv(notes_file_path, sep='\t', usecols=['noteId', 'tweetId', 'summary'])
# note_status_df = pd.read_csv(note_status_history_file_path, sep='\t', usecols=['noteId', 'currentStatus'])

# result = pd.merge(notes_df[['noteId', 'tweetId', 'summary']], note_status_df[['noteId', 'currentStatus']], on='noteId')

# print(result.head())
# print(result.columns)
# print(result.shape)
# print(result.iloc[1])

# Use twitter API to get the tweet text from the tweetId column