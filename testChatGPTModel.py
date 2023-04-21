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
