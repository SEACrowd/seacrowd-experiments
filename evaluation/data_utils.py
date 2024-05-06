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
    # "sib200_ban_seacrowd_text",
    # "sib200_bjn_seacrowd_text",
    # "sib200_bug_seacrowd_text",
    # "sib200_ceb_seacrowd_text",
    # "sib200_ilo_seacrowd_text",
    # "sib200_ind_seacrowd_text",
    # "sib200_jav_seacrowd_text",
    # "sib200_kac_seacrowd_text",
    # "sib200_khm_seacrowd_text",
    # "sib200_lao_seacrowd_text",
    # "sib200_lus_seacrowd_text",
    # "sib200_min_seacrowd_text",
    # "sib200_mya_seacrowd_text",
    # "sib200_pag_seacrowd_text",
    # "sib200_shn_seacrowd_text",
    # "sib200_sun_seacrowd_text",
    # "sib200_tgl_seacrowd_text",
    # "sib200_tha_seacrowd_text",
    # "sib200_vie_seacrowd_text",
    # "sib200_war_seacrowd_text",
    # "sib200_zsm_seacrowd_text",
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
    # "m3exam_tha_seacrowd_qa", # -- some answers are []
    "m3exam_vie_seacrowd_qa",
    # "okapi_m_arc_ind_seacrowd_qa",
    # "okapi_m_mmlu_ind_seacrowd_qa",
    # "okapi_m_arc_vie_seacrowd_qa",
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
    # "facqa_seacrowd_qa", -- extractive
    # "iapp_squad_seacrowd_qa", -- abstractive
    # "idk_mrc_seacrowd_qa", -- extractive
    # "vihealthqa_seacrowd_qa", -- vqa
    # "uit_vicov19qa_seacrowd_qa", -- abstractive
    # "qasina_seacrowd_qa", -- extractive
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
    # "mkqa_khm_seacrowd_qa", -- open domain
    # "mkqa_zsm_seacrowd_qa",
    # "mkqa_tha_seacrowd_qa",
    # "mkqa_vie_seacrowd_qa",
    # "xquad.th_seacrowd_qa", -- cross-lingual QA abstractive
    # "xquad.vi_seacrowd_qa",
    # NLI
    "indonli_seacrowd_pairs",
    "wrete_seacrowd_pairs",
    "snli_indo_seacrowd_pairs",
    "myxnli_seacrowd_pairs",
    "xnli.tha_seacrowd_pairs",
    "xnli.vie_seacrowd_pairs",
    # LID
    "identifikasi_bahasa_seacrowd_text",
    # "openlid_seacrowd_text", -- too big?
    "udhr_lid_seacrowd_text",
    "wili_2018_seacrowd_text",
    # "lti_langid_corpus_seacrowd_text",
}

NLU_TASK_LIST_EXTERNAL = [
    # 'MAPS',
    # 'haryoaw/COPAL',
    # 'MABL/id',
    # 'MABL/jv',
    # 'MABL/su',
    # 'IndoStoryCloze',
    # 'IndoMMLU',
    # # 'MAPS/figurative',
    # # 'MAPS/non_figurative',
]

NLG_TASK_LIST = {
    # # Summarization
    # "indosum_fold0_seacrowd_t2t",
    # "liputan6_canonical_seacrowd_t2t",
    # "thai_sum_seacrowd_t2t",
    "seahorse_seacrowd_t2t",
    # "lr_sum_ind_seacrowd_t2t",
    # "lr_sum_vie_seacrowd_t2t",
    # "lr_sum_lao_seacrowd_t2t",
    # "lr_sum_tha_seacrowd_t2t",
    # "lr_sum_khm_seacrowd_t2t",
    # "lr_sum_mya_seacrowd_t2t",
    # "xl_sum_mya_seacrowd_t2t",
    # "xl_sum_ind_seacrowd_t2t",
    # "xl_sum_tha_seacrowd_t2t",
    # "xl_sum_vie_seacrowd_t2t",
    # # Instruction-following
    # "sea_bench_tgl_seacrowd_qa",
    # "sea_bench_khm_seacrowd_qa",
    # "sea_bench_vie_seacrowd_qa",
    # "sea_bench_tha_seacrowd_qa",
    # "sea_bench_lao_seacrowd_qa",
    # "sea_bench_mya_seacrowd_qa",
    # "sea_bench_ind_seacrowd_qa",
    # "sea_bench_zlm_seacrowd_qa",
    # "aya_dataset_tgl_seacrowd_t2t",
    # "aya_dataset_ceb_seacrowd_t2t",
    # "aya_dataset_tha_seacrowd_t2t",
    # "aya_dataset_mya_seacrowd_t2t",
    # "aya_dataset_zsm_seacrowd_t2t",
    # "aya_dataset_jav_seacrowd_t2t",
    # "aya_dataset_ind_seacrowd_t2t",
    # "aya_dataset_vie_seacrowd_t2t",
    # "aya_dataset_sun_seacrowd_t2t",
    # "aya_dataset_tam_seacrowd_t2t",
    # # Machine Translation
    # "id_mad_bible_seacrowd_t2t",
    # "ud_id_csui_seacrowd_t2t",
    # "burmese_romanize_seacrowd_t2t",
    # "parallel_asian_treebank_eng_khm_seacrowd_t2t",
    # "parallel_asian_treebank_eng_lao_seacrowd_t2t",
    # "parallel_asian_treebank_eng_mya_seacrowd_t2t",
    # "parallel_asian_treebank_eng_ind_seacrowd_t2t",
    # "parallel_asian_treebank_eng_fil_seacrowd_t2t",
    # "parallel_asian_treebank_eng_zlm_seacrowd_t2t",
    # "parallel_asian_treebank_eng_tha_seacrowd_t2t",
    # "parallel_asian_treebank_eng_vie_seacrowd_t2t",
    # "bhinneka_korpus_day_seacrowd_t2t",
    # "bhinneka_korpus_mak_seacrowd_t2t",
    # "bhinneka_korpus_aoz_seacrowd_t2t",
    # "bhinneka_korpus_mkn_seacrowd_t2t",
    # "bhinneka_korpus_abs_seacrowd_t2t",
    # "lio_and_central_flores_mt_eng_end_seacrowd_t2t",
    # "lio_and_central_flores_mt_eng_nxe_seacrowd_t2t",
    # "lio_and_central_flores_mt_eng_ssq_seacrowd_t2t",
    # "lio_and_central_flores_mt_eng_ljl_seacrowd_t2t",
    # "flores200_eng_Latn_ace_Latn_seacrowd_t2t",
    # "flores200_eng_Latn_ban_Latn_seacrowd_t2t",
    # "flores200_eng_Latn_bjn_Latn_seacrowd_t2t",
    # "flores200_eng_Latn_bug_Latn_seacrowd_t2t",
    # "flores200_eng_Latn_ceb_Latn_seacrowd_t2t",
    # "flores200_eng_Latn_ilo_Latn_seacrowd_t2t",
    # "flores200_eng_Latn_ind_Latn_seacrowd_t2t",
    # "flores200_eng_Latn_jav_Latn_seacrowd_t2t",
    # "flores200_eng_Latn_kac_Latn_seacrowd_t2t",
    # "flores200_eng_Latn_khm_Latn_seacrowd_t2t",
    # "flores200_eng_Latn_lao_Latn_seacrowd_t2t",
    # "flores200_eng_Latn_lus_Latn_seacrowd_t2t",
    # "flores200_eng_Latn_min_Latn_seacrowd_t2t",
    # "flores200_eng_Latn_mya_Latn_seacrowd_t2t",
    # "flores200_eng_Latn_pag_Latn_seacrowd_t2t",
    # "flores200_eng_Latn_shn_Latn_seacrowd_t2t",
    # "flores200_eng_Latn_sun_Latn_seacrowd_t2t",
    # "flores200_eng_Latn_tgl_Latn_seacrowd_t2t",
    # "flores200_eng_Latn_tha_Latn_seacrowd_t2t",
    # "flores200_eng_Latn_vie_Latn_seacrowd_t2t",
    # "flores200_eng_Latn_war_Latn_seacrowd_t2t",
    # "flores200_eng_Latn_zsm_Latn_seacrowd_t2t",
    # "ntrex_128_ind_mya_seacrowd_t2t",
    # "ntrex_128_ind_fil_seacrowd_t2t",
    # "ntrex_128_ind_khm_seacrowd_t2t",
    # "ntrex_128_ind_lao_seacrowd_t2t",
    # "ntrex_128_ind_zlm_seacrowd_t2t",
    # "ntrex_128_ind_tha_seacrowd_t2t",
    # "ntrex_128_ind_vie_seacrowd_t2t",
    # "ntrex_128_ind_hmv_seacrowd_t2t",
    # "indo_general_mt_en_id_seacrowd_t2t",
    # "indo_religious_mt_en_id_seacrowd_t2t",
    # "bible_en_id_seacrowd_t2t",
    # "bible_jv_id_seacrowd_t2t",
    # "bible_su_id_seacrowd_t2t",
    # "kde4_eng_ind_seacrowd_t2t",
    # "kde4_eng_khm_seacrowd_t2t",
    # "kde4_eng_zlm_seacrowd_t2t",
    # "kde4_eng_tha_seacrowd_t2t",
    # "kde4_eng_vie_seacrowd_t2t",
    # "malindo_parallel_seacrowd_t2t",
    # "minangnlp_mt_seacrowd_t2t",
    # "mozilla_pontoon_eng_mya_seacrowd_t2t",
    # "mozilla_pontoon_eng_ceb_seacrowd_t2t",
    # "mozilla_pontoon_eng_gor_seacrowd_t2t",
    # "mozilla_pontoon_eng_hil_seacrowd_t2t",
    # "mozilla_pontoon_eng_ilo_seacrowd_t2t",
    # "mozilla_pontoon_eng_ind_seacrowd_t2t",
    # "mozilla_pontoon_eng_jav_seacrowd_t2t",
    # "mozilla_pontoon_eng_khm_seacrowd_t2t",
    # "mozilla_pontoon_eng_lao_seacrowd_t2t",
    # "mozilla_pontoon_eng_zlm_seacrowd_t2t",
    # "mozilla_pontoon_eng_nia_seacrowd_t2t",
    # "mozilla_pontoon_eng_tgl_seacrowd_t2t",
    # "mozilla_pontoon_eng_tha_seacrowd_t2t",
    # "mozilla_pontoon_eng_vie_seacrowd_t2t",
    # "myanmar_rakhine_parallel_seacrowd_t2t",
    # "news_en_id_seacrowd_t2t",
    # "nusatranslation_mt_ind_abs_seacrowd_t2t",
    # "nusatranslation_mt_ind_btk_seacrowd_t2t",
    # "nusatranslation_mt_ind_bew_seacrowd_t2t",
    # "nusatranslation_mt_ind_bhp_seacrowd_t2t",
    # "nusatranslation_mt_ind_jav_seacrowd_t2t",
    # "nusatranslation_mt_ind_mad_seacrowd_t2t",
    # "nusatranslation_mt_ind_mak_seacrowd_t2t",
    # "nusatranslation_mt_ind_min_seacrowd_t2t",
    # "nusatranslation_mt_ind_mui_seacrowd_t2t",
    # "nusatranslation_mt_ind_rej_seacrowd_t2t",
    # "nusatranslation_mt_ind_sun_seacrowd_t2t",
    # "nusax_mt_eng_ace_seacrowd_t2t",
    # "nusax_mt_eng_jav_seacrowd_t2t",
    # "nusax_mt_eng_sun_seacrowd_t2t",
    # "nusax_mt_eng_min_seacrowd_t2t",
    # "nusax_mt_eng_bug_seacrowd_t2t",
    # "nusax_mt_eng_bbc_seacrowd_t2t",
    # "nusax_mt_eng_ban_seacrowd_t2t",
    # "nusax_mt_eng_nij_seacrowd_t2t",
    # "nusax_mt_eng_mad_seacrowd_t2t",
    # "nusax_mt_eng_bjn_seacrowd_t2t",
    # "nusax_mt_eng_ind_seacrowd_t2t",
    # "phomt_seacrowd_t2t",
    # "scb_mt_en_th_eng_tha_seacrowd_t2t",
    # "tatoeba_ind_seacrowd_t2t",
    # "tatoeba_vie_seacrowd_t2t",
    # "tatoeba_tgl_seacrowd_t2t",
    # "tatoeba_jav_seacrowd_t2t",
    # "tatoeba_tha_seacrowd_t2t",
    # "ted_en_id_seacrowd_t2t",
    # "tha_lao_embassy_parcor_seacrowd_t2t",
    # "tico_19_eng_ind_seacrowd_t2t",
    # "tico_19_eng_khm_seacrowd_t2t",
    # "tico_19_eng_zlm_seacrowd_t2t",
    # "tico_19_eng_mya_seacrowd_t2t",
    # "tico_19_eng_tgl_seacrowd_t2t",
    # "tico_19_eng_tam_seacrowd_t2t",
    # "indonesia_chinese_mtrobusteval_seacrowd_t2t",
    # # Cross-lingual summarization
    # "crossum_ind_mya_seacrowd_t2t",
    # "crossum_ind_vie_seacrowd_t2t",
    # "wikilingua_seacrowd_t2t",
}

FLORES200_TASK_LIST = [
    # 'flores200-sun_Latn-ind_Latn',
    # 'flores200-jav_Latn-ind_Latn',
    # 'flores200-bug_Latn-ind_Latn',
    # 'flores200-ace_Latn-ind_Latn',
    # 'flores200-bjn_Latn-ind_Latn',
    # 'flores200-ban_Latn-ind_Latn',
    # 'flores200-min_Latn-ind_Latn',
    # 'flores200-ind_Latn-sun_Latn',
    # 'flores200-ind_Latn-jav_Latn',
    # 'flores200-ind_Latn-bug_Latn',
    # 'flores200-ind_Latn-ace_Latn',
    # 'flores200-ind_Latn-bjn_Latn',
    # 'flores200-ind_Latn-ban_Latn',
    # 'flores200-ind_Latn-min_Latn',
]

VL_TASK_LIST = [
    # "alice_thi_c68_seacrowd_imtext",
    # "alice_thi_d10_seacrowd_imtext",
    # "balita_nlp_seacrowd_imtext",
    "bloom_captioning_abc_seacrowd_imtext",
    "bloom_captioning_ahk_seacrowd_imtext",
    "bloom_captioning_bfn_seacrowd_imtext",
    "bloom_captioning_bjn_seacrowd_imtext",
    "bloom_captioning_bkx_seacrowd_imtext",
    "bloom_captioning_brb_seacrowd_imtext",
    "bloom_captioning_brv_seacrowd_imtext",
    "bloom_captioning_bya_seacrowd_imtext",
    "bloom_captioning_bzi_seacrowd_imtext",
    "bloom_captioning_ceb_seacrowd_imtext",
    "bloom_captioning_cgc_seacrowd_imtext",
    "bloom_captioning_cmo_seacrowd_imtext",
    "bloom_captioning_ddg_seacrowd_imtext",
    "bloom_captioning_dmg_seacrowd_imtext",
    "bloom_captioning_dnw_seacrowd_imtext",
    "bloom_captioning_dtp_seacrowd_imtext",
    "bloom_captioning_dtr_seacrowd_imtext",
    "bloom_captioning_enc_seacrowd_imtext",
    "bloom_captioning_fil_seacrowd_imtext",
    "bloom_captioning_gal_seacrowd_imtext",
    "bloom_captioning_hil_seacrowd_imtext",
    "bloom_captioning_hre_seacrowd_imtext",
    "bloom_captioning_hro_seacrowd_imtext",
    "bloom_captioning_idt_seacrowd_imtext",
    "bloom_captioning_ilo_seacrowd_imtext",
    "bloom_captioning_ind_seacrowd_imtext",
    "bloom_captioning_jra_seacrowd_imtext",
    "bloom_captioning_kak_seacrowd_imtext",
    "bloom_captioning_khb_seacrowd_imtext",
    "bloom_captioning_khm_seacrowd_imtext",
    "bloom_captioning_kqr_seacrowd_imtext",
    "bloom_captioning_krr_seacrowd_imtext",
    "bloom_captioning_ksw_seacrowd_imtext",
    "bloom_captioning_lhu_seacrowd_imtext",
    "bloom_captioning_llg_seacrowd_imtext",
    "bloom_captioning_lsi_seacrowd_imtext",
    "bloom_captioning_lwl_seacrowd_imtext",
    "bloom_captioning_mdr_seacrowd_imtext",
    "bloom_captioning_mgm_seacrowd_imtext",
    # "bloom_captioning_mhx_seacrowd_mtext",
    "bloom_captioning_mkz_seacrowd_imtext",
    "bloom_captioning_mnw_seacrowd_imtext",
    "bloom_captioning_mqj_seacrowd_imtext",
    "bloom_captioning_mry_seacrowd_imtext",
    "bloom_captioning_msb_seacrowd_imtext",
    "bloom_captioning_mya_seacrowd_imtext",
    "bloom_captioning_nod_seacrowd_imtext",
    "bloom_captioning_nst_seacrowd_imtext",
    "bloom_captioning_nxa_seacrowd_imtext",
    "bloom_captioning_nxl_seacrowd_imtext",
    "bloom_captioning_pag_seacrowd_imtext",
    "bloom_captioning_pce_seacrowd_imtext",
    "bloom_captioning_pdu_seacrowd_imtext",
    "bloom_captioning_pea_seacrowd_imtext",
    "bloom_captioning_pmf_seacrowd_imtext",
    "bloom_captioning_sea_seacrowd_imtext",
    "bloom_captioning_sgd_seacrowd_imtext",
    "bloom_captioning_shn_seacrowd_imtext",
    "bloom_captioning_sml_seacrowd_imtext",
    "bloom_captioning_snl_seacrowd_imtext",
    "bloom_captioning_tdt_seacrowd_imtext",
    "bloom_captioning_tet_seacrowd_imtext",
    "bloom_captioning_tha_seacrowd_imtext",
    "bloom_captioning_tkd_seacrowd_imtext",
    "bloom_captioning_tnt_seacrowd_imtext",
    "bloom_captioning_tom_seacrowd_imtext",
    "bloom_captioning_tpu_seacrowd_imtext",
    "bloom_captioning_vie_seacrowd_imtext",
    "bloom_captioning_war_seacrowd_imtext",
    "bloom_captioning_wms_seacrowd_imtext",
    "bloom_captioning_wnk_seacrowd_imtext",
    "bloom_captioning_xmm_seacrowd_imtext",
    "bloom_captioning_yet_seacrowd_imtext",
    "bloom_captioning_zlm_seacrowd_imtext",
    "bloom_vist_abc_seacrowd_imtext",
    "bloom_vist_ahk_seacrowd_imtext",
    "bloom_vist_bfn_seacrowd_imtext",
    'bloom_vist_bjn_seacrowd_imtext',
    "bloom_vist_bkx_seacrowd_imtext",
    'bloom_vist_brb_seacrowd_imtext',
    "bloom_vist_brv_seacrowd_imtext",
    "bloom_vist_bya_seacrowd_imtext",
    'bloom_vist_bzi_seacrowd_imtext',
    "bloom_vist_ceb_seacrowd_imtext",
    "bloom_vist_cgc_seacrowd_imtext",
    "bloom_vist_cmo_seacrowd_imtext",
    "bloom_vist_ddg_seacrowd_imtext",
    "bloom_vist_dmg_seacrowd_imtext",
    "bloom_vist_dnw_seacrowd_imtext",
    "bloom_vist_dtp_seacrowd_imtext",
    "bloom_vist_enc_seacrowd_imtext",
    "bloom_vist_fil_seacrowd_imtext",
    "bloom_vist_hil_seacrowd_imtext",
    "bloom_vist_hro_seacrowd_imtext",
    "bloom_vist_idt_seacrowd_imtext",
    'bloom_vist_ilo_seacrowd_imtext',
    'bloom_vist_ind_seacrowd_imtext',
    "bloom_vist_jra_seacrowd_imtext",
    "bloom_vist_kak_seacrowd_imtext",
    "bloom_vist_khb_seacrowd_imtext",
    "bloom_vist_khm_seacrowd_imtext",
    "bloom_vist_kqr_seacrowd_imtext",
    "bloom_vist_krr_seacrowd_imtext",
    'bloom_vist_ksw_seacrowd_imtext',
    'bloom_vist_lhu_seacrowd_imtext',
    'bloom_vist_lsi_seacrowd_imtext',
    'bloom_vist_lwl_seacrowd_imtext',
    "bloom_vist_mdr_seacrowd_imtext",
    "bloom_vist_mgm_seacrowd_imtext",
    "bloom_vist_mhx_seacrowd_imtext",
    "bloom_vist_mkz_seacrowd_imtext",
    "bloom_vist_mry_seacrowd_imtext",
    "bloom_vist_msb_seacrowd_imtext",
    "bloom_vist_mya_seacrowd_imtext",
    "bloom_vist_nod_seacrowd_imtext",
    "bloom_vist_nxa_seacrowd_imtext",
    "bloom_vist_nxl_seacrowd_imtext",
    "bloom_vist_pag_seacrowd_imtext",
    "bloom_vist_pce_seacrowd_imtext",
    "bloom_vist_pea_seacrowd_imtext",
    "bloom_vist_pmf_seacrowd_imtext",
    'bloom_vist_psp_seacrowd_imtext',
    "bloom_vist_sea_seacrowd_imtext",
    "bloom_vist_sgd_seacrowd_imtext",
    "bloom_vist_sml_seacrowd_imtext",
    "bloom_vist_snl_seacrowd_imtext",
    "bloom_vist_tdt_seacrowd_imtext",
    "bloom_vist_tet_seacrowd_imtext",
    "bloom_vist_tha_seacrowd_imtext",
    "bloom_vist_tkd_seacrowd_imtext",
    "bloom_vist_tpu_seacrowd_imtext",
    "bloom_vist_war_seacrowd_imtext",
    "bloom_vist_wms_seacrowd_imtext",
    "bloom_vist_yet_seacrowd_imtext",
    "bloom_vist_yin_seacrowd_imtext",
    "bloom_vist_zlm_seacrowd_imtext",
    "burapha_th_character_seacrowd_imtext",
    "burapha_th_digit_seacrowd_imtext",
    "burapha_th_syllable_seacrowd_imtext",
    # "cc3m_35l_fil_seacrowd_imtext",
    # "cc3m_35l_ind_seacrowd_imtext",
    # "cc3m_35l_tha_seacrowd_imtext",
    # "cc3m_35l_vie_seacrowd_imtext",
    # "coco_35l_fil_seacrowd_imtext",
    # "coco_35l_ind_seacrowd_imtext",
    # "coco_35l_tha_seacrowd_imtext",
    # "coco_35l_vie_seacrowd_imtext",
    "cub_bahasa_seacrowd_imtext",
    "fsl_105_seacrowd_vidtext",
    # "id_mm_cc_12m_seacrowd_imtext",
    # Indonesian
    # "kvis_th_ocr_seacrowd_imtext",
    "m3exam_jav_seacrowd_imqa",
    "m3exam_tha_seacrowd_imqa",
    "m3exam_vie_seacrowd_imqa",
    # "m3ls_seacrowd_imtext",
    # "id_mvsd_seacrowd_imtext",
    # "mywsl2023_seacrowd_imtext",
    # "openvivqa_seacrowd_imqa",
    # "sleukrith_ocr_seacrowd_imtext",
    # "total_defense_meme_topic_seacrowd_image",
    # "total_defense_meme_stance_seacrowd_image",
    # "total_defense_meme_topic_seacrowd_image",
    # "uit_vilc_seacrowd_imtext",
    # "vintext_seacrowd_imtext",
    # "vivqa_seacrowd_imqa",
    "wit_ceb_seacrowd_imtext",
    "wit_fil_seacrowd_imtext",
    "wit_ind_seacrowd_imtext",
    "wit_jav_seacrowd_imtext",
    # "wit_zlm_seacrowd_imtext",
    "wit_mya_seacrowd_imtext",
    "wit_tha_seacrowd_imtext",
    "wit_vie_seacrowd_imtext",
    "wit_war_seacrowd_imtext",
    "xm3600_fil_seacrowd_imtext",
    "xm3600_id_seacrowd_imtext",
    "xm3600_th_seacrowd_imtext",
    "xm3600_vi_seacrowd_imtext",
]


def load_vl_datasets():
    nc_conhelp = SEACrowdConfigHelper()
    cfg_name_to_dset_map = {}

    for config_name in VL_TASK_LIST:
        # if "bloom" in config_name: continue
        if "burapha" in config_name: continue   # Task name incorrect
        if "fsl" in config_name: continue       # No text
        if "m3exam" in config_name: continue    # No test set   
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
    cfg_name_to_dset_map = {} # {config_name: (datasets.Dataset, task_name)

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
                df.rename({'startphrase': 'premise', 'ending1': 'choice1', 'ending2': 'choice2', 'labels': 'label'}, axis='columns')
            )
            cfg_name_to_dset_map[task] = (datasets.DatasetDict({'test': dset}), NewTasks.MABL)
        elif 'MAPS' in task:
            maps_path = './maps_data'
            df = pd.read_excel(f'{maps_path}/test_proverbs.xlsx')
            
            # Split by subset
            if '/' in task:
                subset = task.split('/')[-1]
                if subset =='figurative':
                    df = df.loc[df['is_figurative'] == 1,:]
                else: # non_figurative
                    df = df.loc[df['is_figurative'] == 0,:]

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
        con = nc_conhelp.for_config_name(config_name)
        cfg_name_to_dset_map[config_name] = (con.load_dataset(), list(con.tasks[0]))

    return cfg_name_to_dset_map

### Forget about this for now
def load_flores_datasets():
    dset_map = {}
    for task in FLORES200_TASK_LIST:
        subset = task.replace('flores200-', '')
        src_lang, tgt_lang = subset.split('-')
        dset = datasets.load_dataset('facebook/flores', subset)
        dset = dset.rename_columns({f'sentence_{src_lang}': 'text_1', f'sentence_{tgt_lang}': 'text_2'}).select_columns(['id', 'text_1', 'text_2'])
        dset_map[task] = (dset, Tasks.MACHINE_TRANSLATION)
    return dset_map

### Forget about this for now
def load_truthfulqa_datasets():
    class NewTasks(Enum):
        TRUTHFULQA = "TRUTHFULQA"
    return {'truthfulqa': (datasets.load_from_disk('./truthfulqa_ind'), NewTasks.TRUTHFULQA)}