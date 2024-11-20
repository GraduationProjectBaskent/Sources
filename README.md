Model Parametrelerinin incelenmesi 

1.1) Train_dfl_loss (Distribution focal loss):
  - YOLO Modellerinde box regression yani bounding box koordinatlarını optimize etme sırasında kullanılan bir metrik, DFL, bounding box regresyonunda daha iyi bir hasasiyet sağlar.
  - Özetle; Modelin öngördüğü bounding box koordinatlarını daha doğru hale getirmek için kullanılır. Yüksek doğruluklu kutu merkezlerini ve boyutlarını öğrenmemiz için önemlidir.
                                                                                                 



![Ekran görüntüsü 2024-11-20 175251](https://github.com/user-attachments/assets/1feb1874-52af-4a47-8e3d-c0d36ba3ad60)


1.2) Train_cls_loss (Class_loss):
   - Nesne sınıflarının tahmini doğruluğunu ölçen kayıp fonksiyonu 
   - Modelin her bounding box için doğru sınıf etiketlerini tahmin etmesini sağlar. Yanlış tahminler bu kaybı artırır ve model bu kaybı minimize etmeye çalışır.


























![Ekran görüntüsü 2024-11-20 175244](https://github.com/user-attachments/assets/df9b650b-9105-448f-a257-ae60552c9655)


1.3) Train_box_loss:
   - Gerçek bounding box koordinatlarıyla (ground truth) modelin tahmin ettiği koordinatlar arasındaki farkı minimize eder.
   - Kısaca; Bounding box'ların doğru pozisyon ve boyutlarını öğrenmek için kullanılan kayıp fonksiyonu.








![Ekran görüntüsü 2024-11-20 175236](https://github.com/user-attachments/assets/44366686-8a86-4637-9857-8215a96c48d9)

1.4) Metrics Recall(B):
   - Modelin, tespit etmesi gereken nesnelerden kaç tanesini doğru şekilde tespit ettiğini gösterir.
   - Değeri 1’e ne kadar yakınsa, modelin gerçek nesneleri kaçırma oranı o kadar düşüktür.

   






![Ekran görüntüsü 2024-11-20 175231](https://github.com/user-attachments/assets/af0c8e99-6480-4500-9cc6-75b5decf8bfe)

1.5) Metrics Precision(B):
   - Modelin yaptığı tahminlerin ne kadarının doğru olduğunu gösterir.
   






![Ekran görüntüsü 2024-11-20 175226](https://github.com/user-attachments/assets/a70ad8dc-b7e1-4e20-bdd2-6cfdd24970ef)

1.6) Metrics/mAP50-95 (Mean Average Precision at IoU 0.5 to 0.95)
   - Bu Metriğin biraz detaylıca incelenmesi gerekiyor ama burada kısaca ne olduğundan bahsedeceğim. 
   - IoU eşik değerleri 0.5'ten 0.95'e kadar 0.05 adımlarla alınarak tüm sınıflar için ortalama doğruluğun hesaplanmasıdır.
   - Değeri: 1’e ne kadar yakınsa, model o kadar iyi performans göstermiştir.








![Ekran görüntüsü 2024-11-20 175220](https://github.com/user-attachments/assets/f9ec7596-10ef-4ca3-93d0-cfffc7561980)

1.7) Metrics/mAP50 (Mean Average Precision at IoU 0.5)
   - Intersection over Union (IoU) eşik değeri 0.5 olarak alındığında, modelin tüm sınıflar için doğruluğunun ortalamasını ifade eder.
   - IoU; Tahmin edilen ve gerçek bounding box'ların ne kadar örtüştüğünü gösterir.
   - Literatürde Faster-RCNN gibi, SSD gibi Nesne tespiti alanındaki algoritmalarda kullanılan en yaygın doğruluk ölçütlerinden biridir ve IoU ≥ 0.5 kabul edilir.






![Ekran görüntüsü 2024-11-20 175208](https://github.com/user-attachments/assets/c2340b0f-38de-4cc7-8d62-e086297a484f)






![Ekran görüntüsü 2024-11-20 175506](https://github.com/user-attachments/assets/1f5dd717-1bdd-4f7e-a183-6447e3119e2b)




https://github.com/user-attachments/assets/f447f730-f2fc-4525-ac76-143280875c8d
