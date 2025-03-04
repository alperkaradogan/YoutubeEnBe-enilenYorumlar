# YouTube API Anahtarı Oluşturma Rehberi

Bu rehber, YouTube Data API'yi kullanmak için gerekli olan API anahtarını nasıl oluşturacağınızı adım adım açıklamaktadır.

## Adım 1: Google Cloud Console'a Giriş Yap

* [Google Cloud Console](https://console.cloud.google.com/) sayfasına gidin.
* Google hesabınızla giriş yapın.

## Adım 2: Yeni Bir Proje Oluştur

* Sol üst köşedeki "Proje Seç" butonuna tıklayın.
* "Yeni Proje" butonuna basın.
* Proje adını girin (örneğin, "YouTube API Projem").
* "Oluştur" butonuna basın ve birkaç saniye bekleyin.

## Adım 3: YouTube Data API'yi Etkinleştir

* Sol taraftaki "API'ler ve Hizmetler" > "Kitaplık" menüsüne gidin.
* Arama çubuğuna "YouTube Data API v3" yazın ve çıkan API'yi seçin.
* "Etkinleştir" butonuna basın.

## Adım 4: API Anahtarı Oluştur

* "API'ler ve Hizmetler" > "Kimlik Bilgileri" sekmesine gidin.
* "Kimlik Bilgileri Oluştur" > "API Anahtarı" seçeneğine tıklayın.
* Google size otomatik olarak bir API anahtarı verecektir.
* Anahtarı kopyalayın ve güvenli bir yerde saklayın.

## Adım 5: API Anahtarını Kullan

* Python kodunuzdaki `API_KEY = "YOUR_YOUTUBE_API_KEY"` satırına kendi API anahtarınızı yapıştırın.
* Artık YouTube verilerine erişmek için API'yi kullanabilirsiniz! 

## Önemli Notlar

* API anahtarınızı kimseyle paylaşmayın.
* API kullanım kotalarını aşmamaya dikkat edin.
* Google Cloud Console'da API anahtarınızın kullanımını kısıtlayabilirsiniz (örneğin, belirli IP adreslerinden gelen isteklerle sınırlayabilirsiniz).

## Ek Kaynaklar

* [YouTube Data API v3 Resmi Belgeleri](https://developers.google.com/youtube/v3)

Umarım bu rehber yardımcı olur!
