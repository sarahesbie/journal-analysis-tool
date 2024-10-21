import tkinter as tk
from tkinter import filedialog
from text_processing import split_document, extract_keyword_sections
from summarization import summarize_sections, generate_recommendation, basic_summary, gpt_summary, gpt_pattern_find
from utils import save_report_to_file, save_report_with_timestamp


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

def summarize_text():
    """Summarizes the entire document with a word limit."""
    input_text = text_display.get(1.0, tk.END).strip()
    if input_text:
        summary = basic_summary(input_text, max_length=150)  # Limit summary to ~150 words
        result_display.delete(1.0, tk.END)
        result_display.insert(tk.END, summary)

def save_report(action):
    """Saves the current report based on the action, either 'new' or 'append'."""
    input_text = result_display.get(1.0, tk.END).strip()
    if input_text:
        if action == 'new':
            # Save report with timestamp in a new file
            save_report_with_timestamp(input_text, "Summary_Report")
        elif action == 'append':
            # Append the report to an existing file
            save_report_with_timestamp(input_text, "project_report.txt", append=True)

def summarize_text_with_gpt():
    """Summarizes the entire document using GPT-4."""
    input_text = text_display.get(1.0, tk.END).strip()
    if input_text:
        summary = gpt_summary(input_text, word_limit=150)  # Limit summary to 150 words
        result_display.delete(1.0, tk.END)
        result_display.insert(tk.END, summary)
        
def find_themes_with_gpt():
    """Summarizes the entire document using GPT-4."""
    input_text = text_display.get(1.0, tk.END).strip()
    if input_text:
        summary = gpt_pattern_find(input_text, word_limit=200)  # Limit summary to 150 words
        result_display.delete(1.0, tk.END)
        result_display.insert(tk.END, summary)

import tkinter as tk

# Tkinter setup
root = tk.Tk()
root.title("Journal Analysis Tool")
root.geometry("800x600")

# Pastel color palette (ice cream-like colors)
colors = ["#FFB3BA", "#FFDFBA", "#FFFFBA", "#BAFFC9", "#BAE1FF", "#FFCCFF", "#D4BAFF"]

# Create a frame to hold the buttons inline
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Upload button
upload_button = tk.Button(button_frame, text="Upload Text File", command=upload_file, bg=colors[0])
upload_button.pack(side="left", padx=5)

# Button for summarizing the entire text
summarize_button = tk.Button(button_frame, text="Summarize Text (150 words)", command=summarize_text, bg=colors[1])
summarize_button.pack(side="left", padx=5)

# Button for summarizing the entire text using GPT
summarize_gpt_button = tk.Button(button_frame, text="Summarize Text (GPT, 150 words)", command=summarize_text_with_gpt, bg=colors[2])
summarize_gpt_button.pack(side="left", padx=5)

# Button for summarizing the entire text using GPT
find_patterns_gpt_button = tk.Button(button_frame, text="Find Patterns (GPT, 200 words)", command=find_themes_with_gpt, bg=colors[1])
find_patterns_gpt_button.pack(side="left", padx=5)

# Predefined questions buttons
for i, question in enumerate(questions_and_keywords):
    button = tk.Button(button_frame, text=question, command=lambda q=question: question_based_summarization(q), bg=colors[(i + 3) % len(colors)])
    button.pack(side="left", padx=5)

# Create another frame for save buttons (also inline)
save_frame = tk.Frame(root)
save_frame.pack(pady=10)

# Button for saving the report to a new file
save_new_button = tk.Button(save_frame, text="Save Report to New File", command=lambda: save_report('new'), bg=colors[4])
save_new_button.pack(side="left", padx=5)

# Button for appending the report to an existing file
append_button = tk.Button(save_frame, text="Append Report to Existing File", command=lambda: save_report('append'), bg=colors[5])
append_button.pack(side="left", padx=5)

# Text display and result display
text_display = tk.Text(root, height=10, width=100)
text_display.pack(pady=10)

result_label = tk.Label(root, text="Findings and Recommendations:")
result_label.pack(pady=5)

result_display = tk.Text(root, height=10, width=100)
result_display.pack(pady=10)

# Start Tkinter loop
root.mainloop()
