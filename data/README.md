**Download Synthetic Data**

Install Python3 and pip (in case you don't have it)

https://wiki.python.org/moin/BeginnersGuide/Download
https://pip.pypa.io/en/stable/installing/

Install Synapse python dependencies
```bash
cd <path-to-repo>/data
pip install -r requirements.txt
```
Download synthetic data:
```bash
python download-synthetic-data.py \
       --synapse_username  <your-synapse-login>  \
       --synapse_password <your-synapse-password>
```
