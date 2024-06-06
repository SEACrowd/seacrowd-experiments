from seacrowd import SEACrowdConfigHelper
from seacrowd.utils.constants import Tasks
import pandas as pd
import datasets
from enum import Enum

NLU_TASK_LIST = {
    # Sentiment Analysis
    "lazada_review_filipino_seacrowd_text",
    "gklmip_sentiment_seacrowd_text",
    "indolem_sentiment_seacrowd_text",
    "id_sentiment_analysis_seacrowd_text",
    "karonese_sentiment_seacrowd_text",
    "wisesight_thai_sentiment_seacrowd_text",
    "wongnai_reviews_seacrowd_text",
    # "vlsp2016_sa_seacrowd_text", -- local dataset, will rectify later
    "typhoon_yolanda_tweets_seacrowd_text",
    # "total_defense_meme_sentiment_seacrowd_text",
    "smsa_seacrowd_text",
    "prdect_id_sentiment_seacrowd_text",
    "id_sent_emo_mobile_apps_sentiment_seacrowd_text",
    "shopee_reviews_tagalog_seacrowd_text",
    "nusatranslation_senti_abs_seacrowd_text",
    "nusatranslation_senti_btk_seacrowd_text",
    "nusatranslation_senti_bew_seacrowd_text",
    "nusatranslation_senti_bhp_seacrowd_text",
    "nusatranslation_senti_jav_seacrowd_text",
    "nusatranslation_senti_mad_seacrowd_text",
    "nusatranslation_senti_mak_seacrowd_text",
    "nusatranslation_senti_min_seacrowd_text",
    "nusatranslation_senti_mui_seacrowd_text",
    "nusatranslation_senti_rej_seacrowd_text",
    "nusatranslation_senti_sun_seacrowd_text",
    "nusax_senti_ind_seacrowd_text",
    "nusax_senti_ace_seacrowd_text",
    "nusax_senti_jav_seacrowd_text",
    "nusax_senti_sun_seacrowd_text",
    "nusax_senti_min_seacrowd_text",
    "nusax_senti_bug_seacrowd_text",
    "nusax_senti_bbc_seacrowd_text",
    "nusax_senti_ban_seacrowd_text",
    "nusax_senti_nij_seacrowd_text",
    "nusax_senti_mad_seacrowd_text",
    "nusax_senti_bjn_seacrowd_text",
    "nusax_senti_eng_seacrowd_text",
    "indonglish_seacrowd_text",
    # Topic Analysis
    "gklmip_newsclass_seacrowd_text",
    "indonesian_news_dataset_seacrowd_text",
    "uit_vion_seacrowd_text",
    # "total_defense_meme_topic_seacrowd_text",
    "sib_200_ace_Arab_seacrowd_text",
    "sib_200_ace_Latn_seacrowd_text",
    "sib_200_ban_Latn_seacrowd_text",
    "sib_200_bjn_Arab_seacrowd_text",
    "sib_200_bjn_Latn_seacrowd_text",
    "sib_200_bug_Latn_seacrowd_text",
    "sib_200_ceb_Latn_seacrowd_text",
    "sib_200_ilo_Latn_seacrowd_text",
    "sib_200_ind_Latn_seacrowd_text",
    "sib_200_jav_Latn_seacrowd_text",
    "sib_200_kac_Latn_seacrowd_text",
    "sib_200_khm_Khmr_seacrowd_text",
    "sib_200_lao_Laoo_seacrowd_text",
    "sib_200_lus_Latn_seacrowd_text",
    "sib_200_min_Arab_seacrowd_text",
    "sib_200_min_Latn_seacrowd_text",
    "sib_200_mya_Mymr_seacrowd_text",
    "sib_200_pag_Latn_seacrowd_text",
    "sib_200_shn_Mymr_seacrowd_text",
    "sib_200_sun_Latn_seacrowd_text",
    "sib_200_tgl_Latn_seacrowd_text",
    "sib_200_tha_Thai_seacrowd_text",
    "sib_200_vie_Latn_seacrowd_text",
    "sib_200_war_Latn_seacrowd_text",
    "sib_200_zsm_Latn_seacrowd_text",
    "nusaparagraph_topic_btk_seacrowd_text",
    "nusaparagraph_topic_bew_seacrowd_text",
    "nusaparagraph_topic_bug_seacrowd_text",
    "nusaparagraph_topic_jav_seacrowd_text",
    "nusaparagraph_topic_mad_seacrowd_text",
    "nusaparagraph_topic_mak_seacrowd_text",
    "nusaparagraph_topic_min_seacrowd_text",
    "nusaparagraph_topic_mui_seacrowd_text",
    "nusaparagraph_topic_rej_seacrowd_text",
    "nusaparagraph_topic_sun_seacrowd_text",
    # Reasoning
    "emotes_3k_tgl_seacrowd_text",
    "emotes_3k_eng_seacrowd_text",
    "indo_story_cloze_seacrowd_qa",
    "xstorycloze_id_seacrowd_qa",
    "xstorycloze_my_seacrowd_qa",
    # Standard Testing QA
    "indommlu_ind_seacrowd_qa",
    "indommlu_ban_seacrowd_qa",
    "indommlu_mad_seacrowd_qa",
    "indommlu_mak_seacrowd_qa",
    "indommlu_sun_seacrowd_qa",
    "indommlu_jav_seacrowd_qa",
    "indommlu_bjn_seacrowd_qa",
    "indommlu_abl_seacrowd_qa",
    "indommlu_nij_seacrowd_qa",
    "seaeval_cross_mmlu_ind_seacrowd_qa",
    "seaeval_cross_mmlu_vie_seacrowd_qa",
    "seaeval_cross_mmlu_zlm_seacrowd_qa",
    "seaeval_cross_mmlu_fil_seacrowd_qa",
    "seaeval_cross_logiqa_ind_seacrowd_qa",
    "seaeval_cross_logiqa_vie_seacrowd_qa",
    "seaeval_cross_logiqa_zlm_seacrowd_qa",
    "seaeval_cross_logiqa_fil_seacrowd_qa",
    "m3exam_jav_seacrowd_qa",
    "m3exam_tha_seacrowd_qa",
    "m3exam_vie_seacrowd_qa",
    "okapi_m_arc_ind_seacrowd_qa",
    # "okapi_m_mmlu_ind_seacrowd_qa",
    "okapi_m_arc_vie_seacrowd_qa",
    # "okapi_m_mmlu_vie_seacrowd_qa",
    # # Cultural QA
    "copal_colloquial_seacrowd_qa",
    "xcopa_tha_seacrowd_qa",
    "xcopa_vie_seacrowd_qa",
    "xcopa_ind_seacrowd_qa",
    "seaeval_sg_eval_eng_seacrowd_qa",
    "seaeval_ph_eval_eng_seacrowd_qa",
    "mabl_ind_seacrowd_qa",
    "mabl_jav_seacrowd_qa",
    "mabl_sun_seacrowd_qa",
    # Other QA
    "belebele_ceb_latn_seacrowd_qa",
    "belebele_ilo_latn_seacrowd_qa",
    "belebele_ind_latn_seacrowd_qa",
    "belebele_jav_latn_seacrowd_qa",
    "belebele_kac_latn_seacrowd_qa",
    "belebele_khm_khmr_seacrowd_qa",
    "belebele_lao_laoo_seacrowd_qa",
    "belebele_mya_mymr_seacrowd_qa",
    "belebele_shn_mymr_seacrowd_qa",
    "belebele_sun_latn_seacrowd_qa",
    "belebele_tgl_latn_seacrowd_qa",
    "belebele_tha_thai_seacrowd_qa",
    "belebele_vie_latn_seacrowd_qa",
    "belebele_war_latn_seacrowd_qa",
    "belebele_zsm_latn_seacrowd_qa",
    # NLI
    "indonli_seacrowd_pairs",
    "wrete_seacrowd_pairs",
    "snli_indo_seacrowd_pairs",
    "myxnli_seacrowd_pairs",
    "xnli.tha_seacrowd_pairs",
    "xnli.vie_seacrowd_pairs",
}

NLU_TASK_LIST_EXTERNAL = []

NLG_TASK_LIST = [
    # SUMMARIZATION
    "lr_sum_ind_seacrowd_t2t",
    "lr_sum_vie_seacrowd_t2t",
    "lr_sum_lao_seacrowd_t2t",
    "lr_sum_tha_seacrowd_t2t",
    "lr_sum_khm_seacrowd_t2t",
    "lr_sum_mya_seacrowd_t2t",
    "xl_sum_mya_seacrowd_t2t",
    "xl_sum_ind_seacrowd_t2t",
    "xl_sum_tha_seacrowd_t2t",
    "xl_sum_vie_seacrowd_t2t",
    # MACHINE TRANSLATION
    "lio_and_central_flores_eng_ljl_seacrowd_t2t",
    "lio_and_central_flores_ljl_eng_seacrowd_t2t",
    "flores200_eng_Latn_ace_Latn_seacrowd_t2t",
    "flores200_eng_Latn_ban_Latn_seacrowd_t2t",
    "flores200_eng_Latn_bjn_Latn_seacrowd_t2t",
    "flores200_eng_Latn_bug_Latn_seacrowd_t2t",
    "flores200_eng_Latn_ceb_Latn_seacrowd_t2t",
    "flores200_eng_Latn_ilo_Latn_seacrowd_t2t",
    "flores200_eng_Latn_ind_Latn_seacrowd_t2t",
    "flores200_eng_Latn_jav_Latn_seacrowd_t2t",
    "flores200_eng_Latn_kac_Latn_seacrowd_t2t",
    "flores200_eng_Latn_khm_Khmr_seacrowd_t2t",
    "flores200_eng_Latn_lao_Laoo_seacrowd_t2t",
    "flores200_eng_Latn_lus_Latn_seacrowd_t2t",
    "flores200_eng_Latn_min_Latn_seacrowd_t2t",
    "flores200_eng_Latn_mya_Mymr_seacrowd_t2t",
    "flores200_eng_Latn_pag_Latn_seacrowd_t2t",
    "flores200_eng_Latn_shn_Mymr_seacrowd_t2t",
    "flores200_eng_Latn_sun_Latn_seacrowd_t2t",
    "flores200_eng_Latn_tha_Thai_seacrowd_t2t",
    "flores200_eng_Latn_vie_Latn_seacrowd_t2t",
    "flores200_eng_Latn_war_Latn_seacrowd_t2t",
    "flores200_eng_Latn_zsm_Latn_seacrowd_t2t",
    "ntrex_128_eng-US_ind_seacrowd_t2t",
    "ntrex_128_eng-US_mya_seacrowd_t2t",
    "ntrex_128_eng-US_fil_seacrowd_t2t",
    "ntrex_128_eng-US_khm_seacrowd_t2t",
    "ntrex_128_eng-US_lao_seacrowd_t2t",
    "ntrex_128_eng-US_zlm_seacrowd_t2t",
    "ntrex_128_eng-US_tha_seacrowd_t2t",
    "ntrex_128_eng-US_vie_seacrowd_t2t",
    "ntrex_128_eng-US_hmv_seacrowd_t2t",
    "nusax_mt_eng_ind_seacrowd_t2t",
    "nusax_mt_eng_ace_seacrowd_t2t",
    "nusax_mt_eng_jav_seacrowd_t2t",
    "nusax_mt_eng_sun_seacrowd_t2t",
    "nusax_mt_eng_min_seacrowd_t2t",
    "nusax_mt_eng_bug_seacrowd_t2t",
    "nusax_mt_eng_bbc_seacrowd_t2t",
    "nusax_mt_eng_ban_seacrowd_t2t",
    "nusax_mt_eng_nij_seacrowd_t2t",
    "nusax_mt_eng_mad_seacrowd_t2t",
    "nusax_mt_eng_bjn_seacrowd_t2t",
    "flores200_ace_Latn_eng_Latn_seacrowd_t2t",
    "flores200_ban_Latn_eng_Latn_seacrowd_t2t",
    "flores200_bjn_Latn_eng_Latn_seacrowd_t2t",
    "flores200_bug_Latn_eng_Latn_seacrowd_t2t",
    "flores200_ceb_Latn_eng_Latn_seacrowd_t2t",
    "flores200_ilo_Latn_eng_Latn_seacrowd_t2t",
    "flores200_ind_Latn_eng_Latn_seacrowd_t2t",
    "flores200_jav_Latn_eng_Latn_seacrowd_t2t",
    "flores200_kac_Latn_eng_Latn_seacrowd_t2t",
    "flores200_khm_Khmr_eng_Latn_seacrowd_t2t",
    "flores200_lao_Laoo_eng_Latn_seacrowd_t2t",
    "flores200_lus_Latn_eng_Latn_seacrowd_t2t",
    "flores200_min_Latn_eng_Latn_seacrowd_t2t",
    "flores200_mya_Mymr_eng_Latn_seacrowd_t2t",
    "flores200_pag_Latn_eng_Latn_seacrowd_t2t",
    "flores200_shn_Mymr_eng_Latn_seacrowd_t2t",
    "flores200_sun_Latn_eng_Latn_seacrowd_t2t",
    "flores200_tha_Thai_eng_Latn_seacrowd_t2t",
    "flores200_vie_Latn_eng_Latn_seacrowd_t2t",
    "flores200_war_Latn_eng_Latn_seacrowd_t2t",
    "flores200_zsm_Latn_eng_Latn_seacrowd_t2t",
    "ntrex_128_ind_eng-US_seacrowd_t2t",
    "ntrex_128_mya_eng-US_seacrowd_t2t",
    "ntrex_128_fil_eng-US_seacrowd_t2t",
    "ntrex_128_khm_eng-US_seacrowd_t2t",
    "ntrex_128_lao_eng-US_seacrowd_t2t",
    "ntrex_128_zlm_eng-US_seacrowd_t2t",
    "ntrex_128_tha_eng-US_seacrowd_t2t",
    "ntrex_128_vie_eng-US_seacrowd_t2t",
    "ntrex_128_hmv_eng-US_seacrowd_t2t",
    "nusax_mt_ace_eng_seacrowd_t2t",
    "nusax_mt_jav_eng_seacrowd_t2t",
    "nusax_mt_sun_eng_seacrowd_t2t",
    "nusax_mt_min_eng_seacrowd_t2t",
    "nusax_mt_bug_eng_seacrowd_t2t",
    "nusax_mt_bbc_eng_seacrowd_t2t",
    "nusax_mt_ban_eng_seacrowd_t2t",
    "nusax_mt_nij_eng_seacrowd_t2t",
    "nusax_mt_mad_eng_seacrowd_t2t",
    "nusax_mt_bjn_eng_seacrowd_t2t",
    # EXTRACTIVE ABSTRACTIVE QA
    "facqa_seacrowd_qa",
    "iapp_squad_seacrowd_qa",
    # "idk_mrc_seacrowd_qa", -- many empty [] answers
    "qasina_seacrowd_qa",
    "mkqa_khm_seacrowd_qa", 
    "mkqa_zsm_seacrowd_qa",
    "mkqa_tha_seacrowd_qa",
    "mkqa_vie_seacrowd_qa"
]
SPEECH_TASK_LIST = list(dict.fromkeys([
    'asr_ibsc_seacrowd_sptext',
    'commonvoice_120_tha_seacrowd_sptext',
    'commonvoice_120_vie_seacrowd_sptext',
    'commonvoice_120_ind_seacrowd_sptext',
    'commonvoice_120_cnh_seacrowd_sptext',
    'fleurs_mya_seacrowd_sptext',
    'fleurs_ceb_seacrowd_sptext',
    'fleurs_fil_seacrowd_sptext',
    'fleurs_ind_seacrowd_sptext',
    'fleurs_jav_seacrowd_sptext',
    'fleurs_khm_seacrowd_sptext',
    'fleurs_lao_seacrowd_sptext',
    'fleurs_zlm_seacrowd_sptext',
    'fleurs_tha_seacrowd_sptext',
    'fleurs_vie_seacrowd_sptext',
    'indspeech_newstra_ethnicsr_nooverlap_sun_seacrowd_sptext',
    'indspeech_newstra_ethnicsr_nooverlap_jav_seacrowd_sptext',
    'indspeech_newstra_ethnicsr_nooverlap_ban_seacrowd_sptext',
    'indspeech_newstra_ethnicsr_nooverlap_btk_seacrowd_sptext',
]))


FLORES200_TASK_LIST = []

VL_TASK_LIST = [
    "xm3600_fil_seacrowd_imtext",
    "xm3600_id_seacrowd_imtext",
    "xm3600_th_seacrowd_imtext",
    "xm3600_vi_seacrowd_imtext",
]


def load_vl_datasets():
    nc_conhelp = SEACrowdConfigHelper()
    cfg_name_to_dset_map = {}

    for config_name in VL_TASK_LIST:
        print(config_name)
        schema = config_name.split('_')[-1]
        language = config_name.split('_')[-3]
        con = nc_conhelp.for_config_name(config_name)
        cfg_name_to_dset_map[config_name] = (con.load_dataset(), language, list(con.tasks)[0])
    
    return cfg_name_to_dset_map


def load_nlu_datasets():
    nc_conhelp = SEACrowdConfigHelper()
    cfg_name_to_dset_map = {}

    for config_name in NLU_TASK_LIST:
        print(config_name)
        schema = config_name.split('_')[-1]
        con = nc_conhelp.for_config_name(config_name)
        cfg_name_to_dset_map[config_name] = (con.load_dataset(), list(con.tasks)[0])

    return cfg_name_to_dset_map


### Forget this for now
def load_external_nlu_datasets(lang='ind'):
    cfg_name_to_dset_map = {}  # {config_name: (datasets.Dataset, task_name)

    # hack, add new Task
    class NewTasks(Enum):
        COPA = "COPA"
        MABL = "MABL"
        MAPS = "MAPS"
        IndoStoryCloze = "IndoStoryCloze"
        IndoMMLU = "IndoMMLU"

    for task in NLU_TASK_LIST_EXTERNAL:
        if 'COPAL' in task:
            dset = datasets.load_dataset(task)
            cfg_name_to_dset_map[task] = (dset, NewTasks.COPA)
        elif 'MABL' in task:
            mabl_path = './mabl_data'
            subset = task.split('/')[-1]

            df = pd.read_csv(f'{mabl_path}/{subset}.csv')
            dset = datasets.Dataset.from_pandas(
                df.rename({'startphrase': 'premise', 'ending1': 'choice1', 'ending2': 'choice2', 'labels': 'label'},
                          axis='columns')
            )
            cfg_name_to_dset_map[task] = (datasets.DatasetDict({'test': dset}), NewTasks.MABL)
        elif 'MAPS' in task:
            maps_path = './maps_data'
            df = pd.read_excel(f'{maps_path}/test_proverbs.xlsx')

            # Split by subset
            if '/' in task:
                subset = task.split('/')[-1]
                if subset == 'figurative':
                    df = df.loc[df['is_figurative'] == 1, :]
                else:  # non_figurative
                    df = df.loc[df['is_figurative'] == 0, :]

            dset = datasets.Dataset.from_pandas(
                df.rename({
                    'proverb': 'premise', 'conversation': 'context',
                    'answer1': 'choice1', 'answer2': 'choice2', 'answer_key': 'label'
                }, axis='columns')
            )
            cfg_name_to_dset_map[task] = (datasets.DatasetDict({'test': dset}), NewTasks.MAPS)
        elif 'IndoStoryCloze' in task:
            df = datasets.load_dataset('indolem/indo_story_cloze')['test'].to_pandas()

            # Preprocess
            df['premise'] = df.apply(lambda x: '. '.join([
                x['sentence-1'], x['sentence-2'], x['sentence-3'], x['sentence-4']
            ]), axis='columns')
            df = df.rename({'correct_ending': 'choice1', 'incorrect_ending': 'choice2'}, axis='columns')
            df = df[['premise', 'choice1', 'choice2']]
            df['label'] = 0

            dset = datasets.Dataset.from_pandas(df)
            cfg_name_to_dset_map[task] = (datasets.DatasetDict({'test': dset}), NewTasks.IndoStoryCloze)
        elif 'IndoMMLU' in task:
            df = pd.read_csv('indommlu_data/IndoMMLU.csv')
            dset = datasets.Dataset.from_pandas(df.rename({'kunci': 'label'}, axis='columns'))
            cfg_name_to_dset_map[task] = (datasets.DatasetDict({'test': dset}), NewTasks.IndoMMLU)
    return cfg_name_to_dset_map


def load_nlg_datasets():
    nc_conhelp = SEACrowdConfigHelper()
    cfg_name_to_dset_map = {}

    for config_name in NLG_TASK_LIST:
        schema = config_name.split('_')[-1]
        con = nc_conhelp.for_config_name(config_name)
        cfg_name_to_dset_map[config_name] = (con.load_dataset(), list(con.tasks)[0])
    return cfg_name_to_dset_map


### Forget about this for now
def load_flores_datasets():
    dset_map = {}
    for task in FLORES200_TASK_LIST:
        subset = task.replace('flores200-', '')
        src_lang, tgt_lang = subset.split('-')
        dset = datasets.load_dataset('facebook/flores', subset)
        dset = dset.rename_columns({f'sentence_{src_lang}': 'text_1', f'sentence_{tgt_lang}': 'text_2'}).select_columns(
            ['id', 'text_1', 'text_2'])
        dset_map[task] = (dset, Tasks.MACHINE_TRANSLATION)
    return dset_map


### Forget about this for now
def load_truthfulqa_datasets():
    class NewTasks(Enum):
        TRUTHFULQA = "TRUTHFULQA"

    return {'truthfulqa': (datasets.load_from_disk('./truthfulqa_ind'), NewTasks.TRUTHFULQA)}


def load_speech_datasets():
    nc_conhelp = SEACrowdConfigHelper()
    cfg_name_to_dset_map = {}

    for config_name in SPEECH_TASK_LIST:
        print(config_name)
        schema = config_name.split('_')[-1]
        con = nc_conhelp.for_config_name(config_name)
        cfg_name_to_dset_map[config_name] = (con.load_dataset(), list(con.tasks)[0])

    return cfg_name_to_dset_map
