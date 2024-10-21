from fpdf import FPDF

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
