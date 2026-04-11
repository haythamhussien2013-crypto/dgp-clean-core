def evaluate(options):
    # اختيار أفضل حل بناء على score
    return max(options, key=lambda x: x["score"])
