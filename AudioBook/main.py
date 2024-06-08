from pdf_to_text import pdf_to_text
from to_voice_converter import text_to_speech

text = pdf_to_text('lord_of_d_rings.pdf')
input('ready for speech...')
voice = text_to_speech(text)
