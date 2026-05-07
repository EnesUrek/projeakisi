📜 ARAŞTIRMA RAPORU: Nesne Tanıma ve Görüntü İşleme Algoritmaları Analizi

     Proje Adı: Nesne Tanıma Tabanlı Akıllı Depo Yönetim Sistemi
   
     Hazırlayan: Şevval Ekmen
  
     Konu: Algoritma Seçimi, Performans Kriterleri ve Uygulama Stratejileri

1. GİRİŞ
Bu rapor, akıllı depo yönetim sisteminde ürünlerin otomatik tespiti, sınıflandırılması ve envanter takibi için kullanılacak en uygun görüntü işleme ve derin öğrenme tekniklerini belirlemek amacıyla hazırlanmıştır. Depo ortamları; değişken ışık koşulları, üst üste binmiş nesneler ve yüksek işlem hızı gereksinimi gibi zorluklar barındırmaktadır.


2. GÖRÜNTÜ İŞLEME TEKNİKLERİ (OpenCV Katmanı)
Nesne tanıma modeline veri gönderilmeden önce, görüntünün kalitesini artırmak ve işlem yükünü azaltmak için aşağıdaki OpenCV yöntemleri uygulanacaktır:

-Gürültü Filtreleme (Noise Reduction): Depo kameralarından gelen düşük ışıklı görüntülerdeki "kumlanmayı" gidermek için Gaussian Blur veya Median Filter kullanılacaktır.

-ROI (Region of Interest - İlgi Alanı): Kameranın gördüğü her yeri değil, sadece rafların veya konveyör bandının olduğu alanı işlemek için görüntü maskeleme yapılacaktır. Bu, CPU kullanımını %30-40 oranında azaltır.

-Renk Uzayı Dönüşümü: Nesne ayrıştırmada ışık değişimlerinden daha az etkilenmek için RGB yerine HSV veya LAB renk uzayları kullanılacaktır.


3. DERİN ÖĞRENME MODELLERİ VE KARŞILAŞTIRMALI ANALİZ
Projenin temelini oluşturacak nesne tanıma mimarileri için üç ana aday belirlenmiştir:

 -A. YOLO (You Only Look Once) - v8 veya v10
Mimari: Tek aşamalı (Single-stage) dedektör.
Avantajlar: İnanılmaz hızlıdır (Real-time). Küçük modelleri (YOLOv8n) mobil cihazlarda bile 50+ FPS verebilir.
Dezavantajlar: Nesneler birbirine çok yakınsa bazen ayırt etmekte zorlanabilir.
Karar: Depodaki anlık stok hareketlerini izlemek için birinci öncelikli adaydır.

 -B. SSD (Single Shot Multibox Detector)
Mimari: Farklı ölçeklerdeki özellik haritalarını kullanan tek aşamalı dedektör.
Avantajlar: YOLO'ya göre daha düşük donanım kaynağı tüketir (TensorFlow Lite ile optimize edildiğinde).
Dezavantajlar: Doğruluk oranı (mAP), YOLO'nun son sürümlerinin gerisindedir.
Karar: Eğer sistem çok eski bir bilgisayarda veya Raspberry Pi'de çalışacaksa yedek plan olarak tutulmalıdır.

 -C. Faster R-CNN
Mimari: İki aşamalı (Two-stage) dedektör (Region Proposal Network kullanır).
Avantajlar: Çok yüksek doğruluk ve küçük nesneleri tanıma kabiliyeti.
Dezavantajlar: Çok yavaştır (Genellikle 5-15 FPS). GPU gereksinimi yüksektir.
Karar: Hızın önemli olmadığı, sadece periyodik yüksek çözünürlüklü raf sayımları için uygundur.


4. PERFORMANS METRİKLERİ VE SEÇİM KRİTERLERİ
 Raporun can alıcı noktası olan seçim kriterlerimizi şu üç parametreye dayandırıyoruz:

 -Doğruluk (mAP - Mean Average Precision): Modelin yanlış ürünü tanıma olasılığı %2'nin altında olmalıdır.

 -Hız (Inference Time): Depo bandındaki bir ürünün kaçırılmaması için gecikme (latency) 50ms'nin altında kalmalıdır.

 -Ölçeklenebilirlik: Sistemin aynı anda 4-8 farklı kameradan gelen akışı işleyebilmesi için modelin "hafif" (lightweight) olması gerekir.

5. SONUÇ VE ÖNERİLER
Yapılan araştırmalar sonucunda, Python dili üzerinde PyTorch kütüphanesi kullanılarak YOLOv8 mimarisinin uygulanması kararlaştırılmıştır.

İzlenecek Adımlar:
Depo ürünlerine ait özel bir veri seti (dataset) toplanacak veya hazır Open Images veri seti kullanılacaktır.

Veriler LabelImg veya Roboflow ile etiketlenecektir.

Model, transfer öğrenme (Transfer Learning) yöntemiyle eğitilerek eğitim süresi kısaltılacaktır.

Elde edilen sonuçlar bir REST API (Flask veya FastAPI) üzerinden envanter yönetim yazılımına aktarılacaktır.
