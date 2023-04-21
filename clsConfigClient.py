################################################
#### Written By: SATYAKI DE                 ####
#### Written On:  15-May-2020               ####
#### Modified On: 21-Feb-2023               ####
####                                        ####
#### Objective: This script is a config     ####
#### file, contains all the keys for        ####
#### OpenAI fine-tune projects.             ####
####                                        ####
################################################

import os
import platform as pl

class clsConfigClient(object):
    Curr_Path = os.path.dirname(os.path.realpath(__file__))

    os_det = pl.system()
    if os_det == "Windows":
        sep = '\\'
    else:
        sep = '/'

    conf = {
        'APP_ID': 1,
        'ARCH_DIR': Curr_Path + sep + 'arch' + sep,
        'PROFILE_PATH': Curr_Path + sep + 'profile' + sep,
        'LOG_PATH': Curr_Path + sep + 'log' + sep,
        'DATA_PATH': Curr_Path + sep + 'data' + sep,
        'TEMP_PATH': Curr_Path + sep + 'temp' + sep,
        'MODEL_DIR': 'model',
        'APP_DESC_1': 'ChatGPT Training!',
        'DEBUG_IND': 'N',
        'INIT_PATH': Curr_Path,
        'FILE_NAME': '2023-4-14-WP.csv',
        'LKP_FILE_NAME': 'HyperDetails.csv',
        'TEMP_FILE_NAME': 'chatGPTData.jsonl',
        'TITLE': "GPT-3 Training!",
        'PATH' : Curr_Path,
        'OUT_DIR': 'data',
        'OPEN_API_KEY': 'sk-hdhrujfrkfjfjfjfhjfjfisososT&jsdgL6KIxx',
        'MODEL_CD':'davinci',
        'URL': 'https://api.openai.com/v1/fine-tunes/',
        'EPOCH': 10,
        'SUFFIX': 'py-saty',
        'EXIT_KEYWORD': 'bye'
    }
