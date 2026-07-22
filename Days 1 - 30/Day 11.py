import easyocr as ocr

reader = ocr.Reader(['en'])
result = reader.readtext('CV/Photos/birdpic.png')

for (bbox, text, prob) in result:
    print(text)