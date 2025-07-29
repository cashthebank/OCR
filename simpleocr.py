import easyocr as ocr  #OCR

reader = ocr.Reader(['en'], model_storage_directory='.', gpu=True)

result = reader.readtext("harry.jpeg")

for text in result:
    print(text[1])