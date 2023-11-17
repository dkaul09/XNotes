import pandas as pd
from sklearn.metrics import accuracy_score


ratings_1_file_path = './Data/ratings-00000.tsv'
ratings_2_file_path = './Data/ratings-00000.tsv'
note_status_history_file_path = './Data/noteStatusHistory-00000.tsv'

def rater_model_performance(api):
    
    print("To be completed. does not need a specific training set, as this is for models with no finetuning.")

def rater_model_performance(api, dataset):
    true_labels = []
    predicted_labels = []
     
    for instance in dataset:
     tweet = instance['tweet']
     note = instance['note']
     true_label = instance['currentStatus'] 
     prediction = api.predict(tweet, note)
     true_labels.append(true_label)
     predicted_labels.append(prediction)

    
    accuracy = accuracy_score(true_labels, predicted_labels)
    print(f"Accuracy: {accuracy:.2f}")



def human_rater_performance():
    rating_1_df = pd.read_csv(ratings_1_file_path, sep='\t', usecols=['noteId', 'helpfulnessLevel'])
    rating_2_df = pd.read_csv(ratings_2_file_path, sep='\t', usecols=['noteId', 'helpfulnessLevel'])
    note_status_df = pd.read_csv(note_status_history_file_path, sep='\t', usecols=['noteId', 'currentStatus'])

    # Map note id to the current status. 0 if not helpful, 1 if helpful
    note_id_to_status = {}
    for i, row in note_status_df.iterrows():
        if row['currentStatus'] == 'CURRENTLY_RATED_NOT_HELPFUL':
            note_id_to_status[row['noteId']] = 0
        elif row['currentStatus'] == 'CURRENTLY_RATED_HELPFUL':
            note_id_to_status[row['noteId']] = 1
    
    print(note_id_to_status)


    # iterate through all user ratings. if they have a note in the map see if its wrong or right
    tp = 0
    fp = 0
    tn = 0
    fn = 0
    for i, row in rating_1_df.iterrows():
        if row['noteId'] in note_id_to_status:
            is_currently_helpful = note_id_to_status[row['noteId']]
            if is_currently_helpful:
                if row['helpfulnessLevel'] == 'HELPFUL':
                    tp += 1
                else:
                    fn += 1
            else:
                if row['helpfulnessLevel'] == 'HELPFUL':
                    fp += 1
                else:
                    tn += 1
    print(tp, fp, tn, fn)

    accuracy = (tp + tn) / (tp + tn + fp + fn)
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    specificity = tn / (tn + fp)
    f1 = 2 * precision * recall / (precision + recall)

    return {'Accuracy': accuracy, 'Precision': precision, 'Recall': recall, 'Specificity': specificity, 'F1': f1}



    

print(human_rater_performance())
