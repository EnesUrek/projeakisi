# Çok Nesne Gerçek Zamanlı Takip Modülü (Multi-Object Real-Time Tracking)

## 📌 Modülün Amacı ve Kapsamı
Bu modül, kamera akışları üzerinden tespit edilen birden fazla hareketli nesneye anlık olarak benzersiz kimlikler (ID) atamak ve bu nesnelerin saha içerisindeki hareket yörüngelerini (trajectory) kesintisiz bir şekilde izlemek amacıyla geliştirilmiştir.

## ⚙️ Kullanılan Algoritmalar ve Teknolojiler

Geliştirme sürecinde nesne takibindeki kararlılığı artırmak ve veri kaybını önlemek için aşağıdaki yaklaşımlar entegre edilmiştir:

### 1. DeepSORT (Deep Simple Online and Realtime Tracking)
* **İşlevi:** Nesnelerin kareler (frames) arasında kimliklerini koruyarak eşleştirilmesini sağlar.
* **Uygulama:** Sadece nesnelerin fiziksel konumlarına (Bounding Box IoU) değil, aynı zamanda derin öğrenme tabanlı görsel özelliklerine (Appearance/ReID) de odaklanır. Bu sayede sahnedeki nesneler birbirinin önünden geçtiğinde veya kısa süreli oklüzyon (kapanma) durumlarında kimlik karışıklıklarının önüne geçilmiştir.

### 2. Kalman Filtresi (Kalman Filter)
* **İşlevi:** Hareketli nesnelerin hız ve yön vektörlerini baz alarak gelecekteki konumlarını matematiksel olarak tahmin eder.
* **Uygulama:** Nesne takibindeki en büyük zorluklardan biri olan **ID kaybı (ID Switch)** sorununu çözmek için sisteme entegre edildi. Kamera açısından anlık olarak çıkan veya engellerin arkasında kalan nesnelerin rotası, Kalman Filtresi sayesinde öngörülerek nesne tekrar görünür olduğunda aynı ID ile takibe devam edilmesi sağlandı.

### 3. OpenCV ve Gelişmiş Python Veri Yapıları
* **İşlevi:** Görüntü akışının işlenmesi ve anlık konum geçmişinin hafızada tutulması.
* **Uygulama:** OpenCV kullanılarak görselleştirme ve matris işlemleri optimize edildi. Her bir nesnenin (ID'nin) X, Y koordinatlarındaki hareket geçmişi, Python veri yapıları (Sözlükler ve Listeler/Deq yapısı) ile dinamik olarak depolandı. Bu sayede ekranda nesnelerin iz bıraktığı kuyruklar (tracking lines) oluşturuldu.

## 🚀 Projeye ve Sisteme Etkileri

Geliştirilen bu modülün sisteme entegre edilmesiyle birlikte elde edilen temel kazanımlar şunlardır:

1. **Kesintisiz ve Kararlı İzleme:** Kalman filtresi ve DeepSORT'un hibrit çalışması sayesinde, yoğun ve hareketli sahnelerde (örneğin hareketli araçlar, saha personelleri) yaşanan kimlik değişimleri minimuma indirildi. Sistemin takip doğruluğu artırıldı.
2. **Geçmişe Yönelik Hareket Analizi (Trajectory Analysis):** Konum verilerinin bellekte tutulması sayesinde, sahadaki nesnelerin nereden gelip nereye gittiği mantıksal olarak analiz edilebilir hale geldi. Bu durum; alan kullanımını optimize etmek, sık kullanılan rotaları belirlemek ve potansiyel trafik sıkışıklıklarını (örneğin depo koridorlarında) tespit etmek için kritik bir altlık oluşturdu.
3. **Yüksek Performanslı Gerçek Zamanlı Çalışma:** Kod mimarisi canlı kamera akışlarında gecikme (lag) yaratmayacak şekilde kurgulandı, anlık reaksiyon verebilen bir takip sistemi elde edildi.
