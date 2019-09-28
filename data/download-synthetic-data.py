import synapseclient
import synapseutils
import argparse
import tarfile
import os
 
if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--synapse_username", type=str, required=True)
    parser.add_argument('--synapse_password', type=str, required=True)

    args = parser.parse_args()

    try:
        syn = synapseclient.Synapse()
        syn.login(args.synapse_username, args.synapse_password)
        files = synapseutils.syncFromSynapse(syn, 'syn20685954', path='./syn20685954')

        print('Extracting synthetic_evaluation.tar.gz ...')
        with tarfile.open('syn20685954/synthetic_evaluation.tar.gz', "r:gz") as tar:
            tar.extractall()
        print('Extracting synthetic_training.tar.gz ...')
        with tarfile.open('syn20685954/synthetic_training.tar.gz', "r:gz") as tar:
            tar.extractall()
        
        print('Making "model", "scratch" and "output" directories')
        for dir_name in ['model', 'scratch', 'output']:
            if not os.path.exists(dir_name):
                 os.makedirs(dir_name)
        
        print('Done!')
    except synapseclient.exceptions.SynapseAuthenticationError as e:
        print(e)
