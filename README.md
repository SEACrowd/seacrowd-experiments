# SEACrowd Experiments

Experiment repository for the "SEACrowd: A Multilingual Multimodal Data Hub and Benchmark Suite for Southeast Asian Languages" paper.

SEACrowd is a [collaborative initiative](https://github.com/SEACrowd) that consolidates a [comprehensive resource hub](https://seacrowd.github.io/seacrowd-catalogue/) that fills the resource gap by [providing standardized corpora](https://github.com/SEACrowd/seacrowd-datahub) in nearly 1,000 Southeast Asian (SEA) languages across three modalities.

> Note: All code in SEACrowd is publicly available under the Apache 2.0 license.

## SEACrowd Benchmarks: State-of-the-Art Models on SEA Languages

Placed under [`evaluation/`](https://github.com/SEACrowd/seacrowd-experiments/tree/main/evaluation).

Through our SEACrowd benchmarks, we assess the quality of AI models on 36 indigenous languages across 13 tasks, offering valuable insights into the current AI landscape in SEA. Furthermore, we propose strategies to facilitate greater AI advancements, maximizing potential utility and resource equity for the future of AI in SEA.

<details open>
  <summary>Eval data subsets</summary>

    | eval_type | subset | lang | task | n_instances |
    |-----------|--------|------|------|-------------|
    | NLG | lr_sum_ind_seacrowd_t2t | ind | Summarization | 500 |
    | NLG | lr_sum_vie_seacrowd_t2t | vie | Summarization | 1460 |
    | NLG | lr_sum_lao_seacrowd_t2t | lao | Summarization | 1496 |
    | NLG | lr_sum_tha_seacrowd_t2t | tha | Summarization | 500 |
    | NLG | lr_sum_khm_seacrowd_t2t | khm | Summarization | 486 |
    | NLG | lr_sum_mya_seacrowd_t2t | mya | Summarization | 990 |
    | NLG | xl_sum_mya_seacrowd_t2t | mya | Summarization | 570 |
    | NLG | xl_sum_ind_seacrowd_t2t | ind | Summarization | 4780 |
    | NLG | xl_sum_tha_seacrowd_t2t | tha | Summarization | 826 |
    | NLG | xl_sum_vie_seacrowd_t2t | vie | Summarization | 4013 |
    | NLG | lio_and_central_flores_eng_ljl_seacrowd_t2t | ljl | MT Eng -> XX | 1658 |
    | NLG | flores200_eng_Latn_ace_Latn_seacrowd_t2t | ace | MT Eng -> XX | 1012 |
    | NLG | flores200_eng_Latn_ban_Latn_seacrowd_t2t | ban | MT Eng -> XX | 1012 |
    | NLG | flores200_eng_Latn_bjn_Latn_seacrowd_t2t | bjn | MT Eng -> XX | 1012 |
    | NLG | flores200_eng_Latn_bug_Latn_seacrowd_t2t | bug | MT Eng -> XX | 1012 |
    | NLG | flores200_eng_Latn_ceb_Latn_seacrowd_t2t | ceb | MT Eng -> XX | 1012 |
    | NLG | flores200_eng_Latn_ilo_Latn_seacrowd_t2t | ilo | MT Eng -> XX | 1012 |
    | NLG | flores200_eng_Latn_ind_Latn_seacrowd_t2t | ind | MT Eng -> XX | 1012 |
    | NLG | flores200_eng_Latn_jav_Latn_seacrowd_t2t | jav | MT Eng -> XX | 1012 |
    | NLG | flores200_eng_Latn_kac_Latn_seacrowd_t2t | kac | MT Eng -> XX | 1012 |
    | NLG | flores200_eng_Latn_khm_Khmr_seacrowd_t2t | khm | MT Eng -> XX | 1012 |
    | NLG | flores200_eng_Latn_lao_Laoo_seacrowd_t2t | lao | MT Eng -> XX | 1012 |
    | NLG | flores200_eng_Latn_lus_Latn_seacrowd_t2t | lus | MT Eng -> XX | 1012 |
    | NLG | flores200_eng_Latn_min_Latn_seacrowd_t2t | min | MT Eng -> XX | 1012 |
    | NLG | flores200_eng_Latn_mya_Mymr_seacrowd_t2t | mya | MT Eng -> XX | 1012 |
    | NLG | flores200_eng_Latn_pag_Latn_seacrowd_t2t | pag | MT Eng -> XX | 1012 |
    | NLG | flores200_eng_Latn_shn_Mymr_seacrowd_t2t | shn | MT Eng -> XX | 1012 |
    | NLG | flores200_eng_Latn_sun_Latn_seacrowd_t2t | sun | MT Eng -> XX | 1012 |
    | NLG | flores200_eng_Latn_tha_Thai_seacrowd_t2t | tha | MT Eng -> XX | 1012 |
    | NLG | flores200_eng_Latn_vie_Latn_seacrowd_t2t | vie | MT Eng -> XX | 1012 |
    | NLG | flores200_eng_Latn_war_Latn_seacrowd_t2t | war | MT Eng -> XX | 1012 |
    | NLG | flores200_eng_Latn_zsm_Latn_seacrowd_t2t | zlm | MT Eng -> XX | 1012 |
    | NLG | ntrex_128_eng-US_ind_seacrowd_t2t | ind | MT Eng -> XX | 1997 |
    | NLG | ntrex_128_eng-US_mya_seacrowd_t2t | mya | MT Eng -> XX | 1997 |
    | NLG | ntrex_128_eng-US_fil_seacrowd_t2t | fil | MT Eng -> XX | 1997 |
    | NLG | ntrex_128_eng-US_khm_seacrowd_t2t | khm | MT Eng -> XX | 1997 |
    | NLG | ntrex_128_eng-US_lao_seacrowd_t2t | lao | MT Eng -> XX | 1997 |
    | NLG | ntrex_128_eng-US_zlm_seacrowd_t2t | zlm | MT Eng -> XX | 1997 |
    | NLG | ntrex_128_eng-US_tha_seacrowd_t2t | tha | MT Eng -> XX | 1997 |
    | NLG | ntrex_128_eng-US_vie_seacrowd_t2t | vie | MT Eng -> XX | 1997 |
    | NLG | ntrex_128_eng-US_hmv_seacrowd_t2t | hmv | MT Eng -> XX | 1997 |
    | NLG | nusax_mt_eng_ind_seacrowd_t2t | ind | MT Eng -> XX | 400 |
    | NLG | nusax_mt_eng_ace_seacrowd_t2t | ace | MT Eng -> XX | 400 |
    | NLG | nusax_mt_eng_jav_seacrowd_t2t | jav | MT Eng -> XX | 400 |
    | NLG | nusax_mt_eng_sun_seacrowd_t2t | sun | MT Eng -> XX | 400 |
    | NLG | nusax_mt_eng_min_seacrowd_t2t | min | MT Eng -> XX | 400 |
    | NLG | nusax_mt_eng_bug_seacrowd_t2t | bug | MT Eng -> XX | 400 |
    | NLG | nusax_mt_eng_bbc_seacrowd_t2t | bbc | MT Eng -> XX | 400 |
    | NLG | nusax_mt_eng_ban_seacrowd_t2t | ban | MT Eng -> XX | 400 |
    | NLG | nusax_mt_eng_nij_seacrowd_t2t | nij | MT Eng -> XX | 400 |
    | NLG | nusax_mt_eng_mad_seacrowd_t2t | mad | MT Eng -> XX | 400 |
    | NLG | nusax_mt_eng_bjn_seacrowd_t2t | bjn | MT Eng -> XX | 400 |
    | NLG | lio_and_central_flores_ljl_eng_seacrowd_t2t | ljl | MT XX -> Eng | 1658 |
    | NLG | flores200_ace_Latn_eng_Latn_seacrowd_t2t | ace | MT XX -> Eng | 1012 |
    | NLG | flores200_ban_Latn_eng_Latn_seacrowd_t2t | ban | MT XX -> Eng | 1012 |
    | NLG | flores200_bjn_Latn_eng_Latn_seacrowd_t2t | bjn | MT XX -> Eng | 1012 |
    | NLG | flores200_bug_Latn_eng_Latn_seacrowd_t2t | bug | MT XX -> Eng | 1012 |
    | NLG | flores200_ceb_Latn_eng_Latn_seacrowd_t2t | ceb | MT XX -> Eng | 1012 |
    | NLG | flores200_ilo_Latn_eng_Latn_seacrowd_t2t | ilo | MT XX -> Eng | 1012 |
    | NLG | flores200_ind_Latn_eng_Latn_seacrowd_t2t | ind | MT XX -> Eng | 1012 |
    | NLG | flores200_jav_Latn_eng_Latn_seacrowd_t2t | jav | MT XX -> Eng | 1012 |
    | NLG | flores200_kac_Latn_eng_Latn_seacrowd_t2t | kac | MT XX -> Eng | 1012 |
    | NLG | flores200_khm_Khmr_eng_Latn_seacrowd_t2t | khm | MT XX -> Eng | 1012 |
    | NLG | flores200_lao_Laoo_eng_Latn_seacrowd_t2t | lao | MT XX -> Eng | 1012 |
    | NLG | flores200_lus_Latn_eng_Latn_seacrowd_t2t | lus | MT XX -> Eng | 1012 |
    | NLG | flores200_min_Latn_eng_Latn_seacrowd_t2t | min | MT XX -> Eng | 1012 |
    | NLG | flores200_mya_Mymr_eng_Latn_seacrowd_t2t | mya | MT XX -> Eng | 1012 |
    | NLG | flores200_pag_Latn_eng_Latn_seacrowd_t2t | pag | MT XX -> Eng | 1012 |
    | NLG | flores200_shn_Mymr_eng_Latn_seacrowd_t2t | shn | MT XX -> Eng | 1012 |
    | NLG | flores200_sun_Latn_eng_Latn_seacrowd_t2t | sun | MT XX -> Eng | 1012 |
    | NLG | flores200_tha_Thai_eng_Latn_seacrowd_t2t | tha | MT XX -> Eng | 1012 |
    | NLG | flores200_vie_Latn_eng_Latn_seacrowd_t2t | vie | MT XX -> Eng | 1012 |
    | NLG | flores200_war_Latn_eng_Latn_seacrowd_t2t | war | MT XX -> Eng | 1012 |
    | NLG | flores200_zsm_Latn_eng_Latn_seacrowd_t2t | zsm | MT XX -> Eng | 1012 |
    | NLG | ntrex_128_ind_eng-US_seacrowd_t2t | ind | MT XX -> Eng | 1997 |
    | NLG | ntrex_128_mya_eng-US_seacrowd_t2t | mya | MT XX -> Eng | 1997 |
    | NLG | ntrex_128_fil_eng-US_seacrowd_t2t | fil | MT XX -> Eng | 1997 |
    | NLG | ntrex_128_khm_eng-US_seacrowd_t2t | khm | MT XX -> Eng | 1997 |
    | NLG | ntrex_128_lao_eng-US_seacrowd_t2t | lao | MT XX -> Eng | 1997 |
    | NLG | ntrex_128_zlm_eng-US_seacrowd_t2t | zlm | MT XX -> Eng | 1997 |
    | NLG | ntrex_128_tha_eng-US_seacrowd_t2t | tha | MT XX -> Eng | 1997 |
    | NLG | ntrex_128_vie_eng-US_seacrowd_t2t | vie | MT XX -> Eng | 1997 |
    | NLG | ntrex_128_hmv_eng-US_seacrowd_t2t | hmv | MT XX -> Eng | 1997 |
    | NLG | nusax_mt_ace_eng_seacrowd_t2t | ace | MT XX -> Eng | 400 |
    | NLG | nusax_mt_jav_eng_seacrowd_t2t | jav | MT XX -> Eng | 400 |
    | NLG | nusax_mt_sun_eng_seacrowd_t2t | sun | MT XX -> Eng | 400 |
    | NLG | nusax_mt_min_eng_seacrowd_t2t | min | MT XX -> Eng | 400 |
    | NLG | nusax_mt_bug_eng_seacrowd_t2t | bug | MT XX -> Eng | 400 |
    | NLG | nusax_mt_bbc_eng_seacrowd_t2t | bbc | MT XX -> Eng | 400 |
    | NLG | nusax_mt_ban_eng_seacrowd_t2t | ban | MT XX -> Eng | 400 |
    | NLG | nusax_mt_nij_eng_seacrowd_t2t | nij | MT XX -> Eng | 400 |
    | NLG | nusax_mt_mad_eng_seacrowd_t2t | mad | MT XX -> Eng | 400 |
    | NLG | nusax_mt_bjn_eng_seacrowd_t2t | bjn | MT XX -> Eng | 400 |
    | NLG | facqa_seacrowd_qa | ind | Question Answering | 311 |
    | NLG | iapp_squad_seacrowd_qa | tha | Question Answering | 739 |
    | NLG | qasina_seacrowd_qa | ind | Question Answering | 500 |
    | NLG | mkqa_khm_seacrowd_qa | khm | Question Answering | 10000 |
    | NLG | mkqa_zsm_seacrowd_qa | zsm | Question Answering | 10000 |
    | NLG | mkqa_tha_seacrowd_qa | tha | Question Answering | 10000 |
    | NLG | mkqa_vie_seacrowd_qa | vie | Question Answering | 10000 |
    | NLU | lazada_review_filipino_seacrowd_text | fil | Sentiment Analysis | 1001 |
    | NLU | gklmip_sentiment_seacrowd_text | mya | Sentiment Analysis | 716 |
    | NLU | indolem_sentiment_seacrowd_text | ind | Sentiment Analysis | 1011 |
    | NLU | id_sentiment_analysis_seacrowd_text | ind | Sentiment Analysis | 10806 |
    | NLU | karonese_sentiment_seacrowd_text | btx | Sentiment Analysis | 1000 |
    | NLU | wisesight_thai_sentiment_seacrowd_text | tha | Sentiment Analysis | 2671 |
    | NLU | wongnai_reviews_seacrowd_text | tha | Sentiment Analysis | 6203 |
    | NLU | typhoon_yolanda_tweets_seacrowd_text | fil | Sentiment Analysis | 153 |
    | NLU | smsa_seacrowd_text | ind | Sentiment Analysis | 500 |
    | NLU | prdect_id_sentiment_seacrowd_text | ind | Sentiment Analysis | 5400 |
    | NLU | id_sent_emo_mobile_apps_sentiment_seacrowd_text | ind | Sentiment Analysis | 21696 |
    | NLU | shopee_reviews_tagalog_seacrowd_text | fil | Sentiment Analysis | 2250 |
    | NLU | nusatranslation_senti_abs_seacrowd_text | abs | Sentiment Analysis | 500 |
    | NLU | nusatranslation_senti_btk_seacrowd_text | btx | Sentiment Analysis | 1200 |
    | NLU | nusatranslation_senti_bew_seacrowd_text | bew | Sentiment Analysis | 1200 |
    | NLU | nusatranslation_senti_bhp_seacrowd_text | bhp | Sentiment Analysis | 500 |
    | NLU | nusatranslation_senti_jav_seacrowd_text | jav | Sentiment Analysis | 1200 |
    | NLU | nusatranslation_senti_mad_seacrowd_text | mad | Sentiment Analysis | 1200 |
    | NLU | nusatranslation_senti_mak_seacrowd_text | mak | Sentiment Analysis | 1200 |
    | NLU | nusatranslation_senti_min_seacrowd_text | min | Sentiment Analysis | 1200 |
    | NLU | nusatranslation_senti_mui_seacrowd_text | mui | Sentiment Analysis | 500 |
    | NLU | nusatranslation_senti_rej_seacrowd_text | rej | Sentiment Analysis | 500 |
    | NLU | nusatranslation_senti_sun_seacrowd_text | sun | Sentiment Analysis | 1200 |
    | NLU | nusax_senti_ind_seacrowd_text | ind | Sentiment Analysis | 400 |
    | NLU | nusax_senti_ace_seacrowd_text | ace | Sentiment Analysis | 400 |
    | NLU | nusax_senti_jav_seacrowd_text | jav | Sentiment Analysis | 400 |
    | NLU | nusax_senti_sun_seacrowd_text | sun | Sentiment Analysis | 400 |
    | NLU | nusax_senti_min_seacrowd_text | min | Sentiment Analysis | 400 |
    | NLU | nusax_senti_bug_seacrowd_text | bug | Sentiment Analysis | 400 |
    | NLU | nusax_senti_bbc_seacrowd_text | bbc | Sentiment Analysis | 400 |
    | NLU | nusax_senti_ban_seacrowd_text | ban | Sentiment Analysis | 400 |
    | NLU | nusax_senti_nij_seacrowd_text | nij | Sentiment Analysis | 400 |
    | NLU | nusax_senti_mad_seacrowd_text | mad | Sentiment Analysis | 400 |
    | NLU | nusax_senti_bjn_seacrowd_text | bjn | Sentiment Analysis | 400 |
    | NLU | nusax_senti_eng_seacrowd_text | eng | Sentiment Analysis | 400 |
    | NLU | indonglish_seacrowd_text | ind | Sentiment Analysis | 1011 |
    | NLU | gklmip_newsclass_seacrowd_text | khm | Topic Classification | 1436 |
    | NLU | indonesian_news_dataset_seacrowd_text | ind | Topic Classification | 2627 |
    | NLU | uit_vion_seacrowd_text | vie | Topic Classification | 26000 |
    | NLU | sib_200_ace_Arab_seacrowd_text | ace | Topic Classification | 204 |
    | NLU | sib_200_ace_Latn_seacrowd_text | ace | Topic Classification | 204 |
    | NLU | sib_200_ban_Latn_seacrowd_text | ban | Topic Classification | 204 |
    | NLU | sib_200_bjn_Arab_seacrowd_text | bjn | Topic Classification | 204 |
    | NLU | sib_200_bjn_Latn_seacrowd_text | bjn | Topic Classification | 204 |
    | NLU | sib_200_bug_Latn_seacrowd_text | bug | Topic Classification | 204 |
    | NLU | sib_200_ceb_Latn_seacrowd_text | ceb | Topic Classification | 204 |
    | NLU | sib_200_ilo_Latn_seacrowd_text | ilo | Topic Classification | 204 |
    | NLU | sib_200_ind_Latn_seacrowd_text | ind | Topic Classification | 204 |
    | NLU | sib_200_jav_Latn_seacrowd_text | jav | Topic Classification | 204 |
    | NLU | sib_200_kac_Latn_seacrowd_text | kac | Topic Classification | 204 |
    | NLU | sib_200_khm_Khmr_seacrowd_text | khm | Topic Classification | 204 |
    | NLU | sib_200_lao_Laoo_seacrowd_text | lao | Topic Classification | 204 |
    | NLU | sib_200_lus_Latn_seacrowd_text | lus | Topic Classification | 204 |
    | NLU | sib_200_min_Arab_seacrowd_text | min | Topic Classification | 204 |
    | NLU | sib_200_min_Latn_seacrowd_text | min | Topic Classification | 204 |
    | NLU | sib_200_mya_Mymr_seacrowd_text | mya | Topic Classification | 204 |
    | NLU | sib_200_pag_Latn_seacrowd_text | pag | Topic Classification | 204 |
    | NLU | sib_200_shn_Mymr_seacrowd_text | shn | Topic Classification | 204 |
    | NLU | sib_200_sun_Latn_seacrowd_text | sun | Topic Classification | 204 |
    | NLU | sib_200_tgl_Latn_seacrowd_text | fil | Topic Classification | 204 |
    | NLU | sib_200_tha_Thai_seacrowd_text | tha | Topic Classification | 204 |
    | NLU | sib_200_vie_Latn_seacrowd_text | vie | Topic Classification | 204 |
    | NLU | sib_200_war_Latn_seacrowd_text | war | Topic Classification | 204 |
    | NLU | sib_200_zsm_Latn_seacrowd_text | zlm | Topic Classification | 204 |
    | NLU | nusaparagraph_topic_btk_seacrowd_text | btx | Topic Classification | 500 |
    | NLU | nusaparagraph_topic_bew_seacrowd_text | bew | Topic Classification | 800 |
    | NLU | nusaparagraph_topic_bug_seacrowd_text | bug | Topic Classification | 300 |
    | NLU | nusaparagraph_topic_jav_seacrowd_text | jav | Topic Classification | 800 |
    | NLU | nusaparagraph_topic_mad_seacrowd_text | mad | Topic Classification | 700 |
    | NLU | nusaparagraph_topic_mak_seacrowd_text | mak | Topic Classification | 700 |
    | NLU | nusaparagraph_topic_min_seacrowd_text | min | Topic Classification | 800 |
    | NLU | nusaparagraph_topic_mui_seacrowd_text | mui | Topic Classification | 400 |
    | NLU | nusaparagraph_topic_rej_seacrowd_text | rej | Topic Classification | 350 |
    | NLU | nusaparagraph_topic_sun_seacrowd_text | sun | Topic Classification | 900 |
    | NLU | emotes_3k_tgl_seacrowd_text | fil | Commonsense Reasoning | 2905 |
    | NLU | emotes_3k_eng_seacrowd_text | eng | Commonsense Reasoning | 2905 |
    | NLU | indo_story_cloze_seacrowd_qa | ind | Commonsense Reasoning | 1135 |
    | NLU | xstorycloze_id_seacrowd_qa | ind | Commonsense Reasoning | 1511 |
    | NLU | xstorycloze_my_seacrowd_qa | mya | Commonsense Reasoning | 1511 |
    | NLU | indommlu_ind_seacrowd_qa | ind | Standard Testing QA | 14979 |
    | NLU | indommlu_ban_seacrowd_qa | ban | Standard Testing QA | 14979 |
    | NLU | indommlu_mad_seacrowd_qa | mad | Standard Testing QA | 14979 |
    | NLU | indommlu_mak_seacrowd_qa | mak | Standard Testing QA | 14979 |
    | NLU | indommlu_sun_seacrowd_qa | sun | Standard Testing QA | 14979 |
    | NLU | indommlu_jav_seacrowd_qa | jav | Standard Testing QA | 14979 |
    | NLU | indommlu_bjn_seacrowd_qa | bjn | Standard Testing QA | 14979 |
    | NLU | indommlu_abl_seacrowd_qa | abl | Standard Testing QA | 14979 |
    | NLU | indommlu_nij_seacrowd_qa | nij | Standard Testing QA | 14979 |
    | NLU | seaeval_cross_mmlu_ind_seacrowd_qa | ind | Standard Testing QA | 150 |
    | NLU | seaeval_cross_mmlu_vie_seacrowd_qa | vie | Standard Testing QA | 150 |
    | NLU | seaeval_cross_mmlu_zlm_seacrowd_qa | zlm | Standard Testing QA | 150 |
    | NLU | seaeval_cross_mmlu_fil_seacrowd_qa | fil | Standard Testing QA | 150 |
    | NLU | seaeval_cross_logiqa_ind_seacrowd_qa | ind | Standard Testing QA | 176 |
    | NLU | seaeval_cross_logiqa_vie_seacrowd_qa | vie | Standard Testing QA | 176 |
    | NLU | seaeval_cross_logiqa_zlm_seacrowd_qa | zlm | Standard Testing QA | 176 |
    | NLU | seaeval_cross_logiqa_fil_seacrowd_qa | fil | Standard Testing QA | 176 |
    | NLU | m3exam_jav_seacrowd_qa | jav | Standard Testing QA | 371 |
    | NLU | m3exam_tha_seacrowd_qa | tha | Standard Testing QA | 2168 |
    | NLU | m3exam_vie_seacrowd_qa | vie | Standard Testing QA | 1789 |
    | NLU | okapi_m_arc_ind_seacrowd_qa | ind | Standard Testing QA | 1170 |
    | NLU | okapi_m_arc_vie_seacrowd_qa | vie | Standard Testing QA | 1170 |
    | NLU | copal_colloquial_seacrowd_qa | ind | Cultural QA | 559 |
    | NLU | xcopa_tha_seacrowd_qa | tha | Cultural QA | 500 |
    | NLU | xcopa_vie_seacrowd_qa | vie | Cultural QA | 500 |
    | NLU | xcopa_ind_seacrowd_qa | ind | Cultural QA | 500 |
    | NLU | seaeval_sg_eval_eng_seacrowd_qa | eng | Cultural QA | 103 |
    | NLU | seaeval_ph_eval_eng_seacrowd_qa | eng | Cultural QA | 100 |
    | NLU | mabl_ind_seacrowd_qa | ind | Cultural QA | 1140 |
    | NLU | mabl_jav_seacrowd_qa | jav | Cultural QA | 600 |
    | NLU | mabl_sun_seacrowd_qa | sun | Cultural QA | 600 |
    | NLU | belebele_ceb_latn_seacrowd_qa | ceb | Other QA | 900 |
    | NLU | belebele_ilo_latn_seacrowd_qa | ilo | Other QA | 900 |
    | NLU | belebele_ind_latn_seacrowd_qa | ind | Other QA | 900 |
    | NLU | belebele_jav_latn_seacrowd_qa | jav | Other QA | 900 |
    | NLU | belebele_kac_latn_seacrowd_qa | kac | Other QA | 900 |
    | NLU | belebele_khm_khmr_seacrowd_qa | khm | Other QA | 900 |
    | NLU | belebele_lao_laoo_seacrowd_qa | lao | Other QA | 900 |
    | NLU | belebele_mya_mymr_seacrowd_qa | mya | Other QA | 900 |
    | NLU | belebele_shn_mymr_seacrowd_qa | shn | Other QA | 900 |
    | NLU | belebele_sun_latn_seacrowd_qa | sun | Other QA | 900 |
    | NLU | belebele_tgl_latn_seacrowd_qa | fil | Other QA | 900 |
    | NLU | belebele_tha_thai_seacrowd_qa | tha | Other QA | 900 |
    | NLU | belebele_vie_latn_seacrowd_qa | vie | Other QA | 900 |
    | NLU | belebele_war_latn_seacrowd_qa | war | Other QA | 900 |
    | NLU | belebele_zsm_latn_seacrowd_qa | zlm | Other QA | 900 |
    | NLU | indonli_seacrowd_pairs | ind | NLI | 5183 |
    | NLU | wrete_seacrowd_pairs | ind | NLI | 100 |
    | NLU | snli_indo_seacrowd_pairs | ind | NLI | 9823 |
    | NLU | myxnli_seacrowd_pairs | mya | NLI | 5010 |
    | NLU | xnli.tha_seacrowd_pairs | tha | NLI | 5010 |
    | NLU | xnli.vie_seacrowd_pairs | vie | NLI | 5010 |
    | Speech | asr_ibsc_seacrowd_sptext | iba | ASR | 473 |
    | Speech | fleurs_vie_seacrowd_sptext | vie | ASR | 857 |
    | Speech | indspeech_newstra_ethnicsr_nooverlap_btk_seacrowd_sptext | btx | ASR | 1000 |
    | Speech | fleurs_ind_seacrowd_sptext | ind | ASR | 687 |
    | Speech | fleurs_lao_seacrowd_sptext | lao | ASR | 405 |
    | Speech | fleurs_zlm_seacrowd_sptext | zlm | ASR | 749 |
    | Speech | commonvoice_120_tha_seacrowd_sptext | tha | ASR | 10964 |
    | Speech | fleurs_mya_seacrowd_sptext | mya | ASR | 880 |
    | Speech | fleurs_fil_seacrowd_sptext | fil | ASR | 964 |
    | Speech | commonvoice_120_vie_seacrowd_sptext | vie | ASR | 1302 |
    | Speech | indspeech_newstra_ethnicsr_nooverlap_sun_seacrowd_sptext | sun | ASR | 1000 |
    | Speech | commonvoice_120_ind_seacrowd_sptext | ind | ASR | 3647 |
    | Speech | fleurs_ceb_seacrowd_sptext | ceb | ASR | 541 |
    | Speech | indspeech_newstra_ethnicsr_nooverlap_jav_seacrowd_sptext | jav | ASR | 1000 |
    | Speech | fleurs_khm_seacrowd_sptext | khm | ASR | 771 |
    | Speech | fleurs_jav_seacrowd_sptext | jav | ASR | 728 |
    | Speech | fleurs_tha_seacrowd_sptext | tha | ASR | 1021 |
    | Speech | indspeech_newstra_ethnicsr_nooverlap_ban_seacrowd_sptext | ban | ASR | 1000 |
    | Speech | commonvoice_120_cnh_seacrowd_sptext | cnh | ASR | 763 |
    | VL | xm3600_fil_seacrowd_imtext | fil | Image Captioning | 2760 |
    | VL | xm3600_id_seacrowd_imtext | ind | Image Captioning | 2775 |
    | VL | xm3600_th_seacrowd_imtext | tha | Image Captioning | 2798 |
    | VL | xm3600_vi_seacrowd_imtext | vie | Image Captioning | 2855 |
</details>

To run a model on our benchmark, simply take add the relevant model to our evaluation script(s):
- NLU
    - [`evaluation/run_nlu_prompt_batch.sh`](https://github.com/SEACrowd/seacrowd-experiments/blob/main/evaluation/run_nlu_prompt.sh) for open-source models
    - [`evaluation/run_nlu_prompt_batch_commercial.sh`](https://github.com/SEACrowd/seacrowd-experiments/blob/main/evaluation/run_nlu_prompt_commercial.sh) for commercial (API-based) models
- NLG
    - [`evaluation/run_nlg_prompt_batch.sh`](https://github.com/SEACrowd/seacrowd-experiments/blob/main/evaluation/run_nlg_prompt.sh) for open-source models
    - [`evaluation/run_nlg_prompt_batch_commercial.sh`](https://github.com/SEACrowd/seacrowd-experiments/blob/main/evaluation/run_nlg_prompt_commercial.sh) for commercial (API-based) models
- Speech
    - [`evaluation/run_speech_mms.sh`](https://github.com/SEACrowd/seacrowd-experiments/blob/main/evaluation/run_speech_mms.sh) for MMS-based models
    - [`evaluation/run_speech_seamless.sh`](https://github.com/SEACrowd/seacrowd-experiments/blob/main/evaluation/run_speech_seamless.sh) for Seamless-based models
    - [`evaluation/run_speech_wav2vec2_xlsr.sh`](https://github.com/SEACrowd/seacrowd-experiments/blob/main/evaluation/run_speech_wav2vec2_xlsr.sh) for Wav2Vec2-based models
    - [`evaluation/run_speech_whisper.sh`](https://github.com/SEACrowd/seacrowd-experiments/blob/main/evaluation/run_speech_seamless.sh) for Whisper-based models
- Vision-language
    - [`evaluation/run_vl_prompt.sh`](https://github.com/SEACrowd/seacrowd-experiments/blob/main/evaluation/run_vl_prompt.sh)

The evaluation run will create a log in `evaluation/outputs_*/` directory to record the model predictions/generations, and finally a summary of the performance measures per data subset in `evaluation/metrics_*/`.

> Note: If you want to modify the prompt templates, check out [`evaluation/prompt_utils.py`](https://github.com/SEACrowd/seacrowd-experiments/blob/main/evaluation/prompt_utils.py). If you want to modify the data subsets being used in the benchmark, check out [`evaluation/data_utils.py`](https://github.com/SEACrowd/seacrowd-experiments/blob/main/evaluation/data_utils.py).

### Evaluation Results

#### LLMs
<img width="940" alt="NLP Performance" src="https://github.com/SEACrowd/seacrowd-experiments/assets/eval-nlp.png">

#### Speech Models
<img width="940" alt="Speech Performance" src="https://github.com/SEACrowd/seacrowd-experiments/assets/eval-speech.png">

#### VLMs
<img width="940" alt="VL Performance" src="https://github.com/SEACrowd/seacrowd-experiments/assets/eval-vl.png">

## Generation Quality in SEA Languages: Translationese vs. Natural

Placed under [`translationese/`](https://github.com/SEACrowd/seacrowd-experiments/blob/main/translationese/).

To analyze the generation quality of LLMs in SEA languages, we build a text classifier to discriminate between translationese and natural texts. We construct a translationese classification training and testing dataset using 49 and 62 data subsets, respectively, covering approximately 39.9k and 51.5k sentences across 9 SEA languages: English (eng), Indonesian (ind), Khmer (khm), Lao (lao), Burmese (mya), Filipino (fil), Thai (tha), Vietnamese (vie), and Malay (zlm).

To fine-tune the translationese classifier, execute [`translationese/run.sh`](https://github.com/SEACrowd/seacrowd-experiments/blob/main/translationese/run.sh). We use a binary label (translationese, i.e., machine-translated or human-translated, or natural, i.e., human-generated) instead of 3 labels (machine-translated, human-translated, human-generated).

To obtain the model generations for the naturalness analysis, execute [`translationese/run_nlg_prompt.sh`](https://github.com/SEACrowd/seacrowd-experiments/blob/main/translationese/run_nlg_prompt.sh) for open-source models and [`translationese/run_nlg_prompt_commercial.sh`](https://github.com/SEACrowd/seacrowd-experiments/blob/main/translationese/run_nlg_prompt_commercial.sh) for commercial models.

To classify the model generations, check out [`translationese/analyze_translationese.ipynb`](https://github.com/SEACrowd/seacrowd-experiments/blob/main/translationese/analyze_translationese.ipynb).


### Naturalness Result

<img width="500" alt="Naturalness Result" src="https://github.com/SEACrowd/seacrowd-experiments/assets/naturalness-result.png">

## Additional Analysis: Language Equity, Resource Gaps, and Language Prioritization

The [`notebooks/viz_metrics.ipynb`](https://github.com/SEACrowd/seacrowd-experiments/blob/main/notebooks/viz_metrics.ipynb) consists of the visualization of all benchmark results in [`figures/`](https://github.com/SEACrowd/seacrowd-experiments/tree/main/figures) and [`notebooks/analysis/`](https://github.com/SEACrowd/seacrowd-experiments/tree/main/notebooks/analysis), as well as language equity results in terms of Gini coefficient in [`notebooks/analysis/`](https://github.com/SEACrowd/seacrowd-experiments/tree/main/notebooks/analysis).

The [`notebooks/viz_resources.ipynb`](https://github.com/SEACrowd/seacrowd-experiments/blob/main/notebooks/viz_resources.ipynb) consists of the visualization of resource gaps analysis in [`figures/`](https://github.com/SEACrowd/seacrowd-experiments/tree/main/figures) and [`notebooks/analysis/`](https://github.com/SEACrowd/seacrowd-experiments/tree/main/notebooks/analysis).

The [`globalutily/run_make_task_boxes.sh`](https://github.com/SEACrowd/globalutility/blob/main/run_make_task_boxes.sh) consists of the [visualization of SEA language prioritization analysis](https://github.com/SEACrowd/globalutility/tree/main/figs/final). This submodule is derived from [neubig/globalutility](https://github.com/neubig/globalutility).

# Citation

If you are using any resources from SEACrowd, including datasheets, dataloaders, code, etc., please cite the following publication:

```
Coming soon!
```