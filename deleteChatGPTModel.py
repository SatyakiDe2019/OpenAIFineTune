#####################################################
#### Written By: SATYAKI DE                      ####
#### Written On: 12-Feb-2023                     ####
#### Modified On 21-Feb-2023                     ####
####                                             ####
#### Objective: This is the main calling         ####
#### python script that will invoke the          ####
#### newly created delete model methods for      ####
#### OpenAI.                                     ####
#####################################################

import clsL as cl
from clsConfigClient import clsConfigClient as cf
import datetime
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

######################################
####         Global Flag      ########
######################################

def main():
    try:
        var = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        print('*' * 120)
        print('Start Time: ' + str(var))
        print('*' * 120)

        r1 = tmodel.delOldModel(open_api_key)

        if r1 == 0:
            print('Successfully checked the status of tuned GPT-3 model.')
        else:
            print('Failed to check the status of the tuned GPT-3 model.')

        var1 = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        print('End Time: ' + str(var1))

    except Exception as e:
        x = str(e)
        print('Error: ', x)

if __name__ == "__main__":
    main()
