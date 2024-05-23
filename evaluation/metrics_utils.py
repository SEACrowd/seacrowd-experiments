from sacremoses import MosesTokenizer
import datasets, evaluate

""" Generation metrics """
bleu = datasets.load_metric('bleu')
rouge = datasets.load_metric('rouge')
sacrebleu = datasets.load_metric('sacrebleu')
# chrf = datasets.load_metric('chrf')
meteor = evaluate.load('meteor')
# squad_v2_metric = datasets.load_metric('squad_v2')
mt = MosesTokenizer(lang='id')


def generation_metrics_fn(list_hyp, list_label):
    # hyp and label are both list of string
    # Check if the lists are empty
    if not list_hyp or not list_label or len(list_hyp) != len(list_label):
        raise ValueError("Input lists must be non-empty and of the same length")
    
    list_hyp = [hyp if hyp is not None else "" for hyp in list_hyp]
    list_label = [label if label is not None else "" for label in list_label]
    
    # Tokenize the hypotheses and labels for BLEU computation
    list_hyp_bleu = list(map(lambda x: mt.tokenize(x), list_hyp))
    list_label_bleu = list(map(lambda x: [mt.tokenize(x)], list_label))    
    list_label_sacrebleu = list(map(lambda x: [x], list_label))

    metrics = {}

    # Compute BLEU score
    try:
        metrics["BLEU"] = bleu._compute(list_hyp_bleu, list_label_bleu)['bleu'] * 100
    except ZeroDivisionError:
        metrics["BLEU"] = 0.0

    # Compute SacreBLEU score
    try:
        metrics["SacreBLEU"] = sacrebleu._compute(list_hyp, list_label_sacrebleu)['score']
    except ZeroDivisionError:
        metrics["SacreBLEU"] = 0.0

    # # Compute chrF++ score
    # try:
    #     metrics["chrF++"] = chrf._compute(list_hyp, list_label_sacrebleu)['score']
    # except ZeroDivisionError:
    #     metrics["chrF++"] = 0.0

    # Compute METEOR score
    try:
        metrics["meteor"] = meteor.compute(predictions=list_hyp, references=list_label)['meteor'] * 100
    except ZeroDivisionError:
        metrics["meteor"] = 0.0

    # Compute ROUGE scores
    try:
        rouge_score = rouge._compute(list_hyp, list_label)
        metrics["ROUGE1"] = rouge_score['rouge1'].mid.fmeasure * 100
        metrics["ROUGE2"] = rouge_score['rouge2'].mid.fmeasure * 100
        metrics["ROUGEL"] = rouge_score['rougeL'].mid.fmeasure * 100
        metrics["ROUGELsum"] = rouge_score['rougeLsum'].mid.fmeasure * 100
    except ZeroDivisionError:
        metrics["ROUGE1"] = 0.0
        metrics["ROUGE2"] = 0.0
        metrics["ROUGEL"] = 0.0
        metrics["ROUGELsum"] = 0.0

    return metrics