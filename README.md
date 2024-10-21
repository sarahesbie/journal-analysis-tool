# Journal Analysis Tool

I've always found immense value in journaling—maybe you do too? While I could spend hours revisiting my notebooks, I wanted a more efficient way to distill the insights and key takeaways from my entries to help improve my life. This tool was born out of that need, to extract the "gold" from my journals and turn reflection into actionable insights. This Journal Analysis Tool is a Python application designed to help you (me) analyse large text documents, such as journals, by summarising and generating insights based on predefined questions. This tool uses the Hugging Face `transformers` library for summarisation and question answering, and outputs findings and recommendations in an easily accessible format, including PDF reports.

## Features

- Upload Documents: Load large text files (e.g., journal entries) for analysis.
- Predefined Questions: analyse text based on predefined questions:
  - What are habits I want to cultivate?
  - What are habits I want to break?
  - What are my limiting beliefs?
  - What are my fears?
  - What do I want?
- Summarisation & Recommendations: Generate summaries and personalized recommendations for each question.
- Word Cloud Generation: visualise important words using word clouds.
- Save PDF Reports: Save findings and recommendations as PDF files, customized by question.

## Getting Started

Follow these steps to set up the Journal Analysis Tool on your local machine.

### Prerequisites

Ensure you have the following installed on your system:

- Python 3.x
- pip (Python package manager)

### Installation

1. Clone the repository:

```
git clone https://github.com/your-username/journal-analysis-tool.git
cd journal-analysis-tool
```

2. Set up a virtual environment (optional but recommended):

```
python -m venv venv
source venv/bin/activate # On Linux/macOS
venv\Scripts\activate # On Windows
```

3. Install the required dependencies:

```
pip install -r requirements.txt
```

## Running the Application

Once the dependencies are installed, run the application with:

```
python main.py
```

This will launch a graphical user interface (GUI) that allows you to upload a document and analyse it using the predefined questions.

## Usage

1. Upload a Document
   - Click the "Upload Text File" button to upload a .txt or .md file into the tool. The document will be chunked into smaller sections for efficient analysis.
2. Analyse Predefined Questions
   - Select one of the predefined questions by clicking the buttons.
   - The tool will extract relevant sections from the document, summarise the content, and generate recommendations based on the question.
3. Generate and Save Reports
   - After analysis, a summary and recommendations will be displayed in the GUI. You can save the findings as a PDF report for each question. The PDF is named according to the selected question
4. Create Word Clouds
   - Optionally, you can generate a word cloud to visualise the most frequent words in the document.

## Project Structure

```
   journal-analysis-tool/
   │
   ├── main.py # Main application with Tkinter GUI
   ├── text_processing.py # Functions for text chunking and keyword extraction
   ├── summarisation.py # summarisation and recommendation functions using transformers
   ├── utils.py # Utility functions (e.g., save to PDF)
   ├── requirements.txt # Project dependencies
   └── README.md # Project documentation (this file)
```

## Files and Functionality

- main.py: The main program that launches the GUI, handles file uploads, and triggers analysis.
- text_processing.py: Manages splitting the document into manageable chunks and keyword extraction.
- summarisation.py: Handles text summarisation and recommendation generation using the Hugging Face transformers library.
- utils.py: Includes utility functions like saving reports to PDF files.
- requirements.txt: Lists the Python libraries required for the project.

## Dependencies

The project requires the following Python libraries:

- transformers
- torch
- nltk
- matplotlib
- fpdf
- fuzzywuzzy

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

Contributing
Contributions are welcome! If you have any ideas or bug reports, feel free to open an issue or submit a pull request. When contributing, please follow these steps:

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Push your branch and open a pull request.

## Acknowledgments

- Hugging Face: For providing the NLP models used in summarisation and question answering.
- FuzzyWuzzy: For enabling flexible keyword matching in text analysis.
- FPDF: For generating PDF reports.

## Author

Sarah Brown - [@sarahesbie](https://github.com/sarahesbie)

<!-- Notes to add
- you need to add your openai key to environment variables if you want to use the gpt functionality -->

<!-- heres' what I did

- transcribed so many of my journals
- chunked it and summarised it into 150 summaries with gpt
- I got it down from 35,000 words to 12,000 words (this cost about $2.50) -->
