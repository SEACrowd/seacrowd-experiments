from seacrowd import SEACrowdConfigHelper
from seacrowd.utils.constants import Tasks
import pandas as pd
import datasets
from enum import Enum


NLU_TASK_LIST = []
NLG_TASK_LIST = []
SPEECH_TASK_LIST = []
INSTRUCTION_TUNING_TASK_LIST = [
    "sea_bench_eng_seacrowd_t2t", 
    "sea_bench_ind_seacrowd_t2t", 
    "sea_bench_khm_seacrowd_t2t", 
    "sea_bench_lao_seacrowd_t2t", 
    "sea_bench_mya_seacrowd_t2t", 
    "sea_bench_tgl_seacrowd_t2t", 
    "sea_bench_tha_seacrowd_t2t", 
    "sea_bench_vie_seacrowd_t2t", 
    "sea_bench_zlm_seacrowd_t2t",
]

def load_nlu_datasets():
    nc_conhelp = SEACrowdConfigHelper()
    cfg_name_to_dset_map = {}

    for config_name in NLU_TASK_LIST:
        print(config_name)
        schema = config_name.split('_')[-1]
        con = nc_conhelp.for_config_name(config_name)
        cfg_name_to_dset_map[config_name] = (con.load_dataset(), list(con.tasks)[0])

    return cfg_name_to_dset_map

def load_nlg_datasets():
    nc_conhelp = SEACrowdConfigHelper()
    cfg_name_to_dset_map = {}

    for config_name in NLG_TASK_LIST:
        schema = config_name.split('_')[-1]
        con = nc_conhelp.for_config_name(config_name)
        cfg_name_to_dset_map[config_name] = (con.load_dataset(), list(con.tasks)[0])
    return cfg_name_to_dset_map

def load_instruction_tuning_datasets():
    nc_conhelp = SEACrowdConfigHelper()
    cfg_name_to_dset_map = {}

    for config_name in INSTRUCTION_TUNING_TASK_LIST:
        schema = config_name.split('_')[-1]
        con = nc_conhelp.for_config_name(config_name)
        cfg_name_to_dset_map[config_name] = (con.load_dataset(), list(con.tasks)[0])
    return cfg_name_to_dset_map