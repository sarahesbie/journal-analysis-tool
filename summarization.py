from transformers import pipeline, AutoTokenizer

# Initialize the summarizer and tokenizer with specific model and revision
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6", revision="a4f8f3e")
tokenizer = AutoTokenizer.from_pretrained("sshleifer/distilbart-cnn-12-6")
qa_model = pipeline("question-answering", model="distilbert-base-cased-distilled-squad", revision="564e9b5")

def summarize_sections(sections, max_tokens=1024):
    """Summarizes an array of text sections."""
    summaries = []

    for section in sections:
        tokens = tokenizer.encode(section)
        if len(tokens) <= max_tokens:
            try:
                summary = summarizer(section, max_length=150, min_length=30, do_sample=False)[0]['summary_text']
                summaries.append(summary)
            except Exception as e:
                print(f"Error summarizing section: {e}")
        else:
            print("Section exceeded token limit.")

    return summaries

def generate_recommendation(finding, question):
    """Generates recommendations based on findings and a question."""
    response = qa_model(question=question, context=finding)
    return response['answer']
