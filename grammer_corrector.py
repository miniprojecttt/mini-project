from transformers import pipeline

def summarize_text(text):
    summarizer = pipeline('summarization', model='facebook/bart-large-cnn')
    summary = summarizer(text, max_length=150, min_length=30, do_sample=False)
    return summary[0]['summary_text']

# Example text
text = """Think deep and bring something for human, and not to scam us by data bundles Bekaaarr no of use plzz don't waste your data by downloading this unseless app...ye sirf hand ko blue kr deta h nothing else Waste of time or net don't install it useless app This app is fake app not work Waste of time Doesnt show anything not even fake bones It is no useful...Because it is fake. ..."""

# Generate summary
summary = summarize_text(text)
print("Formalized Text:\n")
print(summary)
