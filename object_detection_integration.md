 Nesne Tanıma Modülü Entegrasyon Akışı Tasarımı

 1. Amaç

Bu dokümanın amacı, depo içerisindeki kameralardan alınan görüntülerin nesne tanıma modülüne aktarılması, işlenmesi ve elde edilen sonuçların veritabanına kaydedilmesi sürecini tanımlamaktır. Sistem gerçek zamanlı çalışacak şekilde tasarlanmıştır.



 2. Genel Sistem Akışı

Sistemin çalışma adımları aşağıdaki gibidir:

1. Kamera görüntüyü yakalar.
2. Görüntü ön işleme modülüne gönderilir.
3. Ön işleme sonucunda görüntü iyileştirilir.
4. Görüntü nesne tanıma modeline aktarılır.
5. Model ürünleri tespit eder.
6. Sonuçlar ayrıştırılır.
7. Envanter veritabanı güncellenir.
8. Kullanıcı arayüzüne güncel bilgiler gönderilir.

Veri akışı:

Kamera → Ön İşleme → Nesne Tanıma → Sonuç Ayrıştırma → Veritabanı → Kullanıcı Arayüzü



 3. Görüntü Formatları

Sistem aşağıdaki görüntü formatlarını desteklemektedir:

 JPEG

Avantajları:

 Düşük dosya boyutu
 Hızlı aktarım

Dezavantajları:

 Kayıplı sıkıştırma

 PNG

Avantajları:

 Kayıpsız sıkıştırma
 Daha yüksek kalite

Dezavantajları:

 Daha büyük dosya boyutu

Gerçek zamanlı sistemlerde performans avantajı nedeniyle JPEG tercih edilmektedir.



 4. Görüntü Çözünürlüğü

Desteklenen çözünürlükler:

 640x480
 1280x720 (HD)
 1920x1080 (Full HD)

Önerilen çözünürlük:

1280x720

Bu çözünürlük hem yeterli doğruluk hem de kabul edilebilir işlem süresi sunmaktadır.



 5. Görüntü Ön İşleme

Nesne tanıma doğruluğunu artırmak amacıyla aşağıdaki işlemler uygulanacaktır:

 Gürültü Giderme

Gaussian Blur uygulanır.

 Kontrast İyileştirme

CLAHE yöntemi kullanılır.

 Parlaklık Normalizasyonu

Farklı ışık koşullarından kaynaklanan etkileri azaltmak için uygulanır.



 6. Model Yükleme Süreci

Sistem TensorFlow veya PyTorch tabanlı modelleri desteklemektedir.

 PyTorch

Model sistem başlangıcında belleğe yüklenir.

Örnek işlem:

1. Model dosyası okunur.
2. GPU varsa CUDA etkinleştirilir.
3. Model değerlendirme moduna alınır.

Avantajları:

 Hızlı çıkarım
 GPU desteği
 Kolay entegrasyon



 7. Nesne Tanıma Süreci

Model giriş olarak görüntüyü alır.

Model aşağıdaki bilgileri üretir:

 Ürün sınıfı
 Güven skoru
 Konum bilgisi

Örnek çıktı:

Ürün: Koli
Güven Skoru: %94
Konum: (125, 210, 300, 450)



 8. Sonuçların Ayrıştırılması

Model çıktıları işlenerek aşağıdaki formata dönüştürülür:

```json
{
  "product_name": "Koli",
  "count": 5,
  "confidence": 0.94,
  "location": "A1"
}
```

Düşük güven skoruna sahip tespitler filtrelenir.

Önerilen minimum güven değeri:

0.70



 9. Veritabanına Kayıt

Sonuçlar PostgreSQL veritabanına aktarılır.

Güncellenen tablolar:

 Products
 Inventory
 MovementLogs

Örnek işlem:

1. Ürün bulunur.
2. Raf bilgisi bulunur.
3. Stok miktarı güncellenir.
4. Hareket kaydı oluşturulur.



 10. Gerçek Zamanlı Performans Analizi

 Olası Darboğazlar

 Yüksek Çözünürlüklü Görüntüler

Sorun:

 İşlem süresinin uzaması

Çözüm:

 Görüntü yeniden boyutlandırma

 Model Çıkarım Süresi

Sorun:

 Düşük FPS

Çözüm:

 GPU kullanımı
 Optimize edilmiş model

 Veritabanı Yazma İşlemleri

Sorun:

 Gecikme oluşması

Çözüm:

 Toplu kayıt işlemleri
 Asenkron veri yazımı

 Ağ Trafiği

Sorun:

 Veri aktarım gecikmesi

Çözüm:

 JPEG sıkıştırma
 Yerel ağ kullanımı



 11. Teknoloji Seçimi

| Katman         | Teknoloji      |
|  |  |
| Görüntü İşleme | OpenCV         |
| Yapay Zeka     | PyTorch + YOLO |
| API            | FastAPI        |
| Veritabanı     | PostgreSQL     |
| ORM            | SQLAlchemy     |
| Mesaj Kuyruğu  | RabbitMQ       |
| Önbellek       | Redis          |



 12. Sonuç

Tasarlanan entegrasyon akışı, kamera görüntülerinin gerçek zamanlı olarak işlenmesini, nesne tanıma sonuçlarının güvenilir biçimde elde edilmesini ve envanter sistemine aktarılmasını sağlamaktadır. Önerilen mimari ölçeklenebilir, performanslı ve endüstriyel uygulamalar için uygun bir yapı sunmaktadır.
