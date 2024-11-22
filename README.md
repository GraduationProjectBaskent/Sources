Bu kısımda  MavROS yapısını kullanarak Drone kontrol işlemleri ve Odometry gibi sensörlerden verilerin çekilmesi gibi işlemleri yaptım. Şimdi kullandığım yapıları detaylıca açıklayacağım.
Kodlara src dizini altındaki scripts klasöründen ulaşabilirsiniz.

1.1) ROS'un temel kavramları:
- Packages (Paketler):
  Paketler kısaca, ROS'ta yazılımın düzenli olmasını sağlayan ana birimlerdir. Bir paket, işlemleri (düğümleri), ROS'a bağlı kütüphaneleri, yapılandırma dosyaları gibi paket için faydalı olabilecek dosyaları
  içerir. Paketlerin oluşturulma amacı, kodların parçalara bölünerek yeniden kullanılabilir olmasını sağlamaktır.



  oluşturduğumuz Paketlerde  bulunan bazı klasörler ve anlamları:

  CMakeLists.txt: Derleyiciye verilen emirleri ve birçok yapı bilgisini içeren derleme dosyasıdır.

  package.xml : Paketlerle alakalı bilgileri içeren bildiri dosyasıdır.

  scripts/: Doğrudan çalıştırılabilir (executable) kodların bulunduğu klasördür. /Kısaca Python kodlarının bulunduğu klasördür.

  msg/: Mesaj tiplerinin içerildiği klasördür.

  srv/: Servis dosyalarının bulunduğu klasördür.

  action/: Aksiyon dosyalarının bulunduğu klasörlerdir.

  ![0_vfNM1mbkhUpvK-nW](https://github.com/user-attachments/assets/20b30845-b81a-4776-9bef-bace725eff6a)


- Nodes(Düğümler):
  Düğümler, hesaplama yapan işlemlerdir. ROS'taki düğüm yapısı kullanılarak, kodlar parçalara ayrılır ve sistem basitleştirilir.
  basit bir örnek vermem gerekirse; mesela elimizde bir drone var örneğin bir düğüm kamera'nın çalışmasını ve nesne tespiti yapmasını sağlarken, diğer bir düğüm konumlandırma sağlayabilir, bir düğüm motorların arm edilmesini sağlayabilir.
  yani bu tarz sistemlerde her şeyi yapan büyük bir düğüm olucağına yalnızca tek bir işlev sağlayan birçok düğüme sahip olmak daha verimli bir yoldur.

  Python kullanılarak yazılacak düğüm için rospy kütüphanesi kullanılır.

  Bir düğümün sistemde benzersiz bir adının olması gerekir bu annonymous=True parametresi ile sağlanabilmekte kodlarda görebilirsiniz.



- Messages (Mesajlar) ve rosmsg Aracı:
  Mesajlar kısaca düğümlere bilgi sağlayan verileri içeren ve düğümler arasındaki haberleşmeyi sağlayan yapılardır.
  ROS sayesinde istenildiğinde, kendi mesaj tiplerimizi tanımlayabiliyor ve onları kullanabiliyoruz

  Mesaj türleri, paket kaynak adları kullanılarak kod içerisinde belirtiliyor (geometry_msgs) gibi
  
  mesela aşağıdaki mesajı inceleyelim
  
![Screenshot from 2024-11-22 16-51-48](https://github.com/user-attachments/assets/74e717a7-b88c-45a4-bd81-94ecc0295fa6)

  bu mesaj bize 3 eksen boyunca konum bilgisini float64 tipinde veriyor


- Topics (Konular) ve rostopic Aracı:
  Konular, mesaj içeriğini tanımlamak için kullanılan isimlerdir ve düğümlerin üzerinde mesaj alışverişi yaptığı veri yolları olarak düşünülebilir.
  Konular, sürekli mesaj gönderip almaya bağlı bir yapı olduğundan, mesajların sürekli yayınlanmasını gerektiren sensör verileri için uygundur. Örneğin Drone bir engel algılayacaksa sürekli olarak mesafe sensöründen veya kameradan
  veri alması lazım. Bu tarz sensör verilerinin sürekli kullanılmasını gerektiren durumlarda topics(konular) kullanılır.

  Topics'ler ile ilgili bilinmesi gereken en önemli nokta; kullanılan mesajlar, Publisher - Subscriber yapısına sahip bir yapıyla yönlendirilir. Bir düğüm, bir konuyu yayınlayarak başka bir düğüme veya düğümlere belirli bir mesaj tipinde veri
  gönderir. Bu gönderilen mesaj türüyle ilgilenen bir düğüm uygun konuya abone olur.

  
  Tek bir konu için birden fazla eşzamanlı yayıncı ve abone olabiliyor. Tek bir düğüm birden fazla konuda yayın yapabilir ve birden fazla konuya abone olabilir.

  Konular ve servislerin farkı; Konular tek yönlü iletişim içindir. Bir isteğe bağlı olarak yanıt alması gereken düğümler için, servisler kullanılmalıdır.


  Şimdi bunu bir örnekle ve sırayla anlatmaya çalışıcam.
  Yayıncı - Abone (Publisher - Subscriber) İletişim Modeli: Bu iletişim modeli, yayıncını açıkça alıcıları belirtmeden ya da  alıcıların bilgisine sahip olmadan mesajını yayınlamasını gerektirir.
  Abone, yayınlanan mesajlar içerisinden ilgili olanları kullanır. Düğümlerin bilgilerini yöneten ve gerektiğinde düğümler arasında iletişim kuran ROS çekirdeği başlatılır.

  Adımlar:
  1) Yayıncı ve abone düğümler ROS çekirdeğine kayıt olur.
  2) Abone düğüm çalıştırılır ve kendine uygun konuyu aramaya başlar.
  3) Yayıncı düğüm çalıştırılır ve yayına başlar
  4) ROS çekirdeği aboneye, aradığı konular için yayıncı olduğunu bildirir.
  5) Abone ile yayıncı iletişime geçer ve TCPROS ile veri aktarımı olur.
  
  
![Ekran görüntüsü 2024-11-22 174921](https://github.com/user-attachments/assets/1223dfc7-ba2e-4deb-8de8-3509ab6ea459)




- Services (Servisler) :
  Servisler yalnızca bir istek olduğunda yanıt veren, bir sunucudan ve istek gönderen bir istemciden oluşan TALEP - CEVAP iletişim modelini kullanan yapılardır.
  Servislerde, isteğe yanıt verildikten sonra, düğümler arasındaki bağlantı kesilir. Böylece, ağın yükü azaltılmış olur.

  Servis dosyaları talep ve yanıt bölümleri içerir. Bu bölümler dosya içerisinde alt alta yazılarak "---" işareti ile ayrılırlar. aşağıda bir servis dosyasının içeriğini görebilirsiniz

  ![Screenshot from 2024-11-22 14-48-29](https://github.com/user-attachments/assets/3a49e943-9799-4152-9534-d542212fc5b0)

  Şimdi aşağıda bulunan GİF ile Service Client - Service Server ilişkisini kuralım.

  Service Client (İstemci) bir istek (Request) gönderiyor  Service Server'a. Server bu isteği alıyor değerlendiriyor ve istemciye bir cevap (Response) Döndürüyor.
  

  ![Service-SingleServiceClient](https://github.com/user-attachments/assets/9387db63-5f1d-47bc-94a2-eebd7407aedc)

  


  



  
  
  
  
  
  

