from transformers import pipeline
import numpy as np

# Create an NLI pipeline with RoBERTa
nli_pipeline = pipeline("zero-shot-classification", model="roberta-large-mnli")

# detect blatant impersonation

def impersonation_detection(premise, hypothesis):
    try:
        result = nli_pipeline(premise, hypothesis)
        return result['scores'][0]
    except Exception:
        return np.nan
        
        
#detect evidence that it is a fan made account in tribute to the person
def fan_tribute_detection(username, hypothesis):
    scores = []
    for i in ["This is a fan-made account for " + username, "This is not the real " + username, "This is a fan page in tribute to " + username]:
        scores.append(nli_pipeline(i, hypothesis)['scores'])
    #print(scores)
    return np.max(scores)

