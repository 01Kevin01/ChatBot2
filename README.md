
![ChatBot2](https://github.com/01Kevin01/ChatBot2/assets/131346373/5b2f444c-cb22-4f46-8e26-7cb4c484e9a9)
![hesap_makinesi](https://github.com/01Kevin01/ChatBot2/assets/131346373/a1d2a9de-3580-4016-a76c-51fe5a1beec9)
![çizim](https://github.com/01Kevin01/ChatBot2/assets/131346373/15cc14f3-21fa-4b9c-8838-3c198782bb4d)

# ChatBot2
ChatBot2
Bu kod, ChatGPT desteğine sahip farklı bir proje için yardım aldı
This code got help for a different project with ChatGPT support
https://github.com/01Kevin01/Basic-Web-Tools/blob/main/README.md#chatbot2
--------------------------------------------------------------------------
TÜRKÇE
# ChatBot2.py

Bu kod, kullanıcıların bir Tkinter arayüzü üzerinden bir sohbet botuyla etkileşime girmesini sağlayan bir Python programını oluşturuyor. Kullanıcılar metin girişi yapabilir, çeşitli komutları çalıştırabilir ve botun cevaplarını görüntüleyebilirler. Aynı zamanda hava durumu bilgisini çekmek, Wikipedia aramaları yapmak, iletişim bilgilerini göstermek gibi işlevleri de içerir.

Bu programın çalışması için aşağıdaki kütüphanelere ihtiyaç vardır:
- tkinter: Grafik arayüz bileşenleri için kullanılır.
- wikipedia: Wikipedia'dan içerik çekmek ve arama yapmak için kullanılır.
- requests: HTTP istekleri göndermek için kullanılır.
- subprocess: Alt işlemleri başlatmak için kullanılır.

Kodu adım adım açıklamak gerekirse:

1. Kullanıcı girdi ve çıktısını göstermek için bir Tkinter arayüzü oluşturulur.
2. Kullanıcı girdi alanı ve çıktı alanı (sohbet logları) yerleştirilir.
3. Kullanıcı mesajlarını göndermek için bir "Gönder" düğmesi eklenir. Ayrıca yardım, iletişim, hesap makinesi gibi özel düğmeler de eklenir.
4. Kullanıcının girdi yapabilmesi için bir girdi alanı eklenir ve "Enter" tuşuna basılınca mesaj gönderilir.
5. Girdi alınan mesaj, belirli komutlara göre işlenir. Eğer özel bir komut değilse, cevap almak için `get_response` fonksiyonu kullanılır.
6. Hava durumu bilgisini çekmek için WeatherAPI kullanılır. (API anahtarı yerine "WeatherAPI" yazılmış, gerçek bir anahtar kullanılmalıdır.)
7. Renk değiştirme komutları ile sohbet metni rengi değiştirilebilir.
8. `wikipedia` komutu ile Wikipedia'da arama yapılır ve sonuçları kullanıcıya gösterir.
9. Kullanıcıya yardım mesajları ve diğer komutlar hakkında bilgi verilir.
10. "İletişim", "Hesap Makinesi Aç", "Resim Çizme" gibi özel komutlar işlenir.
11. Ana pencere başlatılır ve kullanıcılar botla etkileşime geçebilir.

Bu kodu çalıştırmak için gerekli olan Python kütüphanelerini yüklemeniz gerekebilir. Bunun yanı sıra WeatherAPI için bir anahtara ihtiyaç duyulduğunu unutmayın. Kodu çalıştırmadan önce açıklama satırlarını ve API anahtarını düzenleyerek gereksinimleri yerine getirin.

Kodun açıklamaları doğrultusunda yukarıda verilen görevleri gerçekleştiren bir sohbet botu arayüzü oluşturmuş olacaksınız.
--------------------------------------------------------------------------
# çizim.py

Bu kod, basit bir çizim uygulamasının gelişmiş versiyonunu oluşturuyor. Bu uygulama kullanıcının çizim yapabilmesi için farklı araçlar ve seçenekler sunuyor. Çizimlerin yapılacağı bir tuval (canvas) ve bu tuval üzerinde çizim araçlarını seçmek için butonlar bulunuyor. Ayrıca renk seçimi, çizgi kalınlığı ayarı, çizimlerin kaydedilmesi ve yüklenebilmesi gibi özellikleri de içeriyor.

Bu kodun işleyişi ve açıklamaları şu şekildedir:

1. Bir Tkinter penceresi oluşturulur ve pencere başlığı "Gelişmiş Çizim Uygulaması" olarak ayarlanır.

2. Bir tuval (canvas) oluşturulur ve pencerenin alt kısmına yerleştirilir. Bu tuval, çizimlerin yapıldığı alanı temsil eder.

3. Bazı değişkenler başlatılır: çizgi rengi, çizgi kalınlığı, çizim yapılıp yapılmadığı kontrolü, son x ve y koordinatları, otomatik boyutlandırma, yüklü resim yolu, yüklü resim nesnesi ve yakınlaştırma faktörü gibi.

4. Klavye ve fare etkileşimlerini dinlemek üzere bind fonksiyonu kullanılır.

5. Butonlar ve araçlar oluşturulur. Bu araçlar "pen", "line", "rectangle", "oval", "square", "triangle" ve "circle" gibi çizim araçlarıdır. Ayrıca renk seçimi ve temizleme işlemleri için butonlar da eklenir.

6. `zoom`, `zoom_in` ve `zoom_out` fonksiyonlarıyla yakınlaştırma ve uzaklaştırma işlemleri yapılır.

7. Kullanıcının seçtiği çizim aracı, `select_tool` fonksiyonu ile seçilir.

8. Fare tıklama, sürükleme ve bırakma hareketlerine göre çizim işlemi gerçekleştirilir. Seçilen çizim aracına göre farklı şekiller çizilir.

9. Renk seçimi, çizgi kalınlığı ayarı, çizim temizleme, kaydetme ve yükleme işlemleri için fonksiyonlar bulunur.

10. Oluşturulan Tkinter penceresi çalıştırılır.

Bu kodun çalışması için aşağıdaki kütüphanelere ihtiyaç vardır:
- tkinter: Grafik arayüz bileşenleri için kullanılır.
- PIL (Pillow): Resim işleme işlevleri için kullanılır.

Kodu çalıştırmadan önce Pillow kütüphanesini yüklemeniz gerekebilir. Bu kodu çalıştırdığınızda gelişmiş bir çizim uygulamasının arayüzünü göreceksiniz. Araçları kullanarak çizimler yapabilir, renk ve kalınlık seçimleri yapabilir, çizimleri kaydedebilir veya yükleyebilirsiniz.

--------------------------------------------------------------------------
# hesap_makinesi.py

Bu kod, basit bir üst düzey hesap makinesi uygulamasını oluşturuyor. Bu hesap makinesi, kullanıcının matematiksel işlemler yapabilmesi için bir arayüz sunuyor. Kullanıcı sayıları, matematiksel operatörleri ve hesaplama sonuçlarını görüntülemek için bir girdi alanı, hesaplama butonları ve geçmiş işlemleri göstermek için bir metin alanı içerir.

Bu kodun işleyişi ve açıklamaları şu şekildedir:

1. Bir Tkinter penceresi oluşturulur ve pencere başlığı "Üst Düzey Hesap Makinesi" olarak ayarlanır.

2. Bir girdi alanı (Entry) oluşturulur. Bu alan kullanıcının sayıları, işleçleri ve sonuçları girebileceği alanı temsil eder. Girdi alanı için font ve görünüm ayarları yapılır.

3. Hesap makinesi tuşları, bir liste içinde tutulan bilgilerle oluşturulur. Her bir tuşun metni, konumu (satır ve sütun) ve tıklama işlevi (command) belirlenir. Bu tuşlar sayılar, işleçler, nokta ve eşittir işlemini gerçekleştirmek için kullanılır.

4. Temizle (C) butonu oluşturulur ve bu buton, girdi alanını temizlemek için kullanılır.

5. Hesapla (=) butonu oluşturulur ve bu buton, girilen ifadeyi değerlendirip sonucunu girdi alanına yerleştirir. Aynı zamanda hesaplama geçmişini metin alanına ekler.

6. Geçmiş işlemler için bir metin alanı oluşturulur. Bu alanda kullanıcının yaptığı hesaplamaların geçmişi görüntülenir.

7. Geçmişi temizle butonu oluşturulur ve bu buton, geçmiş işlemleri temizlemek için kullanılır.

8. Tuşların ve metin alanının görünümü (row ve column konumları) ayarlanır.

9. Tkinter penceresi başlatılır ve uygulama çalıştırılır.

Bu kodun çalışması için herhangi bir ekstra kütüphane gerekmese de, Tkinter kütüphanesinin Python'a dahil olarak gelmesi gerekmektedir. Bu kodu çalıştırdığınızda, basit bir hesap makinesi arayüzünü göreceksiniz. Sayıları ve işleçleri girdi alanına girerek hesaplamalar yapabilir, hesaplamaların sonuçlarını görüntüleyebilir ve geçmiş hesaplamaları takip edebilirsiniz.
--------------------------------------------------------------------------
!!UYARI!! EĞİTİM İÇİN YAPILDI
--------------------------------------------------------------------------
🇹🇷"Beni görmek demek mutlaka yüzümü görmek demek değildir. Benim fikirlerimi, benim duygularımı anlıyorsanız ve hissediyorsanız bu yeterlidir."🇹🇷 -Mustafa Kemal Atatürk

00110000 00110001 01001011 01100101 01110110 01101001 01101110 00110000 00110001


Yazdığım kodları isteyen geliştirebilir ve bana danışabilir.Kod yorumlarını ve dosya isimlerini bilerek türkçe yaptım fakat başka dillerde eklenebilir...

--------------------------------------------------------------------------
English
# ChatBot2.py

This code creates a Python program that allows users to interact with a chatbot via a Tkinter interface. Users can enter text, run various commands, and view the bot's responses. It also includes functions such as pulling weather information, doing Wikipedia searches, displaying contact information.

The following libraries are needed for this program to work:
- tkinter: Used for graphical interface components.
- wikipedia: Used to pull content from Wikipedia and search.
- requests: Used to send HTTP requests.
- subprocess: Used to start subprocesses.

To explain the code step by step:

1. A Tkinter interface is created to display user input and output.
2. User input field and output field (chat logs) are placed.
3. A "Send" button is added to send user messages. Special buttons like help, contact, calculator are also added.
4. An input field is added for the user to enter and a message is sent when the "Enter" key is pressed.
5. The input message is processed according to certain commands. If it is not a special command, the `get_response` function is used to get a response.
6. WeatherAPI is used to retrieve weather information. (A real key should be used, with "WeatherAPI" written instead of the API key.)
7. Chat text color can be changed with color changing commands.
8. With the `wikipedia` command, Wikipedia is searched and the results are displayed to the user.
9. The user is informed about help messages and other commands.
10. Special commands such as "Communication", "Open Calculator", "Picture Drawing" are processed.
11. The main window launches and users can interact with the bot.

You may need to install the Python libraries required to run this code. Also note that a key is needed for WeatherAPI. Fulfill the requirements by editing the comment lines and API key before running the code.

In line with the explanations of the code, you will have created a chatbot interface that performs the tasks given above.

--------------------------------------------------------------------------
# çizim.py

This code creates an advanced version of a simple drawing application. This application offers different tools and options for the user to draw. There is a canvas (canvas) on which drawings will be made and buttons to select drawing tools on this canvas. It also includes features such as color selection, line thickness adjustment, saving and loading of drawings.

The operation and explanations of this code are as follows:

1. A Tkinter window is created and the window title is set to "Advanced Drawing Application".

2. A canvas is created and placed at the bottom of the window. This canvas represents the area where the drawings are made.

3. Some variables are initialized: line color, line thickness, check for drawing, final x and y coordinates, auto-sizing, loaded image path, loaded image object, and zoom factor.

4. The bind function is used to listen for keyboard and mouse interactions.

5. Buttons and tools are created. These tools are drawing tools such as "pen", "line", "rectangle", "oval", "square", "triangle" and "circle". In addition, buttons are added for color selection and cleaning operations.

6. Zoom in and out with `zoom`, `zoom_in` and `zoom_out` functions.

7. The drawing tool selected by the user is selected with the `select_tool` function.

8. Drawing is performed according to mouse click, drag and drop movements. Different shapes are drawn according to the selected drawing tool.

9. There are functions for color selection, line thickness adjustment, drawing clearing, saving and loading.

10. The created Tkinter window is run.

The following libraries are needed for this code to work:
- tkinter: Used for graphical interface components.
- PIL (Pillow): Used for image processing functions.

You may need to install the Pillow library before running the code. When you run this code, you will see the interface of an advanced drawing application. Using the tools you can make drawings, make color and thickness selections, and save or load drawings.
--------------------------------------------------------------------------
# hesap_makinesi.py

This code creates a simple high-level calculator. This calculator offers something for users to do their trading. Usergroups contain an input field to display stored operators and calculation results, calculation buttons, and a text field to use past operations.

The validity and explanations of this code are as follows:

1. Creates a Tkinter window and the window title is set to "Top Level Calculator".

2. Create an input field (Login). This field represents the field where users can enter operators and results they use. Font and appearance settings are made for the input field.

3. Calculator instructions are created with data information in a list. The meaning, position (row and column) and click function (command) of each key are determined. These keys are used to use numbers, operators, point and variable sizes.

4. Create the Clean (C) button and this button is used to go in and clear it.

5. Creates the Calculate (=) button and evaluates the entered expression and places it in the region where it enters. It also adds calculation history text field.

6. Create a text field for past transactions. Understanding the history of calculations made by users in this area.

7. Creating a clear history button and this button is used to clear past transactions.

8. Keys and text layout appearance (row and column positions) are set.

9. The Tkinter window is launched and the application is started.

Although this code does not require any extra libraries to run, the Tkinter library should be included with Python. When you run this code, it publishes a simple calculator. By entering numbers and operators into the field, he can perform calculations, view the results of calculations and follow past calculations.
--------------------------------------------------------------------------
!!WARNING!! MADE FOR EDUCATION
--------------------------------------------------------------------------
🇹🇷"Seeing me doesn't necessarily mean seeing my face. If you understand and feel my ideas and my feelings, that's enough." -Mustafa Kemal Atatürk

00110000 00110001 01001011 01100101 01110110 01101001 01101110 00110000 00110001

Anyone who wants to develop the codes I wrote and consult me. I made the code comments and filenames in Turkish knowingly, but they can be added in other languages.
--------------------------------------------------------------------------

