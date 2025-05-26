# Forecast Engine

This `README.md` was created using my package [README_genie](https://github.com/browshanravan/README_genie).

An interactive Streamlit application for univariate time‐series forecasting using Facebook’s Prophet library. Upload your data, validate date formats and granularity, visualize historical trends, and generate future forecasts with customisable seasonality.

---

## Table of Contents

- [About This Project](#about-this-project)  
- [Project Description](#project-description)  
- [Features](#features)  
- [Getting Started](#getting-started)  
  - [Prerequisites](#prerequisites)  
  - [Installation](#installation)  
  - [Quick Start](#quick-start)  
- [Usage](#usage)  
  - [Data Upload & Validation](#data-upload--validation)  
  - [Historical Plot](#historical-plot)  
  - [Forecasting](#forecasting)  
- [Development](#development)  
  - [Dev Container](#dev-container)  
- [Project Structure](#project-structure)  
- [Contributing](#contributing)  
- [License](#license)  

---

## About This Project

This repository provides an end-to-end demonstration of univariate time-series forecasting:

- Built with **Streamlit** for interactive web UI  
- Powered by **Prophet** for robust seasonality modeling  
- Leverages **Pandas**, **NumPy**, **Altair** and **Matplotlib** for data processing and visualisation  

---

## Project Description

Forecast Engine guides users through:

1. **Uploading** a CSV containing a date column (in `DD-MM-YYYY` format) and a target variable.  
2. **Validating** date formats and detecting missing observations at the chosen granularity (daily/weekly/monthly/yearly).  
3. **Visualising** the cleaned time series with an interactive Altair line chart.  
4. **Specifying** the dominant seasonality period (e.g., 12 months) and the forecast horizon.  
5. **Fitting** a Prophet model with a custom seasonality component and **plotting** future predictions.  

Use cases include sales forecasting, web traffic prediction, energy demand planning, or any scenario with regular temporal cycles.

---

## Features

- Interactive file upload and column selection  
- Automatic date‐format checking and resampling  
- Missing‐data detection for chosen granularity  
- Exploratory Altair chart with zoom & tooltips  
- Custom seasonality addition to Prophet model  
- Future‐forecast plotting via Matplotlib  
- Configurable theme and upload limits via `.streamlit/config.toml`  

---

## Getting Started

### Prerequisites

- Python 3.10  
- [pip](https://pip.pypa.io/)  
- (Optional) [Conda](https://docs.conda.io/) for environment management  
- Docker & VS Code (for Dev Container setup)  

### Installation

1. Clone the repo:  
   ```bash
   git clone https://github.com/behzadrowshanravan/forecast_engine.git
   cd forecast_engine
   ```
2. Install dependencies via pip:  
   ```bash
   pip3 install -r requirements.txt
   ```

Alternatively, create a Conda environment:

```bash
conda create -n forecast_env python=3.10
conda activate forecast_env
pip install -r requirements.txt
```

### Quick Start

Run the helper script:

```bash
sh app.sh
```

Then open your browser at <http://localhost:8501>.

Or launch manually:

```bash
streamlit run main.py --server.port 8501
```

---

## Usage

### Data Upload & Validation

1. Click **Browse files** and select your CSV.  
2. Choose the **date column** (must be `DD-MM-YYYY`).  
3. Select the **target variable** column.  
4. Pick a **granularity** (daily/weekly/monthly/yearly).  
5. The app checks for missing data at that frequency—if none, the workflow continues.

### Historical Plot

- Click **Generate Data Plot** to render an interactive line chart of your time series.  
- Zoom, pan, and hover to inspect timestamps.

### Forecasting

1. Enter the approximate number of units (e.g., months) in one full seasonal cycle.  
2. Specify the number of future units to predict.  
3. Click **Generate Future Plot**.  
4. View the forecast with the historical cutoff marked by a vertical line.

---

## Development

Clone the repository and open in VS Code. A Dev Container is configured for instant setup.

### Dev Container

The `.devcontainer/` folder contains:

- **Dockerfile**: Base image with Python tooling  
- **devcontainer.json**: Mounts the workspace, installs Python 3.10  

To launch:

1. Install the **Remote – Containers** extension in VS Code.  
2. Reopen the folder in container.  
3. All dependencies will be available; run `sh app.sh` inside the container.

---

## Project Structure

```
forecast_engine/
├── .devcontainer/
│   ├── Dockerfile
│   └── devcontainer.json
├── .streamlit/
│   └── config.toml
├── forecast_engine/
│   └── src/
│       └── utils.py       # I/O, validation, and Prophet‐fitting functions
├── app.sh                 # Install & launch script
├── main.py                # Streamlit app entry point
├── requirements.txt
├── LICENSE
└── README.md
```

---

## Contributing

1. Fork the repository  
2. Create a feature branch (`git checkout -b feature/foo`)  
3. Commit your changes (`git commit -am 'Add foo'`)  
4. Push to the branch (`git push origin feature/foo`)  
5. Open a Pull Request  

Please ensure code is linted and includes docstrings where appropriate.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.