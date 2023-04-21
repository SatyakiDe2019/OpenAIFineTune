# Easy Fine Tune of GPT-3 in Python.

## About this package

This post will use a curently unpublished version of extended PYPI package, which is developed by me. Once, published, people can easily fine tune their GPT-3 models, with a predefined supplied custom data that talks about their topics. This application developed using openai, json, pandas & other useful libraries. This project is for the advanced Python developer & Data Science Newbi's.


## How to use this package

(The following instructions apply to Posix/bash. Windows users should check
[here](https://docs.python.org/3/library/venv.html).)

First, clone this repository and open a terminal inside the root folder.

Create and activate a new virtual environment (recommended) by running
the following:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the requirements:

```bash
pip install -r requirements.txt
```

Run the GPT-3 Tuning-App:

```bash
python trainChatGPTModel.py
```

Run the GPT-3 Tuning Job Status Check:

```bash
python checkFineTuneChatGPTModelStat.py
```

Run the GPT-3 Test-App:

```bash
python testChatGPTModel.py
```

Also, you can delete any old tuned model:

```bash
python deleteChatGPTModel.py
```

Please find the dependent package -

```
nltk==3.8.1
numpy==1.24.2
openai==0.27.4
packaging==23.0
pandas==1.5.3

```

## How to use this Package - Coming Soon!

We will publish the main library shortly with more information updated on this very page. Till then, you have to wait!

Let's explore the test script ->

### playPII.py

```
#####################################################
#### Written By: SATYAKI DE                      ####
#### Written On: 12-Feb-2023                     ####
#### Modified On 19-Apr-2023                     ####
####                                             ####
#### Objective: This is the main calling         ####
#### python script that will invoke the          ####
#### newly created class that will test the      ####
#### tuned model output.                         ####
#####################################################

import clsL as cl
from clsConfigClient import clsConfigClient as cf
import datetime
import pandas as p
import clsTestModel3 as tm

# Disbling Warning
def warn(*args, **kwargs):
    pass

import warnings
warnings.warn = warn

######################################
### Get your global values        ####
######################################
debug_ind = 'Y'

# Initiating Logging Instances
clog = cl.clsL()
tmodel = tm.clsTestModel3()

open_api_key = cf.conf['OPEN_API_KEY']
lkpDataPath = cf.conf['DATA_PATH']
lkpFileName = cf.conf['LKP_FILE_NAME']

######################################
####         Global Flag      ########
######################################

def main():
    try:
        var = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        print('*' * 120)
        print('Start Time: ' + str(var))
        print('*' * 120)

        LookUpFileName = lkpDataPath + lkpFileName

        r1 = tmodel.testModel(LookUpFileName, open_api_key)

        if r1 == 0:
            print('Successfully tested the tuned GPT-3 model.')
        else:
            print('Failed to test the tuned GPT-3 model.')

        var1 = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        print('End Time: ' + str(var1))

    except Exception as e:
        x = str(e)
        print('Error: ', x)

if __name__ == "__main__":
    main()

```

Note that the debug indicator is set to "Y". This will generate logs. If you change this to 'N'. No logs will be generated. However, the process will be faster.

You can certainly contact me to add any features. Depending upon my bandwidth, I'll add them. Please share your feedback at my Technical blog site shared below.

## Screenshots

![demo.GIF](demo.GIF)

## Resources

- To view the complete demo with sound, check out our [YouTube Page](https://youtu.be/ua1eKqv0J5Q).
- To know more on OpenAI, please visit the [OpenAI Page](https://platform.openai.com/overview).
