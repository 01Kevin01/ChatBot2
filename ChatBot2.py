import tkinter as tk
from tkinter import ttk
import random
import wikipedia
import requests
import subprocess


# WeatherAPI API anahtarı
api_key = "WeatherAPI key gelecektir"



# Cevap veritabanı
responses = {
    "merhaba": [
         "Merhaba! Size nasıl yardımcı olabilirim?",
         "Selam! Size ne yapabileceğimi söyleyin.", 
         "Merhabalar! Size nasıl yardımcı olabilirim?"
    ],
    "kimsin": [
         "Ben bir botum.",
         "İlk uygulamadan sonra gelen uygulamayım.",
         "ChatBot2'im..." 
    ],
    "nasılsın": [
         "Ben bir botum, iyi olmam gerek!",
         "Oldukça iyi, teşekkür ederim! Peki ya siz?",
         "Ben bir botum, duygularım yok, ama teşekkür ederim!"
    ],
    "espri": [
         "Neden martılar denize dalış yapar? Balıkları şaka yollamak için!",
         "İnternetsiz yaşayamam diyen var mı? Tabii ki var, OFFline'lar var!"
    ],
    "kedi": [
        "Kediler çok sevimli yaratıklar, değil mi?",
        "Ben bir bot olsam da kedileri seviyorum!",
        "Kedilerin tatlı mırıltıları insanı rahatlatır."
    ],
    "köpek": [
        "Köpekler sadık ve sevimli dostlardır.",
        "Benim gibi bir botun köpekleri sevmesi biraz garip olabilir ama...",
        "Köpekler enerjik ve cana yakındır."
    ],
    "renkler": [
        "Renkler dünyayı güzelleştirir, favori renginiz nedir?",
        "Mavi gökyüzüne bakmak insana huzur verir.",
        "Kırmızı enerji ve tutkuyu simgeler."
    ],
    "film": [
        "Sizce en iyi film hangisi?",
        "Ben bir bot olduğum için duygularım olmasa da, bazı filmler gerçekten etkileyicidir.",
        "Bir film gecesi düzenlemek her zaman güzel bir fikirdir."
    ],
    "yemek tarifi": [
        "En sevdiğim yemek tarifi makarna: su kaynat, makarnayı at, pişir, sos ekle, afiyet olsun!",
        "Kahvaltı için güzel bir omlet yapabilirsiniz: yumurtayı çırp, tuz ekle, tavada pişir.",
        "Sağlıklı bir salata tarifi: Yeşil yaprakları doğra, sevdiğin malzemeleri ekle, zeytinyağı ve limon suyuyla karıştır."
    ],
    "şehir önerisi": [
        "Eğer tarihi yerleri görmek istiyorsanız Roma harika bir seçenek olabilir.",
        "Sanat ve kültür sevenler için Paris çok özel bir yer.",
        "Doğa ile iç içe vakit geçirmek isterseniz Yeni Zelanda harika manzaralara sahip."
    ],
    "teşekkür ederim": [
        "Rica ederim! Size yardımcı olabildiysem ne mutlu bana.",
        "Her zaman yardımcı olmaktan memnuniyet duyarım.",
        "Ne zaman isterseniz buradayım, lütfen sormaktan çekinmeyin."
    ],
    "günaydın": [
        "Günaydın! Harika bir gün geçirmenizi dilerim.",
        "Günaydın! Bugün neler yapmayı planlıyorsunuz?",
        "Günaydın! Size nasıl yardımcı olabilirim?"
    ],
    "iyi geceler": [
        "İyi geceler! Güzel bir uyku geçirmenizi dilerim.",
        "Tatlı rüyalar! Dinlendirici bir uyku geçirmeniz dileğiyle.",
        "Uyumadan önce sormak istediğiniz bir şey var mı?"
    ],
    "tebrik ederim": [
        "Tebrikler! Harika bir iş çıkardınız.",
        "Bravo! Bu gerçekten harika bir başarı.",
        "Siz gerçekten çok yeteneklisiniz, tebrik ederim!"
    ],
    "kahve": [
        "Kahve kokusu insanı hemen canlandırır, değil mi?",
        "Ben bir yapay zeka olduğum için kahveyi tadamıyorum ama insanların neden sevdiğini anlayabiliyorum.",
        "Kahve içerken en sevdiğiniz tür hangisi?"
    ],
    "kitap": [
        "Kitaplar büyülü dünyalara kapı açar.",
        "Bir kitap okumak her zaman iyi bir fikirdir, hangi türü tercih edersiniz?",
        "Okuma alışkanlığı insanın hayatını zenginleştirir."
    ],
    "tatil": [
        "Tatil planı yapmak harika bir fikir! Hangi yerleri düşünüyorsunuz?",
        "Tatilinizi nerede geçirmek istersiniz? Deniz mi, dağ mı, yoksa şehir mi?",
        "Tatil, stresten uzaklaşmak için harika bir fırsattır."
    ],



}


def get_response(message):
    message = message.lower()
    if message in responses:
        return random.choice(responses[message])
    elif "resim çizme" in message:
        open_paint()
        return "Resim çizme penceresi açıldı."
    elif "iletişim" in message:
        open_contact_window()
        return "İletişim penceresi açılıyor...|İletişim Bilgileri:\nE-posta: 01Kevin0110@proton.me\n"
    elif "hesap makinesi" in message:
        open_calculator()
        return "Hesap makinesi penceresi açılıyor..."
    else:
        try:
            wikipedia.set_lang("tr")  # Set Wikipedia language to Turkish
            wiki_summary = wikipedia.summary(message)
            return wiki_summary
        except wikipedia.exceptions.DisambiguationError as e:
            options = e.options
            return f"Çoklu anlam sorunu. Aşağıdaki seçeneklerden birini seçebilirsiniz: {', '.join(options)}"
        except wikipedia.exceptions.PageError:
            return "Üzgünüm, aradığınız konu hakkında bilgi bulunamadı."


# Bu örnekte wikipedia paketini kullanarak, belirtilen anahtar kelimenin Wikipedia açıklamasını get_response fonksiyonuna entegre edebilirsiniz.

def send_message(event=None):
    message = user_input.get()
    chat_log.insert(tk.END, "Sen: " + message + "\n")

    if message.startswith("/yardım"):
        help_message = "Kullanabileceğiniz komutlar:\n"
        help_message += "hava durumu şehir/bölge\n"
        help_message += "wikipedia (araştıracağınız kelime)\n" 
        help_message += "iletişim\n"
        help_message += "hesap makinesi\n"
        help_message += "resim çizme\n"
        help_message += "nasılsın\n"
        help_message += "merhaba\n"
        help_message += "kimsin\n"
        help_message += "espri\n"
        help_message += "kedi\n"
        help_message += "köpek\n"
        help_message += "renkler\n"
        help_message += "film\n"
        help_message += "yemek tarifi\n"
        help_message += "şehir önerisi\n"
        help_message += "teşekkür ederim\n"
        help_message += "günaydın\n"
        help_message += "iyi geceler\n"
        help_message += "tebrik ederim\n"
        help_message += "kahve\n"
        help_message += "kitap\n"
        help_message += "tatil\n"
        help_message += "/kırmızı - (Yazı rengini kırmızı yapar)\n"
        help_message += "/yeşil - (Yazı rengini yeşil yapar)\n"
        help_message += "/mavi - (Yazı rengini mavi yapar)\n"
        help_message += "/pembe - (Yazı rengini pembe yapar)\n"
        help_message += "/turuncu - (Yazı rengini turuncu yapar)\n"
        help_message += "/temizle (Sohbeti temizler)\n"
        chat_log.insert(tk.END, "Bot: " + help_message + "\n")
    elif message.startswith("hava durumu"):
        city = message.split(" ", 2)[2]  # Kullanıcının girdiği şehir/bölge
        weather_info = get_weather(city)
        chat_log.insert(tk.END, "Bot: " + weather_info + "\n")
    elif message.startswith("/temizle"):
        chat_log.delete(1.0, tk.END)
    elif message.startswith("/"):
        color_command = message.split("/")[1].strip()
        change_text_color(color_command)

    else:
        if message.lower().startswith("wikipedia "):
            # Kullanıcı Wikipedia'ya yönlendirilmek istiyor
            chat_log.insert(tk.END, "Bot: Lütfen Wikipedia üzerinden daha fazla bilgi edinin: https://tr.wikipedia.org/wiki/" + message[10:] + "\n")
        else:
            response = get_response(message)
            chat_log.insert(tk.END, "Bot: " + response + "\n")
            chat_log.see(tk.END)
    user_input.delete(0, tk.END)

def change_text_color(color_command):
    colors = {
        "kırmızı": "red",
        "yeşil": "green",
        "mavi": "blue",
        "pembe": "pink",
        "turuncu": "orange",
    }

    if color_command in colors:
        chat_log.config(foreground=colors[color_command])
    else:
        chat_log.insert(tk.END, "Bot: Geçerli bir renk seçeneği değil. Renkleri değiştirmek için /kırmızı,/pembe,/turuncu, /yeşil ve /mavi kullanabilirsiniz veya /yardım komutu ile hangi komutları yapabileceğimizi görebilirsiniz.\n")
        chat_log.see(tk.END)

def send_message_from_button():
    send_message()
# WeatherAPI'den hava durumu bilgilerini çekmek için fonksiyon
def get_weather(city):
    base_url = "http://api.weatherapi.com/v1/current.json"
    params = {
        "key": api_key,
        "q": city,
        "lang": "tr"
    }
    response = requests.get(base_url, params=params)
    data = response.json()

    if "error" in data:
        return "Hava durumu bilgileri alınamadı."

    location = data["location"]["name"]
    condition = data["current"]["condition"]["text"]
    temp_c = data["current"]["temp_c"]
    humidity = data["current"]["humidity"]
    wind_kph = data["current"]["wind_kph"]

    weather_info = f"{location} şehrinde hava durumu:\n"
    weather_info += f"Şu an {condition}\n"
    weather_info += f"Sıcaklık: {temp_c}°C\n"
    weather_info += f"Nem: %{humidity}\n"
    weather_info += f"Rüzgar Hızı: {wind_kph} km/saat"

    return weather_info


# Oluşturulacak ana ekran
root = tk.Tk()
root.title("ChatBot2")



# Sohbet logları için metin alanı
chat_log = tk.Text(root, width=60, height=30)
chat_log.pack()






# Kullanıcı giriş kutusu
user_input = tk.Entry(root, width=55)
user_input.pack()
user_input.bind("<Return>", send_message)  # Enter tuşuna basınca mesajı gönder




# Temizle düğmesi
clear_button = tk.Button(root, text="Temizle", command=lambda: chat_log.delete(1.0, tk.END))
clear_button.pack(side=tk.LEFT)
# "İletişim" penceresini açan fonksiyon
def open_contact_window():
    contact_window = tk.Toplevel(root)
    contact_window.title("İletişim")
    contact_label = tk.Label(contact_window, text="İletişim Bilgileri:\nE-posta: 01Kevin0110@proton.me\n")
    contact_label.pack()

# "İletişim" düğmesi ile open_contact_window fonksiyonunu çağırma
contact_button = tk.Button(root, text="İletişim", command=open_contact_window)
contact_button.pack(side=tk.LEFT)

# "Yardım" komutunu otomatik olarak gönderen fonksiyon
def send_help_message():
    help_command = "/yardım"
    user_input.delete(0, tk.END)  # Kullanıcı giriş kutusunu temizle
    user_input.insert(0, help_command)  # Yardım komutunu giriş kutusuna ekleyin
    send_message()  # Mesajı otomatik olarak gönder

# "Yardım" düğmesi (help_button) ile send_help_message fonksiyonunu çağırma
help_button = tk.Button(root, text="Yardım", command=send_help_message)
help_button.pack(side=tk.LEFT)




# Başlangıç mesajı
initial_message = "Bot: Merhaba! Size nasıl yardımcı olabilirim?(Uygulamaya ilk girişiniz ise /yardım komutunu yazın.)\n"
chat_log.insert(tk.END, initial_message)

def open_calculator():
    subprocess.Popen(["python", "hesap_makinesi.py"])

def open_paint():
    subprocess.Popen(["python", "çizim.py"])


# Hesap Makinesi Butonu
calculator_button = tk.Button(root, text="Hesap Makinesi Aç", command=open_calculator)
calculator_button.pack(side=tk.LEFT)


# Çizim Butonu
calculator_button = tk.Button(root, text="Resim Çizme", command=open_paint)
calculator_button.pack(side=tk.LEFT)




# Gönder düğmesi
send_button = tk.Button(root, text="Gönder", command=send_message_from_button)
send_button.pack(side=tk.LEFT)



root.mainloop()

