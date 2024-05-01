TASK_TO_PROMPT = {
    'eng': {
        # Tasks.SENTIMENT_ANALYSIS
        'SA': [
            'Classify the sentiment of the text below.\n[INPUT] => Sentiment ([OPTIONS]): [LABEL_CHOICE]',
            'Predict the sentiment of the following text.\nText: [INPUT]\nAnswer with [OPTIONS]: [LABEL_CHOICE]',
            '[INPUT]\nWhat would be the sentiment of the text above? [OPTIONS]? [LABEL_CHOICE]',
        ],
        # Tasks.EMOTION_CLASSIFICATION
        'EC': [
            'Classify the emotion of the text below.\n[INPUT] => Emotion ([OPTIONS]): [LABEL_CHOICE]',
            'Predict the emotion of the following text.\nText: [INPUT]\nAnswer with [OPTIONS]: [LABEL_CHOICE]',
            '[INPUT]\nWhat would be the emotion of the text above? [OPTIONS]? [LABEL_CHOICE]',
        ],
        # Tasks.TEXTUAL_ENTAILMENT
        'TE': [
            'Hypothesis: [INPUT_A]\nPremise: [INPUT_B]\nQuestion: What is the relation between the hypothesis and the premise? [OPTIONS]? [LABEL_CHOICE]',
            'Given the following premise and hypothesis:\nHypothesis: [INPUT_A]\nPremise: [INPUT_B]\nDetermine the logical relationship (([OPTIONS])): [LABEL_CHOICE]',
            'Choose the most appropriate relationship ([OPTIONS]) between the premise and hypothesis:\nRelationship between "[INPUT_B]" and "[INPUT_A]": [LABEL_CHOICE]',
        ],
        # Tasks.MACHINE_TRANSLATION
        'MT': [
            'Translate the following text from [SOURCE] to [TARGET].\nText: [INPUT]\nTranslation:',
            '[INPUT]\nTranslate the text above from [SOURCE] to [TARGET].',
            'Text in [SOURCE]: [INPUT]\nHow would you translate that in [TARGET]?',
        ],
        # Tasks.QUESTION_ANSWERING
        'QA': [
            'Refer to the passage below and answer the following question:\nPassage: [CONTEXT]\nQuestion: [QUESTION\nChoices: [ANSWER_CHOICES]\nAnswer: [LABEL_CHOICE]',
            '[CONTEXT]\nBased on the above text, [QUESTION]\nChoices: [ANSWER_CHOICES]\nAnswer: [LABEL_CHOICE]',
            '[CONTEXT]\nQuestion: [QUESTION]\nChoices:[ANSWER_CHOICES]\nReferring to the passage above, the correct answer to the given question is: [LABEL_CHOICE]',
        ],
        # Tasks.SUMMARIZATION
        'SUM': [
            'Write a summary from of the following text.\nText: [INPUT]\nSummary:',
            '[INPUT]\nWrite a summary of the text above.',
            'Text: [INPUT]\nHow would you summarize this text?',
        ],
        # Tasks.TOPIC_MODELING
        'TL': [
            'Classify the topic of the text below.\n[INPUT] => Topic ([OPTIONS]): [LABEL_CHOICE]',
            'Predict the topic of the following text.\nText: [INPUT]\nAnswer with [OPTIONS]: [LABEL_CHOICE]',
            '[INPUT]\nWhat would be the topic of the text above? [OPTIONS]? [LABEL_CHOICE]',
        ],
        # Tasks.MORALITY_CLASSIFICATION
        'MC': [
            'Classify the morality of the text below.\n[INPUT] => Morality ([OPTIONS]): [LABEL_CHOICE]',
            'Predict the morality of the following text.\nText: [INPUT]\nAnswer with [OPTIONS]: [LABEL_CHOICE]',
            '[INPUT]\nWhat would be the morality of the text above? [OPTIONS]? [LABEL_CHOICE]',
        ],
        # Tasks.COMMONSENSE_REASONING
        'CR': [
            'Question: [QUESTION]\nWhat reply makes more sense to answer this question?\nChoices: [ANSWER_CHOICES]\nAnswer: [LABEL_CHOICE]',
            'Based on the the following question: "[QUESTION]" and choices: [ANSWER_CHOICES], the correct answer is: [LABEL_CHOICE]',
            'Question: [QUESTION]\nChoices: [ANSWER_CHOICES]\nThe correct answer to the given question is: [LABEL_CHOICE]',
        ],
        # Tasks.LANGUAGE_IDENTIFICATION
        'LI': [
            'Classify the language of the text below.\n[INPUT] => [LABEL_CHOICE]',
            'Predict the language of the following text.\nText: [INPUT]\nAnswer: [LABEL_CHOICE]',
            '[INPUT]\nWhat would be the language of the text above? [LABEL_CHOICE]',
        ],
    },
    'ind': {
        # Tasks.SENTIMENT_ANALYSIS
        'SA': [
            'Klasifikasikan sentimen dari kalimat berikut.\n[INPUT] => Sentimen ([OPTIONS]): [LABEL_CHOICE]',
            'Prediksikan sentimen dari kalimat berikut.\nTeks: [INPUT]\nJawab dengan [OPTIONS]: [LABEL_CHOICE]',
            '[INPUT]\nApakah sentimen dari kalimat diatas? [OPTIONS]? [LABEL_CHOICE]',
        ],
        # Tasks.EMOTION_CLASSIFICATION
        'EC': [
            'Klasifikasikan emosi dari kalimat berikut.\n[INPUT] => Emosi ([OPTIONS]): [LABEL_CHOICE]',
            'Prediksikan emosi dari kalimat berikut.\nTeks: [INPUT]\nJawab dengan [OPTIONS]: [LABEL_CHOICE]',
            '[INPUT]\nApakah emosi dari kalimat diatas? [OPTIONS]? [LABEL_CHOICE]',
        ],
        # Tasks.TEXTUAL_ENTAILMENT
        'TE': [
            'Hipotesis: [INPUT_A]\nPremis: [INPUT_B]\nPertanaan: Apakah hubungan antara hipotesis dan premis diatas? [OPTIONS]? [LABEL_CHOICE]',
            'Diberikan hipotesis dan premis sebagai berikut:\nHipotesis: [INPUT_A]\nPremis: [INPUT_B]\nTentukan hubungan logis ([OPTIONS]) dari kedua kalimat tersebut: [LABEL_CHOICE]',
            'Pilih hubungan ([OPTIONS]) yang paling cocok antara premis dan hipotesis berikut:\nHubungan antara "[INPUT_B]" dan "[INPUT_A]": [LABEL_CHOICE]',
        ],
        # Tasks.MACHINE_TRANSLATION
        'MT': [
            'Terjemahkan teks berikut dari bahasa [SOURCE] ke bahasa [TARGET].\nTeks: [INPUT]\nTerjemahan:',
            '[INPUT]\nTerjemahkan teks di atas dari bahasa [SOURCE] ke bahasa [TARGET].',
            'Teks dalam bahasa [SOURCE]: [INPUT]\nApa terjemahannya dalam bahasa [TARGET]?',
        ],
        # Tasks.QUESTION_ANSWERING
        'QA': [
            'Lihat paragraf di bawah ini dan jawab pertanyaannya.\nParagraf: [CONTEXT]\nPertanyaan: [QUESTION]\nPilihan: [ANSWER_CHOICES]\nJawaban: [LABEL_CHOICE]',
            '[CONTEXT]\nBerdasarkan teks di atas, [QUESTION]\nPilihan: [ANSWER_CHOICES]\nJawaban: [LABEL_CHOICE]',
            '[CONTEXT]\nPertanyaan: [QUESTION]\nPilihan: [ANSWER_CHOICES]\nMengacu pada teks di atas, jawaban yang benar untuk pertanyaan yang diberikan adalah: [LABEL_CHOICE]',
        ],
        # Tasks.SUMMARIZATION
        'SUM': [
            'Tuliskan ringkasan dari teks berikut.\nTeks: [INPUT]\nRingkasan:',
            '[INPUT]\nTulis ringkasan dari teks di atas.',
            'Teks: [INPUT]\nApa ringkasan dari teks tersebut?',
        ],
        # Tasks.TOPIC_MODELING
        'TL': [
            'Klasifikasikan topik dari kalimat berikut.\n[INPUT] => Topik ([OPTIONS]): [LABEL_CHOICE]',
            'Prediksikan topik dari kalimat berikut.\nTeks: [INPUT]\nJawab dengan [OPTIONS]: [LABEL_CHOICE]',
            '[INPUT]\nApakah topik dari kalimat diatas? [OPTIONS]? [LABEL_CHOICE]',
        ],
        # Tasks.MORALITY_CLASSIFICATION
        'MC': [
            'Klasifikasikan moralitas dari kalimat berikut.\n[INPUT] => Moralitas ([OPTIONS]): [LABEL_CHOICE]',
            'Prediksikan moralitas dari kalimat berikut.\nTeks: [INPUT]\nJawab dengan [OPTIONS]: [LABEL_CHOICE]',
            '[INPUT]\nApakah moralitas dari kalimat diatas? [OPTIONS]? [LABEL_CHOICE]',
        ],
        # Tasks.COMMONSENSE_REASONING
        'CR': [
            'Pertanyaan: [QUESTION]\nBalasan apa yang lebih masuk akal untuk menjawab pertanyaan tersebut?\nPilihan: [ANSWER_CHOICES]\nJawaban: [LABEL_CHOICE]',
            'Berdasarkan pertanyaan berikut: "[QUESTION]" dan pilihan: [ANSWER_CHOICES], jawaban yang benar adalah: [LABEL_CHOICE]',
            'Pertanyaan: [QUESTION]\nPilihan: [ANSWER_CHOICES]\nJawaban yang benar untuk pertanyaan tersebut adalah: [LABEL_CHOICE]',
        ],
        # Tasks.LANGUAGE_IDENTIFICATION
        'LI': [
            'Klasifikasikan bahasa dari kalimat berikut.\n[INPUT] => Bahasa [LABEL_CHOICE]',
            'Prediksikan bahasa dari kalimat berikut.\nTeks: [INPUT]\nJawaban: [LABEL_CHOICE]',
            '[INPUT]\nApakah bahasa dari kalimat diatas? [LABEL_CHOICE]',
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
    'shopee_reviews_tagalog_seacrowd_text': {
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
    'sib_200_ace_Arab_seacrowd_text': {
        'eng': {"geography": "geography", "science/technology": "science/technology", "health": "health", "travel": "travel", "entertainment": "entertainment", "politics": "politics", "sports": "sports"},
        'ind': {"geography": "geografi", "science/technology": "sains & teknologi", "health": "kesehatan", "travel": "jalan-jalan", "entertainment": "hiburan", "politics": "politik", "sports": "olahraga"},
    },
    'sib_200_ace_Latn_seacrowd_text': {
        'eng': {"geography": "geography", "science/technology": "science/technology", "health": "health", "travel": "travel", "entertainment": "entertainment", "politics": "politics", "sports": "sports"},
        'ind': {"geography": "geografi", "science/technology": "sains & teknologi", "health": "kesehatan", "travel": "jalan-jalan", "entertainment": "hiburan", "politics": "politik", "sports": "olahraga"},
    },
    'sib_200_ban_Latn_seacrowd_text': {
        'eng': {"geography": "geography", "science/technology": "science/technology", "health": "health", "travel": "travel", "entertainment": "entertainment", "politics": "politics", "sports": "sports"},
        'ind': {"geography": "geografi", "science/technology": "sains & teknologi", "health": "kesehatan", "travel": "jalan-jalan", "entertainment": "hiburan", "politics": "politik", "sports": "olahraga"},
    },
    'sib_200_bjn_Arab_seacrowd_text': {
        'eng': {"geography": "geography", "science/technology": "science/technology", "health": "health", "travel": "travel", "entertainment": "entertainment", "politics": "politics", "sports": "sports"},
        'ind': {"geography": "geografi", "science/technology": "sains & teknologi", "health": "kesehatan", "travel": "jalan-jalan", "entertainment": "hiburan", "politics": "politik", "sports": "olahraga"},
    },
    'sib_200_bjn_Latn_seacrowd_text': {
        'eng': {"geography": "geography", "science/technology": "science/technology", "health": "health", "travel": "travel", "entertainment": "entertainment", "politics": "politics", "sports": "sports"},
        'ind': {"geography": "geografi", "science/technology": "sains & teknologi", "health": "kesehatan", "travel": "jalan-jalan", "entertainment": "hiburan", "politics": "politik", "sports": "olahraga"},
    },
    'sib_200_bug_Latn_seacrowd_text': {
        'eng': {"geography": "geography", "science/technology": "science/technology", "health": "health", "travel": "travel", "entertainment": "entertainment", "politics": "politics", "sports": "sports"},
        'ind': {"geography": "geografi", "science/technology": "sains & teknologi", "health": "kesehatan", "travel": "jalan-jalan", "entertainment": "hiburan", "politics": "politik", "sports": "olahraga"},
    },
    'sib_200_ceb_Latn_seacrowd_text': {
        'eng': {"geography": "geography", "science/technology": "science/technology", "health": "health", "travel": "travel", "entertainment": "entertainment", "politics": "politics", "sports": "sports"},
        'ind': {"geography": "geografi", "science/technology": "sains & teknologi", "health": "kesehatan", "travel": "jalan-jalan", "entertainment": "hiburan", "politics": "politik", "sports": "olahraga"},
    },
    'sib_200_ilo_Latn_seacrowd_text': {
        'eng': {"geography": "geography", "science/technology": "science/technology", "health": "health", "travel": "travel", "entertainment": "entertainment", "politics": "politics", "sports": "sports"},
        'ind': {"geography": "geografi", "science/technology": "sains & teknologi", "health": "kesehatan", "travel": "jalan-jalan", "entertainment": "hiburan", "politics": "politik", "sports": "olahraga"},
    },
    'sib_200_ind_Latn_seacrowd_text': {
        'eng': {"geography": "geography", "science/technology": "science/technology", "health": "health", "travel": "travel", "entertainment": "entertainment", "politics": "politics", "sports": "sports"},
        'ind': {"geography": "geografi", "science/technology": "sains & teknologi", "health": "kesehatan", "travel": "jalan-jalan", "entertainment": "hiburan", "politics": "politik", "sports": "olahraga"},
    },
    'sib_200_jav_Latn_seacrowd_text': {
        'eng': {"geography": "geography", "science/technology": "science/technology", "health": "health", "travel": "travel", "entertainment": "entertainment", "politics": "politics", "sports": "sports"},
        'ind': {"geography": "geografi", "science/technology": "sains & teknologi", "health": "kesehatan", "travel": "jalan-jalan", "entertainment": "hiburan", "politics": "politik", "sports": "olahraga"},
    },
    'sib_200_kac_Latn_seacrowd_text': {
        'eng': {"geography": "geography", "science/technology": "science/technology", "health": "health", "travel": "travel", "entertainment": "entertainment", "politics": "politics", "sports": "sports"},
        'ind': {"geography": "geografi", "science/technology": "sains & teknologi", "health": "kesehatan", "travel": "jalan-jalan", "entertainment": "hiburan", "politics": "politik", "sports": "olahraga"},
    },
    'sib_200_khm_Khmr_seacrowd_text': {
        'eng': {"geography": "geography", "science/technology": "science/technology", "health": "health", "travel": "travel", "entertainment": "entertainment", "politics": "politics", "sports": "sports"},
        'ind': {"geography": "geografi", "science/technology": "sains & teknologi", "health": "kesehatan", "travel": "jalan-jalan", "entertainment": "hiburan", "politics": "politik", "sports": "olahraga"},
    },
    'sib_200_lao_Laoo_seacrowd_text': {
        'eng': {"geography": "geography", "science/technology": "science/technology", "health": "health", "travel": "travel", "entertainment": "entertainment", "politics": "politics", "sports": "sports"},
        'ind': {"geography": "geografi", "science/technology": "sains & teknologi", "health": "kesehatan", "travel": "jalan-jalan", "entertainment": "hiburan", "politics": "politik", "sports": "olahraga"},
    },
    'sib_200_lus_Latn_seacrowd_text': {
        'eng': {"geography": "geography", "science/technology": "science/technology", "health": "health", "travel": "travel", "entertainment": "entertainment", "politics": "politics", "sports": "sports"},
        'ind': {"geography": "geografi", "science/technology": "sains & teknologi", "health": "kesehatan", "travel": "jalan-jalan", "entertainment": "hiburan", "politics": "politik", "sports": "olahraga"},
    },
    'sib_200_min_Arab_seacrowd_text': {
        'eng': {"geography": "geography", "science/technology": "science/technology", "health": "health", "travel": "travel", "entertainment": "entertainment", "politics": "politics", "sports": "sports"},
        'ind': {"geography": "geografi", "science/technology": "sains & teknologi", "health": "kesehatan", "travel": "jalan-jalan", "entertainment": "hiburan", "politics": "politik", "sports": "olahraga"},
    },
    'sib_200_min_Latn_seacrowd_text': {
        'eng': {"geography": "geography", "science/technology": "science/technology", "health": "health", "travel": "travel", "entertainment": "entertainment", "politics": "politics", "sports": "sports"},
        'ind': {"geography": "geografi", "science/technology": "sains & teknologi", "health": "kesehatan", "travel": "jalan-jalan", "entertainment": "hiburan", "politics": "politik", "sports": "olahraga"},
    },
    'sib_200_mya_Mymr_seacrowd_text': {
        'eng': {"geography": "geography", "science/technology": "science/technology", "health": "health", "travel": "travel", "entertainment": "entertainment", "politics": "politics", "sports": "sports"},
        'ind': {"geography": "geografi", "science/technology": "sains & teknologi", "health": "kesehatan", "travel": "jalan-jalan", "entertainment": "hiburan", "politics": "politik", "sports": "olahraga"},
    },
    'sib_200_pag_Latn_seacrowd_text': {
        'eng': {"geography": "geography", "science/technology": "science/technology", "health": "health", "travel": "travel", "entertainment": "entertainment", "politics": "politics", "sports": "sports"},
        'ind': {"geography": "geografi", "science/technology": "sains & teknologi", "health": "kesehatan", "travel": "jalan-jalan", "entertainment": "hiburan", "politics": "politik", "sports": "olahraga"},
    },
    'sib_200_shn_Mymr_seacrowd_text': {
        'eng': {"geography": "geography", "science/technology": "science/technology", "health": "health", "travel": "travel", "entertainment": "entertainment", "politics": "politics", "sports": "sports"},
        'ind': {"geography": "geografi", "science/technology": "sains & teknologi", "health": "kesehatan", "travel": "jalan-jalan", "entertainment": "hiburan", "politics": "politik", "sports": "olahraga"},
    },
    'sib_200_sun_Latn_seacrowd_text': {
        'eng': {"geography": "geography", "science/technology": "science/technology", "health": "health", "travel": "travel", "entertainment": "entertainment", "politics": "politics", "sports": "sports"},
        'ind': {"geography": "geografi", "science/technology": "sains & teknologi", "health": "kesehatan", "travel": "jalan-jalan", "entertainment": "hiburan", "politics": "politik", "sports": "olahraga"},
    },
    'sib_200_tgl_Latn_seacrowd_text': {
        'eng': {"geography": "geography", "science/technology": "science/technology", "health": "health", "travel": "travel", "entertainment": "entertainment", "politics": "politics", "sports": "sports"},
        'ind': {"geography": "geografi", "science/technology": "sains & teknologi", "health": "kesehatan", "travel": "jalan-jalan", "entertainment": "hiburan", "politics": "politik", "sports": "olahraga"},
    },
    'sib_200_tha_Thai_seacrowd_text': {
        'eng': {"geography": "geography", "science/technology": "science/technology", "health": "health", "travel": "travel", "entertainment": "entertainment", "politics": "politics", "sports": "sports"},
        'ind': {"geography": "geografi", "science/technology": "sains & teknologi", "health": "kesehatan", "travel": "jalan-jalan", "entertainment": "hiburan", "politics": "politik", "sports": "olahraga"},
    },
    'sib_200_vie_Latn_seacrowd_text': {
        'eng': {"geography": "geography", "science/technology": "science/technology", "health": "health", "travel": "travel", "entertainment": "entertainment", "politics": "politics", "sports": "sports"},
        'ind': {"geography": "geografi", "science/technology": "sains & teknologi", "health": "kesehatan", "travel": "jalan-jalan", "entertainment": "hiburan", "politics": "politik", "sports": "olahraga"},
    },
    'sib_200_war_Latn_seacrowd_text': {
        'eng': {"geography": "geography", "science/technology": "science/technology", "health": "health", "travel": "travel", "entertainment": "entertainment", "politics": "politics", "sports": "sports"},
        'ind': {"geography": "geografi", "science/technology": "sains & teknologi", "health": "kesehatan", "travel": "jalan-jalan", "entertainment": "hiburan", "politics": "politik", "sports": "olahraga"},
    },
    'sib_200_zsm_Latn_seacrowd_text': {
        'eng': {"geography": "geography", "science/technology": "science/technology", "health": "health", "travel": "travel", "entertainment": "entertainment", "politics": "politics", "sports": "sports"},
        'ind': {"geography": "geografi", "science/technology": "sains & teknologi", "health": "kesehatan", "travel": "jalan-jalan", "entertainment": "hiburan", "politics": "politik", "sports": "olahraga"},
    },
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
    # Tasks.MORALITY_CLASSIFICATION
    'emotes_3k_tgl_seacrowd_text': {
        'eng': {'Moral': 'moral', 'Immoral': 'immoral'},
        'ind': {'Moral': 'bermoral', 'Immoral': 'tidak bermoral'},
    },
    'emotes_3k_eng_seacrowd_text': {
        'eng': {'Moral': 'moral', 'Immoral': 'immoral'},
        'ind': {'Moral': 'bermoral', 'Immoral': 'tidak bermoral'},
    },
    # # Tasks.QUESTION_ANSWERING & Tasks.COMMONSENSE_REASONING - no need
    "indo_story_cloze_seacrowd_qa": {
        'eng': {0: 'a', 1: 'b'},
        'ind': {0: 'a', 1: 'b'},
    },
    "xstorycloze_id_seacrowd_qa": {
        'eng': {0: 'a', 1: 'b'},
        'ind': {0: 'a', 1: 'b'},
    },
    "xstorycloze_my_seacrowd_qa": {
        'eng': {0: 'a', 1: 'b'},
        'ind': {0: 'a', 1: 'b'},
    },
    "indommlu_ind_seacrowd_qa": {
        'eng': {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e'},
        'ind': {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e'},
    },
    "indommlu_ban_seacrowd_qa": {
        'eng': {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e'},
        'ind': {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e'},
    },
    "indommlu_mad_seacrowd_qa": {
        'eng': {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e'},
        'ind': {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e'},
    },
    "indommlu_mak_seacrowd_qa": {
        'eng': {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e'},
        'ind': {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e'},
    },
    "indommlu_sun_seacrowd_qa": {
        'eng': {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e'},
        'ind': {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e'},
    },
    "indommlu_jav_seacrowd_qa": {
        'eng': {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e'},
        'ind': {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e'},
    },
    "indommlu_bjn_seacrowd_qa": {
        'eng': {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e'},
        'ind': {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e'},
    },
    "indommlu_abl_seacrowd_qa": {
        'eng': {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e'},
        'ind': {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e'},
    },
    "indommlu_nij_seacrowd_qa": {
        'eng': {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e'},
        'ind': {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e'},
    },
    "seaeval_cross_mmlu_ind_seacrowd_qa": {
        'eng': {0: 'a', 1: 'b', 2: 'c', 3: 'd'},
        'ind': {0: 'a', 1: 'b', 2: 'c', 3: 'd'},
    },
    "seaeval_cross_mmlu_vie_seacrowd_qa": {
        'eng': {0: 'a', 1: 'b', 2: 'c', 3: 'd'},
        'ind': {0: 'a', 1: 'b', 2: 'c', 3: 'd'},
    },
    "seaeval_cross_mmlu_zlm_seacrowd_qa": {
        'eng': {0: 'a', 1: 'b', 2: 'c', 3: 'd'},
        'ind': {0: 'a', 1: 'b', 2: 'c', 3: 'd'},
    },
    "seaeval_cross_mmlu_fil_seacrowd_qa": {
        'eng': {0: 'a', 1: 'b', 2: 'c', 3: 'd'},
        'ind': {0: 'a', 1: 'b', 2: 'c', 3: 'd'},
    },
    "seaeval_cross_logiqa_ind_seacrowd_qa": {
        'eng': {0: 'a', 1: 'b', 2: 'c', 3: 'd'},
        'ind': {0: 'a', 1: 'b', 2: 'c', 3: 'd'},
    },
    "seaeval_cross_logiqa_vie_seacrowd_qa": {
        'eng': {0: 'a', 1: 'b', 2: 'c', 3: 'd'},
        'ind': {0: 'a', 1: 'b', 2: 'c', 3: 'd'},
    },
    "seaeval_cross_logiqa_zlm_seacrowd_qa": {
        'eng': {0: 'a', 1: 'b', 2: 'c', 3: 'd'},
        'ind': {0: 'a', 1: 'b', 2: 'c', 3: 'd'},
    },
    "seaeval_cross_logiqa_fil_seacrowd_qa": {
        'eng': {0: 'a', 1: 'b', 2: 'c', 3: 'd'},
        'ind': {0: 'a', 1: 'b', 2: 'c', 3: 'd'},
    },
    "m3exam_jav_seacrowd_qa": {
        'eng': {0: 'a', 1: 'b', 2: 'c', 3: 'd'},
        'ind': {0: 'a', 1: 'b', 2: 'c', 3: 'd'},
    },
    "m3exam_tha_seacrowd_qa": {
        'eng': {0: 'a', 1: 'b', 2: 'c', 3: 'd'},
        'ind': {0: 'a', 1: 'b', 2: 'c', 3: 'd'},
    },
    "m3exam_vie_seacrowd_qa": {
        'eng': {0: 'a', 1: 'b', 2: 'c', 3: 'd'},
        'ind': {0: 'a', 1: 'b', 2: 'c', 3: 'd'},
    },
    "copal_colloquial_seacrowd_qa": {
        'eng': {0: 'a', 1: 'b'},
        'ind': {0: 'a', 1: 'b'},
    },
    "xcopa_tha_seacrowd_qa": {
        'eng': {0: 'a', 1: 'b'},
        'ind': {0: 'a', 1: 'b'},
    },
    "xcopa_vie_seacrowd_qa": {
        'eng': {0: 'a', 1: 'b'},
        'ind': {0: 'a', 1: 'b'},
    },
    "xcopa_ind_seacrowd_qa": {
        'eng': {0: 'a', 1: 'b'},
        'ind': {0: 'a', 1: 'b'},
    },
    "seaeval_sg_eval_eng_seacrowd_qa": {
        'eng': {0: 'a', 1: 'b', 2: 'c', 3: 'd'},
        'ind': {0: 'a', 1: 'b', 2: 'c', 3: 'd'},
    },
    "seaeval_ph_eval_eng_seacrowd_qa": {
        'eng': {0: 'a', 1: 'b', 2: 'c', 3: 'd'},
        'ind': {0: 'a', 1: 'b', 2: 'c', 3: 'd'},
    },
    "mabl_ind_seacrowd_qa": {
        'eng': {0: 'a', 1: 'b'},
        'ind': {0: 'a', 1: 'b'},
    },
    "mabl_jav_seacrowd_qa": {
        'eng': {0: 'a', 1: 'b'},
        'ind': {0: 'a', 1: 'b'},
    },
    "mabl_sun_seacrowd_qa": {
        'eng': {0: 'a', 1: 'b'},
        'ind': {0: 'a', 1: 'b'},
    },
    # "facqa_seacrowd_qa",
    # "iapp_squad_seacrowd_qa",
    # "idk_mrc_seacrowd_qa",
    # "vihealthqa_seacrowd_qa",
    # "uit_vicov19qa_seacrowd_qa",
    # "qasina_seacrowd_qa",
    "belebele_ceb_latn_seacrowd_qa": {
        'eng': {0: 'a', 1: 'b', 2: 'c', 3: 'd'},
        'ind': {0: 'a', 1: 'b', 2: 'c', 3: 'd'},
    },
    "belebele_ilo_latn_seacrowd_qa": {
        'eng': {0: 'a', 1: 'b', 2: 'c', 3: 'd'},
        'ind': {0: 'a', 1: 'b', 2: 'c', 3: 'd'},
    },
    "belebele_ind_latn_seacrowd_qa": {
        'eng': {0: 'a', 1: 'b', 2: 'c', 3: 'd'},
        'ind': {0: 'a', 1: 'b', 2: 'c', 3: 'd'},
    },
    "belebele_jav_latn_seacrowd_qa": {
        'eng': {0: 'a', 1: 'b', 2: 'c', 3: 'd'},
        'ind': {0: 'a', 1: 'b', 2: 'c', 3: 'd'},
    },
    "belebele_kac_latn_seacrowd_qa": {
        'eng': {0: 'a', 1: 'b', 2: 'c', 3: 'd'},
        'ind': {0: 'a', 1: 'b', 2: 'c', 3: 'd'},
    },
    "belebele_khm_khmr_seacrowd_qa": {
        'eng': {0: 'a', 1: 'b', 2: 'c', 3: 'd'},
        'ind': {0: 'a', 1: 'b', 2: 'c', 3: 'd'},
    },
    "belebele_lao_laoo_seacrowd_qa": {
        'eng': {0: 'a', 1: 'b', 2: 'c', 3: 'd'},
        'ind': {0: 'a', 1: 'b', 2: 'c', 3: 'd'},
    },
    "belebele_mya_mymr_seacrowd_qa": {
        'eng': {0: 'a', 1: 'b', 2: 'c', 3: 'd'},
        'ind': {0: 'a', 1: 'b', 2: 'c', 3: 'd'},
    },
    "belebele_shn_mymr_seacrowd_qa": {
        'eng': {0: 'a', 1: 'b', 2: 'c', 3: 'd'},
        'ind': {0: 'a', 1: 'b', 2: 'c', 3: 'd'},
    },
    "belebele_sun_latn_seacrowd_qa": {
        'eng': {0: 'a', 1: 'b', 2: 'c', 3: 'd'},
        'ind': {0: 'a', 1: 'b', 2: 'c', 3: 'd'},
    },
    "belebele_tgl_latn_seacrowd_qa": {
        'eng': {0: 'a', 1: 'b', 2: 'c', 3: 'd'},
        'ind': {0: 'a', 1: 'b', 2: 'c', 3: 'd'},
    },
    "belebele_tha_thai_seacrowd_qa": {
        'eng': {0: 'a', 1: 'b', 2: 'c', 3: 'd'},
        'ind': {0: 'a', 1: 'b', 2: 'c', 3: 'd'},
    },
    "belebele_vie_latn_seacrowd_qa": {
        'eng': {0: 'a', 1: 'b', 2: 'c', 3: 'd'},
        'ind': {0: 'a', 1: 'b', 2: 'c', 3: 'd'},
    },
    "belebele_war_latn_seacrowd_qa": {
        'eng': {0: 'a', 1: 'b', 2: 'c', 3: 'd'},
        'ind': {0: 'a', 1: 'b', 2: 'c', 3: 'd'},
    },
    "belebele_zsm_latn_seacrowd_qa": {
        'eng': {0: 'a', 1: 'b', 2: 'c', 3: 'd'},
        'ind': {0: 'a', 1: 'b', 2: 'c', 3: 'd'},
    },
    # "mkqa_khm_seacrowd_qa",
    # "mkqa_zsm_seacrowd_qa",
    # "mkqa_tha_seacrowd_qa",
    # "mkqa_vie_seacrowd_qa",
    # "xquad.th_seacrowd_qa",
    # "xquad.vi_seacrowd_qa",
    "okapi_m_arc_ind_seacrowd_qa": {
        'eng': {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e'},
        'ind': {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e'},
    },
    # "okapi_m_mmlu_ind_seacrowd_qa",
    "okapi_m_arc_vie_seacrowd_qa": {
        'eng': {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e'},
        'ind': {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e'},
    },
    # "okapi_m_mmlu_vie_seacrowd_qa",
    # # Tasks.TEXTUAL_ENTAILMENT
    'indonli_seacrowd_pairs': {
        'eng': {'c': 'contradiction', 'e': 'entailment', 'n': 'irrelevant'},
        'ind': {'c': 'saling berlawanan', 'e': 'saling mendukung', 'n': 'tidak berhubungan'},
    },
    'wrete_seacrowd_pairs': {
        'eng': {'NotEntail': 'contradiction', 'Entail_or_Paraphrase': 'entailment'},
        'ind': {'NotEntail': 'saling berlawanan', 'Entail_or_Paraphrase': 'saling mendukung'},
    },
    'snli_indo_seacrowd_pairs': {
        'eng': {"kontradiksi": "contradiction", "keterlibatan": "entailment", "netral": "irrelevant"},
        'ind': {"kontradiksi": "saling berlawanan", "keterlibatan": "saling mendukung", "netral": "tidak berhubungan"},
    },
    'myxnli_seacrowd_pairs': {
        'eng': {"contradiction": "contradiction", "entailment": "neutral", "neutral": "irrelevant"},
        'ind': {"contradiction": "saling berlawanan", "entailment": "saling mendukung", "neutral": "tidak berhubungan"},
    },
    'xnli.tha_seacrowd_pairs': {
        'eng': {"contradiction": "contradiction", "entailment": "neutral", "neutral": "irrelevant"},
        'ind': {"contradiction": "saling berlawanan", "entailment": "saling mendukung", "neutral": "tidak berhubungan"},
    },
    'xnli.vie_seacrowd_pairs': {
        'eng': {"contradiction": "contradiction", "entailment": "neutral", "neutral": "irrelevant"},
        'ind': {"contradiction": "saling berlawanan", "entailment": "saling mendukung", "neutral": "tidak berhubungan"},
    },
    'identifikasi_bahasa_seacrowd_text': {
        'eng': {"Ambon": "Ambonese", "Indo": "Indonesian", "Jawa": "Javanese"},
        'ind': {"Ambon": "Ambon", "Indo": "Indonesia", "Jawa": "Jawa"},
    },
    'udhr_lid_seacrowd_text': {
        'eng': {"sun": "Sundanese", "ace": "Acehnese", "mad": "Madurese", "lao": "Lao", "cfm": "Falam Chin", "hnj": "Hmong Njua", "min": "Minangkabau", "zlm": "Malay", "tha": "Thai", "blt": "Tai Dam", "hni": "Hani", "jav": "Javanese", "tdt": "Tetun Dili", "cnh": "Hakha Chin", "khm": "Khmer", "ban": "Balinese", "ind": "Indonesian", "mya": "Burmese", "ccp": "Chakma", "duu": "Drung", "tet": "Tetun", "kkh": "Khün", "bug": "Buginese", "vie": "Vietnamese"},
        'ind': {"sun": "Sunda", "ace": "Aceh", "mad": "Madura", "lao": "Laos", "cfm": "Falam Chin", "hnj": "Hmong Njua", "min": "Minangkabau", "zlm": "Malay", "tha": "Thai", "blt": "Tai Dam", "hni": "Hani", "jav": "Jawa", "tdt": "Tetun Dili", "cnh": "Hakha Chin", "khm": "Khmer", "ban": "Bali", "ind": "Indonesia", "mya": "Burma", "ccp": "Chakma", "duu": "Drung", "tet": "Tetun", "kkh": "Khün", "bug": "Bugis", "vie": "Vietnam"},
    },
    'wili_2018_seacrowd_text': {
        'eng': {"nrm": "Narom", "jav": "Javanese", "min": "Minangkabau", "lao": "Lao", "mya": "Burmese", "pag": "Pangasinan", "ind": "Indonesian", "cbk": "Chavacano", "tet": "Tetum", "tha": "Thai", "ceb": "Cebuano", "tgl": "Tagalog", "bjn": "Banjar", "bcl": "Central Bikol", "vie": "Vietnamese"},
        'ind': {"nrm": "Narom", "jav": "Jawa", "min": "Minangkabau", "lao": "Laos", "mya": "Burma", "pag": "Pangasinan", "ind": "Indonesia", "cbk": "Chavacano", "tet": "Tetum", "tha": "Thai", "ceb": "Cebuano", "tgl": "Tagalog", "bjn": "Banjar", "bcl": "Central Bikol", "vie": "Vietnam"},
    },
    'lti_langid_corpus_seacrowd_text': {
        'eng': {"aai": "Miniafia", "aak": "Angave", "aau": "Abau", "aaz": "Amarasi", "abk": "Abkhazian", "abt": "Ambula Maprik dialect", "abx": "Inabaknon", "aby": "Aneme Wake", "aca": "Achagua", "acc": "Achi-de-Cubulco", "ace": "Acehnese", "acf": "Saint Lucian Creole French", "acr": "Achi-newortho", "acu": "Achuar-shiwiar", "adj": "Adioukrou", "ady": "Adyghe", "adz": "Adzera", "aer": "Eastern Arrente", "aey": "Amele", "afr": "Afrikaans", "agd": "Agarabi", "agg": "Angor", "agm": "Angaataha", "agn": "Agutaynen", "agr": "Aguaruna", "agt": "Central Cagayan Agta", "agu": "Aguacateco", "ahr": "Ahirani", "aia": "Arosi", "aii": "Assyrian NeoAramaic", "ake": "Akawaio", "akh": "Angal Heneng-train", "alb": "Albanian", "alp": "Alune", "als": "Tosk Albanian", "aly": "Alyawarr", "ame": "Yanesha", "amf": "Hamer-Banna", "amh": "Amharic", "ami": "Amis", "amk": "Ambai", "amm": "Sawiyanu", "amn": "Amanab Naineri dialect", "amo": "Timap -Amo-", "amp": "Alamblak", "amr": "Amarakaeri", "amu": "Guerrero Amuzgo", "amx": "Anmatyerr", "ang": "Anglo-Saxon", "anh": "Nend", "anp": "Angika", "anv": "Denya", "aoi": "Anindilyakwa", "aoj": "Filifita", "aom": "Omie", "aon": "Arapesh", "apb": "Sa a", "ape": "Central Bukiyip", "apn": "Apinaye", "apr": "Arop-Lokep", "apu": "Apurina", "apw": "Western Apache", "apy": "Apalai", "apz": "Ampeeli-Wojokeso", "ara": "Arabic", "arb": "Arabic", "arc": "Imperial Aramaic", "are": "Western Arrarnta", "arg": "Aragonese", "arl": "Arabela", "arn": "Mapudungun", "arp": "Arapaho", "arq": "Algerian Arabic", "ary": "Moroccan Arabic", "arz": "Egyptian Arabic", "ase": "American Sign Language", "asm": "Assamese", "aso": "Dano", "ast": "Asturian", "ata": "Pele-Ata", "atb": "Zaiwa", "atd": "Ata Manobo", "atg": "Ivbie North-Okpela-Arhe", "atj": "Atikamekw", "att": "Pamplona Atta", "aty": "Aneityum", "auc": "Waorani", "aui": "Anuki", "auy": "Awiyaana", "ava": "Avaric", "avk": "Kotava", "avt": "Au", "awa": "Awadhi", "awb": "Awa", "awk": "Awabakalkoba", "awx": "Awara", "aym": "Aymara", "ayp": "North Mesopotamian Arabic", "azb": "South Azerbaijani", "azd": "Eastern Durango Nahuatl", "aze": "Azerbaijani", "azg": "San Pedro Amuzgo", "azz": "Highland Puebla Nahuatl", "bak": "Bashkir", "ban": "Balinese", "bao": "Waimaha", "bar": "Bavarian", "bba": "Bariba", "bbb": "Barai", "bbr": "Girawa", "bch": "Bariai", "bcl": "Central Bicolano", "bco": "Kaluli", "bdd": "Bunama", "bdv": "Bodo Parja", "bea": "Dane Zaa", "bef": "Bena-bena", "bel": "Belarusian", "ben": "Bengali", "beo": "Bedamuni", "ber": "Berber", "beu": "Pura-train", "bfb": "Bareli Pauri", "bfz": "Baghlayani", "bgc": "Haryanvi", "bgn": "Western Balochi", "bgs": "Tagabawa", "bgt": "Bughotu", "bgw": "Bhatri", "bhd": "Bhadrawahi", "bhg": "Binandere", "bhl": "Bimin", "bho": "Bhojpuri", "bht": "Bhattiyali", "big": "Biangai", "bjk": "Barok", "bjn": "Banjar", "bjp": "Fanamaket", "bjr": "Binumarien", "bjv": "Bedjond", "bjz": "Baruga", "bkd": "Binukid", "bki": "Baki", "bkq": "Bakairi", "bla": "Blackfoot", "blw": "Balangao", "blz": "Balantak", "bmh": "Kein", "bmr": "Muinane", "bmu": "Burum-Mindik or Somba-Siawari", "bnp": "Bola", "boa": "Bora", "bod": "Tibetan", "boj": "Anjam", "bon": "Bine", "bos": "Bosnian", "box": "Buamu", "bpr": "Koronadal Blaan", "bps": "Sarangani Blaan", "bpy": "Bisnupriyan", "bqc": "Boko", "bqi": "Bakhtiari", "bqj": "Bandial", "bqp": "Busa", "bre": "Breton", "bsj": "Bangunji", "bsn": "Barasana-Eduria", "bsp": "Baga Sitemu", "bss": "Akoose", "btm": "Batak Mandailing", "buk": "Bukawa", "bul": "Bulgarian", "bus": "Bokobaru", "bvd": "Baegu", "bvr": "Burarra", "bwd": "Bwaidoka", "bwo": "Borna", "bxh": "Buhutu", "bxr": "Buryat", "byr": "Yipma", "byx": "Qaqet", "bzd": "Bribri", "bzh": "Central Buang", "bzj": "Belize Kriol English", "caa": "Chorti", "cab": "Garifuna", "cac": "Chuj de San Mateo Ixtatan", "caf": "Southern Carrier", "cak": "Kaqchikel-Chimaltenango", "cao": "Chacobo", "cap": "Chipaya", "car": "Carib", "cat": "Catalan", "cav": "Cavinena", "cax": "Chiquitano", "cbc": "Carapana", "cbi": "Chachi", "cbk": "Chavacano", "cbm": "Yepocapa Southwestern Kaqchikel", "cbr": "Cashibo-Cacataibo", "cbs": "Kashinawa", "cbt": "Chayahuita", "cbu": "Candoshi-Shapra", "cbv": "Cacua", "cco": "Comaltepec Chinantec", "ccp": "Chakma", "cdh": "Chambeali", "cdj": "Churahi", "cdo": "Min Dong", "ceb": "Cebuano", "ceg": "Chamacoco", "cek": "Eastern Kumi Chin", "ces": "Czech", "cgc": "Kagayanen", "cha": "Chamorro", "chd": "Highland Oaxaca Chontal", "che": "Chechen", "chf": "Tabasco Chontal", "chk": "Chuukese", "chq": "Quiotepec Chinantec", "chr": "Cherokee", "chu": "Old Church Slavonic", "chv": "Chuvash", "chz": "Ozumacin Chinantec", "cjo": "Asheninka Pajonal", "cjv": "Chuave", "ckb": "Central Kurdish", "cke": "Eastern Kaqchikel", "cki": "Santa Maria de Jesus Kaqchikel", "ckw": "Western Kaqchikel", "cle": "Lealao Chinantec", "clu": "Caluyanun", "cly": "Eastern Highland Chatino", "cme": "Cerma", "cmn": "Mandarin Chinese", "cni": "Ashaninka", "cnl": "Lalana Chinantec", "cnr": "Montenegrin", "cnt": "Tepetotutla Chinantec", "coe": "Koreguaje", "cof": "Colorado", "cok": "Santa Teresa Cora", "con": "Cofan", "cop": "Boharic Coptic", "cor": "Cornish", "cos": "Corsican", "cot": "Caquinte", "cox": "Nandi", "cpa": "Palantla Chinantec", "cpb": "Asheninka Ucayali yurua", "cpc": "Ajyininka Apurucayali", "cpu": "Pichis Asheninka", "cpy": "Asheninka Ucayali del Sur", "crh": "Crimean Tatar", "crm": "Moose Cree", "crn": "Cora-Presidio-de-Los-Reyes", "cro": "Crow", "crx": "Carrier", "csb": "Kashubian", "cso": "Sochiapam Chinantec", "csy": "Siyin Chin", "cta": "Tataltepec Chatino", "cth": "Thaiphum Chin", "cti": "Chol-Tila", "cto": "Embera-Catio", "ctp": "Western Highland Chatino", "ctu": "Chol-Tumbala", "cub": "Cubeo", "cuc": "Usila Chinantec", "cui": "Cuiba", "cuk": "San Blas Kuna", "cul": "Culina", "cut": "Teutila Cuicatec", "cux": "Tepeuxila Cuicatec", "cwe": "Kwere", "cya": "Nopala Chatino", "cym": "Welsh", "daa": "Dangaleat", "dad": "Marik", "dag": "Dagbani", "dah": "Gwahatike", "dan": "Danish", "dao": "Daai Chin", "ded": "Dedua", "des": "Desano", "deu": "German", "dgc": "Casiguran Dumagat Agta", "dgo": "Dogri", "dgz": "Daga", "dhi": "Dhimal", "dhn": "Dhanki", "dif": "Dieri", "dik": "Southwestern Dinka", "din": "Dinka", "diq": "Zazaki", "div": "Divehi", "djk": "Eastern Maroon Creole", "djr": "Djambarrpuynu", "dnj": "Dan Gweetaawu", "dob": "Dobu", "dop": "Lokpa", "dov": "Toka-Leya-Dombe", "dsb": "Lower Sorbian", "dso": "Desiya", "dty": "Doteli", "dub": "Dubli", "due": "Umiray Dumaget Agta", "duo": "Dupaninan Agta", "dwr": "Dawro", "dww": "Dawawa", "dyi": "Djimini Senoufo", "dzo": "Dzongkha", "ebk": "Eastern Bontok", "egl": "Emilian-Romagnol", "eip": "Lik", "eka": "Ekajuk", "ekk": "Standard Estonian", "eko": "Kote", "ell": "Greek-Tischendorf", "emi": "Mussau-Emira", "emp": "Northen Embera", "eng": "Aboriginal English", "enm": "Middle English", "enq": "Enga", "epo": "Esperanto", "eri": "Ogea", "ese": "Ese Ejja", "esi": "North Alaskan Inupiat", "esk": "Northwest Alaska Inupiatun", "ess": "Yupik", "est": "Estonian", "etr": "Edolo", "eus": "Basque", "ewe": "Ewe", "ext": "Extremaduran", "eza": "Ezaa", "faa": "Fasu", "fai": "Faiwol", "fan": "Fang", "fao": "Faroese", "far": "Fataleka", "fas": "Farsi", "ffm": "Maasina Fulfulde", "fin": "Finnish", "fit": "Meankieli", "for": "Fore", "fra": "French", "frp": "Franco-Provencal", "frr": "North Frisian", "fry": "Western Frisian", "fue": "Borgu Fulfulde", "fuf": "Pular", "fuh": "Burkina Fulfulde", "fur": "Friulian", "fuv": "Nigerian Fulfulde", "gag": "Gagauz", "gah": "Alekano aka Gahuku", "gai": "Borei", "gam": "Kandawo", "gan": "Gan", "gaq": "Gata", "gas": "Adiwasi Garasia", "gaw": "Nobonob", "gaz": "West Central Oromo", "gbk": "Gaddi", "gbl": "Gamit", "gbm": "Garhwali", "gcr": "Guianan Creole", "gdg": "Gadang", "gdn": "Umanakaina", "gdr": "Wipi", "geb": "Kire", "gfk": "Patpatar-train", "ghs": "Guhu-Samane", "gla": "Scottish Gaelic", "gle": "Irish Gaelic", "glg": "Galician", "glk": "Gilaki", "glv": "Manx Gaelic", "gmv": "Gamo", "gng": "Ngangam", "gnn": "Gumatj", "gnw": "Western Bolivian Guarani", "gof": "Gofa", "gok": "Gowli", "gom": "Goan Konkani", "gor": "Gorontalo", "got": "Gothic", "gqr": "Gor", "grc": "Ancient Greek", "grn": "Guarani", "gsw": "Alemannic", "gub": "Guajajara", "guc": "Wayuu", "guh": "Guahibo", "gui": "Eastern Bolivian Guarani", "guj": "Gujarati", "gul": "Sea Island Creole English", "gum": "Guambiano", "gun": "Mbya Guarani", "guo": "Guayabero", "gup": "Kunwijku", "gux": "Gourmantche", "gvc": "Guanano", "gvf": "Golin", "gvn": "Kuku Yalanji", "gvs": "Gumawana", "gwi": "Gwichin", "gym": "Ngabere", "gyr": "Guarayu", "hak": "Hakka", "hat": "Haitian Creole", "hau": "Hausa", "haw": "Hawaiian", "hbo": "Ancient Hebrew", "hch": "Huichol", "heb": "Hebrew", "heg": "Helong", "hif": "Fiji Hindi", "hin": "Hindi", "hix": "Hixkaryana", "hla": "Halia", "hlb": "Halbi", "hlt": "Matu Chin", "hmo": "Hiri Motu", "hns": "Caribbean Hindustani", "hop": "Hopi", "hot": "Hote-Male", "hoy": "Holiya", "hrv": "Croatian", "hsb": "Upper Sorbian", "hto": "Minica Huitoto", "hub": "Huambisa", "hui": "Huli", "hun": "Hungarian", "hus": "Huastec", "huu": "Murui Huitoto", "huv": "San Mateo del Mar Huave", "hva": "San Luis Potosi Huastec", "hvn": "Hawu", "hwc": "Hawaiian Pidgin", "hye": "Eastern Armenian", "hyw": "Western Armenian-1853", "ian": "Ngepma Kwundi", "ibo": "Igbo", "icr": "Islander-Creole-English", "ido": "Ido", "ifa": "Amganad Ifugao", "ifu": "Mayoyao Ifugao", "ify": "Antipolo Ifugao", "ign": "Ignaciano", "iii": "Sichuan Yi", "ikk": "Ika", "ikw": "Ikwere", "ile": "Interlingue", "ilo": "Ilocano", "imo": "Imbo Ungu", "ina": "Interlingua", "inb": "Inga", "ind": "Indonesian", "inh": "Ingush", "ino": "Inoke-Yat", "iou": "Tuma-Irumu", "ipi": "Ipili", "iqw": "Ikwo", "iri": "Irigwe", "isd": "Isnag", "isl": "Icelandic", "isn": "Kiisanzu", "ita": "Italian", "ivb": "Ibatan", "ivv": "Ivatan", "iws": "Sepik Iwam", "ixl": "Ixil Cotzal", "izz": "Izii", "jaa": "Jamamadi", "jac": "Jakalteko", "jae": "Jabem", "jam": "Jamaican Patois", "jao": "Yanyuwa", "jav": "Javanese", "jbo": "Lojban", "jic": "Tol", "jid": "Jida", "jiv": "Shuar", "jni": "Ajanji", "jpn": "Japanese", "juy": "Juray", "jvn": "Caribbean Javanese", "kaa": "Karakalpak", "kab": "Kabyle", "kaj": "Jju", "kal": "Kalaallisut", "kan": "Kannada", "kaq": "Capanahua", "kat": "Georgian", "kaz": "Kazahk", "kbc": "Kadiweu", "kbd": "Kabardian", "kbh": "Camsa", "kbm": "Iwal", "kbp": "Kabiye", "kbq": "Kamano-Kafe", "kca": "Khanty", "kdc": "Kutu", "kde": "Makonde", "kdl": "Tsikimba", "kek": "Kekchi", "ken": "Kenyang", "kew": "West Kewa", "kfs": "Bilaspuri", "kfw": "Kharam Naga", "kfx": "Kulvi Outer Seraji", "kfy": "Soriyali Kumaoni", "kgf": "Mongi", "kgk": "Kaiwa", "kgp": "Kaingang", "khm": "Central Khmer", "khn": "Khandesi", "khs": "Kasua", "khw": "Khowar", "khz": "Kalo aka Keapara", "kij": "Kilivila", "kik": "Gikuyu", "kin": "Kinyarwanda", "kip": "Sheshi Kham", "kiu": "Kirmanjaki", "kiz": "Kisi", "kjb": "Eastern Kanjobal", "kje": "Kisar", "kjo": "Pahari Kinnauri", "kjp": "Pwo Eastern Karen", "kjs": "East Kewa", "kkc": "Odoodee", "kkl": "Kosarek Yale", "klt": "Nukna", "klv": "Maskelynes", "kmg": "Kate", "kmh": "Kalam Minimib dialect", "kmk": "Limos Kalinga", "kmo": "Washkuk", "kms": "Kamasau", "kmu": "Kanite", "kne": "Kankanaey", "knf": "Mankanya", "knj": "Akateko", "knv": "Tabo Aramia dialect", "kog": "Kogi", "koi": "Komi-Permyak", "kom": "Komi", "kor": "Korean", "kos": "Kosrae", "kpf": "Komba", "kpg": "Kapingamarangi", "kpj": "Karaja", "kpr": "Korafe-Yegha", "kpw": "Kobon", "kpx": "Mountain Koiali", "kqa": "Mum", "kqc": "Doromu-Koki", "kqe": "Eastern Kalagan", "kqf": "Kakabai", "kql": "Kyenele", "kqw": "Kandas", "krc": "Karachay Balkar", "ksc": "Southern Kalinga", "ksd": "Kuanua aka Tolai", "ksh": "Ripuarian", "ksj": "Uare", "ksr": "Borong", "ktj": "Plapo Krumen", "ktm": "Kurti", "kto": "Kuot", "kud": "Auhelawa", "kue": "Kuman", "kum": "Kumyk", "kup": "Kunimaipa", "kur": "Kurdish", "kvg": "Kuni-Boazi", "kvn": "Border Kuna", "kwd": "Kwaio", "kwf": "Kwaraae", "kwi": "Awa-Cuaiquer", "kwj": "Kwanga", "kxp": "Wadiyari Koli", "kxv": "Kuvi", "kyc": "Kyaka Ena", "kyf": "Kouya", "kyg": "Keyagana", "kyq": "Kenga", "kyu": "Western Kayah", "kyv": "Kayort", "kyz": "Kayabi", "kze": "Kosena", "lac": "Lacandon", "lad": "Ladino", "lao": "Lao", "lat": "Latin", "lbb": "Label", "lbf": "Lahauli", "lbk": "Central Bontok", "lbm": "Lodhi", "lcm": "Tungag", "leu": "Kara", "lex": "Luang", "lez": "Lezgian", "lfn": "Lingua Franca Nova", "lgl": "Wala", "lid": "Nyindrou", "lif": "Limbu", "lij": "Ligurian", "lim": "Limburgish", "lin": "Lingala", "lit": "Lithuanian", "liv": "Livonian", "lki": "Laki", "lld": "Ladin", "llg": "Rote Lole", "lmo": "Lombard", "lrc": "Northern Luri", "ltg": "Latgalian", "lti": "Lithuanian", "ltz": "Luxembourgish", "lug": "Luganda", "luo": "Dholuo", "lus": "Mizo Lushai", "luz": "Southern Luri", "lvs": "Latvian", "lww": "Lewo", "lzh": "Classical Chinese", "lzz": "Laz", "maa": "Mazatec San Antonio", "mah": "Marshallese", "mai": "Maithili", "maj": "Jalapa de Diaz Mazatec", "mal": "Malayalam", "mam": "Central Mam", "maq": "Chiquihuitlan Mazatec", "mar": "Marathi", "mau": "Huautla Mazatec", "mav": "Satere-Mawe", "maz": "Central Mazahua", "mbb": "Western Bukidnon Manobo", "mbc": "Macushi", "mbd": "Dibabawon Manobo", "mbh": "Mangseng", "mbi": "Ilianen Manobo", "mbj": "Nadeb", "mbl": "Maxakali", "mbs": "Sarangani Manobo", "mbt": "Matigsalug Manobo", "mca": "Maka", "mcb": "Machiguenga", "mcd": "Sharanahua", "mcf": "Matses", "mco": "Coatlan Mixe", "mcp": "Makaa", "mcq": "Managalasi", "mcr": "Menya", "mdf": "Moksha", "mdy": "Maale", "med": "Melpa", "mee": "Mengen", "meh": "Southwestern Tlaxiaco Mixtec", "mek": "Mekeo", "meq": "Merey", "met": "Mato", "meu": "Motu", "mfy": "Mayo", "mgc": "Morokodo", "mgh": "Makhuwa-Meetto", "mhr": "Meadow Mari", "mib": "Atatlahuca Mixtec", "mie": "Ocotepec Mixtec", "mig": "San Miguel el Grande Mixtec", "mih": "Chayuco Mixtec", "mil": "Penoles Mixtec", "mim": "Mixtec-Alacatlatzala", "min": "Minankabau", "mio": "Pinotepa Nacional Mixtec", "mir": "Isthmus Mixe", "mit": "Southern Puebla Mixtec", "mix": "Mixtepec Mixtec", "miy": "Ayutla Mixtec", "miz": "Coatzospan Mixtec", "mjc": "San Juan Colorado Mixtec", "mjl": "Mandeali", "mkd": "Macedonian", "mkj": "Mokilese", "mkl": "Monkole", "mkn": "Kupang", "mks": "Silacayoapan Mixtec", "mle": "Manambu", "mlg": "Malagasy", "mlh": "Mape", "mlp": "Bargam", "mlt": "Maltese", "mmn": "Mamanwa", "mmo": "Mangga Buang", "mmx": "Madak", "mna": "Mbula", "mnc": "Manchu", "mni": "Meitei", "mnw": "Mon", "moh": "Mohawk", "mon": "Mongolian", "mop": "Mopan Maya", "mox": "Molima", "mpd": "Machinere", "mpj": "Martu Wangka", "mpm": "Yosondua Mixtec", "mpp": "Migabac", "mps": "Dadibi", "mpt": "Mian Weng", "mpx": "Misima-Paneati", "mqb": "Mbuko", "mqj": "Mamasa", "mri": "Maori", "mrj": "Hill Mari", "msb": "Masbatenyo", "msc": "Sankaran Maninka", "msk": "Mansaka", "msm": "Agusan Manobo", "msy": "Aruamu", "mta": "Cotabato Manobo", "mti": "Maiwa", "mto": "Totontepec Mixe", "mux": "Bo-Ung aka Mara-Gomu", "muy": "Muyang", "mva": "Manam", "mvn": "Minaveha", "mwc": "Are", "mwe": "Mwera", "mwf": "Murrinpatha", "mwl": "Mirandese", "mwp": "Kala Lagaw", "mxb": "Tezoatlan Mixtec", "mxp": "Tlahuitoltepec Mixe", "mxq": "Juquila Mixe", "mxt": "Jamiltepec Mixtec", "mxv": "Metlatonoc Mixtec", "mya": "Burmese", "myk": "Mamara Senoufo", "myu": "Munduruku", "myv": "Erzya", "myw": "Muyuw", "myy": "Macuna", "mza": "Mixtec-Santa-Maria-Zacatepec", "mzi": "Mazatec Ixcatlan", "mzn": "Mazandarani", "nab": "Southern Nambikuara", "naf": "Nabak", "nag": "Nagamese", "nah": "Nahuatl", "nak": "Nakanai", "nan": "Min Nan", "nap": "Neapolitan", "nas": "Naasioi", "nav": "Navajo", "nbq": "Nggem", "nca": "Iyo", "nce": "Yale", "nch": "Central Huasteca Nahuatl", "ncj": "Northern Puebla Nahuatl", "ncl": "Michoacan Nahuatl", "ncu": "Chumburung", "nde": "isiNdebele", "ndg": "Kindengereko", "ndj": "Ndamba", "nds": "Dutch Low Saxon", "new": "Newar", "nfa": "Dhao", "nfr": "Nafaanra", "ngp": "Nguu", "ngu": "Guerrero Nahuatl", "nhe": "Eastern Huasteca Nahuatl", "nhg": "Tetelcingo Nahuatl", "nhi": "Zacatlan-Ahuacatlan-Tepetzintla Nahuatl", "nho": "Takuu", "nhr": "Naro", "nhu": "Noone", "nhw": "Western Huasteca Nahuatl", "nhx": "Isthmus-Mecayapan Nahuatl", "nhy": "Northern Oaxaca Nahuatl", "nif": "Nek", "nii": "Nii", "nin": "Ninzo", "niy": "Ndruna", "nko": "Nkonya", "nld": "Dutch", "nlg": "Gela", "nlx": "Nahali", "nmw": "Saisai", "nna": "Nyangumarta", "nno": "Nynorsk", "nnq": "Ngindo", "noa": "Woun Meu-altortho", "nob": "Norsk Bokmal", "nod": "Northern Thai", "noi": "Noiri", "nop": "Numangan", "not": "Nomatsiguenga", "nou": "Ewage-Notu", "nov": "Novial", "npi": "Nepali", "npl": "Southeastern Puebla Nahuatl", "nqo": "Nko", "nsn": "Nehan", "nso": "Northern Sotho", "nss": "Nali", "nsu": "Sierra Negra Nahuatl", "ntj": "Ngaanyatjarra", "ntp": "Northern Tepehuan", "ntu": "Natqgu", "nuy": "Wubuy", "nvm": "Namiai aka Barai", "nwi": "Southwest Tanna", "nya": "Chichewa", "nys": "Nyoongar", "nyu": "Nyungwe", "obo": "Obo Manobo", "oci": "Occitan", "okv": "Orokaiva Ehija dialect", "olo": "Livvi", "omw": "Sotuh Tairora Omwunra-Toqura", "ong": "Olo", "ons": "Ono", "ood": "Tohono Oodham", "opm": "Oksapmin", "ory": "Oriya", "oss": "Ossetian", "ota": "Ottoman Turkish", "ote": "Mezquital Otomi", "otm": "Eastern Highland Otomi", "otn": "Tenango Otomi", "otq": "Queretaro Otomi", "ots": "Estado de Mexico Otomi", "oym": "Wayampi", "pab": "Parecis", "pad": "Paumari", "pag": "Pangasinan", "pah": "Tenharim", "pam": "Kapampangan", "pan": "Eastern Panjabi", "pao": "Nothern Paiute", "pap": "Papiamentu", "pbb": "Paez", "pbc": "Patamona", "pcd": "Picard", "pdc": "Pennsylvania Dutch", "peg": "Pengo", "pes": "Persian", "pfl": "Pfaelzisch", "pib": "Yine", "pio": "Piapoco", "pir": "Piratapuyo", "piu": "Pintupi-Luritja", "pjt": "Pitjantjatjara", "pli": "Pali", "pls": "San Marcos Tlalcoyalco Popoloca", "plt": "Plateau Malagasy", "plu": "Palikur", "plw": "Brookes Point Palawano", "pma": "Paama", "pms": "Piedmontese", "pnb": "Western Panjabic", "pnt": "Pontic", "pob": "Western Poqomchi", "poe": "San Juan Atzingo Popoloca", "poh": "Poqomchi", "poi": "Highland Popoluca", "pol": "Polish", "pon": "Pohnpeian-apocrypha", "por": "Portugese", "poy": "Pogolo", "ppo": "Folopa", "pps": "San Luis Temalacayuca Popoloca", "prf": "Paranan", "pri": "Paici", "prq": "Asheninka Perene", "pst": "Pashto", "ptp": "Patep", "ptu": "Bambam", "pwg": "Gapapaiwa", "qub": "Huallaga Huanuco Quechua", "quc": "Kiche Cantel-newortho", "quf": "Lambayeque Quechua", "quh": "South Bolivian Quechua", "qul": "North Bolivian Quechua", "qup": "Southern Pastaza Quechua", "quy": "Quechua-Ayacucho", "qvc": "Cajamarca Quechua", "qve": "Eastern Apurimac Quechua", "qvh": "Huamalies-Dos de Mayo Huanuco Quechua", "qvm": "Margos-Yarowilca-Lauricocha Quechua", "qvn": "North Junin Quechua", "qvs": "San Martin Quechua", "qvw": "Huaylla Wanca Quechua", "qvz": "Northern Pastaza Quichua", "qwh": "Huaylas Ancash Quechua", "qxh": "Panao Huanuco Quechua", "qxl": "Salasaca Highland Quichua", "qxn": "Northern Conchucos Ancash Quechua", "qxo": "Southern Conchucos Ancash Quechua", "rai": "Ramoaaina", "ram": "Kanela", "rap": "Rapa Nui", "reg": "Kikara", "rgu": "Rote Rikou", "rkb": "Rikbaktsa", "rmc": "Carpathian Romani", "rmn": "Balkan Romani", "rmy": "Vlax Romani-Arli", "roh": "Romansh", "ron": "Ludari Romanian", "roo": "Rotokas", "rop": "Kriol", "row": "Rote Dela", "rro": "Waima", "rtw": "Rathawi", "rue": "Rusyn", "ruf": "Luguru", "rug": "Roviana", "rup": "Aromanian", "rus": "Russian", "rwo": "Karo Rawa", "sab": "Buglere", "sah": "Sakha", "san": "Sanskrit", "sat": "Santali", "sbe": "Saliba", "sbk": "Kisafwa", "sbl": "Sambali Botolan", "sbs": "Chikuahane", "sby": "Soli", "sch": "Sakachep", "sck": "Sadri", "scn": "Sicilian", "sco": "Scots", "sdh": "Sourthern Kurdish", "seh": "Sena", "sey": "Secoya", "sgb": "Mag-antsi Ayta", "sgj": "Surgujia", "sgs": "Samogitian", "sgz": "Sursurunga", "shi": "Tachelhit", "shj": "Shatt", "shn": "Shan", "shp": "Shipibo-Conibo", "sim": "Mende", "sin": "Sinhalese", "sja": "Epena", "skr": "Saraiki", "sli": "Lower Silesian", "slk": "Slovak", "sll": "Salt-Yui", "slv": "Slovenian", "sme": "Northern Sami", "smk": "Bolinao", "smo": "Samoan", "sna": "Shona", "snc": "Sinaugoro", "snd": "Sindhi", "snn": "Siona", "snp": "Siane Komongu dialect", "sny": "Saniyo-Hiyewe", "som": "Somali", "soq": "Kanasi", "soy": "Sola", "spa": "Spanish", "spl": "Selepet", "spm": "Akukem", "spp": "Supyire Senoufo", "sps": "Saposa", "spy": "Sabaot", "srd": "Sardinian", "sri": "Siriano", "srm": "Saramaccan", "srn": "Sranan", "srp": "Serbian", "srq": "Siriono", "srx": "Sirmauri", "ssd": "Siroi", "ssg": "Seimat", "ssx": "Sembeleke", "stp": "Southeastern Tepehuan", "stq": "Saterland Frisian", "sua": "Sulka", "suc": "Western Subanon", "sue": "Suena", "sun": "Sundanese", "sus": "Susu", "suz": "Sunwar", "swe": "Swedish", "swh": "Swahili", "swp": "Suau", "sxb": "Suba", "syb": "Central Subanen", "szl": "Silesian", "szy": "Sakizaya", "tac": "Western Tarahumara", "taj": "Eastern Tamang", "tam": "Tamil", "tar": "Tarahumara-del-Centro", "tat": "Tatar", "tau": "Upper Tanana", "tav": "Tatuyo", "taw": "Tay", "tay": "Atayal", "tbc": "Takia", "tbf": "Mandara", "tbg": "Arau", "tbk": "Calamian Tagbanwa", "tbl": "Tboli", "tbo": "Tawala", "tbz": "Ditammari", "tca": "Ticuna", "tcf": "Malinaltepec Mephaa", "tcs": "Yumplatok", "tcy": "Tulu", "tcz": "Thado Chin-train", "tdj": "Tajio", "tdt": "Tetun Dili", "tdx": "Tandroy-Mahafaly Malagasy", "ted": "Tepo Krumen", "tee": "Huehuetla Tepehua", "tel": "Telugu", "ter": "Terena", "tet": "Tetun", "tew": "Tewa", "tfr": "Teribe", "tgk": "Tajik", "tgl": "Tagalog", "tgo": "Sudest", "tgp": "Tangoa", "tha": "Thai", "thr": "Rana Tharu", "tif": "Tifal", "tik": "Tikar", "tim": "Timbe", "tir": "Tigrinya", "tiw": "Tiwi", "tiy": "Tiruray", "tke": "Takwane", "tkr": "Tsakhur", "tku": "Upper Necaxa Totonac", "tlf": "Telefol Weng", "tlh": "Klingon", "tly": "Talysh", "tmd": "Haruai", "tna": "Tacana", "tnc": "Tanimuca-Retuara", "tnk": "Kwamera", "tnn": "North Tanna", "tnp": "Whitesands", "toc": "Coyutla Totonac", "tod": "Toma", "tof": "Gizzra", "toj": "Tojolabal", "tok": "Toki Pona", "ton": "Tongan", "too": "Xicotepec de Juarez Totonac", "top": "Papantla Totonac", "tos": "Highland Totonac", "tpi": "Tok Pisin", "tpt": "Tlachichilco Tepehua", "tpx": "Acatepec Mephaa", "tpz": "Vasui aka Tinputz", "trc": "Copala Triqui", "trq": "Triqui-San-Martin-Itunyoso", "trs": "Chicahuaxtla Triqui", "trv": "Taroko", "tsn": "Setswana", "tso": "Tsonga", "tsw": "Tsishingini", "ttc": "Tektiteko", "tte": "Tubetube", "tuc": "Saveeng Oov", "tue": "Tuyuca", "tuf": "Central Tunebo", "tuk": "Turkmen", "tuo": "Tucano", "tur": "Turkish", "tvk": "Southeast Ambrym", "tvt": "Tutsa Naga", "twi": "Twi", "txq": "Rote Tii", "txu": "Kayapo", "tyv": "Tuvinian", "tzc": "Tzotzil de Chamula", "tze": "Tzotzil de Chenalho", "tzj": "Eastern Tzutujil", "tzm": "Central Atlas Tamazight", "tzo": "Tzotzil-Huixtan", "tzs": "Tzotzil San Andres", "tzz": "Tzotzil Zinacantan", "ubr": "Ubir", "ubu": "Umbu-Ungu Andale", "udm": "Udmurt", "udu": "Uduk", "uig": "Uyghur", "ukr": "Ukrainian", "uli": "Ulithian", "ulk": "Meriam Mir", "unx": "Munda", "upv": "Uripiv", "ura": "Urarina", "urb": "Kaapor", "urd": "Urdu", "uri": "Urim", "urt": "Urat", "urw": "Sob Dora", "ury": "Orya", "usa": "Usarufa", "usp": "Uspanteko", "uvh": "Uri", "uvl": "Lote", "uzb": "Uzbek", "vah": "Varhadi-Nagpuri", "vai": "Vai", "var": "Huarijio", "vec": "Venetian", "vep": "Vepsian", "vid": "Vidunda", "vie": "Vietnamese", "viv": "Iduna", "vls": "Vlaams", "vmy": "Ayautla Mazateco", "vol": "Volapuk", "vro": "Voro", "waj": "Waffa", "wal": "Wolaytta", "wap": "Wapishana", "wat": "Kaninuwa", "waw": "Waiwai", "wbi": "Kivwanji", "wbp": "Warlpiri", "wed": "Wedau", "wer": "Weri", "wim": "Wik-Mungkan", "wiu": "Witu", "wiv": "Vitu", "wln": "Walloon", "wmt": "Walmajarri", "wmw": "Mwani", "wnc": "Wantoat", "wnu": "Usan", "wol": "Wolof", "wos": "Hanga Hundi", "wrk": "Garrwa", "wrs": "Walsa Waris", "wsk": "Waskia", "wuu": "Wu", "wuv": "Wuvalu-Aua", "xal": "Kalmyk", "xav": "Xavante", "xbi": "Kombio Wampukuamp", "xed": "Hdi", "xer": "Xerente", "xho": "Xhosa", "xir": "Xiriana", "xla": "Kamula", "xmf": "Mingrelian", "xnj": "Chingoni", "xnn": "Northern Kankanay", "xno": "Norman", "xnr": "Kangri", "xon": "Konkomba", "xri": "Krikati Gaviao", "xsb": "Sambal", "xsi": "Sio", "xta": "Alcozauca Mixtec", "xtd": "Diuxi Mixtec-tilantongo", "xtm": "Magdalena Penasco Mixtec", "xtn": "Northern Tlaxico Mixtec", "xuo": "Kuo", "yaa": "Yaminahua", "yad": "Yagua", "yal": "Yalunka", "yam": "Yamba", "yao": "Chiyawo", "yap": "Yapese", "yaq": "Yaqui", "yby": "Yaweyuha", "ycn": "Yucuna", "yid": "Yiddish", "yka": "Yakan", "yle": "Yele Rossel", "yml": "Iamalele", "yom": "Yombe", "yon": "Yongkom", "yor": "Yoruba", "yrb": "Yareba", "yre": "Yaoure", "yss": "Yessan-Mayo Yamano dialect", "yua": "YucatecMaya", "yue": "Cantonese", "yuj": "Karkar-Yuri", "yut": "Yopno", "yuw": "Yau", "yva": "Yawa", "zaa": "Sierra de Juarez Zapotec", "zab": "San Juan Guelavia Zapotec", "zac": "Ocotlan Zapotec", "zad": "Cajonos Zapotec", "zae": "Yareni Zapotec", "zai": "Isthmus Zapotec", "zaj": "Zaramo", "zam": "Miahuatlan Zapotec", "zao": "Ozolotepec Zapotec", "zaq": "Aloapam Zapotec", "zar": "Rincon Zapotec", "zas": "Santo Domingo Albarradas Zapotec", "zat": "Tabaa Zapotec", "zav": "Yatzachi Zapotec", "zaw": "Mitla Zapotec", "zca": "Coatecas Altas Zapotec", "zea": "Zealandic", "zga": "Mahanji", "zgh": "Standard Moroccan Tamazight", "zia": "Zia", "ziw": "Zigua", "zlm": "Malay", "zos": "Francisco Leon Zoque", "zpc": "Choapan Zapotec", "zpg": "Guevea de Humboldt Zapotec", "zpi": "Santa Maria Quiegolani Zapotec", "zpl": "Lachixio Zapotec", "zpm": "Mixtepec Zapotec", "zpo": "Amatlan Zapotec", "zpq": "Zoogocho Zapotec", "zpt": "Zapotec San Vicente Coatlan", "zpu": "Yalalag Zapotec", "zpv": "Chichicapan Zapotec", "zpz": "Texmelucan Zapotec", "zsr": "Southern Rincon Zapotec", "ztg": "Xanaguia Zapotec", "ztq": "Quioquitani-Quieri Zapotec", "zty": "Yatee Zapotec", "zul": "Zulu", "zyp": "Zyphe Chin",},
        'ind': {"aai": "Miniafia", "aak": "Angave", "aau": "Abau", "aaz": "Amarasi", "abk": "Abkhazian", "abt": "Ambula Maprik dialect", "abx": "Inabaknon", "aby": "Aneme Wake", "aca": "Achagua", "acc": "Achi-de-Cubulco", "ace": "Acehnese", "acf": "Saint Lucian Creole French", "acr": "Achi-newortho", "acu": "Achuar-shiwiar", "adj": "Adioukrou", "ady": "Adyghe", "adz": "Adzera", "aer": "Eastern Arrente", "aey": "Amele", "afr": "Afrikaans", "agd": "Agarabi", "agg": "Angor", "agm": "Angaataha", "agn": "Agutaynen", "agr": "Aguaruna", "agt": "Central Cagayan Agta", "agu": "Aguacateco", "ahr": "Ahirani", "aia": "Arosi", "aii": "Assyrian NeoAramaic", "ake": "Akawaio", "akh": "Angal Heneng-train", "alb": "Albanian", "alp": "Alune", "als": "Tosk Albanian", "aly": "Alyawarr", "ame": "Yanesha", "amf": "Hamer-Banna", "amh": "Amharic", "ami": "Amis", "amk": "Ambai", "amm": "Sawiyanu", "amn": "Amanab Naineri dialect", "amo": "Timap -Amo-", "amp": "Alamblak", "amr": "Amarakaeri", "amu": "Guerrero Amuzgo", "amx": "Anmatyerr", "ang": "Anglo-Saxon", "anh": "Nend", "anp": "Angika", "anv": "Denya", "aoi": "Anindilyakwa", "aoj": "Filifita", "aom": "Omie", "aon": "Arapesh", "apb": "Sa a", "ape": "Central Bukiyip", "apn": "Apinaye", "apr": "Arop-Lokep", "apu": "Apurina", "apw": "Western Apache", "apy": "Apalai", "apz": "Ampeeli-Wojokeso", "ara": "Arabic", "arb": "Arabic", "arc": "Imperial Aramaic", "are": "Western Arrarnta", "arg": "Aragonese", "arl": "Arabela", "arn": "Mapudungun", "arp": "Arapaho", "arq": "Algerian Arabic", "ary": "Moroccan Arabic", "arz": "Egyptian Arabic", "ase": "American Sign Language", "asm": "Assamese", "aso": "Dano", "ast": "Asturian", "ata": "Pele-Ata", "atb": "Zaiwa", "atd": "Ata Manobo", "atg": "Ivbie North-Okpela-Arhe", "atj": "Atikamekw", "att": "Pamplona Atta", "aty": "Aneityum", "auc": "Waorani", "aui": "Anuki", "auy": "Awiyaana", "ava": "Avaric", "avk": "Kotava", "avt": "Au", "awa": "Awadhi", "awb": "Awa", "awk": "Awabakalkoba", "awx": "Awara", "aym": "Aymara", "ayp": "North Mesopotamian Arabic", "azb": "South Azerbaijani", "azd": "Eastern Durango Nahuatl", "aze": "Azerbaijani", "azg": "San Pedro Amuzgo", "azz": "Highland Puebla Nahuatl", "bak": "Bashkir", "ban": "Balinese", "bao": "Waimaha", "bar": "Bavarian", "bba": "Bariba", "bbb": "Barai", "bbr": "Girawa", "bch": "Bariai", "bcl": "Central Bicolano", "bco": "Kaluli", "bdd": "Bunama", "bdv": "Bodo Parja", "bea": "Dane Zaa", "bef": "Bena-bena", "bel": "Belarusian", "ben": "Bengali", "beo": "Bedamuni", "ber": "Berber", "beu": "Pura-train", "bfb": "Bareli Pauri", "bfz": "Baghlayani", "bgc": "Haryanvi", "bgn": "Western Balochi", "bgs": "Tagabawa", "bgt": "Bughotu", "bgw": "Bhatri", "bhd": "Bhadrawahi", "bhg": "Binandere", "bhl": "Bimin", "bho": "Bhojpuri", "bht": "Bhattiyali", "big": "Biangai", "bjk": "Barok", "bjn": "Banjar", "bjp": "Fanamaket", "bjr": "Binumarien", "bjv": "Bedjond", "bjz": "Baruga", "bkd": "Binukid", "bki": "Baki", "bkq": "Bakairi", "bla": "Blackfoot", "blw": "Balangao", "blz": "Balantak", "bmh": "Kein", "bmr": "Muinane", "bmu": "Burum-Mindik or Somba-Siawari", "bnp": "Bola", "boa": "Bora", "bod": "Tibetan", "boj": "Anjam", "bon": "Bine", "bos": "Bosnian", "box": "Buamu", "bpr": "Koronadal Blaan", "bps": "Sarangani Blaan", "bpy": "Bisnupriyan", "bqc": "Boko", "bqi": "Bakhtiari", "bqj": "Bandial", "bqp": "Busa", "bre": "Breton", "bsj": "Bangunji", "bsn": "Barasana-Eduria", "bsp": "Baga Sitemu", "bss": "Akoose", "btm": "Batak Mandailing", "buk": "Bukawa", "bul": "Bulgarian", "bus": "Bokobaru", "bvd": "Baegu", "bvr": "Burarra", "bwd": "Bwaidoka", "bwo": "Borna", "bxh": "Buhutu", "bxr": "Buryat", "byr": "Yipma", "byx": "Qaqet", "bzd": "Bribri", "bzh": "Central Buang", "bzj": "Belize Kriol English", "caa": "Chorti", "cab": "Garifuna", "cac": "Chuj de San Mateo Ixtatan", "caf": "Southern Carrier", "cak": "Kaqchikel-Chimaltenango", "cao": "Chacobo", "cap": "Chipaya", "car": "Carib", "cat": "Catalan", "cav": "Cavinena", "cax": "Chiquitano", "cbc": "Carapana", "cbi": "Chachi", "cbk": "Chavacano", "cbm": "Yepocapa Southwestern Kaqchikel", "cbr": "Cashibo-Cacataibo", "cbs": "Kashinawa", "cbt": "Chayahuita", "cbu": "Candoshi-Shapra", "cbv": "Cacua", "cco": "Comaltepec Chinantec", "ccp": "Chakma", "cdh": "Chambeali", "cdj": "Churahi", "cdo": "Min Dong", "ceb": "Cebuano", "ceg": "Chamacoco", "cek": "Eastern Kumi Chin", "ces": "Czech", "cgc": "Kagayanen", "cha": "Chamorro", "chd": "Highland Oaxaca Chontal", "che": "Chechen", "chf": "Tabasco Chontal", "chk": "Chuukese", "chq": "Quiotepec Chinantec", "chr": "Cherokee", "chu": "Old Church Slavonic", "chv": "Chuvash", "chz": "Ozumacin Chinantec", "cjo": "Asheninka Pajonal", "cjv": "Chuave", "ckb": "Central Kurdish", "cke": "Eastern Kaqchikel", "cki": "Santa Maria de Jesus Kaqchikel", "ckw": "Western Kaqchikel", "cle": "Lealao Chinantec", "clu": "Caluyanun", "cly": "Eastern Highland Chatino", "cme": "Cerma", "cmn": "Mandarin Chinese", "cni": "Ashaninka", "cnl": "Lalana Chinantec", "cnr": "Montenegrin", "cnt": "Tepetotutla Chinantec", "coe": "Koreguaje", "cof": "Colorado", "cok": "Santa Teresa Cora", "con": "Cofan", "cop": "Boharic Coptic", "cor": "Cornish", "cos": "Corsican", "cot": "Caquinte", "cox": "Nandi", "cpa": "Palantla Chinantec", "cpb": "Asheninka Ucayali yurua", "cpc": "Ajyininka Apurucayali", "cpu": "Pichis Asheninka", "cpy": "Asheninka Ucayali del Sur", "crh": "Crimean Tatar", "crm": "Moose Cree", "crn": "Cora-Presidio-de-Los-Reyes", "cro": "Crow", "crx": "Carrier", "csb": "Kashubian", "cso": "Sochiapam Chinantec", "csy": "Siyin Chin", "cta": "Tataltepec Chatino", "cth": "Thaiphum Chin", "cti": "Chol-Tila", "cto": "Embera-Catio", "ctp": "Western Highland Chatino", "ctu": "Chol-Tumbala", "cub": "Cubeo", "cuc": "Usila Chinantec", "cui": "Cuiba", "cuk": "San Blas Kuna", "cul": "Culina", "cut": "Teutila Cuicatec", "cux": "Tepeuxila Cuicatec", "cwe": "Kwere", "cya": "Nopala Chatino", "cym": "Welsh", "daa": "Dangaleat", "dad": "Marik", "dag": "Dagbani", "dah": "Gwahatike", "dan": "Danish", "dao": "Daai Chin", "ded": "Dedua", "des": "Desano", "deu": "German", "dgc": "Casiguran Dumagat Agta", "dgo": "Dogri", "dgz": "Daga", "dhi": "Dhimal", "dhn": "Dhanki", "dif": "Dieri", "dik": "Southwestern Dinka", "din": "Dinka", "diq": "Zazaki", "div": "Divehi", "djk": "Eastern Maroon Creole", "djr": "Djambarrpuynu", "dnj": "Dan Gweetaawu", "dob": "Dobu", "dop": "Lokpa", "dov": "Toka-Leya-Dombe", "dsb": "Lower Sorbian", "dso": "Desiya", "dty": "Doteli", "dub": "Dubli", "due": "Umiray Dumaget Agta", "duo": "Dupaninan Agta", "dwr": "Dawro", "dww": "Dawawa", "dyi": "Djimini Senoufo", "dzo": "Dzongkha", "ebk": "Eastern Bontok", "egl": "Emilian-Romagnol", "eip": "Lik", "eka": "Ekajuk", "ekk": "Standard Estonian", "eko": "Kote", "ell": "Greek-Tischendorf", "emi": "Mussau-Emira", "emp": "Northen Embera", "eng": "Aboriginal English", "enm": "Middle English", "enq": "Enga", "epo": "Esperanto", "eri": "Ogea", "ese": "Ese Ejja", "esi": "North Alaskan Inupiat", "esk": "Northwest Alaska Inupiatun", "ess": "Yupik", "est": "Estonian", "etr": "Edolo", "eus": "Basque", "ewe": "Ewe", "ext": "Extremaduran", "eza": "Ezaa", "faa": "Fasu", "fai": "Faiwol", "fan": "Fang", "fao": "Faroese", "far": "Fataleka", "fas": "Farsi", "ffm": "Maasina Fulfulde", "fin": "Finnish", "fit": "Meankieli", "for": "Fore", "fra": "French", "frp": "Franco-Provencal", "frr": "North Frisian", "fry": "Western Frisian", "fue": "Borgu Fulfulde", "fuf": "Pular", "fuh": "Burkina Fulfulde", "fur": "Friulian", "fuv": "Nigerian Fulfulde", "gag": "Gagauz", "gah": "Alekano aka Gahuku", "gai": "Borei", "gam": "Kandawo", "gan": "Gan", "gaq": "Gata", "gas": "Adiwasi Garasia", "gaw": "Nobonob", "gaz": "West Central Oromo", "gbk": "Gaddi", "gbl": "Gamit", "gbm": "Garhwali", "gcr": "Guianan Creole", "gdg": "Gadang", "gdn": "Umanakaina", "gdr": "Wipi", "geb": "Kire", "gfk": "Patpatar-train", "ghs": "Guhu-Samane", "gla": "Scottish Gaelic", "gle": "Irish Gaelic", "glg": "Galician", "glk": "Gilaki", "glv": "Manx Gaelic", "gmv": "Gamo", "gng": "Ngangam", "gnn": "Gumatj", "gnw": "Western Bolivian Guarani", "gof": "Gofa", "gok": "Gowli", "gom": "Goan Konkani", "gor": "Gorontalo", "got": "Gothic", "gqr": "Gor", "grc": "Ancient Greek", "grn": "Guarani", "gsw": "Alemannic", "gub": "Guajajara", "guc": "Wayuu", "guh": "Guahibo", "gui": "Eastern Bolivian Guarani", "guj": "Gujarati", "gul": "Sea Island Creole English", "gum": "Guambiano", "gun": "Mbya Guarani", "guo": "Guayabero", "gup": "Kunwijku", "gux": "Gourmantche", "gvc": "Guanano", "gvf": "Golin", "gvn": "Kuku Yalanji", "gvs": "Gumawana", "gwi": "Gwichin", "gym": "Ngabere", "gyr": "Guarayu", "hak": "Hakka", "hat": "Haitian Creole", "hau": "Hausa", "haw": "Hawaiian", "hbo": "Ancient Hebrew", "hch": "Huichol", "heb": "Hebrew", "heg": "Helong", "hif": "Fiji Hindi", "hin": "Hindi", "hix": "Hixkaryana", "hla": "Halia", "hlb": "Halbi", "hlt": "Matu Chin", "hmo": "Hiri Motu", "hns": "Caribbean Hindustani", "hop": "Hopi", "hot": "Hote-Male", "hoy": "Holiya", "hrv": "Croatian", "hsb": "Upper Sorbian", "hto": "Minica Huitoto", "hub": "Huambisa", "hui": "Huli", "hun": "Hungarian", "hus": "Huastec", "huu": "Murui Huitoto", "huv": "San Mateo del Mar Huave", "hva": "San Luis Potosi Huastec", "hvn": "Hawu", "hwc": "Hawaiian Pidgin", "hye": "Eastern Armenian", "hyw": "Western Armenian-1853", "ian": "Ngepma Kwundi", "ibo": "Igbo", "icr": "Islander-Creole-English", "ido": "Ido", "ifa": "Amganad Ifugao", "ifu": "Mayoyao Ifugao", "ify": "Antipolo Ifugao", "ign": "Ignaciano", "iii": "Sichuan Yi", "ikk": "Ika", "ikw": "Ikwere", "ile": "Interlingue", "ilo": "Ilocano", "imo": "Imbo Ungu", "ina": "Interlingua", "inb": "Inga", "ind": "Indonesian", "inh": "Ingush", "ino": "Inoke-Yat", "iou": "Tuma-Irumu", "ipi": "Ipili", "iqw": "Ikwo", "iri": "Irigwe", "isd": "Isnag", "isl": "Icelandic", "isn": "Kiisanzu", "ita": "Italian", "ivb": "Ibatan", "ivv": "Ivatan", "iws": "Sepik Iwam", "ixl": "Ixil Cotzal", "izz": "Izii", "jaa": "Jamamadi", "jac": "Jakalteko", "jae": "Jabem", "jam": "Jamaican Patois", "jao": "Yanyuwa", "jav": "Javanese", "jbo": "Lojban", "jic": "Tol", "jid": "Jida", "jiv": "Shuar", "jni": "Ajanji", "jpn": "Japanese", "juy": "Juray", "jvn": "Caribbean Javanese", "kaa": "Karakalpak", "kab": "Kabyle", "kaj": "Jju", "kal": "Kalaallisut", "kan": "Kannada", "kaq": "Capanahua", "kat": "Georgian", "kaz": "Kazahk", "kbc": "Kadiweu", "kbd": "Kabardian", "kbh": "Camsa", "kbm": "Iwal", "kbp": "Kabiye", "kbq": "Kamano-Kafe", "kca": "Khanty", "kdc": "Kutu", "kde": "Makonde", "kdl": "Tsikimba", "kek": "Kekchi", "ken": "Kenyang", "kew": "West Kewa", "kfs": "Bilaspuri", "kfw": "Kharam Naga", "kfx": "Kulvi Outer Seraji", "kfy": "Soriyali Kumaoni", "kgf": "Mongi", "kgk": "Kaiwa", "kgp": "Kaingang", "khm": "Central Khmer", "khn": "Khandesi", "khs": "Kasua", "khw": "Khowar", "khz": "Kalo aka Keapara", "kij": "Kilivila", "kik": "Gikuyu", "kin": "Kinyarwanda", "kip": "Sheshi Kham", "kiu": "Kirmanjaki", "kiz": "Kisi", "kjb": "Eastern Kanjobal", "kje": "Kisar", "kjo": "Pahari Kinnauri", "kjp": "Pwo Eastern Karen", "kjs": "East Kewa", "kkc": "Odoodee", "kkl": "Kosarek Yale", "klt": "Nukna", "klv": "Maskelynes", "kmg": "Kate", "kmh": "Kalam Minimib dialect", "kmk": "Limos Kalinga", "kmo": "Washkuk", "kms": "Kamasau", "kmu": "Kanite", "kne": "Kankanaey", "knf": "Mankanya", "knj": "Akateko", "knv": "Tabo Aramia dialect", "kog": "Kogi", "koi": "Komi-Permyak", "kom": "Komi", "kor": "Korean", "kos": "Kosrae", "kpf": "Komba", "kpg": "Kapingamarangi", "kpj": "Karaja", "kpr": "Korafe-Yegha", "kpw": "Kobon", "kpx": "Mountain Koiali", "kqa": "Mum", "kqc": "Doromu-Koki", "kqe": "Eastern Kalagan", "kqf": "Kakabai", "kql": "Kyenele", "kqw": "Kandas", "krc": "Karachay Balkar", "ksc": "Southern Kalinga", "ksd": "Kuanua aka Tolai", "ksh": "Ripuarian", "ksj": "Uare", "ksr": "Borong", "ktj": "Plapo Krumen", "ktm": "Kurti", "kto": "Kuot", "kud": "Auhelawa", "kue": "Kuman", "kum": "Kumyk", "kup": "Kunimaipa", "kur": "Kurdish", "kvg": "Kuni-Boazi", "kvn": "Border Kuna", "kwd": "Kwaio", "kwf": "Kwaraae", "kwi": "Awa-Cuaiquer", "kwj": "Kwanga", "kxp": "Wadiyari Koli", "kxv": "Kuvi", "kyc": "Kyaka Ena", "kyf": "Kouya", "kyg": "Keyagana", "kyq": "Kenga", "kyu": "Western Kayah", "kyv": "Kayort", "kyz": "Kayabi", "kze": "Kosena", "lac": "Lacandon", "lad": "Ladino", "lao": "Lao", "lat": "Latin", "lbb": "Label", "lbf": "Lahauli", "lbk": "Central Bontok", "lbm": "Lodhi", "lcm": "Tungag", "leu": "Kara", "lex": "Luang", "lez": "Lezgian", "lfn": "Lingua Franca Nova", "lgl": "Wala", "lid": "Nyindrou", "lif": "Limbu", "lij": "Ligurian", "lim": "Limburgish", "lin": "Lingala", "lit": "Lithuanian", "liv": "Livonian", "lki": "Laki", "lld": "Ladin", "llg": "Rote Lole", "lmo": "Lombard", "lrc": "Northern Luri", "ltg": "Latgalian", "lti": "Lithuanian", "ltz": "Luxembourgish", "lug": "Luganda", "luo": "Dholuo", "lus": "Mizo Lushai", "luz": "Southern Luri", "lvs": "Latvian", "lww": "Lewo", "lzh": "Classical Chinese", "lzz": "Laz", "maa": "Mazatec San Antonio", "mah": "Marshallese", "mai": "Maithili", "maj": "Jalapa de Diaz Mazatec", "mal": "Malayalam", "mam": "Central Mam", "maq": "Chiquihuitlan Mazatec", "mar": "Marathi", "mau": "Huautla Mazatec", "mav": "Satere-Mawe", "maz": "Central Mazahua", "mbb": "Western Bukidnon Manobo", "mbc": "Macushi", "mbd": "Dibabawon Manobo", "mbh": "Mangseng", "mbi": "Ilianen Manobo", "mbj": "Nadeb", "mbl": "Maxakali", "mbs": "Sarangani Manobo", "mbt": "Matigsalug Manobo", "mca": "Maka", "mcb": "Machiguenga", "mcd": "Sharanahua", "mcf": "Matses", "mco": "Coatlan Mixe", "mcp": "Makaa", "mcq": "Managalasi", "mcr": "Menya", "mdf": "Moksha", "mdy": "Maale", "med": "Melpa", "mee": "Mengen", "meh": "Southwestern Tlaxiaco Mixtec", "mek": "Mekeo", "meq": "Merey", "met": "Mato", "meu": "Motu", "mfy": "Mayo", "mgc": "Morokodo", "mgh": "Makhuwa-Meetto", "mhr": "Meadow Mari", "mib": "Atatlahuca Mixtec", "mie": "Ocotepec Mixtec", "mig": "San Miguel el Grande Mixtec", "mih": "Chayuco Mixtec", "mil": "Penoles Mixtec", "mim": "Mixtec-Alacatlatzala", "min": "Minankabau", "mio": "Pinotepa Nacional Mixtec", "mir": "Isthmus Mixe", "mit": "Southern Puebla Mixtec", "mix": "Mixtepec Mixtec", "miy": "Ayutla Mixtec", "miz": "Coatzospan Mixtec", "mjc": "San Juan Colorado Mixtec", "mjl": "Mandeali", "mkd": "Macedonian", "mkj": "Mokilese", "mkl": "Monkole", "mkn": "Kupang", "mks": "Silacayoapan Mixtec", "mle": "Manambu", "mlg": "Malagasy", "mlh": "Mape", "mlp": "Bargam", "mlt": "Maltese", "mmn": "Mamanwa", "mmo": "Mangga Buang", "mmx": "Madak", "mna": "Mbula", "mnc": "Manchu", "mni": "Meitei", "mnw": "Mon", "moh": "Mohawk", "mon": "Mongolian", "mop": "Mopan Maya", "mox": "Molima", "mpd": "Machinere", "mpj": "Martu Wangka", "mpm": "Yosondua Mixtec", "mpp": "Migabac", "mps": "Dadibi", "mpt": "Mian Weng", "mpx": "Misima-Paneati", "mqb": "Mbuko", "mqj": "Mamasa", "mri": "Maori", "mrj": "Hill Mari", "msb": "Masbatenyo", "msc": "Sankaran Maninka", "msk": "Mansaka", "msm": "Agusan Manobo", "msy": "Aruamu", "mta": "Cotabato Manobo", "mti": "Maiwa", "mto": "Totontepec Mixe", "mux": "Bo-Ung aka Mara-Gomu", "muy": "Muyang", "mva": "Manam", "mvn": "Minaveha", "mwc": "Are", "mwe": "Mwera", "mwf": "Murrinpatha", "mwl": "Mirandese", "mwp": "Kala Lagaw", "mxb": "Tezoatlan Mixtec", "mxp": "Tlahuitoltepec Mixe", "mxq": "Juquila Mixe", "mxt": "Jamiltepec Mixtec", "mxv": "Metlatonoc Mixtec", "mya": "Burmese", "myk": "Mamara Senoufo", "myu": "Munduruku", "myv": "Erzya", "myw": "Muyuw", "myy": "Macuna", "mza": "Mixtec-Santa-Maria-Zacatepec", "mzi": "Mazatec Ixcatlan", "mzn": "Mazandarani", "nab": "Southern Nambikuara", "naf": "Nabak", "nag": "Nagamese", "nah": "Nahuatl", "nak": "Nakanai", "nan": "Min Nan", "nap": "Neapolitan", "nas": "Naasioi", "nav": "Navajo", "nbq": "Nggem", "nca": "Iyo", "nce": "Yale", "nch": "Central Huasteca Nahuatl", "ncj": "Northern Puebla Nahuatl", "ncl": "Michoacan Nahuatl", "ncu": "Chumburung", "nde": "isiNdebele", "ndg": "Kindengereko", "ndj": "Ndamba", "nds": "Dutch Low Saxon", "new": "Newar", "nfa": "Dhao", "nfr": "Nafaanra", "ngp": "Nguu", "ngu": "Guerrero Nahuatl", "nhe": "Eastern Huasteca Nahuatl", "nhg": "Tetelcingo Nahuatl", "nhi": "Zacatlan-Ahuacatlan-Tepetzintla Nahuatl", "nho": "Takuu", "nhr": "Naro", "nhu": "Noone", "nhw": "Western Huasteca Nahuatl", "nhx": "Isthmus-Mecayapan Nahuatl", "nhy": "Northern Oaxaca Nahuatl", "nif": "Nek", "nii": "Nii", "nin": "Ninzo", "niy": "Ndruna", "nko": "Nkonya", "nld": "Dutch", "nlg": "Gela", "nlx": "Nahali", "nmw": "Saisai", "nna": "Nyangumarta", "nno": "Nynorsk", "nnq": "Ngindo", "noa": "Woun Meu-altortho", "nob": "Norsk Bokmal", "nod": "Northern Thai", "noi": "Noiri", "nop": "Numangan", "not": "Nomatsiguenga", "nou": "Ewage-Notu", "nov": "Novial", "npi": "Nepali", "npl": "Southeastern Puebla Nahuatl", "nqo": "Nko", "nsn": "Nehan", "nso": "Northern Sotho", "nss": "Nali", "nsu": "Sierra Negra Nahuatl", "ntj": "Ngaanyatjarra", "ntp": "Northern Tepehuan", "ntu": "Natqgu", "nuy": "Wubuy", "nvm": "Namiai aka Barai", "nwi": "Southwest Tanna", "nya": "Chichewa", "nys": "Nyoongar", "nyu": "Nyungwe", "obo": "Obo Manobo", "oci": "Occitan", "okv": "Orokaiva Ehija dialect", "olo": "Livvi", "omw": "Sotuh Tairora Omwunra-Toqura", "ong": "Olo", "ons": "Ono", "ood": "Tohono Oodham", "opm": "Oksapmin", "ory": "Oriya", "oss": "Ossetian", "ota": "Ottoman Turkish", "ote": "Mezquital Otomi", "otm": "Eastern Highland Otomi", "otn": "Tenango Otomi", "otq": "Queretaro Otomi", "ots": "Estado de Mexico Otomi", "oym": "Wayampi", "pab": "Parecis", "pad": "Paumari", "pag": "Pangasinan", "pah": "Tenharim", "pam": "Kapampangan", "pan": "Eastern Panjabi", "pao": "Nothern Paiute", "pap": "Papiamentu", "pbb": "Paez", "pbc": "Patamona", "pcd": "Picard", "pdc": "Pennsylvania Dutch", "peg": "Pengo", "pes": "Persian", "pfl": "Pfaelzisch", "pib": "Yine", "pio": "Piapoco", "pir": "Piratapuyo", "piu": "Pintupi-Luritja", "pjt": "Pitjantjatjara", "pli": "Pali", "pls": "San Marcos Tlalcoyalco Popoloca", "plt": "Plateau Malagasy", "plu": "Palikur", "plw": "Brookes Point Palawano", "pma": "Paama", "pms": "Piedmontese", "pnb": "Western Panjabic", "pnt": "Pontic", "pob": "Western Poqomchi", "poe": "San Juan Atzingo Popoloca", "poh": "Poqomchi", "poi": "Highland Popoluca", "pol": "Polish", "pon": "Pohnpeian-apocrypha", "por": "Portugese", "poy": "Pogolo", "ppo": "Folopa", "pps": "San Luis Temalacayuca Popoloca", "prf": "Paranan", "pri": "Paici", "prq": "Asheninka Perene", "pst": "Pashto", "ptp": "Patep", "ptu": "Bambam", "pwg": "Gapapaiwa", "qub": "Huallaga Huanuco Quechua", "quc": "Kiche Cantel-newortho", "quf": "Lambayeque Quechua", "quh": "South Bolivian Quechua", "qul": "North Bolivian Quechua", "qup": "Southern Pastaza Quechua", "quy": "Quechua-Ayacucho", "qvc": "Cajamarca Quechua", "qve": "Eastern Apurimac Quechua", "qvh": "Huamalies-Dos de Mayo Huanuco Quechua", "qvm": "Margos-Yarowilca-Lauricocha Quechua", "qvn": "North Junin Quechua", "qvs": "San Martin Quechua", "qvw": "Huaylla Wanca Quechua", "qvz": "Northern Pastaza Quichua", "qwh": "Huaylas Ancash Quechua", "qxh": "Panao Huanuco Quechua", "qxl": "Salasaca Highland Quichua", "qxn": "Northern Conchucos Ancash Quechua", "qxo": "Southern Conchucos Ancash Quechua", "rai": "Ramoaaina", "ram": "Kanela", "rap": "Rapa Nui", "reg": "Kikara", "rgu": "Rote Rikou", "rkb": "Rikbaktsa", "rmc": "Carpathian Romani", "rmn": "Balkan Romani", "rmy": "Vlax Romani-Arli", "roh": "Romansh", "ron": "Ludari Romanian", "roo": "Rotokas", "rop": "Kriol", "row": "Rote Dela", "rro": "Waima", "rtw": "Rathawi", "rue": "Rusyn", "ruf": "Luguru", "rug": "Roviana", "rup": "Aromanian", "rus": "Russian", "rwo": "Karo Rawa", "sab": "Buglere", "sah": "Sakha", "san": "Sanskrit", "sat": "Santali", "sbe": "Saliba", "sbk": "Kisafwa", "sbl": "Sambali Botolan", "sbs": "Chikuahane", "sby": "Soli", "sch": "Sakachep", "sck": "Sadri", "scn": "Sicilian", "sco": "Scots", "sdh": "Sourthern Kurdish", "seh": "Sena", "sey": "Secoya", "sgb": "Mag-antsi Ayta", "sgj": "Surgujia", "sgs": "Samogitian", "sgz": "Sursurunga", "shi": "Tachelhit", "shj": "Shatt", "shn": "Shan", "shp": "Shipibo-Conibo", "sim": "Mende", "sin": "Sinhalese", "sja": "Epena", "skr": "Saraiki", "sli": "Lower Silesian", "slk": "Slovak", "sll": "Salt-Yui", "slv": "Slovenian", "sme": "Northern Sami", "smk": "Bolinao", "smo": "Samoan", "sna": "Shona", "snc": "Sinaugoro", "snd": "Sindhi", "snn": "Siona", "snp": "Siane Komongu dialect", "sny": "Saniyo-Hiyewe", "som": "Somali", "soq": "Kanasi", "soy": "Sola", "spa": "Spanish", "spl": "Selepet", "spm": "Akukem", "spp": "Supyire Senoufo", "sps": "Saposa", "spy": "Sabaot", "srd": "Sardinian", "sri": "Siriano", "srm": "Saramaccan", "srn": "Sranan", "srp": "Serbian", "srq": "Siriono", "srx": "Sirmauri", "ssd": "Siroi", "ssg": "Seimat", "ssx": "Sembeleke", "stp": "Southeastern Tepehuan", "stq": "Saterland Frisian", "sua": "Sulka", "suc": "Western Subanon", "sue": "Suena", "sun": "Sundanese", "sus": "Susu", "suz": "Sunwar", "swe": "Swedish", "swh": "Swahili", "swp": "Suau", "sxb": "Suba", "syb": "Central Subanen", "szl": "Silesian", "szy": "Sakizaya", "tac": "Western Tarahumara", "taj": "Eastern Tamang", "tam": "Tamil", "tar": "Tarahumara-del-Centro", "tat": "Tatar", "tau": "Upper Tanana", "tav": "Tatuyo", "taw": "Tay", "tay": "Atayal", "tbc": "Takia", "tbf": "Mandara", "tbg": "Arau", "tbk": "Calamian Tagbanwa", "tbl": "Tboli", "tbo": "Tawala", "tbz": "Ditammari", "tca": "Ticuna", "tcf": "Malinaltepec Mephaa", "tcs": "Yumplatok", "tcy": "Tulu", "tcz": "Thado Chin-train", "tdj": "Tajio", "tdt": "Tetun Dili", "tdx": "Tandroy-Mahafaly Malagasy", "ted": "Tepo Krumen", "tee": "Huehuetla Tepehua", "tel": "Telugu", "ter": "Terena", "tet": "Tetun", "tew": "Tewa", "tfr": "Teribe", "tgk": "Tajik", "tgl": "Tagalog", "tgo": "Sudest", "tgp": "Tangoa", "tha": "Thai", "thr": "Rana Tharu", "tif": "Tifal", "tik": "Tikar", "tim": "Timbe", "tir": "Tigrinya", "tiw": "Tiwi", "tiy": "Tiruray", "tke": "Takwane", "tkr": "Tsakhur", "tku": "Upper Necaxa Totonac", "tlf": "Telefol Weng", "tlh": "Klingon", "tly": "Talysh", "tmd": "Haruai", "tna": "Tacana", "tnc": "Tanimuca-Retuara", "tnk": "Kwamera", "tnn": "North Tanna", "tnp": "Whitesands", "toc": "Coyutla Totonac", "tod": "Toma", "tof": "Gizzra", "toj": "Tojolabal", "tok": "Toki Pona", "ton": "Tongan", "too": "Xicotepec de Juarez Totonac", "top": "Papantla Totonac", "tos": "Highland Totonac", "tpi": "Tok Pisin", "tpt": "Tlachichilco Tepehua", "tpx": "Acatepec Mephaa", "tpz": "Vasui aka Tinputz", "trc": "Copala Triqui", "trq": "Triqui-San-Martin-Itunyoso", "trs": "Chicahuaxtla Triqui", "trv": "Taroko", "tsn": "Setswana", "tso": "Tsonga", "tsw": "Tsishingini", "ttc": "Tektiteko", "tte": "Tubetube", "tuc": "Saveeng Oov", "tue": "Tuyuca", "tuf": "Central Tunebo", "tuk": "Turkmen", "tuo": "Tucano", "tur": "Turkish", "tvk": "Southeast Ambrym", "tvt": "Tutsa Naga", "twi": "Twi", "txq": "Rote Tii", "txu": "Kayapo", "tyv": "Tuvinian", "tzc": "Tzotzil de Chamula", "tze": "Tzotzil de Chenalho", "tzj": "Eastern Tzutujil", "tzm": "Central Atlas Tamazight", "tzo": "Tzotzil-Huixtan", "tzs": "Tzotzil San Andres", "tzz": "Tzotzil Zinacantan", "ubr": "Ubir", "ubu": "Umbu-Ungu Andale", "udm": "Udmurt", "udu": "Uduk", "uig": "Uyghur", "ukr": "Ukrainian", "uli": "Ulithian", "ulk": "Meriam Mir", "unx": "Munda", "upv": "Uripiv", "ura": "Urarina", "urb": "Kaapor", "urd": "Urdu", "uri": "Urim", "urt": "Urat", "urw": "Sob Dora", "ury": "Orya", "usa": "Usarufa", "usp": "Uspanteko", "uvh": "Uri", "uvl": "Lote", "uzb": "Uzbek", "vah": "Varhadi-Nagpuri", "vai": "Vai", "var": "Huarijio", "vec": "Venetian", "vep": "Vepsian", "vid": "Vidunda", "vie": "Vietnamese", "viv": "Iduna", "vls": "Vlaams", "vmy": "Ayautla Mazateco", "vol": "Volapuk", "vro": "Voro", "waj": "Waffa", "wal": "Wolaytta", "wap": "Wapishana", "wat": "Kaninuwa", "waw": "Waiwai", "wbi": "Kivwanji", "wbp": "Warlpiri", "wed": "Wedau", "wer": "Weri", "wim": "Wik-Mungkan", "wiu": "Witu", "wiv": "Vitu", "wln": "Walloon", "wmt": "Walmajarri", "wmw": "Mwani", "wnc": "Wantoat", "wnu": "Usan", "wol": "Wolof", "wos": "Hanga Hundi", "wrk": "Garrwa", "wrs": "Walsa Waris", "wsk": "Waskia", "wuu": "Wu", "wuv": "Wuvalu-Aua", "xal": "Kalmyk", "xav": "Xavante", "xbi": "Kombio Wampukuamp", "xed": "Hdi", "xer": "Xerente", "xho": "Xhosa", "xir": "Xiriana", "xla": "Kamula", "xmf": "Mingrelian", "xnj": "Chingoni", "xnn": "Northern Kankanay", "xno": "Norman", "xnr": "Kangri", "xon": "Konkomba", "xri": "Krikati Gaviao", "xsb": "Sambal", "xsi": "Sio", "xta": "Alcozauca Mixtec", "xtd": "Diuxi Mixtec-tilantongo", "xtm": "Magdalena Penasco Mixtec", "xtn": "Northern Tlaxico Mixtec", "xuo": "Kuo", "yaa": "Yaminahua", "yad": "Yagua", "yal": "Yalunka", "yam": "Yamba", "yao": "Chiyawo", "yap": "Yapese", "yaq": "Yaqui", "yby": "Yaweyuha", "ycn": "Yucuna", "yid": "Yiddish", "yka": "Yakan", "yle": "Yele Rossel", "yml": "Iamalele", "yom": "Yombe", "yon": "Yongkom", "yor": "Yoruba", "yrb": "Yareba", "yre": "Yaoure", "yss": "Yessan-Mayo Yamano dialect", "yua": "YucatecMaya", "yue": "Cantonese", "yuj": "Karkar-Yuri", "yut": "Yopno", "yuw": "Yau", "yva": "Yawa", "zaa": "Sierra de Juarez Zapotec", "zab": "San Juan Guelavia Zapotec", "zac": "Ocotlan Zapotec", "zad": "Cajonos Zapotec", "zae": "Yareni Zapotec", "zai": "Isthmus Zapotec", "zaj": "Zaramo", "zam": "Miahuatlan Zapotec", "zao": "Ozolotepec Zapotec", "zaq": "Aloapam Zapotec", "zar": "Rincon Zapotec", "zas": "Santo Domingo Albarradas Zapotec", "zat": "Tabaa Zapotec", "zav": "Yatzachi Zapotec", "zaw": "Mitla Zapotec", "zca": "Coatecas Altas Zapotec", "zea": "Zealandic", "zga": "Mahanji", "zgh": "Standard Moroccan Tamazight", "zia": "Zia", "ziw": "Zigua", "zlm": "Malay", "zos": "Francisco Leon Zoque", "zpc": "Choapan Zapotec", "zpg": "Guevea de Humboldt Zapotec", "zpi": "Santa Maria Quiegolani Zapotec", "zpl": "Lachixio Zapotec", "zpm": "Mixtepec Zapotec", "zpo": "Amatlan Zapotec", "zpq": "Zoogocho Zapotec", "zpt": "Zapotec San Vicente Coatlan", "zpu": "Yalalag Zapotec", "zpv": "Chichicapan Zapotec", "zpz": "Texmelucan Zapotec", "zsr": "Southern Rincon Zapotec", "ztg": "Xanaguia Zapotec", "ztq": "Quioquitani-Quieri Zapotec", "zty": "Yatee Zapotec", "zul": "Zulu", "zyp": "Zyphe Chin",},
    },


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
