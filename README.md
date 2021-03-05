# operation-odessa

<img src='https://img.shields.io/badge/Python-3.6.9-brightgreen'></img>

operation-odessa is a Python module for machine learning built on top of google colab and is distributed under the MIT license.

See the About us page for a list of core contributors.  It is currently maintained by a group of Data Scientist.


# API Credentials

To use Kaggle API, sign up for a Kaggle account at https://kaggle.com. Then go to account 'tab' of your user profile (https://www.kaggle.com/<username>/account) and select 'Create API Token'. 
This will trigger the download of kaggle.json, a file containing your API credentials. Place this file in the location ~/.kaggle/kaggle.json

```bash 
chmod 600 ~/.kaggle/kaggle.json
```

You can choose to export your Kaggle username and token to the environment: 

```bash 
export KAGGLE_USERNAME = <username> 
export KAGGLE_KEY = <key>
```

# Secret Environment 
To run our app, you must 
1) Create .env file

2) Set a file directory <root_file_dir> 
and KAGGLE <kaggle_api_command>. 
   
Please ensure you have a valid kaggle download command.

`kaggle competitions download [-h] [-f FILE_NAME] [-p PATH] [-w] [-o]
                                    [-q]
                                    [competition]`

Run the following commands. 

```bash
vim .env 
```
``` bash 
./.env

DIR = <root_file_dir> 
KAGGLE = <kaggle_api_command> 
```
```bash 
:wq
```

