import pyttsx3
import pdfplumber
import PyPDF2


file = 'Capital Markets.pdf'
pdfFileObject = open(file, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
pages = pdfReader.numPages
print(pages)
with pdfplumber.open(file) as pdf:
    for i in range(0, pages):
        page = pdf.pages[i]
        text = page.extract_text()
        print(text)
        speaker = pyttsx3.init()
        speaker.say(text)
        speaker.runAndWait()
pass
