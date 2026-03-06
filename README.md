# Odoo 15 Shift Modülü

Odoo 15 için vardiya planlaması modülü. Çalışanların vardiya atamalarını yönetir ve Odoo Analitik Hesaplar ile entegre çalışır.

## Özellikler

- **Vardiya Şablonları**: Sabah, öğle, gece gibi vardiya türlerini tanımlama
- **Vardiya Planları**: Haftalık/aylık vardiya planları oluşturma
- **Vardiya Atamaları**: Çalışanları vardiya planlarına atama
- **Analitik Hesaplar**: Her vardiya/plan/atama için analitik hesap ile maliyet analizi
- **İç Kullanıcılar**: Sadece Odoo iç kullanıcıları (portal kullanıcıları hariç) erişebilir

## Bağımlılıklar

- Odoo 15.0
- base
- hr (İnsan Kaynakları)
- analytic (Analitik Hesaplar)

## Kurulum

1. Modülü Odoo addons dizinine kopyalayın veya `addons_path`'e ekleyin:
   ```
   addons_path = /path/to/odoo/addons,/path/to/custom_addons
   ```

2. Odoo'yu yeniden başlatın

3. Geliştirici modunu etkinleştirin (Ayarlar > Geliştirici Araçları)

4. Uygulamalar menüsünde "Uygulama Listesini Güncelle" tıklayın

5. "Shift" modülünü arayın ve yükleyin

## Cloudpepper Deploy

1. Bu repoyu GitHub'a yükleyin
2. Cloudpepper yönetim panelinde Custom Addons veya Git Integration bölümüne repo URL'sini ekleyin
3. Odoo addons dizinine modül eklenecek şekilde yapılandırın
4. Odoo'da Uygulama Listesini Güncelleyin ve Shift modülünü yükleyin

## Kullanım

1. **Vardiya Şablonları** (Yapılandırma): Sabah 08-16, Öğle 12-20, Gece 22-06 gibi şablonlar oluşturun
2. **Vardiya Planları**: Yeni plan oluşturun, başlangıç ve bitiş tarihlerini belirleyin
3. **Atamalar**: Plan içinde çalışanları vardiya şablonlarına atayın
4. **Analitik**: Her kayıtta analitik hesap seçerek maliyet analizi yapın

## Lisans

LGPL-3
