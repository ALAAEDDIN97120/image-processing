#!/usr/bin/env python
# coding: utf-8

# In[1]:


#ALAA EDDIN ABOU YAHAI
#02200201090
import cv2
import numpy as np

# Kamera
cap = cv2.VideoCapture(0)

while True:
    # Kameradan bir kare al
    ret, kare = cap.read()

    # RGB'den HSV'ye dönüşüm yap
    hsv = cv2.cvtColor(kare, cv2.COLOR_BGR2HSV)

    # Kırmızı renk aralığı
    alt_kirmizi = np.array([0, 100, 100])
    ust_kirmizi = np.array([10, 255, 255])

    # HSV görüntüsünde belirtilen renk aralığındaki pikselleri beyaz yap, diğerlerini siyah yap
    maske = cv2.inRange(hsv, alt_kirmizi, ust_kirmizi)

    # Orijinal görüntüde sadece belirtilen renk aralığındaki pikselleri göster
    sonuc = cv2.bitwise_and(kare, kare, mask=maske)

    # Görüntüleri göster
    cv2.imshow('Orijinal', kare)
    cv2.imshow('Sadece Kırmızı Nesne', sonuc)

    # Çıkış için 'q' tuşuna basılmasını bekle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamera bağlantısını kapat
cap.release()
cv2.destroyAllWindows()


  

