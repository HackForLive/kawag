import configparser
from pathlib import Path
from pypdf import PdfReader
from io import BytesIO


from requests_html import HTMLSession

config = configparser.ConfigParser()
config.read(Path(__file__).parent.parent.joinpath('config.ini'))

session = HTMLSession()

r = session.get(config['DEFAULT']['BASE_URL'])

prefix = 'https://www.mujkaktus.cz/api/download'
print(r.html.links)

pdf_links = [l for l in r.html.links if l.startswith(prefix)]
pdf_link = pdf_links[0]
rr = session.get(pdf_link).content
pdf_data = BytesIO(rr)
read_pdf = PdfReader(pdf_data)
for page in read_pdf.pages:
    text = (page.extract_text())
    is_to_p = False
    for l in text.split('\n'):
        # print(l)
        if l.startswith('4.'):
            is_to_p = True
        if l.startswith('5.'):
            is_to_p = False
        if is_to_p:
            print(l)




# box = r.html.find('.box-bubble', first=True).find('p', first=True)
# print(box.text)
