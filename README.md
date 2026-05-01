# Solar Irradiation & Production Forecasting with AI ☀️

![Project Status](https://img.shields.io/badge/status-active-success.svg)
![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-green.svg)
![H2O](https://img.shields.io/badge/H2O%20AutoML-3.0-yellow.svg)
![Flask](https://img.shields.io/badge/Flask-3.0-lightgrey.svg)
![Docker](https://img.shields.io/badge/Docker-ready-blue.svg)

A comprehensive AI-powered solution for solar energy production forecasting and financial analysis. This project predicts solar irradiation based on geographic location, calculates energy production based on panel efficiency, and analyzes investment payback period (ROI).

## 🎯 Project Overview

This system is a comprehensive decision support tool developed for those evaluating solar energy investments. Using TMY3 (Typical Meteorological Year 3) data from 1991-2005, it:

- Makes **30-year solar irradiation forecasts**
- Calculates **energy production** (kWh)
- Provides **financial analysis** (monthly/yearly profit, payback period)
- Generates **graphical reports** with investment projections

### Core Objectives
- Determine feasibility of solar energy investments
- Perform location-specific optimization
- Compare different scenarios based on panel selection
- Conduct risk analysis in renewable energy projects

## ✨ Key Features

### 🤖 Advanced AI Model
- **H2O AutoML** for automatic model selection
- **XGBoost**-based best model pipeline
- **30-year forecasting** capacity (12 months × 30 years)
- **Real-time learning** (H2O cluster integration)

### 🌍 Geographic Calculations
- **Solar angles**: Azimuth (horizon angle) and Elevation calculations
- **Real-time location data**: Elevation detection via Open-Meteo API
- **Solar position**: Solar declination and hour angle calculations
- **Coordinate support**: Latitude and longitude support

### 💰 Financial Analysis
- **Energy price integration** (cost per kWh)
- **Panel wattage or area/efficiency** based calculations
- **Inverter cost** calculation (tiered by capacity)
- **Payback period** (break-even point) determination
- **30-year cumulative profit** projection

### 🚀 Ready-to-Deploy
- **Flask REST API** (/predict_energy endpoint)
- **Docker containerization** (single command deployment with docker-compose)
- **CORS support** (open to cross-origin requests)
- **Base64 chart** output (ready to embed in web applications)

## 🛠️ Technologies Used

| Technology | Version | Purpose |
|-----------|---------|---------|
| Python | 3.8+ | Main programming language |
| H2O AutoML | 3.x | Automated machine learning |
| Flask | 3.0.3 | REST API server |
| XGBoost | 2.1.1 | Gradient boosting model |
| scikit-learn | 1.4.1 | Data scaling (StandardScaler) |
| pandas | Latest | Data manipulation |
| NumPy | Latest | Numerical calculations |
| Matplotlib | Latest | Chart plotting |
| joblib | Latest | Model serialization |
| Docker | Latest | Containerization |
| Open-Meteo API | - | Elevation data |

## 📁 Project Structure

```
Solar_Irradiation-Production_Forecasting_Access_AI/
├── 📂 data/
│   ├── 1991-2005/
│   │   ├── monthly/solar_dataset.csv     # Monthly solar data
│   │   └── tmy3/                         # TMY3 raw data
│   │       ├── TMY3_StationsMeta(1).csv
│   │       ├── TMY3_StationsMetaMeta.doc
│   │       ├── tmy3_description.docx
│   │       └── tmy3_user_manual.pdf
│   └── link.txt                          # Data source link
├── 📂 __pycache__/                       # Python cache files
├── 🐍 app.py                              # Flask API application
├── 🐍 best_solar_model.pkl                # Trained H2O model
├── 🐍 scaler.pkl                          # StandardScaler object
├── 🐍 preprocess_train.py                 # Model training script
├── 🐍 calculate_azimuth.py                # Solar angle calculations
├── 🐍 elevation_api.py                    # Open-Meteo API integration
├── 📓 preprocess_train.ipynb              # Jupyter notebook (training)
├── 📓 convert_to_montly.ipynb             # Monthly data conversion
├── 📓 merge_wlocations.ipynb              # Location merging
├── 📄 best_model_pipeline.py               # Best model pipeline
├── 📄 dockerfile                          # Docker image definition
├── 📄 docker-compose.yaml                 # Docker compose configuration
├── 📄 requirements.txt                    # Python requirements
├── 📄 r.txt                               # Additional dependencies
├── 📄 solar.csv                           # Processed solar data
├── 📄 output.png                          # Sample output graph
├── 📄 unlog.txt                           # Error logs
├── 📄 LICENSE                             # Apache 2.0 License
├── 📄 README.md                           # This file
├── 📄 .gitignore                          # Git ignore rules
└── 📄 .gitattributes                      # Git attributes
```

## ☀️ Solar Angle Calculations

### `calculate_azimuth.py` Content

**Solar Declination (δ)**:
```
δ = 23.45 × sin(360/365 × (day_of_year - 81))
```

**Solar Elevation Angle (α)**:
```
sin(α) = sin(φ) × sin(δ) + cos(φ) × cos(δ) × cos(H)
```
- φ: Latitude
- H: Hour angle

**Solar Azimuth Angle (A)**:
```
cos(A) = (sin(δ) - sin(α) × sin(φ)) / (cos(α) × cos(φ))
```

These calculations determine the sun's position at any moment of the day to improve irradiation forecasting.

## 🔬 Dataset Details

### TMY3 Data (1991-2005)
- **Source**: Typical Meteorological Year 3 database
- **Time resolution**: Monthly aggregated values
- **Station count**: Multiple meteorological stations
- **Variables**:
  - Azimuth (deg): Sun horizon angle
  - Longitude: Longitude
  - Elevation: Altitude
  - Latitude: Latitude
  - Year: Year
  - Month: Month
  - **Merged Glo (Wh/m²)**: Merged solar irradiation (target variable)

### Feature Engineering
- **StandardScaler** for normalizing coordinate data
- **Monthly grouping** to capture seasonality
- **Year-based trend** analysis

## 🧠 Model Architecture

### H2O AutoML Pipeline
1. **Load data**: pandas DataFrame → H2OFrame conversion
2. **Train-Test split**: 80% training, 20% testing
3. **Run AutoML**:
   - `max_runtime_secs=600` (10 minutes)
   - `nfolds=5` (5-fold cross-validation)
   - Seed: 42 (reproducibility)
4. **Select best model**: XGBoost pipeline from leaderboard
5. **Retrain with full data**: Final model using all data
6. **Save**: `joblib.dump()` to `best_solar_model.pkl`

### Model Performance
- **Target**: Merged Glo (Wh/m²)
- **Algorithms**: XGBoost, Random Forest, GLM, Deep Learning (H2O AutoML selection)
- **Evaluation**: MSE, RMSE, MAE metrics

## 🚀 Installation

### Requirements
- Python 3.8 or higher
- pip (Python package manager)
- Docker (optional, for container deployment)
- H2O cluster (for model training, `10.1.234.150:54321`)

### Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/TugayTalha/Solar_Irradiation-Production_Forecasting_Access_AI.git
   cd Solar_Irradiation-Production_Forecasting_Access_AI
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # or
   venv\Scripts\activate     # Windows
   ```

3. **Install requirements:**
   ```bash
   pip install -r requirements.txt
   ```

4. **H2O Cluster (for model training):**
   - If you don't have your own H2O cluster:
   ```python
   import h2o
   h2o.init()  # Local startup
   ```
   - Or use the cluster at `10.1.234.150:54321`

## 💡 Usage

### A. Retraining the Model (For Developers)

```bash
python preprocess_train.py
# or
jupyter notebook preprocess_train.ipynb
```

This process:
- Loads TMY3 data
- Selects the best model with H2O AutoML
- Creates `best_solar_model.pkl` and `scaler.pkl` files

### B. Running the Flask API

#### 1. Local Execution
```bash
python app.py
# API starts at http://0.0.0.0:5000
```

#### 2. Docker Execution (Recommended)
```bash
docker-compose up --build
# Flask app runs inside container
```

### C. API Usage

#### Endpoint: `/predict_energy`
**Method**: POST  
**Content-Type**: application/json

**Request Example:**
```json
{
  "latitude": 40.7128,
  "longitude": -74.0060,
  "kwh_price": 0.15,
  "panel_wattage": 400
}
```
OR
```json
{
  "latitude": 40.7128,
  "longitude": -74.0060,
  "kwh_price": 0.15,
  "panel_area": 10,
  "panel_efficiency": 0.20
}
```

**Fields:**
| Field | Type | Description | Required |
|-------|------|-------------|----------|
| latitude | float | Latitude (-90 to 90) | Yes |
| longitude | float | Longitude (-180 to 180) | Yes |
| kwh_price | float | Electricity price per kWh ($) | Yes |
| panel_wattage | float | Panel power (Watts) | * |
| panel_area | float | Panel area (m²) | ** |
| panel_efficiency | float | Panel efficiency (0.0-1.0) | ** |

*Either send `panel_wattage` OR `panel_area + panel_efficiency` pair.

**Response Example:**
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

**Response Fields:**
| Field | Type | Description |
|-------|------|-------------|
| monthly_energy_output_kWh | float | Monthly energy production (kWh) |
| yearly_energy_output_kWh | float | Yearly energy production (kWh) |
| monthly_profit | int | Monthly profit ($) |
| yearly_profit | int | Yearly profit ($) |
| break_even_month | int | Payback period (months) |
| break_even_year | float | Payback period (years) |
| chart | string | Base64 encoded PNG chart |

## 📊 Financial Calculation Logic

### Panel Cost
```python
if coeff <= 0.1:       # Small system
    inverter_price = 100
elif coeff <= 0.3:     # Medium system
    inverter_price = 1300
elif coeff <= 1:        # Large system
    inverter_price = 1800
else:                    # Industrial
    inverter_price = 6000

panel_price = coeff * 13000 + (1500 if coeff > 0.1 else 0) + inverter_price
```

### Energy Production
```
energy_output = (panel_wattage / 1000) × (irradiation / 1000)
# OR
energy_output = (panel_area × panel_efficiency) × (irradiation / 1000)
```

### Profit Calculation
```
monthly_profit = energy_output × kwh_price
yearly_profit = monthly_profit × 12
```

### Payback Period (Break-Even)
Monthly profits are accumulated until they exceed the panel price.

## 📈 Sample Output Chart

The `chart` field in the API response contains this graph:
- **X-axis**: Years (current year + 30 years)
- **Y-axis**: Cumulative profit ($)
- **Blue line**: Cumulative profit
- **Orange line**: Panel cost (fixed)

The graph visualizes when the investment pays for itself.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Contribution Areas
- Integration of more ML models (Prophet, LSTM, Transformer)
- Real-time data integration with weather APIs
- Mobile app development (React Native / Flutter)
- Advanced financial analysis (inflation, tax incentives)
- Panel soiling and degradation calculation
- Multi-panel array optimization

## 📄 License

This project is licensed under the **Apache License 2.0**. You can find the license text in the [LICENSE](LICENSE) file.

## 📧 Contact

**Tugay Talha İçen**
- GitHub: [@Tugaytalha](https://github.com/Tugaytalha)
- Twitter: [@TugayTalhaIcen](https://twitter.com/TugayTalhaIcen)
- LinkedIn: [Tugay Talha İçen](https://linkedin.com/in/tugaytalhaicen)

**Project Link**: [https://github.com/TugayTalha/Solar_Irradiation-Production_Forecasting_Access_AI](https://github.com/TugayTalha/Solar_Irradiation-Production_Forecasting_Access_AI)

## 🙏 Acknowledgments

- To **NREL (National Renewable Energy Laboratory)** for providing TMY3 data
- To **H2O.ai** team for the automated ML infrastructure
- To **Open-Meteo** for the free API service
- To **XGBoost** developers for the powerful gradient boosting algorithm

---

☀️ **A cleaner future with renewable energy!**

⭐ Don't forget to star this project if you found it useful!

🐛 Use the [Issues](https://github.com/TugayTalha/Solar_Irradiation-Production_Forecasting_Access_AI/issues) tab for bug reports or suggestions.
