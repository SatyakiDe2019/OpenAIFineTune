#####################################################
#### Written By: SATYAKI DE                      ####
#### Written On: 12-Feb-2023                     ####
#### Modified On 16-Feb-2023                     ####
####                                             ####
#### Objective: This is the main calling         ####
#### python script that will invoke the          ####
#### newly created fine-tune job status inside   ####
#### the OpenAI enviornment.                     ####
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

url_part = cf.conf['URL']
open_api_key = cf.conf['OPEN_API_KEY']
######################################
####         Global Flag      ########
######################################

def main():
    try:
        var = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        print('*'*120)
        print('Start Time: ' + str(var))
        print('*'*120)

        # Example usage
        input_text = str(input("Please provide the fine tune Id (Start with ft-*): "))
        url = url_part + input_text
        print('URL: ', url)

        r1 = tmodel.checkStat(url, open_api_key)

        if r1 == 0:
            print('Successfully checked the status of tuned GPT-3 model.')
        else:
            print('Failed to check the status of the tuned GPT-3 model.')

        print('*'*120)
        var1 = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        print('End Time: ' + str(var1))

    except Exception as e:
        x = str(e)
        print('Error: ', x)

if __name__ == "__main__":
    main()
