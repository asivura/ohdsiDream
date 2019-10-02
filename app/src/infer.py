import os
import pandas as pd

if __name__ == '__main__':

    # Making sure all input files are in the infer directory
    infer_file_names = [f for f in os.listdir('/infer')]
    for file_name in ['observation_period.csv', 'drug_exposure.csv', 'measurement.csv', \
                      'condition_occurrence.csv', 'visit_occurrence.csv', 'person.csv', 'observation.csv', \
                      'procedure_occurrence.csv']:
        assert file_name in infer_file_names, file_name

    # Reading csv file with persons
    person_df = pd.read_csv('/infer/person.csv')
    print("Person count: ", person_df.shape[0])

    # Reading a file in the "/model" directory to make sure we have the same content there we created on the "train" step
    with open('/model/model.txt', 'r') as f:
        text = f.read() 
        assert text == 'model'  

    # Reading a file in the "/scratch" directory to make sure we have the same content there we created on the "train" step
    with open('/scratch/scratch.txt', 'r') as f:
        text = f.read() 
        assert text == 'scratch' 

    # Creating file with dummy predictions
    prediction_df = person_df[['person_id']].copy()
    prediction_df['score'] = 0.5
    prediction_df.to_csv('/output/predictions.csv', index=False)