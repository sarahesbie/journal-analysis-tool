import tkinter as tk
from tkinter import filedialog
from text_processing import split_document, extract_keyword_sections
from summarization import summarize_sections, generate_recommendation
from utils import save_report_to_file

# Global variables to store processed data
processed_chunks = None
keyword_results = {}

# Predefined questions and their associated keywords
questions_and_keywords = {
    "What are habits I want to cultivate?": ["cultivate", "build", "start", "improve"],
    "What are habits I want to break?": ["break", "stop", "quit"],
    "What are my limiting beliefs?": ["limiting", "belief", "I can't", "I'm not"],
    "What are my fears?": ["fear", "scared", "afraid", "worried"],
    "What do I want?": ["want", "desire", "wish", "goal"],
}

def upload_file():
    global processed_chunks
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("Markdown files", "*.md")])
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            text_display.delete(1.0, tk.END)
            text_display.insert(tk.END, text)
            # Only chunk the document once, storing the result globally
            processed_chunks = split_document(text)
        return text
    return None

def question_based_summarization(question):
    global processed_chunks, keyword_results
    input_text = text_display.get(1.0, tk.END).strip()
    
    if question not in questions_and_keywords:
        result_display.delete(1.0, tk.END)
        result_display.insert(tk.END, "Invalid question selected.")
        return

    # Get the keywords associated with the selected question
    keywords = questions_and_keywords[question]
    keyword_key = ','.join(keywords)  # Unique key to store results based on the keywords

    # If the question has been analyzed before, use the stored result
    if keyword_key in keyword_results:
        final_summary, final_recommendation = keyword_results[keyword_key]
    else:
        all_summaries = []
        all_recommendations = []

        # Process each chunk, extracting sections related to the keywords
        for chunk in processed_chunks:
            sections = []
            for keyword in keywords:
                sections.extend(extract_keyword_sections(chunk, keyword))
            
            if sections:
                # Summarize the sections
                summaries = summarize_sections(sections)
                all_summaries.extend(summaries)

                # Generate recommendations based on the findings
                for summary in summaries:
                    recommendation = generate_recommendation(summary, f"What should I do about {question}?")
                    all_recommendations.append(recommendation)

        # Combine summaries and recommendations
        final_summary = ' '.join(all_summaries)
        final_recommendation = ' '.join(all_recommendations)

        # Store the result globally for future use
        keyword_results[keyword_key] = (final_summary, final_recommendation)

    # Display and save the report
    report = f"Findings for '{question}':\n\n{final_summary}\n\nRecommendations:\n\n{final_recommendation}"
    result_display.delete(1.0, tk.END)
    result_display.insert(tk.END, report)

    # Save the report with a filename based on the question
    save_report_to_file(report, f"{question.replace(' ', '_')}_report.pdf")

# Tkinter setup
root = tk.Tk()
root.title("Question-Based Summarization Tool")
root.geometry("800x600")

# Create UI elements
upload_button = tk.Button(root, text="Upload Text File", command=upload_file)
upload_button.pack(pady=10)

# Buttons for predefined questions
for question in questions_and_keywords:
    button = tk.Button(root, text=question, command=lambda q=question: question_based_summarization(q))
    button.pack(pady=5)

text_display = tk.Text(root, height=10, width=100)
text_display.pack(pady=10)

result_label = tk.Label(root, text="Findings and Recommendations:")
result_label.pack(pady=5)

result_display = tk.Text(root, height=10, width=100)
result_display.pack(pady=10)

# Start Tkinter loop
root.mainloop()
