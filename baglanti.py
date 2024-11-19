from dronekit import connect

# Connect fonksiyonu ile Python kodunu simulasyon ortamı ile bağlayabilcem
drone = connect('127.0.0.1:14550',wait_ready=True)

print(f'Drone Arm Durumu: {drone.armed}')

# Konum ifadeleri 3 adet veri sunuyor x,y,z ifadeleri
# x,y,z --> enlem, boylam, yükseklik
# Global Frame ve Global Relative Frame farkı yükseklikte ortaya çıkıyor
# Global Frame --> Deniz seviyesine göre bir irtifa sunuyor
# Global Relative Frame --> Drone'un kendisinin yerden yüksekliğini veriyor.
print(f'Global Frame{drone.location.global_frame}') 
print(f'Global Relative Frame{drone.location.global_relative_frame}')

# altitude (yüksekliği verir.)
print(f'İrtifa:{drone.location.global_relative_frame.alt}')

"""
------------------------ Drone'a MAVlink komutu yollayip Drone'u Havalandircam -------------------------------
"""


