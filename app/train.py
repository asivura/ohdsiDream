import os
import pandas as pd

def remove_files(dir_name):
    filelist = [f for f in os.listdir(dir_name)]
    for f in filelist:
        os.remove(os.path.join(dir_name, f))

if __name__ == '__main__':
    
    # Removing all content from model and scratch directories
    # That's important for local run to make sure directories we mount to docker container are empty
    # We can have there files from previous local run
    remove_files(dir_name='/model')
    remove_files(dir_name='/scratch')

    # Making sure all input files are in the train directory
    training_file_names = [f for f in os.listdir('/train')]
    for file_name in ['observation_period.csv', 'drug_exposure.csv', 'death.csv', 'measurement.csv', \
                      'condition_occurrence.csv', 'visit_occurrence.csv', 'person.csv', 'observation.csv', \
                      'procedure_occurrence.csv']:
        assert file_name in training_file_names

    # Reading csv file with persons
    person_df = pd.read_csv('/train/person.csv')
    print("Person count: ", person_df.shape[0])

    # Creating a file in the "/model" directory to make sure it will be availabale on the "infer" step
    with open('/model/model.txt', 'w') as f:
        f.write('model')    

    # Creating a file in the "/model" directory to make sure it will be availabale on the "infer" step
    with open('/scratch/scratch.txt', 'w') as f:
        f.write('scratch')    
