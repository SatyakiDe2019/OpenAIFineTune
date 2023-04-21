#####################################################
#### Written By: SATYAKI DE                      ####
#### Written On: 12-Feb-2023                     ####
#### Modified On 16-Feb-2023                     ####
####                                             ####
#### Objective: This is the main calling         ####
#### python script that will invoke the          ####
#### newly created light data masking class.     ####
####                                             ####
#####################################################

import pandas as p
import clsL as cl
from clsConfigClient import clsConfigClient as cf
import datetime

import clsTrainModel3 as tm

# Disbling Warning
def warn(*args, **kwargs):
    pass

import warnings
warnings.warn = warn

######################################
### Get your global values        ####
######################################
debug_ind = 'Y'
#tModel = tm.clsTrainModel()
tModel = tm.clsTrainModel3()

# Initiating Logging Instances
clog = cl.clsL()

data_path = cf.conf['DATA_PATH']
data_file_name = cf.conf['FILE_NAME']
######################################
####         Global Flag      ########
######################################

######################################
### Wrapper functions to invoke    ###
### the desired class from newly   ###
### built class.                   ###
######################################

######################################
### End of wrapper functions.      ###
######################################

def main():
    try:
        var = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        print('*'*120)
        print('Start Time: ' + str(var))
        print('*'*120)

        FullFileName = data_path + data_file_name

        r1 = tModel.trainModel(FullFileName)

        if r1 == 0:
            print('Successfully Trained!')
        else:
            print('Failed to Train!')

        #clog.logr(OutPutFileName, debug_ind, df, subdir)

        print('*'*120)
        var1 = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        print('End Time: ' + str(var1))

    except Exception as e:
        x = str(e)
        print('Error: ', x)

if __name__ == "__main__":
    main()
