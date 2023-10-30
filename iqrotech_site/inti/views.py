# from urllib.request import Request
from django.shortcuts import render
# from .diacritic.hmm import HMM
# import difflib

# Create your views here.
def index(request):
    return render(request, 'inti/inti.html')

# def your_view(request):
#     if request.method == "POST":
#         arabic_text = request.POST["arabic_text"]  # Gantilah ini dengan nama field dari input pengguna
#         hmm = HMM()
#         diacritized_text = hmm.diacritized_word(arabic_text)

# def index(request):
#     error = None
#     result = None
#     arabic_text = None
#     speech_to_text = None

#     if request.method == 'POST':
#         speech_to_text = request.POST.get('speech_to_text')

#         quran_text_response = Request.get('http://api.alquran.cloud/v1/juz/30/quran-uthmani')
#         quran_text_data = quran_text_response.json()
#         quran_text = quran_text_data['data']['text']

#         # Membandingkan dua string menggunakan SequenceMatcher
#         matcher = difflib.SequenceMatcher(None, speech_to_text, quran_text)
#         similarity = matcher.ratio()

#         if similarity == 1.0:
#             result = "Teks yang Anda ucapkan cocok dengan teks Al-Qur'an."
#         else:
#             result = "Teks yang Anda ucapkan tidak cocok dengan teks Al-Qur'an. Kemiripan: {}%".format(similarity * 100)

#         arabic_text = quran_text

#     return render(request, 'inti/inti.html', {'error': error, 'result': result, 'arabic_text': arabic_text, 'speech_to_text': speech_to_text})