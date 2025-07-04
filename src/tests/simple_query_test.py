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
    print(page.extract_text())

# box = r.html.find('.box-bubble', first=True).find('p', first=True)
# print(box.text)
