import csv, json, zipfile
import requests, PyPDF2


zip_url = "https://disclosures-clerk.house.gov/public_disc/financial-pdfs/2021FD.ZIP"
pdf_url = "https://disclosures-clerk.house.gov/public_disc/ptr-pdfs/2021/"

r = requests.get(zip_url)
zip_name = "2021.zip"

with open(zip_name, "wb") as f:
    f.write(r.content)
    
with zipfile.ZipFile(zip_name) as z:
    z.extractall(".")

with open("2021FD.txt") as f:
    for line in csv.reader(f, delimiter="\t"):
        if line[1] == "Pelosi":
            print(line)
            date = line[7]
            doc_id = line[8]
            
            r = requests.get(f"{pdf_url}{doc_id}.pdf")
            
            with open(f"{doc_id}.pdf", "wb") as pdf_file:
                pdf_file.write(r.content)
                
                doc = fitz.open("{doc_id}.pdf")
            