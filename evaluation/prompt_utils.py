TASK_TO_PROMPT = {
    'eng': {
        # NOT NLG
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
        # Tasks.QUESTION_ANSWERING
        'QA': [
            'Refer to the passage below and answer the following question:\nPassage: [CONTEXT]\nQuestion: [QUESTION]\nAnswer:',
            '[CONTEXT]\nBased on the text, [QUESTION]\nAnswer: ',
            '[CONTEXT]\nQuestion: [QUESTION]\nReferring to the passage above, the correct answer to the given question is: '
            #'Refer to the passage below and answer the following question:\nPassage: [CONTEXT]\nQuestion: [QUESTION\nChoices: [ANSWER_CHOICES]\nAnswer: [LABEL_CHOICE]',
            #'[CONTEXT]\nBased on the above text, [QUESTION]\nChoices: [ANSWER_CHOICES]\nAnswer: [LABEL_CHOICE]',
            #'[CONTEXT]\nQuestion: [QUESTION]\nChoices:[ANSWER_CHOICES]\nReferring to the passage above, the correct answer to the given question is: [LABEL_CHOICE]',
            #'Paragraph: [CONTEXT]\nQuestion: [QUESTION]\nChoices: [ANSWER_CHOICES]\nBased on the paragraph, what is the answer to the question? [LABEL_CHOICE]',
            #'Passage: [CONTEXT]\nQuestion: [QUESTION]\nChoices: [ANSWER_CHOICES]\nAnswer: [LABEL_CHOICE]'
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
        # Tasks.COMMONSENSE_REASONING
        'CR': [
            'Question: [QUESTION]\nWhat reply makes more sense to answer this question?\nChoices: [ANSWER_CHOICES]\nAnswer: [LABEL_CHOICE]',
            'Based on the the following question: "[QUESTION]" and choices: [ANSWER_CHOICES], the correct answer is: [LABEL_CHOICE]',
            'Question: [QUESTION]\nChoices: [ANSWER_CHOICES]\nThe correct answer to the given question is: [LABEL_CHOICE]',
            'What is the answer to the following question according to common sense?\nQuestion: [QUESTION]\nChoices: [ANSWER_CHOICES]\nAnswer: [LABEL_CHOICE]',
            'Question: [QUESTION]\nChoices: [ANSWER_CHOICES]\nAnswer: [LABEL_CHOICE]'
        ],
        # Tasks.LANGUAGE_IDENTIFICATION
        'LI': [
            'Classify the language of the text below.\n[INPUT] => [LABEL_CHOICE]',
            'Predict the language of the following text.\nText: [INPUT]\nAnswer: [LABEL_CHOICE]',
            '[INPUT]\nWhat would be the language of the text above? [LABEL_CHOICE]',
            'What is the language of this text?\nText: [INPUT]\nAnswer: [LABEL_CHOICE]',
            'Text: [INPUT]\nPlease classify the language of above text. Answer: [LABEL_CHOICE]',
        ],

        # NLG STARTS HERE
        # Tasks.MACHINE_TRANSLATION
        'MT': [
            'Translate the following text from [SOURCE] to [TARGET]. Give your translation directly.\nText: [INPUT]\nTranslation:',
            '[INPUT]\nTranslate the text above from [SOURCE] to [TARGET]. Give your translation directly.',
            'Text in [SOURCE]: [INPUT]\nHow would you translate that in [TARGET]? Give your answer directly.'
            #'Translate the following [SOURCE] text to [TARGET].\nText: [INPUT]\nTranslation:',
            #'Text in [SOURCE]: [INPUT]\nText in [TARGET]:',
        ],
        
        # Tasks.SUMMARIZATION
        'SUM': [
            'Write a summary from the following text.\nText: [INPUT]\nSummary:',
            '[INPUT]\nWrite a summary of the text above.',
            'Text: [INPUT]\nHow would you summarize this text?'
            #'Summarize this text: [INPUT]\nSummary:',
            #'[INPUT]\nGiven the above document, write one sentence to summarize:',
        ],

        # Tasks.CROSSLINGUAL_SUMMARIZATION
        'CSUM': [
            'Write a summary from the following text.\nText: [INPUT]\nSummary:',
            '[INPUT]\nWrite a summary of the text above.',
            'Text: [INPUT]\nHow would you summarize this text?'
        ],

        # Tasks.INSTRUCTION_TUNING
        'IT': [
            'Task: [INPUT]\n What is your output upon completing the insturction or question given?',
            'Address the instruction or question below: [INPUT]',
            'Produce the best output for the following task: [INPUT]'
        ],

        # Task.QA_EXTRACTIVE_ABSTRACTIVE
        'QAE':[
            'Refer to the passage below and answer the following question:\nPassage: [CONTEXT]\nQuestion: [QUESTION]\nAnswer:',
            '[CONTEXT]\nBased on the text, [QUESTION]\nAnswer: ',
            '[CONTEXT]\nQuestion: [QUESTION]\nReferring to the passage above, the correct answer to the given question is: '
        ]

    },
    
    'ind': {
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
        # Tasks.QUESTION_ANSWERING
        'QA': [
            'Lihat paragraf di bawah ini dan jawab pertanyaannya.\nParagraf: [CONTEXT]\nPertanyaan: [QUESTION]\nPilihan: [ANSWER_CHOICES]\nJawaban: [LABEL_CHOICE]',
            '[CONTEXT]\nBerdasarkan teks di atas, [QUESTION]\nPilihan: [ANSWER_CHOICES]\nJawaban: [LABEL_CHOICE]',
            '[CONTEXT]\nPertanyaan: [QUESTION]\nPilihan: [ANSWER_CHOICES]\nMengacu pada teks di atas, jawaban yang benar untuk pertanyaan yang diberikan adalah: [LABEL_CHOICE]',
            'Paragraf: [CONTEXT]\nPertanyaan: [QUESTION]\nPilihan: [ANSWER_CHOICES]\nBerdasarkan paragraf di atas, apa jawaban dari pertanyaan yang diberikan? [LABEL_CHOICE]',
            'Teks: [CONTEXT]\nPertanyaan: [QUESTION]\nPilihan: [ANSWER_CHOICES]\nJawaban: [LABEL_CHOICE]'
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
        # Tasks.COMMONSENSE_REASONING
        'CR': [
            'Pertanyaan: [QUESTION]\nBalasan apa yang lebih masuk akal untuk menjawab pertanyaan tersebut?\nPilihan: [ANSWER_CHOICES]\nJawaban: [LABEL_CHOICE]',
            'Berdasarkan pertanyaan berikut: "[QUESTION]" dan pilihan: [ANSWER_CHOICES], jawaban yang benar adalah: [LABEL_CHOICE]',
            'Pertanyaan: [QUESTION]\nPilihan: [ANSWER_CHOICES]\nJawaban yang benar untuk pertanyaan tersebut adalah: [LABEL_CHOICE]',
            'Jawaban apa yang wajar diberikan untuk pertanyaan berikut?\nPertanyaan: [QUESTION]\nPilihan: [ANSWER_CHOICES]\nJawaban: [LABEL_CHOICE]',
            'Pertanyaan: [QUESTION]\nPilihan: [ANSWER_CHOICES]\nJawaban: [LABEL_CHOICE]'
        ],
        # Tasks.LANGUAGE_IDENTIFICATION
        'LI': [
            'Klasifikasikan bahasa dari kalimat berikut.\n[INPUT] => Bahasa [LABEL_CHOICE]',
            'Prediksikan bahasa dari kalimat berikut.\nTeks: [INPUT]\nJawaban: [LABEL_CHOICE]',
            '[INPUT]\nApakah bahasa dari kalimat diatas? [LABEL_CHOICE]',
            'Apakah bahasa dari teks berikut?\nTeks: [INPUT]\nBahasa [LABEL_CHOICE]',
            'Teks: [INPUT]\nTolong klasifikasikan bahasa dari teks diatas. Jawaban: Bahasa [LABEL_CHOICE]',
        ],

        # NLG TASKS
        # Tasks.SUMMARIZATION
        'SUM': [
            'Tuliskan ringkasan dari teks berikut.\nTeks: [INPUT]\nRingkasan:',
            '[INPUT]\nTulis ringkasan dari teks di atas.',
            'Teks: [INPUT]\nApa ringkasan dari teks tersebut?'
            #'Ringkaslah teks berikut: [INPUT]\nRingkasan:',
            #'[INPUT]\nBerdasarkan dokumen di atas, tulis satu kalimat ringkasan:',
        ],
        # Tasks.MACHINE_TRANSLATION
        'MT': [
            'Terjemahkan teks berikut dari bahasa [SOURCE] ke bahasa [TARGET].\nTeks: [INPUT]\nTerjemahan:',
            '[INPUT]\nTerjemahkan teks di atas dari bahasa [SOURCE] ke bahasa [TARGET].',
            'Teks dalam bahasa [SOURCE]: [INPUT]\nApa terjemahannya dalam bahasa [TARGET]?'
            #'Terjemahkan teks bahasa [SOURCE] berikut ke bahasa [TARGET].\nTeks: [INPUT]\nTerjemahan:',
            #'Teks dalam bahasa [SOURCE]: [INPUT]\nTeks dalam bahasa [TARGET]:',
        ],

        # Tasks.CROSSLINGUAL_SUMMARIZATION
        'CSUM': [
            'Tuliskan ringkasan dari teks berikut.\nTeks: [INPUT]\nRingkasan:',
            '[INPUT]\nTulis ringkasan dari teks di atas.',
            'Teks: [INPUT]\nApa ringkasan dari teks tersebut?'
            #'Ringkaslah teks berikut: [INPUT]\nRingkasan:',
            #'[INPUT]\nBerdasarkan dokumen di atas, tulis satu kalimat ringkasan:',
        ],

        # Tasks.INSTRUCTION_TUNING
        'IT': [
            '',
            '',
            ''
        ]
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
    'openlid_seacrowd_text': {
        'eng': {"kbp_Latn": "Kabiyè", "zul_Latn": "Zulu", "zho_Hans": "Chinese", "uig_Arab": "Uighur", "smo_Latn": "Samoan", "hrv_Latn": "Croatian", "tgk_Cyrl": "Tajik", "guj_Gujr": "Gujarati", "azj_Latn": "North Azerbaijani", "mai_Deva": "Maithili", "bul_Cyrl": "Bulgarian", "hne_Deva": "Chhattisgarhi", "wol_Latn": "Wolof", "ind_Latn": "Indonesian", "lit_Latn": "Lithuanian", "epo_Latn": "Esperanto", "prs_Arab": "Dari", "kmr_Latn": "Northern Kurdish", "fao_Latn": "Faroese", "swh_Latn": "Swahili", "slk_Latn": "Slovak", "srp_Cyrl": "Serbian", "bod_Tibt": "Tibetan", "eus_Latn": "Basque", "tir_Ethi": "Tigrinya", "tam_Taml": "Tamil", "kas_Deva": "Kashmiri", "glg_Latn": "Galician", "crh_Latn": "Crimean Tatar", "kon_Latn": "Kongo", "ayr_Latn": "Central Aymara", "por_Latn": "Portuguese", "ben_Beng": "Bengali", "zho_Hant": "Chinese", "bug_Latn": "Buginese", "umb_Latn": "Umbundu", "tzm_Tfng": "Central Atlas Tamazight", "kan_Knda": "Kannada", "tgl_Latn": "Tagalog", "luo_Latn": "Luo", "lij_Latn": "Ligurian", "hun_Latn": "Hungarian", "kin_Latn": "Kinyarwanda", "hat_Latn": "Haitian", "sag_Latn": "Sango", "khm_Khmr": "Khmer", "heb_Hebr": "Hebrew", "hye_Armn": "Armenian", "fuv_Latn": "Nigerian Fulfulde", "cjk_Latn": "Chokwe", "ckb_Arab": "Central Kurdish", "srd_Latn": "Sardinian", "cat_Latn": "Catalan", "dan_Latn": "Danish", "lao_Laoo": "Lao", "fra_Latn": "French", "kam_Latn": "Kamba (Kenya)", "aeb_Arab": "Tunisian Arabic", "ydd_Hebr": "Eastern Yiddish", "afr_Latn": "Afrikaans", "khk_Cyrl": "Halh Mongolian", "lug_Latn": "Ganda", "lin_Latn": "Lingala", "nya_Latn": "Nyanja", "tsn_Latn": "Tswana", "dzo_Tibt": "Dzongkha", "min_Latn": "Minangkabau", "war_Latn": "Waray-Waray", "rus_Cyrl": "Russian", "nob_Latn": "Norwegian Bokmål", "tpi_Latn": "Tok Pisin", "mlt_Latn": "Maltese", "mni_Beng": "Manipuri", "ilo_Latn": "Ilocano", "amh_Ethi": "Amharic", "taq_Latn": "Tamasheq", "acq_Arab": "Ta'izzi-Adeni Arabic", "gaz_Latn": "West Central Oromo", "ltg_Latn": "Latgalian", "kac_Latn": "Jingpho", "ibo_Latn": "Igbo", "gle_Latn": "Irish", "mya_Mymr": "Burmese", "grn_Latn": "Guarani", "kik_Latn": "Kikuyu", "jav_Latn": "Javanese", "awa_Deva": "Awadhi", "ars_Arab": "Najdi Arabic", "swe_Latn": "Swedish", "uzn_Latn": "Northern Uzbek", "mos_Latn": "Mossi", "lus_Latn": "Mizo Chin", "mal_Mlym": "Malayalam", "ita_Latn": "Italian", "dik_Latn": "Southwestern Dinka", "ewe_Latn": "Ewe", "sat_Olck": "Santali", "pan_Guru": "Panjabi", "est_Latn": "Estonian", "kab_Latn": "Kabyle", "bam_Latn": "Bambara", "pag_Latn": "Pangasinan", "isl_Latn": "Icelandic", "eng_Latn": "English", "fon_Latn": "Fon", "kas_Arab": "Kashmiri", "asm_Beng": "Assamese", "lim_Latn": "Limburgan", "bjn_Arab": "Banjar", "taq_Tfng": "Tamasheq", "deu_Latn": "German", "pbt_Arab": "Southern Pashto", "pap_Latn": "Papiamento", "quy_Latn": "Ayacucho Quechua", "kea_Latn": "Kabuverdianu", "npi_Deva": "Nepali", "xho_Latn": "Xhosa", "shn_Mymr": "Shan", "nso_Latn": "Pedi", "urd_Arab": "Urdu", "bos_Latn": "Bosnian", "ron_Latn": "Romanian", "fur_Latn": "Friulian", "gla_Latn": "Scottish Gaelic", "nus_Latn": "Nuer", "ltz_Latn": "Luxembourgish", "arz_Arab": "Egyptian Arabic", "bem_Latn": "Bemba", "fin_Latn": "Finnish", "kir_Cyrl": "Kirghiz", "tha_Thai": "Thai", "mag_Deva": "Magahi", "azb_Arab": "South Azerbaijani", "tel_Telu": "Telugu", "ell_Grek": "Modern Greek", "sot_Latn": "Southern Sotho", "spa_Latn": "Spanish", "vie_Latn": "Vietnamese", "yor_Latn": "Yoruba", "ceb_Latn": "Cebuano", "vec_Latn": "Venetian", "sin_Sinh": "Sinhala", "pol_Latn": "Polish", "als_Latn": "Tosk Albanian", "lmo_Latn": "Lombard", "scn_Latn": "Sicilian", "ces_Latn": "Czech", "fij_Latn": "Fijian", "run_Latn": "Rundi", "som_Latn": "Somali", "mkd_Cyrl": "Macedonian", "mar_Deva": "Marathi", "ast_Latn": "Asturian", "san_Deva": "Sanskrit", "ary_Arab": "Moroccan Arabic", "twi_Latn": "Twi", "acm_Arab": "Mesopotamian Arabic", "nno_Latn": "Norwegian Nynorsk", "zsm_Latn": "Standard Malay", "mri_Latn": "Maori", "kor_Hang": "Korean", "sna_Latn": "Shona", "pes_Arab": "Iranian Persian", "ace_Latn": "Acehnese", "bak_Cyrl": "Bashkir", "kat_Geor": "Georgian", "tur_Latn": "Turkish", "jpn_Jpan": "Japanese", "arb_Arab": "Standard Arabic", "ukr_Cyrl": "Ukrainian", "yue_Hant": "Cantonese", "kaz_Cyrl": "Kazakh", "hau_Latn": "Hausa", "nld_Latn": "Dutch", "oci_Latn": "Occitan", "apc_Arab": "Levantine Arabic", "tum_Latn": "Tumbuka", "ace_Arab": "Acehnese", "dyu_Latn": "Dyula", "knc_Latn": "Central Kanuri", "knc_Arab": "Central Kanuri", "kmb_Latn": "Kimbundu", "bel_Cyrl": "Belarusian", "slv_Latn": "Slovenian", "lvs_Latn": "Standard Latvian", "bho_Deva": "Bhojpuri", "tuk_Latn": "Turkmen", "snd_Arab": "Sindhi", "sun_Latn": "Sundanese", "lua_Latn": "Luba-Lulua", "ajp_Arab": "South Levantine Arabic", "hin_Deva": "Hindi", "tso_Latn": "Tsonga", "tat_Cyrl": "Tatar", "cym_Latn": "Welsh", "ory_Orya": "Odia", "ban_Latn": "Balinese", "szl_Latn": "Silesian", "plt_Latn": "Plateau Malagasy", "bjn_Latn": "Banjar", "ssw_Latn": "Swati"},
        'ind': {"kbp_Latn": "Kabiye", "zul_Latn": "Zulu", "zho_Hans": "Mandarin", "uig_Arab": "Uighur", "smo_Latn": "Samoa", "hrv_Latn": "Kroasia", "tgk_Cyrl": "Tajik", "guj_Gujr": "Gujarati", "azj_Latn": "Azerbaijan Utara", "mai_Deva": "Maithili", "bul_Cyrl": "Bulgaria", "hne_Deva": "Chhattisgarhi", "wol_Latn": "Wolof", "ind_Latn": "Indonesia", "lit_Latn": "Lithuania", "epo_Latn": "Esperanto", "prs_Arab": "Dari", "kmr_Latn": "Kurmanji", "fao_Latn": "Faroe", "swh_Latn": "Swahili", "slk_Latn": "Slovakia", "srp_Cyrl": "Serbia", "bod_Tibt": "Tibet Lhasa", "eus_Latn": "Basque", "tir_Ethi": "Tigrinya", "tam_Taml": "Tamil", "kas_Deva": "Kashmir", "glg_Latn": "Galisia", "crh_Latn": "Tatar Krimea", "kon_Latn": "Kongo", "ayr_Latn": "Aymara Tengah", "por_Latn": "Portugis", "ben_Beng": "Benggala", "zho_Hant": "Cina", "bug_Latn": "Bugis", "umb_Latn": "Umbundu", "tzm_Tfng": "Atlas Pusat Tamazight", "kan_Knda": "Kannada", "tgl_Latn": "Tagalog", "luo_Latn": "Luo", "lij_Latn": "Liguria", "hun_Latn": "Hongaria", "kin_Latn": "Kinyarwanda", "hat_Latn": "Haiti", "sag_Latn": "Sango", "khm_Khmr": "Khmer", "heb_Hebr": "Ibrani", "hye_Armn": "Armenia", "fuv_Latn": "Fulfulde Nigeria", "cjk_Latn": "Chokwe", "ckb_Arab": "Kurdi Tengah", "srd_Latn": "Sardinia", "cat_Latn": "Katalan", "dan_Latn": "Denmark", "lao_Laoo": "Laos", "fra_Latn": "Perancis", "kam_Latn": "Kamba", "aeb_Arab": "Arab Tunisia", "ydd_Hebr": "Yiddish Timur", "afr_Latn": "Afrikanas", "khk_Cyrl": "Halh Mongolia", "lug_Latn": "Ganda", "lin_Latn": "Lingala", "nya_Latn": "Nyanja", "tsn_Latn": "Tswana", "dzo_Tibt": "Dzongkha", "min_Latn": "Minangkabau", "war_Latn": "Waray-Waray", "rus_Cyrl": "Rusia", "nob_Latn": "Bokmål Norwegia", "tpi_Latn": "Tok Pisin", "mlt_Latn": "Malta", "mni_Beng": "Manipuri", "ilo_Latn": "Ilocano", "amh_Ethi": "Amharik", "taq_Latn": "Tamasheq", "acq_Arab": "Arab Ta'izzi-Adeni", "gaz_Latn": "Oromo Tengah Barat", "ltg_Latn": "Latgalia", "kac_Latn": "Jingfo", "ibo_Latn": "Igbo", "gle_Latn": "Irlandia", "mya_Mymr": "Birma", "grn_Latn": "Guarani", "kik_Latn": "Kikuyu", "jav_Latn": "Jawa", "awa_Deva": "Awadhi", "ars_Arab": "Arab Najdi", "swe_Latn": "Swedia", "uzn_Latn": "Uzbekistan Utara", "mos_Latn": "Mossi", "lus_Latn": "Mizo Chin", "mal_Mlym": "Malayalam", "ita_Latn": "Italia", "dik_Latn": "Dinka Barat Daya", "ewe_Latn": "Ewe", "sat_Olck": "Santali", "pan_Guru": "Panjabi", "est_Latn": "Estonia", "kab_Latn": "Kabyle", "bam_Latn": "Bambara", "pag_Latn": "Pangasinan", "isl_Latn": "Islandia", "eng_Latn": "Inggris", "fon_Latn": "Fon", "kas_Arab": "Kashmir", "asm_Beng": "Assam", "lim_Latn": "Limburgan", "bjn_Arab": "Banjar", "taq_Tfng": "Tamasheq", "deu_Latn": "Jerman", "pbt_Arab": "Pashto Selatan", "pap_Latn": "Papiamento", "quy_Latn": "Ayacucho Quechua", "kea_Latn": "Kabuverdianu", "npi_Deva": "Nepal", "xho_Latn": "Xhosa", "shn_Mymr": "Shan", "nso_Latn": "Pedi", "urd_Arab": "Urdu", "bos_Latn": "Bosnia", "ron_Latn": "Rumania", "fur_Latn": "Friulian", "gla_Latn": "Gaelik Skotlandia", "nus_Latn": "Nuer", "ltz_Latn": "Luksemburg", "arz_Arab": "Arab Mesir", "bem_Latn": "Bemba", "fin_Latn": "Finlandia", "kir_Cyrl": "Kirgiz", "tha_Thai": "Thai", "mag_Deva": "Magahi", "azb_Arab": "Azerbaijan Selatan", "tel_Telu": "Telugu", "ell_Grek": "Yunani Modern", "sot_Latn": "Sotho Selatan", "spa_Latn": "Spanyol", "vie_Latn": "Vietnam", "yor_Latn": "Yoruba", "ceb_Latn": "Cebuano", "vec_Latn": "Venesia", "sin_Sinh": "Sinhala", "pol_Latn": "Polandia", "als_Latn": "Tosk Albania", "lmo_Latn": "Lombard", "scn_Latn": "Sisilia", "ces_Latn": "Ceko", "fij_Latn": "Fiji", "run_Latn": "Rundi", "som_Latn": "Somalia", "mkd_Cyrl": "Makedonia", "mar_Deva": "Marathi", "ast_Latn": "Asturian", "san_Deva": "Sansekerta", "ary_Arab": "Arab Maroko", "twi_Latn": "Twi", "acm_Arab": "Arab Mesopotamia", "nno_Latn": "Nynorsk Norwegia", "zsm_Latn": "Melayu Baku", "mri_Latn": "Maori", "kor_Hang": "Korea", "sna_Latn": "Shona", "pes_Arab": "Persia Iran", "ace_Latn": "Aceh", "bak_Cyrl": "Bashkir", "kat_Geor": "Georgia", "tur_Latn": "Turki", "jpn_Jpan": "Jepang", "arb_Arab": "Arab Standar", "ukr_Cyrl": "Ukraina", "yue_Hant": "Kanton", "kaz_Cyrl": "Kazakh", "hau_Latn": "Hausa", "nld_Latn": "Belanda", "oci_Latn": "Occitania", "apc_Arab": "Arab Levantin", "tum_Latn": "Tumbuka", "ace_Arab": "Aceh", "dyu_Latn": "Dyula", "knc_Latn": "Kanuri Tengah", "knc_Arab": "Kanuri Tengah", "kmb_Latn": "Kimbundu", "bel_Cyrl": "Belarusia", "slv_Latn": "Slovenia", "lvs_Latn": "Standar Latvia", "bho_Deva": "Bhojpuri", "tuk_Latn": "Turkmenistan", "snd_Arab": "Sindhi", "sun_Latn": "Sunda", "lua_Latn": "Luba-Lulua", "ajp_Arab": "Arab Levantine Selatan", "hin_Deva": "Hindi", "tso_Latn": "Tsonga", "tat_Cyrl": "Tatar", "cym_Latn": "Wales", "ory_Orya": "Odia", "ban_Latn": "Bali", "szl_Latn": "Silesia", "plt_Latn": "Dataran Tinggi Malagasi", "bjn_Latn": "Banjar", "ssw_Latn": "Swati"},
    },
    'udhr_lid_seacrowd_text': {
        'eng': {"sun": "Sundanese", "ace": "Acehnese", "mad": "Madurese", "lao": "Lao", "cfm": "Falam Chin", "hnj": "Hmong Njua", "min": "Minangkabau", "zlm": "Malay", "tha": "Thai", "blt": "Tai Dam", "hni": "Hani", "jav": "Javanese", "tdt": "Tetun Dili", "cnh": "Hakha Chin", "khm": "Khmer", "ban": "Balinese", "ind": "Indonesian", "mya": "Burmese", "ccp": "Chakma", "duu": "Drung", "tet": "Tetun", "kkh": "Khün", "bug": "Buginese", "vie": "Vietnamese"},
        'ind': {"sun": "Sunda", "ace": "Aceh", "mad": "Madura", "lao": "Laos", "cfm": "Falam Chin", "hnj": "Hmong Njua", "min": "Minangkabau", "zlm": "Malay", "tha": "Thai", "blt": "Tai Dam", "hni": "Hani", "jav": "Jawa", "tdt": "Tetun Dili", "cnh": "Hakha Chin", "khm": "Khmer", "ban": "Bali", "ind": "Indonesia", "mya": "Burma", "ccp": "Chakma", "duu": "Drung", "tet": "Tetun", "kkh": "Khün", "bug": "Bugis", "vie": "Vietnam"},
    },
    'wili_2018_seacrowd_text': {
        'eng': {"nrm": "Narom", "jav": "Javanese", "min": "Minangkabau", "lao": "Lao", "mya": "Burmese", "pag": "Pangasinan", "ind": "Indonesian", "cbk": "Chavacano", "tet": "Tetum", "tha": "Thai", "ceb": "Cebuano", "tgl": "Tagalog", "bjn": "Banjar", "bcl": "Central Bikol", "vie": "Vietnamese"},
        'ind': {"nrm": "Narom", "jav": "Jawa", "min": "Minangkabau", "lao": "Laos", "mya": "Burma", "pag": "Pangasinan", "ind": "Indonesia", "cbk": "Chavacano", "tet": "Tetum", "tha": "Thai", "ceb": "Cebuano", "tgl": "Tagalog", "bjn": "Banjar", "bcl": "Central Bikol", "vie": "Vietnam"},
    },
    # 'lti_langid_corpus_seacrowd_text': {
    #     'eng': {},
    #     'ind': {},
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
        'min': 'Minangkabau',
        'eng': 'English',
        'vie': 'Vietnamese',
        'mya': 'Burmese',
        'gor': 'Gorontalo',
        'ceb': 'Cebuano',
        'ilo': 'Iloko',
        'hil': 'Hiligaynon',
        'khm': 'Khmer',
        'lao': 'Lao',
        'zlm': 'Malay',
        'nia': 'Nias',
        'tgl': 'Tagalog',
        'tha': 'Thai',
        'end': 'Ende',
        'nxe': 'Nage',
        'ssq': 'ssq',
        'ljl': 'Lio',
        'kac': 'Kachin',
        'eng-US': 'English',
        'lus': 'Lushai',
        'min': 'Minangkabau',
        'pag': 'Pangasinan',
        'shn': 'Shan',
        'war': 'Waray',
        'zsm': 'Standard Malay',
        'hmv': 'Hmong Do',
        'bbc': 'Batak Toba',
        'nij': 'Ngaju',
        'fil': 'Filipino',
        'tl': 'Tagalog',
        'km': 'Khmer',
        'vi': 'Vietnamese',
        'th': 'Thai',
        'ms': 'Malay',
        'id': 'Indonesian',
        'lo': 'Lao',
        'my': 'Mayan',
        'en': 'English',
        'tam': 'Tamil'
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
