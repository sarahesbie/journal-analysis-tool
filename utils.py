from fpdf import FPDF
from datetime import datetime

def save_report_to_file(report, output_filename="report.pdf"):
    """Saves the generated report to a PDF file with a specific filename."""
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Title
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="Analysis Report", ln=True, align='C')

    # Body Content
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, report)

    # Output the PDF
    pdf.output(output_filename)
    print(f"PDF report saved as {output_filename}")

def save_report_with_timestamp(report, file_name_prefix="Report", append=False):
    """Saves or appends a report with a timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_name = f"{file_name_prefix}_{timestamp}.txt"

    if append:
        # Append to the existing file
        with open(file_name_prefix, 'a') as file:
            file.write(f"\n\n--- Report Entry: {timestamp} ---\n\n")
            file.write(report)
            print(f"Appended report to {file_name_prefix}")
    else:
        # Save as a new file with a timestamp
        with open(file_name, 'w') as file:
            file.write(report)
            print(f"Saved report to {file_name}")
