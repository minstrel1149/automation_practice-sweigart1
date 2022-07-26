import PyPDF2
import os
from pathlib import Path

p1 = Path.cwd() / 'attachments'
p2 = Path.cwd() / 'result_attachments'

# os.listdir() 함수를 이용해 pdf 형식의 filename 수집 -> list comprehension 활용
# os.listdir() 대신 Path 모듈의 glob() 메서드도 활용 가능할듯. 그런 경우에는 아래 open시 경로 지정 불필요
pdfFiles = [filename for filename in os.listdir(p1) if filename.endswith('.pdf')]
pdfFiles.sort()

pdfWriter = PyPDF2.PdfFileWriter()

for filename in pdfFiles:
    # 이진 형식으로 열어야 -> mode='rb'
    pdfFileObj = open(p1 / filename, mode='rb')
    # 암호화가 되어있을 경우를 대비하여 예외처리 진행
    try:
        # PyPDF2.PdfFileReader() 함수는 꼭 파일이 괄호 안에 들어가야
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        for pageNum in range(1, pdfReader.numPages):
            pageObj = pdfReader.getPage(pageNum)
            pdfWriter.addPage(pageObj)
    except:
        print(f'{filename} is encrypted')

outputFileObj = open(p2 / 'allPdfCombined.pdf', mode='wb')
pdfWriter.write(outputFileObj)

outputFileObj.close()