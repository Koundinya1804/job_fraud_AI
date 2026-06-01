from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

fraud_phrases = [
    "registration fee required",
    "training fee required",
    "processing charges required",
    "security deposit required",
    "joining amount required",
    "payment required before joining"
]

fraud_embeddings = model.encode(fraud_phrases)


def semantic_fraud_check(text):

    text_embedding = model.encode(text)

    scores = util.cos_sim(text_embedding, fraud_embeddings)

    max_score = scores.max().item()

    if max_score > 0.6:
        return True, max_score

    return False, max_score