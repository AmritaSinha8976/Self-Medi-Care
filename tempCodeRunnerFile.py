
        pdf.cell(200, 10, txt=f"- {wrk}", ln=True)
    pdf.ln(10)

    # Save the PDF to a file
    output_path = "static/prescription_report.pdf"
    pdf.output(output_path)

    return output_path



# about view funtion and path
