# Receipt OCR 

CV test task that uses Tesseract and OpenCV to extract text from receipts photos.

## Quickstart

I'd highly recommend using Docker to setup this project.

```bash
docker build -t receipt_ocr_test:latest
docker run -d -p 8080:8080 receipt_ocr_test:latest
```

To set it up on the local machine use:
```bash
pip3 install -r requirements.txt
python3 flask -m run
```

Use localhost:8080 to access Web UI. 

## Usage

Upload a photo and specify document language(eng, ger, rus, ukr, etc.).
The accuracy of the OCR detection depends on photo quality, lighting and other factors. 

TODO: Add Language model/Spellchecker to improve accuracy. Formatted data extraction is also an interesting idea. 
