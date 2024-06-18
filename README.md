<img width="100%" alt="SEACrowd Logo" src="https://github.com/SEACrowd/.github/blob/main/profile/assets/seacrowd-email-banner-without-logo.png?raw=true">

# SEACrowd Experiments

Experiment repository for the ["SEACrowd: A Multilingual Multimodal Data Hub and Benchmark Suite for Southeast Asian Languages"](https://arxiv.org/pdf/2406.10118) paper.

SEACrowd is a [collaborative initiative](https://github.com/SEACrowd) that consolidates a [comprehensive resource hub](https://seacrowd.github.io/seacrowd-catalogue/) that fills the resource gap by [providing standardized corpora](https://github.com/SEACrowd/seacrowd-datahub) in nearly 1,000 Southeast Asian (SEA) languages across three modalities.

> Note: All code in SEACrowd is publicly available under the Apache 2.0 license.

## SEACrowd Benchmarks: State-of-the-Art Models on SEA Languages

Placed under [`evaluation/`](https://github.com/SEACrowd/seacrowd-experiments/tree/main/evaluation).

Through our SEACrowd benchmarks, we assess the quality of AI models on 36 indigenous languages across 13 tasks, offering valuable insights into the current AI landscape in SEA. Furthermore, we propose strategies to facilitate greater AI advancements, maximizing potential utility and resource equity for the future of AI in SEA.

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
<img width="900" alt="NLP Performance" src="https://github.com/SEACrowd/seacrowd-experiments/blob/main/assets/eval-nlp.png?raw=true">

#### Speech Models
<img width="500" alt="Speech Performance" src="https://github.com/SEACrowd/seacrowd-experiments/blob/main/assets/eval-speech.png?raw=true">

#### VLMs
<img width="500" alt="VL Performance" src="https://github.com/SEACrowd/seacrowd-experiments/blob/main/assets/eval-vl.png?raw=true">

## Generation Quality in SEA Languages: Translationese vs. Natural

Placed under [`translationese/`](https://github.com/SEACrowd/seacrowd-experiments/blob/main/translationese/).

To analyze the generation quality of LLMs in SEA languages, we build a text classifier to discriminate between translationese and natural texts. We construct a translationese classification training and testing dataset using 49 and 62 data subsets, respectively, covering approximately 39.9k and 51.5k sentences across 9 SEA languages: English (eng), Indonesian (ind), Khmer (khm), Lao (lao), Burmese (mya), Filipino (fil), Thai (tha), Vietnamese (vie), and Malay (zlm).

> Our translationese vs. natural train/test data is available on [HuggingFace](https://huggingface.co/datasets/SEACrowd/sea_translationese_resampled)!

To fine-tune the translationese classifier, execute [`translationese/run.sh`](https://github.com/SEACrowd/seacrowd-experiments/blob/main/translationese/run.sh). We use a binary label (translationese, i.e., machine-translated or human-translated, or natural, i.e., human-generated) instead of 3 labels (machine-translated, human-translated, human-generated).

> Our fine-tuned mDEBERTA SEA translationese classifier is available on [HuggingFace](https://huggingface.co/SEACrowd/mdeberta-v3_sea_translationese)!

To obtain the model generations for the naturalness analysis, execute [`translationese/run_nlg_prompt.sh`](https://github.com/SEACrowd/seacrowd-experiments/blob/main/translationese/run_nlg_prompt.sh) for open-source models and [`translationese/run_nlg_prompt_commercial.sh`](https://github.com/SEACrowd/seacrowd-experiments/blob/main/translationese/run_nlg_prompt_commercial.sh) for commercial models.

To classify the model generations, check out [`translationese/analyze_translationese.ipynb`](https://github.com/SEACrowd/seacrowd-experiments/blob/main/translationese/analyze_translationese.ipynb).


### Naturalness Result

<img width="500" alt="Naturalness Result" src="https://github.com/SEACrowd/seacrowd-experiments/blob/main/assets/naturalness-result.png?raw=true">

## Additional Analysis: Language Equity, Resource Gaps, and Language Prioritization

The [`notebooks/viz_metrics.ipynb`](https://github.com/SEACrowd/seacrowd-experiments/blob/main/notebooks/viz_metrics.ipynb) consists of the visualization of all benchmark results in [`figures/`](https://github.com/SEACrowd/seacrowd-experiments/tree/main/figures) and [`notebooks/analysis/`](https://github.com/SEACrowd/seacrowd-experiments/tree/main/notebooks/analysis), as well as language equity results in terms of Gini coefficient in [`notebooks/analysis/`](https://github.com/SEACrowd/seacrowd-experiments/tree/main/notebooks/analysis).g

The [`notebooks/viz_resources.ipynb`](https://github.com/SEACrowd/seacrowd-experiments/blob/main/notebooks/viz_resources.ipynb) consists of the visualization of resource gaps analysis in [`figures/`](https://github.com/SEACrowd/seacrowd-experiments/tree/main/figures) and [`notebooks/analysis/`](https://github.com/SEACrowd/seacrowd-experiments/tree/main/notebooks/analysis).

The [`globalutily/run_make_task_boxes.sh`](https://github.com/SEACrowd/globalutility/blob/main/run_make_task_boxes.sh) consists of the [visualization of SEA language prioritization analysis](https://github.com/SEACrowd/globalutility/tree/main/figs/final). This submodule is derived from [neubig/globalutility](https://github.com/neubig/globalutility).

# Citation

If you are using any resources from SEACrowd, including datasheets, dataloaders, code, etc., please cite [the following publication](https://arxiv.org/pdf/2406.10118):

```
@article{lovenia2024seacrowd,
      title={SEACrowd: A Multilingual Multimodal Data Hub and Benchmark Suite for Southeast Asian Languages}, 
      author={Holy Lovenia and Rahmad Mahendra and Salsabil Maulana Akbar and Lester James V. Miranda and Jennifer Santoso and Elyanah Aco and Akhdan Fadhilah and Jonibek Mansurov and Joseph Marvin Imperial and Onno P. Kampman and Joel Ruben Antony Moniz and Muhammad Ravi Shulthan Habibi and Frederikus Hudi and Railey Montalan and Ryan Ignatius and Joanito Agili Lopo and William Nixon and Börje F. Karlsson and James Jaya and Ryandito Diandaru and Yuze Gao and Patrick Amadeus and Bin Wang and Jan Christian Blaise Cruz and Chenxi Whitehouse and Ivan Halim Parmonangan and Maria Khelli and Wenyu Zhang and Lucky Susanto and Reynard Adha Ryanda and Sonny Lazuardi Hermawan and Dan John Velasco and Muhammad Dehan Al Kautsar and Willy Fitra Hendria and Yasmin Moslem and Noah Flynn and Muhammad Farid Adilazuarda and Haochen Li and Johanes Lee and R. Damanhuri and Shuo Sun and Muhammad Reza Qorib and Amirbek Djanibekov and Wei Qi Leong and Quyet V. Do and Niklas Muennighoff and Tanrada Pansuwan and Ilham Firdausi Putra and Yan Xu and Ngee Chia Tai and Ayu Purwarianti and Sebastian Ruder and William Tjhi and Peerat Limkonchotiwat and Alham Fikri Aji and Sedrick Keh and Genta Indra Winata and Ruochen Zhang and Fajri Koto and Zheng-Xin Yong and Samuel Cahyawijaya},
      year={2024},
      eprint={2406.10118},
      journal={arXiv preprint arXiv: 2406.10118}
}
```
