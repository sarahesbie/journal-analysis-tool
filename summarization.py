from transformers import pipeline, AutoTokenizer
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path='.env.local')

client = OpenAI(
  api_key=os.environ['OPENAI_API_KEY'],  
)

# Initialize the summarizer and tokenizer with specific model and revision
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6", revision="a4f8f3e")
tokenizer = AutoTokenizer.from_pretrained("sshleifer/distilbart-cnn-12-6")
qa_model = pipeline("question-answering", model="distilbert-base-cased-distilled-squad", revision="564e9b5")

from openai import OpenAI
import os

# Initialize the OpenAI client
client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))

def gpt_summary(text, word_limit=150):
    """Uses GPT-4 or GPT-3.5 to summarize text using the Chat API."""
    try:
        # Send the request to the OpenAI Chat API
        response = client.chat.completions.create(
            model="gpt-4",  # Or use "gpt-3.5-turbo"
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes text."},
                {"role": "user", "content": f"Please summarize the following text in {word_limit} words while keeping the first-person perspective intact:\n\n{text}"}
            ],
            max_tokens=word_limit * 4,  # Adjust tokens based on your word limit
            temperature=0.7,
        )

        # Access the summary from the response using the new Pydantic model
        summary = response.choices[0].message.content.strip()

        # Return the summary
        return summary

    except Exception as e:
        return f"Error generating summary: {e}"

def gpt_summary(text, word_limit=150):
    """Uses GPT-4 or GPT-3.5 to summarize text using the Chat API."""
    try:
        # Send the request to the OpenAI Chat API
        response = client.chat.completions.create(
            model="gpt-4",  # Or use "gpt-3.5-turbo"
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes text."},
                {"role": "user", "content": f"Please summarize the following text in {word_limit} words while keeping the first-person perspective intact:\n\n{text}"}
            ],
            max_tokens=word_limit * 4,  # Adjust tokens based on your word limit
            temperature=0.7,
        )

        # Access the summary from the response using the new Pydantic model
        summary = response.choices[0].message.content.strip()

        # Return the summary
        return summary

    except Exception as e:
        return f"Error generating summary: {e}"
    
def gpt_pattern_find(text, word_limit=200):
    """Uses GPT-4 or GPT-3.5 to find patterns and themes in the text."""
    try:
        # Send the request to the OpenAI Chat API
        response = client.chat.completions.create(
            model="gpt-4",  # Or use "gpt-3.5-turbo"
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes text."},
                {"role": "user", "content": f"Analyze the following text and identify any recurring themes or patterns that appear multiple times.:\n\n{text}"}
            ],
            max_tokens=word_limit * 4,  # Adjust tokens based on your word limit
            temperature=0.7,
        )

        # Access the summary from the response using the new Pydantic model
        summary = response.choices[0].message.content.strip()

        # Return the summary
        return summary

    except Exception as e:
        return f"Error generating summary: {e}"

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

def basic_summary(text, max_length=150):
    """Generates a basic summary of the given text, limited to a certain number of words."""
    try:
        summary = summarizer(text, max_length=max_length, min_length=50, do_sample=False)[0]['summary_text']
        return summary
    except Exception as e:
        return f"Error summarizing text: {e}"
