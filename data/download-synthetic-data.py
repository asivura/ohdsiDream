import synapseclient
import synapseutils
import argparse
 
if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--synapse_username", type=str, required=True)
    parser.add_argument('--synapse_password', type=str, required=True)

    args = parser.parse_args()

    try:
        syn = synapseclient.Synapse()
        syn.login(args.synapse_username, args.synapse_password)
        files = synapseutils.syncFromSynapse(syn, 'syn20685954', path='./syn20685954')
    except synapseclient.exceptions.SynapseAuthenticationError as e:
        print(e)
