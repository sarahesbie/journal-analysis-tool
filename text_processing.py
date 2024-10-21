from fuzzywuzzy import fuzz, process

def split_document(text, chunk_size=5000):
    """Splits a large document into smaller chunks for processing."""
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

def fuzzy_keyword_search(text, keyword, threshold=80):
    """Search for a keyword in lemmatized text, allowing for some misspellings and variations."""
    words = text.split()
    matches = process.extractBests(keyword, words, scorer=fuzz.ratio, score_cutoff=threshold)
    matched_words = [match[0] for match in matches]
    return matched_words

def extract_keyword_sections(text, keyword, context_window=2, threshold=80):
    """Extract sections of the text surrounding a fuzzy-matched keyword."""
    sentences = text.split('. ')  # Split the text into sentences
    keyword_sections = []
    
    for idx, sentence in enumerate(sentences):
        matches = fuzzy_keyword_search(sentence, keyword, threshold)
        if matches:
            # Extract a window of sentences before and after the matched keyword
            start_idx = max(0, idx - context_window)
            end_idx = min(len(sentences), idx + context_window + 1)
            section = '. '.join(sentences[start_idx:end_idx])
            keyword_sections.append(section)

    return keyword_sections
