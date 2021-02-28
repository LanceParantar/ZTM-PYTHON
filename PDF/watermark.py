import PyPDF2

with open('super.pdf', 'rb') as file_pdf:
    pdf = PyPDF2.PdfFileReader(file_pdf)

    with open('./SamplePDF/wtr.pdf', 'rb') as file_watermark:
        file_watermark = PyPDF2.PdfFileReader(file_watermark)
        pdf_writer = PyPDF2.PdfFileWriter()
        for i in range(pdf.getNumPages()):
            page = pdf.getPage(i)
            page.mergePage(file_watermark.getPage(0))
            pdf_writer.addPage(page)

        with open('./WaterMarkPDF.pdf', 'wb') as file_output_pdf:
            pdf_writer.write(file_output_pdf)