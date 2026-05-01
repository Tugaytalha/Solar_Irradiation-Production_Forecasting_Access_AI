# Solar Irradiation & Production Forecasting with AI ☀️

![Project Status](https://img.shields.io/badge/status-active-success.svg)
![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-green.svg)
![H2O](https://img.shields.io/badge/H2O%20AutoML-3.0-yellow.svg)
![Flask](https://img.shields.io/badge/Flask-3.0-lightgrey.svg)
![Docker](https://img.shields.io/badge/Docker-ready-blue.svg)

Güneş enerjisi üretim tahmini ve finansal analiz için kapsamlı bir AI destekli çözüm. Bu proje, coğrafi konuma göre güneş ışınımını (irradiasyon) tahmin eder, panel verimliliğine göre enerji üretimini hesaplar ve yatırım geri dönüş süresini (ROI) analiz eder.

## 🎯 Proje Hakkında

Bu sistem, güneş enerjisi yatırımlarını değerlendirmek isteyenler için geliştirilmiş kapsamlı bir karar destek aracıdır. 1991-2005 yılları arası TMY3 (Typical Meteorological Year 3) verilerini kullanarak:

- **30 yıllık güneş ışınımı tahmini** yapar
- **Enerji üretimini** (kWh) hesaplar
- **Finansal analiz** (aylık/yıllık kâr, amortisman süresi) sunar
- **Grafiksel raporlama** ile yatırım projeksiyonu çizer

### Temel Amaçlar
- Güneş enerjisi yatırımlarının fizibilitesini belirlemek
- Konuma özel optimizasyon yapmak
- Panel seçimine göre farklı senaryoları karşılaştırmak
- Yenilenebilir enerji projelerinde risk analizi yapmak

## ✨ Öne Çıkan Özellikler

### 🤖 Gelişmiş AI Modeli
- **H2O AutoML** ile otomatik model seçimi
- **XGBoost** tabanlı en iyi model pipeline'ı
- **30 yıllık tahmin** kapasitesi (12 ay × 30 yıl)
- **Gerçek zamanlı öğrenme** (H2O cluster entegrasyonu)

### 🌍 Coğrafi Hesaplamalar
- **Güneş açıları**: Azimuth (ufuk açısı) ve Elevation (yükseklik) hesaplamaları
- **Gerçek zamanlı konum verisi**: Open-Meteo API ile rakım (elevation) tespiti
- **Günün hangi anı**: Solar declination ve hour angle hesaplamaları
- **Koordinat bazlı**: Enlem (latitude) ve boylam (longitude) desteği

### 💰 Finansal Analiz
- **Enerji fiyatı entegrasyonu** (kWh başına maliyet)
- **Panel wattage veya alan/verimlilik** bazlı hesaplama
- **İnverter maliyeti** hesaplama (kapasiteye göre kademeli)
- **Amortisman süresi** (break-even point) belirleme
- **30 yıllık kümülatif kâr** projeksiyonu

### 🚀 Hazır Deployment
- **Flask REST API** (/predict_energy endpoint'i)
- **Docker containerization** (docker-compose ile tek komutla ayağa kalkar)
- **CORS desteği** (cross-origin isteklerine açık)
- **Base64 grafik** çıktısı (web uygulamalarına gömülmeye hazır)

## 🛠️ Kullanılan Teknolojiler

| Teknoloji | Sürüm | Kullanım Amacı |
|-----------|-------|----------------|
| Python | 3.8+ | Ana programlama dili |
| H2O AutoML | 3.x | Otomatik makine öğrenmesi |
| Flask | 3.0.3 | REST API sunucusu |
| XGBoost | 2.1.1 | Gradient boosting modeli |
| scikit-learn | 1.4.1 | Veri ölçeklendirme (StandardScaler) |
| pandas | Latest | Veri manipülasyonu |
| NumPy | Latest | Sayısal hesaplamalar |
| Matplotlib | Latest | Grafik çizimi |
| joblib | Latest | Model serileştirme |
| Docker | Latest | Konteynerizasyon |
| Open-Meteo API | - | Rakım (elevation) verisi |

## 📁 Proje Yapısı

```
Solar_Irradiation-Production_Forecasting_Access_AI/
├── 📂 data/
│   ├── 1991-2005/
│   │   ├── monthly/solar_dataset.csv     # Aylık güneş verisi
│   │   └── tmy3/                         # TMY3 ham verileri
│   │       ├── TMY3_StationsMeta(1).csv
│   │       ├── TMY3_StationsMetaMeta.doc
│   │       ├── tmy3_description.docx
│   │       └── tmy3_user_manual.pdf
│   └── link.txt                          # Veri kaynağı linki
├── 📂 __pycache__/                       # Python cache dosyaları
├── 🐍 app.py                              # Flask API uygulaması
├── 🐍 best_solar_model.pkl                # Eğitilmiş H2O modeli
├── 🐍 scaler.pkl                          # StandardScaler nesnesi
├── 🐍 preprocess_train.py                 # Model eğitim scripti
├── 🐍 calculate_azimuth.py                # Güneş açı hesaplamaları
├── 🐍 elevation_api.py                    # Open-Meteo API entegrasyonu
├── 📓 preprocess_train.ipynb              # Jupyter notebook (eğitim)
├── 📓 convert_to_montly.ipynb             # Aylık veri dönüşümü
├── 📓 merge_wlocations.ipynb              # Lokasyon birleştirme
├── 📄 best_model_pipeline.py               # En iyi model pipeline'ı
├── 📄 dockerfile                          # Docker imaj tanımı
├── 📄 docker-compose.yaml                 # Docker compose yapılandırması
├── 📄 requirements.txt                    # Python gereksinimleri
├── 📄 r.txt                               # Ek bağımlılıklar
├── 📄 solar.csv                           # İşlenmiş güneş verisi
├── 📄 output.png                          # Örnek çıktı grafiği
├── 📄 unlog.txt                           # Hata kayıtları
├── 📄 LICENSE                             # Apache 2.0 Lisansı
├── 📄 README.md                           # Bu dosya
├── 📄 .gitignore                          # Git yoksayma kuralları
└── 📄 .gitattributes                      # Git özellikleri
```

## ☀️ Güneş Açıları Hesaplama

### `calculate_azimuth.py` İçeriği

**Solar Declination (δ)**:
```
δ = 23.45 × sin(360/365 × (day_of_year - 81))
```

**Solar Elevation Angle (α)**:
```
sin(α) = sin(φ) × sin(δ) + cos(φ) × cos(δ) × cos(H)
```
- φ: Enlem (latitude)
- H: Saat açısı (hour angle)

**Solar Azimuth Angle (A)**:
```
cos(A) = (sin(δ) - sin(α) × sin(φ)) / (cos(α) × cos(φ))
```

Bu hesaplamalar, günün her anı için güneşin konumunu belirleyerek irradiasyon tahminini iyileştirir.

## 🔬 Veri Seti Detayları

### TMY3 Verisi (1991-2005)
- **Kaynak**: Typical Meteorological Year 3 veritabanı
- **Zaman çözünürlüğü**: Aylık aggregated değerler
- **İstasyon sayısı**: Çok sayıda meteoroloji istasyonu
- **Değişkenler**:
  - Azimuth (deg): Güneş ufuk açısı
  - Longitude: Boylam
  - Elevation: Rakım
  - Latitude: Enlem
  - Year: Yıl
  - Month: Ay
  - **Merged Glo (Wh/m²)**: Birleştirilmiş güneş ışınımı (hedef değişken)

### Özellik Mühendisliği
- **StandardScaler** ile koordinat verilerinin normalize edilmesi
- **Aylık gruplama** ile mevsimsellik yakalama
- **Yıl bazlı trend** analizi

## 🧠 Model Mimarisi

### H2O AutoML Pipeline
1. **Veri yükleme**: pandas DataFrame → H2OFrame dönüşümü
2. **Train-Test split**: %80 eğitim, %20 test
3. **AutoML çalıştırma**:
   - `max_runtime_secs=600` (10 dakika)
   - `nfolds=5` (5-katlı çapraz doğrulama)
   - Seed: 42 (yeniden üretilebilirlik)
4. **En iyi model seçimi**: Leaderboard'dan en iyi XGBoost pipeline'ı
5. **Tam veri ile yeniden eğitim**: Tüm veriyi kullanarak final model
6. **Kaydetme**: `joblib.dump()` ile `best_solar_model.pkl`

### Model Performansı
- **Target**: Merged Glo (Wh/m²)
- **Algorithms**: XGBoost, Random Forest, GLM, Deep Learning (H2O AutoML seçimi)
- **Evaluation**: MSE, RMSE, MAE metrikleri

## 🚀 Kurulum

### Gereksinimler
- Python 3.8 veya üzeri
- pip (Python paket yöneticisi)
- Docker (opsiyonel, container çalıştırmak için)
- H2O cluster (model eğitimi için, `10.1.234.150:54321`)

### Adımlar

1. **Projeyi klonlayın:**
   ```bash
   git clone https://github.com/TugayTalha/Solar_Irradiation-Production_Forecasting_Access_AI.git
   cd Solar_Irradiation-Production_Forecasting_Access_AI
   ```

2. **Sanal ortam oluşturun (önerilir):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # veya
   venv\Scripts\activate     # Windows
   ```

3. **Gereksinimleri yükleyin:**
   ```bash
   pip install -r requirements.txt
   ```

4. **H2O Cluster (model eğitimi için):**
   - Eğer kendi H2O clusterınız yoksa:
   ```python
   import h2o
   h2o.init()  # Yerel başlatma
   ```
   - Veya `10.1.234.150:54321` adresindeki clusterı kullanın

## 💡 Kullanım

### A. Modeli Yeniden Eğitmek (Geliştiriciler İçin)

```bash
python preprocess_train.py
# veya
jupyter notebook preprocess_train.ipynb
```

Bu işlem:
- TMY3 verisini yükler
- H2O AutoML ile en iyi modeli seçer
- `best_solar_model.pkl` ve `scaler.pkl` dosyalarını oluşturur

### B. Flask API'yi Çalıştırmak

#### 1. Yerel Çalıştırma
```bash
python app.py
# API http://0.0.0.0:5000 adresinde ayağa kalkar
```

#### 2. Docker ile Çalıştırma (Önerilen)
```bash
docker-compose up --build
# Flask uygulaması container içinde çalışır
```

### C. API Kullanımı

#### Endpoint: `/predict_energy`
**Method**: POST  
**Content-Type**: application/json

**İstek (Request) Örneği:**
```json
{
  "latitude": 40.7128,
  "longitude": -74.0060,
  "kwh_price": 0.15,
  "panel_wattage": 400
}
```
VEYA
```json
{
  "latitude": 40.7128,
  "longitude": -74.0060,
  "kwh_price": 0.15,
  "panel_area": 10,
  "panel_efficiency": 0.20
}
```

**Alanlar:**
| Alan | Tip | Açıklama | Gerekli |
|------|-----|----------|---------|
| latitude | float | Enlem (-90 ile 90 arası) | Evet |
| longitude | float | Boylam (-180 ile 180 arası) | Evet |
| kwh_price | float | kWh başına elektrik fiyatı ($) | Evet |
| panel_wattage | float | Panel gücü (Watt) | * |
| panel_area | float | Panel alanı (m²) | ** |
| panel_efficiency | float | Panel verimliliği (0.0-1.0) | ** |

*İsterseniz `panel_wattage` VEYA `panel_area + panel_efficiency` çiftini gönderin.

**Yanıt (Response) Örneği:**
```json
{
  "monthly_energy_output_kWh": 125.456,
  "yearly_energy_output_kWh": 1505.472,
  "monthly_profit": 18.82,
  "yearly_profit": 225.84,
  "break_even_month": 95,
  "break_even_year": 7.9,
  "chart": "<img src=\"data:image/png;base64,...\">"
}
```

**Yanıt Alanları:**
| Alan | Tip | Açıklama |
|------|-----|----------|
| monthly_energy_output_kWh | float | Aylık enerji üretimi (kWh) |
| yearly_energy_output_kWh | float | Yıllık enerji üretimi (kWh) |
| monthly_profit | int | Aylık kâr ($) |
| yearly_profit | int | Yıllık kâr ($) |
| break_even_month | int | Amortisman süresi (ay) |
| break_even_year | float | Amortisman süresi (yıl) |
| chart | string | Base64 kodlanmış PNG grafiği |

## 📊 Finansal Hesaplama Mantığı

### Panel Maliyeti
```python
if coeff <= 0.1:       # Küçük sistem
    inverter_price = 100
elif coeff <= 0.3:     # Orta sistem
    inverter_price = 1300
elif coeff <= 1:        # Büyük sistem
    inverter_price = 1800
else:                    # Endüstriyel
    inverter_price = 6000

panel_price = coeff * 13000 + (1500 if coeff > 0.1 else 0) + inverter_price
```

### Enerji Üretimi
```
energy_output = (panel_wattage / 1000) × (irradiation / 1000)
# VEYA
energy_output = (panel_area × panel_efficiency) × (irradiation / 1000)
```

### Kâr Hesaplama
```
monthly_profit = energy_output × kwh_price
yearly_profit = monthly_profit × 12
```

### Amortisman (Break-Even)
Aylık kârlar toplanarak panel fiyatını geçtiği ay belirlenir.

## 📈 Örnek Çıktı Grafiği

API yanıtındaki `chart` alanı, şu grafiği içerir:
- **X ekseni**: Yıllar (mevcut yıl + 30 yıl)
- **Y ekseni**: Kümülatif kâr ($)
- **Mavi çizgi**: Kümülatif kâr
- **Turuncu çizgi**: Panel maliyeti (sabit)

Grafik sayesinde yatırımın ne zaman kendini amorti edeceği görselleştirilir.

## 🤝 Katkıda Bulunma

1. Bu repoyu fork edin
2. Yeni bir özellik dalı oluşturun (`git checkout -b feature/AmazingFeature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add some AmazingFeature'`)
4. Dalınıza push yapın (`git push origin feature/AmazingFeature`)
5. Bir Pull Request açın

### Katkı Alanları
- Daha fazla ML modeli entegrasyonu (Prophet, LSTM, Transformer)
- Hava durumu API'leri ile gerçek zamanlı veri entegrasyonu
- Mobil uygulama geliştirme (React Native / Flutter)
- Daha gelişmiş finansal analiz (enflasyon, vergi teşvikleri)
- Panel kirliliği ve degradasyon hesabı
- Çoklu panel dizilimi optimizasyonu

## 📄 Lisans

Bu proje **Apache License 2.0** altında lisanslanmıştır. Lisans metnini [LICENSE](LICENSE) dosyasında bulabilirsiniz.

## 📧 İletişim

**Tugay Talha İçen**
- GitHub: [@Tugaytalha](https://github.com/TugayTalha)
- Twitter: [@TugayTalhaIcen](https://twitter.com/TugayTalhaIcen)
- LinkedIn: [Tugay Talha İçen](https://linkedin.com/in/tugaytalhaicen)

**Proje Linki**: [https://github.com/TugayTalha/Solar_Irradiation-Production_Forecasting_Access_AI](https://github.com/TugayTalha/Solar_Irradiation-Production_Forecasting_Access_AI)

## 🙏 Teşekkürler

- **NREL (National Renewable Energy Laboratory)** TMY3 verilerini sağladığı için
- **H2O.ai** ekibi otomatik ML altyapısı için
- **Open-Meteo** ücretsiz API hizmeti için
- **XGBoost** geliştiricileri güçlü gradient boosting algoritması için

---

☀️ **Yenilenebilir enerji ile daha temiz bir gelecek!**

⭐ Bu projeyi yararlı bulduysanız yıldızlamayı unutmayın!

🐛 Hata bildirimi veya önerileriniz için [Issues](https://github.com/TugayTalha/Solar_Irradiation-Production_Forecasting_Access_AI/issues) sekmesini kullanın.
