from pypdf import PdfWriter

merger=PdfWriter()
# reader=PdfReader("pdfname.pdf")
# print(len(reader.pages))

for pdf in ["pdf1 .pdf","pdf2.pdf"]:
    merger.append(pdf)

merger.write("merged-df.pdf")
merger.close()