TASK_TO_PROMPT = {
    'eng': {
        # IndoMMLU-style (no nusacrowd Tasks yet)
        'IndoMMLU': [
            'This is a [SUBJECT] question for [LEVEL]. Choose one of the answers that is considered correct!\n\n[INPUT]\n[OPTION]\n\nAnswer: [LABEL_CHOICE]',
            'The following is a [SUBJECT] question for [LEVEL] level. Choose the right answer!\nQuestion:[INPUT]\nChoice: [OPTION]\nAnswer: [LABEL_CHOICE]',
            'Choose one of the most appropriate answers to answer the [SUBJECT] question for [LEVEL]!\nQuestion: [INPUT]\nChoice: [OPTION]\n\nAnswer: [LABEL_CHOICE]' 
            ],
        # Tasks.SENTIMENT_ANALYSIS
        'SA': [
            'Classify the sentiment of the text below.\n[INPUT] => Sentiment ([OPTIONS]): [LABEL_CHOICE]',
            'Predict the sentiment of the following text.\nText: [INPUT]\nAnswer with [OPTIONS]: [LABEL_CHOICE]',
            '[INPUT]\nWhat would be the sentiment of the text above? [OPTIONS]? [LABEL_CHOICE]',
            'What is the sentiment of this text?\nText: [INPUT]\nSentiment ([OPTIONS]): [LABEL_CHOICE]',
            'Text: [INPUT]\nPlease classify the sentiment of above text. Answer with [OPTIONS].\nSentiment: [LABEL_CHOICE]',
        ],
        # Tasks.EMOTION_CLASSIFICATION
        'EC': [
            'Classify the emotion of the text below.\n[INPUT] => Emotion ([OPTIONS]): [LABEL_CHOICE]',
            'Predict the emotion of the following text.\nText: [INPUT]\nAnswer with [OPTIONS]: [LABEL_CHOICE]',
            '[INPUT]\nWhat would be the emotion of the text above? [OPTIONS]? [LABEL_CHOICE]',
            'What is the emotion of this text?\nText: [INPUT]\nEmotion ([OPTIONS]): [LABEL_CHOICE]',
            'Text: [INPUT]\nPlease classify the emotion of above text. Answer with [OPTIONS].\nEmotion: [LABEL_CHOICE]',
        ],
        # Tasks.TEXTUAL_ENTAILMENT
        'TE': [
            'Hypothesis: [INPUT_A]\nPremise: [INPUT_B]\nQuestion: What is the relation between the hypothesis and the premise? [OPTIONS]? [LABEL_CHOICE]',
            'Given the following premise and hypothesis:\nHypothesis: [INPUT_A]\nPremise: [INPUT_B]\nDetermine the logical relationship (([OPTIONS])): [LABEL_CHOICE]',
            'Choose the most appropriate relationship ([OPTIONS]) between the premise and hypothesis:\nRelationship between "[INPUT_B]" and "[INPUT_A]": [LABEL_CHOICE]',
            'Identify the relationship between the premise and hypothesis:\nHypothesis: [INPUT_A]\nPremise: [INPUT_B]\nLabel ([OPTIONS]): [LABEL_CHOICE]',
            'Classify the relationship between the premise and hypothesis:\nPremise: [INPUT_B]\nHypothesis: [INPUT_A]\nRelationship ([OPTIONS]): [LABEL_CHOICE]',
        ],
        # Tasks.MACHINE_TRANSLATION
        'MT': [
            'Translate the following text from [SOURCE] to [TARGET].\nText: [INPUT]\nTranslation:',
            '[INPUT]\nTranslate the text above from [SOURCE] to [TARGET].',
            'Text in [SOURCE]: [INPUT]\nHow would you translate that in [TARGET]?',
            'Translate the following [SOURCE] text to [TARGET].\nText: [INPUT]\nTranslation:',
            'Text in [SOURCE]: [INPUT]\nText in [TARGET]:',
        ],
        # Tasks.QUESTION_ANSWERING
        'QA': [
            'Refer to the passage below and answer the following question:\nPassage: [CONTEXT]\nQuestion: [QUESTION]\nAnswer:',
            '[CONTEXT]\nBased on the above text, [QUESTION]',
            '[CONTEXT]\nQuestion: [QUESTION]\nReferring to the passage above, the correct answer to the given question is:',
            'Paragraph: [CONTEXT]\nQuestion: [QUESTION]\nBased on the paragraph, what is the answer to the question?',
            'Passage: [CONTEXT]\nQuestion: [QUESTION]\nAnswer:'
        ],
        # Tasks.SUMMARIZATION
        'SUM': [
            'Write a summary from of the following text.\nText: [INPUT]\nSummary:',
            '[INPUT]\nWrite a summary of the text above.',
            'Text: [INPUT]\nHow would you summarize this text?',
            'Summarize this text: [INPUT]\nSummary:',
            '[INPUT]\nGiven the above document, write one sentence to summarize:',
        ],
        # Tasks.TOPIC_MODELING
        'TL': [
            'Classify the topic of the text below.\n[INPUT] => Topic ([OPTIONS]): [LABEL_CHOICE]',
            'Predict the topic of the following text.\nText: [INPUT]\nAnswer with [OPTIONS]: [LABEL_CHOICE]',
            '[INPUT]\nWhat would be the topic of the text above? [OPTIONS]? [LABEL_CHOICE]',
            'What is the topic of this text?\nText: [INPUT]\nTopic ([OPTIONS]): [LABEL_CHOICE]',
            'Text: [INPUT]\nPlease classify the topic of above text. Answer with [OPTIONS].\nTopic: [LABEL_CHOICE]',
        ],
        # Tasks.MORALITY_CLASSIFICATION
        'MC': [
            'Classify the morality of the text below.\n[INPUT] => Morality ([OPTIONS]): [LABEL_CHOICE]',
            'Predict the morality of the following text.\nText: [INPUT]\nAnswer with [OPTIONS]: [LABEL_CHOICE]',
            '[INPUT]\nWhat would be the morality of the text above? [OPTIONS]? [LABEL_CHOICE]',
            'What is the morality of this text?\nText: [INPUT]\Morality ([OPTIONS]): [LABEL_CHOICE]',
            'Text: [INPUT]\nPlease classify the morality of above text. Answer with [OPTIONS].\Morality: [LABEL_CHOICE]',
        ],
        # # Tasks.COMMONSENSE_REASONING
        # 'CR': [
        #     'Answer the following question:\nQuestion: [QUESTION]\nAnswer:',
        #     '[CONTEXT]\nBased on the above text, [QUESTION]',
        #     '[CONTEXT]\nQuestion: [QUESTION]\nReferring to the passage above, the correct answer to the given question is:',
        #     'Paragraph: [CONTEXT]\nQuestion: [QUESTION]\nBased on the paragraph, what is the answer to the question?',
        #     'Passage: [CONTEXT]\nQuestion: [QUESTION]\nAnswer:'
        # ],
    },
    'ind': {
        # IndoMMLU-style (no nusacrowd Tasks yet)
        'IndoMMLU': [
            'Ini adalah soal [SUBJECT] untuk [LEVEL]. Pilihlah salah satu jawaban yang dianggap benar!\n\n[INPUT]\n[OPTION]\n\nJawaban: [LABEL_CHOICE]',
            'Berikut ini adalah soal [SUBJECT] untuk tingkat [LEVEL]. Pilih jawaban yang tepat!\nSoal:[INPUT]\nPilihan: [OPTION]\nJawaban: [LABEL_CHOICE]',
            'Pilihlah salah satu jawaban yang paling tepat untuk menjawab soal [SUBJECT] untuk [LEVEL] berikut!\nSoal: [INPUT]\nPilihan: [OPTION]\n\nJawaban: [LABEL_CHOICE]'
        ],
        # Tasks.SENTIMENT_ANALYSIS
        'SA': [
            'Klasifikasikan sentimen dari kalimat berikut.\n[INPUT] => Sentimen ([OPTIONS]): [LABEL_CHOICE]',
            'Prediksikan sentimen dari kalimat berikut.\nTeks: [INPUT]\nJawab dengan [OPTIONS]: [LABEL_CHOICE]',
            '[INPUT]\nApakah sentimen dari kalimat diatas? [OPTIONS]? [LABEL_CHOICE]',
            'Apakah sentimen dari teks berikut?\nTeks: [INPUT]\nSentimen ([OPTIONS]): [LABEL_CHOICE]',
            'Teks: [INPUT]\nTolong klasifikasikan sentimen dari teks diatas. Jawab dengan [OPTIONS].\nSentimen: [LABEL_CHOICE]',
        ],
        # Tasks.EMOTION_CLASSIFICATION
        'EC': [
            'Klasifikasikan emosi dari kalimat berikut.\n[INPUT] => Emosi ([OPTIONS]): [LABEL_CHOICE]',
            'Prediksikan emosi dari kalimat berikut.\nTeks: [INPUT]\nJawab dengan [OPTIONS]: [LABEL_CHOICE]',
            '[INPUT]\nApakah emosi dari kalimat diatas? [OPTIONS]? [LABEL_CHOICE]',
            'Apakah emosi dari teks berikut?\nTeks: [INPUT]\nEmosi ([OPTIONS]): [LABEL_CHOICE]',
            'Teks: [INPUT]\nTolong klasifikasikan emosi dari teks diatas. Jawab dengan [OPTIONS].\nEmosi: [LABEL_CHOICE]',
        ],
        # Tasks.TEXTUAL_ENTAILMENT
        'TE': [
            'Hipotesis: [INPUT_A]\nPremis: [INPUT_B]\nPertanaan: Apakah hubungan antara hipotesis dan premis diatas? [OPTIONS]? [LABEL_CHOICE]',
            'Diberikan hipotesis dan premis sebagai berikut:\nHipotesis: [INPUT_A]\nPremis: [INPUT_B]\nTentukan hubungan logis ([OPTIONS]) dari kedua kalimat tersebut: [LABEL_CHOICE]',
            'Pilih hubungan ([OPTIONS]) yang paling cocok antara premis dan hipotesis berikut:\nHubungan antara "[INPUT_B]" dan "[INPUT_A]": [LABEL_CHOICE]',
            'Identifikasi hubungan antara premis dan hipotesis berikut:\nHipotesis: [INPUT_A]\nPremis: [INPUT_B]\nLabel ([OPTIONS]): [LABEL_CHOICE]',
            'Klasifikasikan hubungan antara premis dan hypothesis berikut:\nPremis: [INPUT_B]\nHipotesis: [INPUT_A]\nHubungan ([OPTIONS]): [LABEL_CHOICE]',
        ],
        # Tasks.MACHINE_TRANSLATION
        'MT': [
            'Terjemahkan teks berikut dari bahasa [SOURCE] ke bahasa [TARGET].\nTeks: [INPUT]\nTerjemahan:',
            '[INPUT]\nTerjemahkan teks di atas dari bahasa [SOURCE] ke bahasa [TARGET].',
            'Teks dalam bahasa [SOURCE]: [INPUT]\nApa terjemahannya dalam bahasa [TARGET]?',
            'Terjemahkan teks bahasa [SOURCE] berikut ke bahasa [TARGET].\nTeks: [INPUT]\nTerjemahan:',
            'Teks dalam bahasa [SOURCE]: [INPUT]\nTeks dalam bahasa [TARGET]:',
        ],
        # Tasks.QUESTION_ANSWERING
        'QA': [
            'Lihat paragraf di bawah ini dan jawab pertanyaannya.\nParagraf: [CONTEXT]\nPertanyaan: [QUESTION]\nJawaban:',
            '[CONTEXT]\nBerdasarkan teks di atas, [QUESTION]',
            '[CONTEXT]\nQuestion: [QUESTION]\nMengacu pada teks di atas, jawaban yang benar untuk pertanyaan yang diberikan adalah:',
            'Paragraf: [CONTEXT]\nPertanyaan: [QUESTION]\nBerdasarkan paragraf di atas, apa jawaban dari pertanyaan yang diberikan?',
            'Teks: [CONTEXT]\nPertanyaan: [QUESTION]\nJawaban:'
        ],
        # Tasks.SUMMARIZATION
        'SUM': [
            'Tuliskan ringkasan dari teks berikut.\nTeks: [INPUT]\nRingkasan:',
            '[INPUT]\nTulis ringkasan dari teks di atas.',
            'Teks: [INPUT]\nApa ringkasan dari teks tersebut?',
            'Ringkaslah teks berikut: [INPUT]\nRingkasan:',
            '[INPUT]\nBerdasarkan dokumen di atas, tulis satu kalimat ringkasan:',
        ],
        # Tasks.TOPIC_MODELING
        'TL': [
            'Klasifikasikan topik dari kalimat berikut.\n[INPUT] => Topik ([OPTIONS]): [LABEL_CHOICE]',
            'Prediksikan topik dari kalimat berikut.\nTeks: [INPUT]\nJawab dengan [OPTIONS]: [LABEL_CHOICE]',
            '[INPUT]\nApakah topik dari kalimat diatas? [OPTIONS]? [LABEL_CHOICE]',
            'Apakah topik dari teks berikut?\nTeks: [INPUT]\nTopik ([OPTIONS]): [LABEL_CHOICE]',
            'Teks: [INPUT]\nTolong klasifikasikan topik dari teks diatas. Jawab dengan [OPTIONS].\nTopik: [LABEL_CHOICE]',
        ],
        # Tasks.MORALITY_CLASSIFICATION
        'MC': [
            'Klasifikasikan moralitas dari kalimat berikut.\n[INPUT] => Moralitas ([OPTIONS]): [LABEL_CHOICE]',
            'Prediksikan moralitas dari kalimat berikut.\nTeks: [INPUT]\nJawab dengan [OPTIONS]: [LABEL_CHOICE]',
            '[INPUT]\nApakah moralitas dari kalimat diatas? [OPTIONS]? [LABEL_CHOICE]',
            'Apakah moralitas dari teks berikut?\nTeks: [INPUT]\nMoralitas ([OPTIONS]): [LABEL_CHOICE]',
            'Teks: [INPUT]\nTolong klasifikasikan moralitas dari teks diatas. Jawab dengan [OPTIONS].\nMoralitas: [LABEL_CHOICE]',
        ],
    }
}

LABEL_LANG_MAP ={
    # Tasks.SENTIMENT_ANALYSIS
    'lazada_review_filipino_seacrowd_text': {
        'eng': {'1': 'very negative', '2': 'negative', '3': 'neutral', '4': 'positive', '5': 'very positive'},
        'ind': {'1': 'sangat negatif', '2': 'negatif', '3': 'netral', '4': 'positif', '5': 'sangat positif'},
    },
    'gklmip_sentiment_seacrowd_text': {
        'eng': {'1': 'very negative', '2': 'negative', '3': 'neutral', '4': 'positive', '5': 'very positive'},
        'ind': {'1': 'sangat negatif', '2': 'negatif', '3': 'netral', '4': 'positif', '5': 'sangat positif'},
    },
    'indolem_sentiment_seacrowd_text': {
        'eng': {'negative': 'negative', 'positive': 'positive'},
        'ind': {'negative': 'negatif', 'positive': 'positif'},
    },
    'id_sentiment_analysis_seacrowd_text': {
        'eng': {'-1': 'negative', '0': 'neutral', '1': 'positive'},
        'ind': {'-1': 'negatif', '0': 'netral', '1': 'positif'},
    },
    'karonese_sentiment_seacrowd_text': {
        'eng': {'negative': 'negative', 'neutral': 'neutral', 'positive': 'positive'},
        'ind': {'negative': 'negatif', 'neutral': 'netral', 'positive': 'positif'},
    },
    'wisesight_thai_sentiment_seacrowd_text': {
        'eng': {'pos': 'positive', 'neu': 'neutral', 'neg': 'negative', 'q': 'not applicable (question)'},
        'ind': {'pos': 'positif', 'neu': 'netral', 'neg': 'negatif', 'q': 'tidak berlaku (pertanyaan)'},
    },
    'wongnai_reviews_seacrowd_text': {
        'eng': {'1': 'very negative', '2': 'negative', '3': 'neutral', '4': 'positive', '5': 'very positive'},
        'ind': {'1': 'sangat negatif', '2': 'negatif', '3': 'netral', '4': 'positif', '5': 'sangat positif'},
    },
    'vlsp2016_sa_seacrowd_text': {
        'eng': {'POS': 'positive', 'NEU': 'neutral', 'NEG': 'negative'},
        'ind': {'POS': 'positif', 'NEU': 'netral', 'NEG': 'negatif'},
    },
    'typhoon_yolanda_tweets_seacrowd_text': {
        'eng': {'-1': 'negative', '0': 'neutral', '1': 'positive'},
        'ind': {'-1': 'negatif', '0': 'netral', '1': 'positif'},
    },
    # 'total_defense_meme_sentiment_seacrowd_text' - will be added later
    'smsa_seacrowd_text': {
        'eng': {'negative': 'negative', 'neutral': 'neutral', 'positive': 'positive'},
        'ind': {'negative': 'negatif', 'neutral': 'netral', 'positive': 'positif'},
    },
    'prdect_id_sentiment_seacrowd_text': {
        'eng': {'Negative': 'negative', 'Positive': 'positive'},
        'ind': {'Negative': 'negatif', 'Positive': 'positif'},
    },
    'id_sent_emo_mobile_apps_sentiment_seacrowd_text': {
        'eng': {'Negative': 'negative', 'Neutral': 'neutral', 'Positive': 'positive'},
        'ind': {'Negative': 'negatif', 'Neutral': 'netral', 'Positive': 'positif'},
    },
    'shopee_reviews_tagalog_seacrowd_qa': {
        'eng': {'0': 'very negative', '1': 'negative', '2': 'neutral', '3': 'positive', '4': 'very positive'},
        'ind': {'0': 'sangat negatif', '1': 'negatif', '2': 'netral', '3': 'positif', '4': 'sangat positif'},
    },
    'nusatranslation_senti_ind_seacrowd_text': {
        'eng': {'negative': 'negative', 'neutral': 'neutral', 'positive': 'positive'},
        'ind': {'negative': 'negatif', 'neutral': 'netral', 'positive': 'positif'},
    },
    'nusatranslation_senti_abs_seacrowd_text': {
        'eng': {'negative': 'negative', 'neutral': 'neutral', 'positive': 'positive'},
        'ind': {'negative': 'negatif', 'neutral': 'netral', 'positive': 'positif'},
    },
    'nusatranslation_senti_btk_seacrowd_text': {
        'eng': {'negative': 'negative', 'neutral': 'neutral', 'positive': 'positive'},
        'ind': {'negative': 'negatif', 'neutral': 'netral', 'positive': 'positif'},
    },
    'nusatranslation_senti_bew_seacrowd_text': {
        'eng': {'negative': 'negative', 'neutral': 'neutral', 'positive': 'positive'},
        'ind': {'negative': 'negatif', 'neutral': 'netral', 'positive': 'positif'},
    },
    'nusatranslation_senti_bhp_seacrowd_text': {
        'eng': {'negative': 'negative', 'neutral': 'neutral', 'positive': 'positive'},
        'ind': {'negative': 'negatif', 'neutral': 'netral', 'positive': 'positif'},
    },
    'nusatranslation_senti_jav_seacrowd_text': {
        'eng': {'negative': 'negative', 'neutral': 'neutral', 'positive': 'positive'},
        'ind': {'negative': 'negatif', 'neutral': 'netral', 'positive': 'positif'},
    },
    'nusatranslation_senti_mad_seacrowd_text': {
        'eng': {'negative': 'negative', 'neutral': 'neutral', 'positive': 'positive'},
        'ind': {'negative': 'negatif', 'neutral': 'netral', 'positive': 'positif'},
    },
    'nusatranslation_senti_mak_seacrowd_text': {
        'eng': {'negative': 'negative', 'neutral': 'neutral', 'positive': 'positive'},
        'ind': {'negative': 'negatif', 'neutral': 'netral', 'positive': 'positif'},
    },
    'nusatranslation_senti_min_seacrowd_text': {
        'eng': {'negative': 'negative', 'neutral': 'neutral', 'positive': 'positive'},
        'ind': {'negative': 'negatif', 'neutral': 'netral', 'positive': 'positif'},
    },
    'nusatranslation_senti_mui_seacrowd_text': {
        'eng': {'negative': 'negative', 'neutral': 'neutral', 'positive': 'positive'},
        'ind': {'negative': 'negatif', 'neutral': 'netral', 'positive': 'positif'},
    },
    'nusatranslation_senti_rej_seacrowd_text': {
        'eng': {'negative': 'negative', 'neutral': 'neutral', 'positive': 'positive'},
        'ind': {'negative': 'negatif', 'neutral': 'netral', 'positive': 'positif'},
    },
    'nusatranslation_senti_sun_seacrowd_text': {
        'eng': {'negative': 'negative', 'neutral': 'neutral', 'positive': 'positive'},
        'ind': {'negative': 'negatif', 'neutral': 'netral', 'positive': 'positif'},
    },
    'nusax_senti_ind_seacrowd_text': {
        'eng': {'negative': 'negative', 'neutral': 'neutral', 'positive': 'positive'},
        'ind': {'negative': 'negatif', 'neutral': 'netral', 'positive': 'positif'},
    },
    'nusax_senti_ace_seacrowd_text': {
        'eng': {'negative': 'negative', 'neutral': 'neutral', 'positive': 'positive'},
        'ind': {'negative': 'negatif', 'neutral': 'netral', 'positive': 'positif'},
    },
    'nusax_senti_jav_seacrowd_text': {
        'eng': {'negative': 'negative', 'neutral': 'neutral', 'positive': 'positive'},
        'ind': {'negative': 'negatif', 'neutral': 'netral', 'positive': 'positif'},
    },
    'nusax_senti_sun_seacrowd_text': {
        'eng': {'negative': 'negative', 'neutral': 'neutral', 'positive': 'positive'},
        'ind': {'negative': 'negatif', 'neutral': 'netral', 'positive': 'positif'},
    },
    'nusax_senti_min_seacrowd_text': {
        'eng': {'negative': 'negative', 'neutral': 'neutral', 'positive': 'positive'},
        'ind': {'negative': 'negatif', 'neutral': 'netral', 'positive': 'positif'},
    },
    'nusax_senti_bug_seacrowd_text': {
        'eng': {'negative': 'negative', 'neutral': 'neutral', 'positive': 'positive'},
        'ind': {'negative': 'negatif', 'neutral': 'netral', 'positive': 'positif'},
    },
    'nusax_senti_bbc_seacrowd_text': {
        'eng': {'negative': 'negative', 'neutral': 'neutral', 'positive': 'positive'},
        'ind': {'negative': 'negatif', 'neutral': 'netral', 'positive': 'positif'},
    },
    'nusax_senti_ban_seacrowd_text': {
        'eng': {'negative': 'negative', 'neutral': 'neutral', 'positive': 'positive'},
        'ind': {'negative': 'negatif', 'neutral': 'netral', 'positive': 'positif'},
    },
    'nusax_senti_nij_seacrowd_text': {
        'eng': {'negative': 'negative', 'neutral': 'neutral', 'positive': 'positive'},
        'ind': {'negative': 'negatif', 'neutral': 'netral', 'positive': 'positif'},
    },
    'nusax_senti_mad_seacrowd_text': {
        'eng': {'negative': 'negative', 'neutral': 'neutral', 'positive': 'positive'},
        'ind': {'negative': 'negatif', 'neutral': 'netral', 'positive': 'positif'},
    },
    'nusax_senti_bjn_seacrowd_text': {
        'eng': {'negative': 'negative', 'neutral': 'neutral', 'positive': 'positive'},
        'ind': {'negative': 'negatif', 'neutral': 'netral', 'positive': 'positif'},
    },
    'nusax_senti_eng_seacrowd_text': {
        'eng': {'negative': 'negative', 'neutral': 'neutral', 'positive': 'positive'},
        'ind': {'negative': 'negatif', 'neutral': 'netral', 'positive': 'positif'},
    },
    'indonglish_seacrowd_text': {
        'eng': {'Negatif': 'negative', 'Netral': 'neutral', 'Positif': 'positive'},
        'ind': {'Negatif': 'negatif', 'Netral': 'netral', 'Positif': 'positif'},
    },
    # Tasks.TOPIC_MODELING
    'gklmip_newsclass_seacrowd_text': {
        'eng': {"culture": "culture", "economic": "economic", "education": "education", "environment": "environment", "health": "health", "politics": "politics", "right": "right", "science": "science"},
        'ind': {"culture": "kebudayaan", "economic": "ekonomi", "education": "edukasi", "environment": "lingkungan", "health": "kesehatan", "politics": "politik", "right": "hak", "science": "sains"},
    },
    'indonesian_news_dataset_seacrowd_text': {
        'eng': {"bola": "soccer", "news": "news", "bisnis": "business", "tekno": "technology", "otomotif": "vehicle"},
        'ind': {"bola": "sepak bola", "news": "berita", "bisnis": "bisnis", "tekno": "teknologi", "otomotif": "otomotif"},
    },
    'uit_vion_seacrowd_text': {
        'eng': {0: 'technology', 1: 'travel', 2: 'education', 3: 'entertainment', 4: 'science', 5: 'business', 6: 'law', 7: 'health', 8: 'world', 9: 'sports', 10: 'news', 11: 'vehicle', 12: 'life'},
        'ind': {0: 'teknologi', 1: 'jalan-jalan', 2: 'edukasi', 3: 'hiburan', 4: 'sains', 5: 'bisnis', 6: 'hukum', 7: 'kesehatan', 8: 'dunia', 9: 'olahraga', 10: 'berita', 11: 'otomotif', 12: 'kehidupan sehari-hari'},
    },
    # total_defense_meme_topic_seacrowd_text - will be added later
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
    'nusaparagraph_topic_btk_seacrowd_text': {
        'eng': {'food & beverages': 'food & beverages', 'sports': 'sports', 'leisures': 'leisures', 'religion': 'religion', 'culture & heritage': 'culture & heritage', 'slice of life': 'slice of life', 'technology': 'technology', 'business': 'business'},
        'ind': {'food & beverages': 'makanan & minuman', 'sports': 'olahraga', 'leisures': 'aktivitas santai', 'religion': 'agama', 'culture & heritage': 'kebudayaan & sejarah', 'slice of life': 'kehidupan sehari-hari', 'technology': 'teknologi', 'business': 'bisnis'},
    },
    'nusaparagraph_topic_bew_seacrowd_text': {
        'eng': {'food & beverages': 'food & beverages', 'sports': 'sports', 'leisures': 'leisures', 'religion': 'religion', 'culture & heritage': 'culture & heritage', 'slice of life': 'slice of life', 'technology': 'technology', 'business': 'business'},
        'ind': {'food & beverages': 'makanan & minuman', 'sports': 'olahraga', 'leisures': 'aktivitas santai', 'religion': 'agama', 'culture & heritage': 'kebudayaan & sejarah', 'slice of life': 'kehidupan sehari-hari', 'technology': 'teknologi', 'business': 'bisnis'},
    },
    'nusaparagraph_topic_bug_seacrowd_text': {
        'eng': {'food & beverages': 'food & beverages', 'sports': 'sports', 'leisures': 'leisures', 'religion': 'religion', 'culture & heritage': 'culture & heritage', 'slice of life': 'slice of life', 'technology': 'technology', 'business': 'business'},
        'ind': {'food & beverages': 'makanan & minuman', 'sports': 'olahraga', 'leisures': 'aktivitas santai', 'religion': 'agama', 'culture & heritage': 'kebudayaan & sejarah', 'slice of life': 'kehidupan sehari-hari', 'technology': 'teknologi', 'business': 'bisnis'},
    },
    'nusaparagraph_topic_jav_seacrowd_text': {
        'eng': {'food & beverages': 'food & beverages', 'sports': 'sports', 'leisures': 'leisures', 'religion': 'religion', 'culture & heritage': 'culture & heritage', 'slice of life': 'slice of life', 'technology': 'technology', 'business': 'business'},
        'ind': {'food & beverages': 'makanan & minuman', 'sports': 'olahraga', 'leisures': 'aktivitas santai', 'religion': 'agama', 'culture & heritage': 'kebudayaan & sejarah', 'slice of life': 'kehidupan sehari-hari', 'technology': 'teknologi', 'business': 'bisnis'},
    },
    'nusaparagraph_topic_mad_seacrowd_text': {
        'eng': {'food & beverages': 'food & beverages', 'sports': 'sports', 'leisures': 'leisures', 'religion': 'religion', 'culture & heritage': 'culture & heritage', 'slice of life': 'slice of life', 'technology': 'technology', 'business': 'business'},
        'ind': {'food & beverages': 'makanan & minuman', 'sports': 'olahraga', 'leisures': 'aktivitas santai', 'religion': 'agama', 'culture & heritage': 'kebudayaan & sejarah', 'slice of life': 'kehidupan sehari-hari', 'technology': 'teknologi', 'business': 'bisnis'},
    },
    'nusaparagraph_topic_mak_seacrowd_text': {
        'eng': {'food & beverages': 'food & beverages', 'sports': 'sports', 'leisures': 'leisures', 'religion': 'religion', 'culture & heritage': 'culture & heritage', 'slice of life': 'slice of life', 'technology': 'technology', 'business': 'business'},
        'ind': {'food & beverages': 'makanan & minuman', 'sports': 'olahraga', 'leisures': 'aktivitas santai', 'religion': 'agama', 'culture & heritage': 'kebudayaan & sejarah', 'slice of life': 'kehidupan sehari-hari', 'technology': 'teknologi', 'business': 'bisnis'},
    },
    'nusaparagraph_topic_min_seacrowd_text': {
        'eng': {'food & beverages': 'food & beverages', 'sports': 'sports', 'leisures': 'leisures', 'religion': 'religion', 'culture & heritage': 'culture & heritage', 'slice of life': 'slice of life', 'technology': 'technology', 'business': 'business'},
        'ind': {'food & beverages': 'makanan & minuman', 'sports': 'olahraga', 'leisures': 'aktivitas santai', 'religion': 'agama', 'culture & heritage': 'kebudayaan & sejarah', 'slice of life': 'kehidupan sehari-hari', 'technology': 'teknologi', 'business': 'bisnis'},
    },
    'nusaparagraph_topic_mui_seacrowd_text': {
        'eng': {'food & beverages': 'food & beverages', 'sports': 'sports', 'leisures': 'leisures', 'religion': 'religion', 'culture & heritage': 'culture & heritage', 'slice of life': 'slice of life', 'technology': 'technology', 'business': 'business'},
        'ind': {'food & beverages': 'makanan & minuman', 'sports': 'olahraga', 'leisures': 'aktivitas santai', 'religion': 'agama', 'culture & heritage': 'kebudayaan & sejarah', 'slice of life': 'kehidupan sehari-hari', 'technology': 'teknologi', 'business': 'bisnis'},
    },
    'nusaparagraph_topic_rej_seacrowd_text': {
        'eng': {'food & beverages': 'food & beverages', 'sports': 'sports', 'leisures': 'leisures', 'religion': 'religion', 'culture & heritage': 'culture & heritage', 'slice of life': 'slice of life', 'technology': 'technology', 'business': 'business'},
        'ind': {'food & beverages': 'makanan & minuman', 'sports': 'olahraga', 'leisures': 'aktivitas santai', 'religion': 'agama', 'culture & heritage': 'kebudayaan & sejarah', 'slice of life': 'kehidupan sehari-hari', 'technology': 'teknologi', 'business': 'bisnis'},
    },
    'nusaparagraph_topic_sun_seacrowd_text': {
        'eng': {'food & beverages': 'food & beverages', 'sports': 'sports', 'leisures': 'leisures', 'religion': 'religion', 'culture & heritage': 'culture & heritage', 'slice of life': 'slice of life', 'technology': 'technology', 'business': 'business'},
        'ind': {'food & beverages': 'makanan & minuman', 'sports': 'olahraga', 'leisures': 'aktivitas santai', 'religion': 'agama', 'culture & heritage': 'kebudayaan & sejarah', 'slice of life': 'kehidupan sehari-hari', 'technology': 'teknologi', 'business': 'bisnis'},
    },
    # # Tasks.MORALITY_CLASSIFICATION
    # 'emotes_3k_tgl_seacrowd_qa': {
    #     'eng': {'Moral': 'moral', 'Immoral': 'immoral'},
    #     'ind': {'Moral': 'bermoral', 'Immoral': 'tidak bermoral'},
    # },
    # 'emotes_3k_eng_seacrowd_qa': {
    #     'eng': {'Moral': 'moral', 'Immoral': 'immoral'},
    #     'ind': {'Moral': 'bermoral', 'Immoral': 'tidak bermoral'},
    # },

}

LANG_MAP = {
    'eng': {
        'ind': 'Indonesian',
        'xdy': 'Dayak',
        'bug': 'Buginese',
        'mad': 'Madurese',
        'bjn': 'Banjarese',
        'tiociu': 'Tiociu',
        'jav': 'Javanese',
        'sun': 'Sundanese',
        'ace': 'Acehnese',
        'ban': 'Balinese',
        'min': 'Minangkabau'
    },
    'ind': {
        'ind': 'Indonesia',
        'xdy': 'Dayak',
        'bug': 'Bugis',
        'mad': 'Madura',
        'bjn': 'Banjar',
        'tiociu': 'Tiociu',
        'jav': 'Jawa',
        'sun': 'Sunda',
        'ace': 'Aceh',
        'ban': 'Bali',
        'min': 'Minangkabau'
    }
}

def get_label_mapping(dset_subset, prompt_lang):
    return LABEL_LANG_MAP[dset_subset][prompt_lang]

def get_lang_name(prompt_lang, lang_code):
    return LANG_MAP[prompt_lang][lang_code]

def get_prompt(prompt_lang):
    prompt_templates = {}
    for config, prompts in TASK_TO_PROMPT[prompt_lang].items():
        prompt_templates[config] = prompts
    return prompt_templates
