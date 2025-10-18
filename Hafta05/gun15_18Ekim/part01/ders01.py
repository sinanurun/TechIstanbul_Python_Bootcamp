"""
Web otomasyonunun ne olduğunu ve neden kullanıldığını anlamak
Selenium WebDriver kurulumu ve temel kullanımı
Web sayfalarında element bulma ve etkileşim kurma
Form doldurma, buton tıklama, sayfa gezinme işlemleri
Gerçek hayat örnekleriyle otomasyon projeleri geliştirmek

"""

#web otomasyonu : İnsan müdahalesi olmadan web sitelerinde işlemler yapma.
"""
Kullanım alanları:
Test otomasyonu (QA)
Veri toplama (web scraping alternatifi)
Otomatik form doldurma
Bot geliştirme (örneğin: fiyat takibi)
"""

"""
Selenium Nedir?
Açık kaynaklı bir web otomasyon aracıdır.
Tarayıcıları (Chrome, Firefox, Edge vb.) programatik olarak kontrol eder.
Selenium WebDriver: Tarayıcıyla doğrudan iletişim kurar.
"""
# Selenium kullanma sebepleri:
# 1. JavaScript ile yüklenen sayfaları çekmek için
# 2. Form doldurma, butona tıklama gibi işlemler için  
# 3. Kullanıcı girişi gerektiren işlemler için
# 4. Tarayıcıda yapılan testleri otomatikleştirmek için

"""
BeautifulSoup:
- Sadece HTML çözümleyici
- Statik sayfalar için ideal
- Hızlı ve hafif

Selenium:
- Gerçek tarayıcı kontrolü
- JavaScript çalıştırabilir
- Dinamik sayfalar için ideal
- Daha yavaş ama güçlü
"""
#kurulum adımları

# 1. Selenium kütüphanesini yükle
# pip install selenium

# 2. WebDriver Manager'ı yükle (otomatik driver kurulumu için)
# pip install webdriver-manager

# VEYA Manuel olarak ChromeDriver indir:
# https://chromedriver.chromium.org/


#https://googlechromelabs.github.io/chrome-for-testing/

#https://github.com/mozilla/geckodriver/releases

#https://msedgewebdriverstorage.z22.web.core.windows.net/