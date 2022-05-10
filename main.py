from gtts import gTTS
import pdfplumber
from pathlib import Path
from art import tprint

def pdf_to_mp3(file_path, language='en'):
   
    # Checking if the file exists and has a '.pdf' extension 
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf' and language == 'ru' or language == 'en':
        print(f'[+] Original file name: {Path(file_path).name}')
        print('[+] Processing...')

        # Open the file for reading in binary mode. Extracting text from each page
        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]
        
        # Connecting text
        text = ''.join(pages)
        # Removing line breaks
        text = text.replace('\n', '')

        # Formation of the audio file
        audio = gTTS(text=text, lang=language, slow=False)
        # Getting the name of the source file
        file_name = Path(file_path).stem
        # Saving the audio file
        audio.save(f'mp3/{file_name}.mp3')

        return f'[+] {file_name}.mp3 saved successfully'
    
    else:
        return 'File not exists, check the file path'

def main():
    tprint('PDF>>TO>>MP3', font='bulbhead')
    
    file_path = input("Enter file's path: ")
    language = input("Choose language 'en' or 'ru': ")

    print(pdf_to_mp3(file_path=file_path, language=language))

if __name__ == '__main__':
    main()