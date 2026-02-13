# Airline Delay Analysis Dashboard 🛫📊

A comprehensive data visualization project analyzing airline flight delays with interactive charts and insights.

## 🎯 Project Overview

This project provides in-depth analysis of airline delays through:
- **Data Generation**: Realistic airline delay dataset with 5,000+ flight records
- **Statistical Analysis**: Key metrics and insights about delays
- **Interactive Visualizations**: 7 different charts using Plotly
- **Modern Dashboard**: Beautiful web interface with glassmorphism design

## ✨ Features

### Visualizations
1. **Delay Distribution** - Histogram showing delay frequency
2. **Airline Comparison** - Average delays across different airlines
3. **Hourly Analysis** - Delays by time of day
4. **Delay Reasons** - Breakdown of why flights get delayed
5. **Delay Categories** - Flight counts by severity
6. **Monthly Trends** - Seasonal patterns in delays
7. **Top Delayed Routes** - Most problematic flight paths

### Key Metrics
- Total flights analyzed
- Average delay time
- On-time percentage
- Severe delay rate
- Best/worst performing airlines
- Peak delay times

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Install Python dependencies**
```bash
pip install -r requirements.txt
```

### Running the Project

2. **Generate the dataset**
```bash
python generate_data.py
```
This creates `airline_delays.csv` with 5,000 flight records.

3. **Create visualizations**
```bash
python visualization.py
```
This generates all charts in the `charts/` folder.

4. **View the dashboard**
Open `index.html` in your web browser:
- Double-click the file, or
- Right-click and select "Open with" → your browser
- Or use Python's built-in server:
```bash
python -m http.server 8000
```
Then visit: http://localhost:8000

## 📁 Project Structure

```
airlinedelayanalysiseda/
├── generate_data.py         # Dataset generation script
├── visualization.py          # Chart creation script
├── index.html               # Main dashboard
├── styles.css               # Styling and animations
├── script.js                # Interactive features
├── requirements.txt         # Python dependencies
├── README.md               # This file
├── airline_delays.csv      # Generated dataset
└── charts/                 # Generated visualizations
    ├── delay_distribution.html
    ├── airline_comparison.html
    ├── hourly_delays.html
    ├── delay_reasons.html
    ├── delay_categories.html
    ├── monthly_trends.html
    ├── top_delayed_routes.html
    └── stats.json
```

## 📊 Dataset Information

The generated dataset includes:
- **5,000 flights** across 8 major airlines
- **24 major US airports**
- **Full year** of data (2024)
- **Realistic delay patterns** based on common factors

### Data Fields
- Flight number & airline
- Origin & destination airports
- Scheduled vs actual departure times
- Delay duration (minutes)
- Delay category (On Time, Minor, Moderate, Severe)
- Delay reason (Weather, Aircraft Issue, etc.)
- Date, time, and other temporal data

## 🎨 Design Features

- **Dark Mode**: Easy on the eyes with a modern dark theme
- **Glassmorphism**: Frosted glass effect on cards
- **Smooth Animations**: Hover effects and transitions
- **Responsive Design**: Works on desktop, tablet, and mobile
- **Interactive Charts**: Zoom, pan, and explore the data
- **Modern Typography**: Clean, professional font (Inter)

## 🔧 Technologies Used

- **Python**: Data processing and analysis
  - pandas: Data manipulation
  - numpy: Numerical operations
  - plotly: Interactive visualizations
- **HTML5**: Structure
- **CSS3**: Modern styling with animations
- **JavaScript**: Interactivity and dynamic updates

## 📈 Key Findings

After running the analysis, you'll discover insights such as:
- Which airlines have the best on-time performance
- What times of day experience the most delays
- Common reasons for flight delays
- Seasonal patterns in delay frequency
- Most problematic flight routes

## 🛠️ Customization

### Modify Dataset Size
Edit `generate_data.py`:
```python
NUM_FLIGHTS = 5000  # Change this number
```

### Add More Airlines/Airports
Edit the `AIRLINES` and `AIRPORTS` lists in `generate_data.py`

### Change Color Scheme
Edit the CSS variables in `styles.css`:
```css
:root {
    --color-primary: #6366f1;
    --color-accent: #ec4899;
    /* ...modify other colors... */
}
```

## 📝 License

This project is open source and available for educational purposes.

## 👤 Author

Created as a data visualization project demonstrating:
- Python data analysis skills
- Interactive visualization techniques
- Modern web development practices
- UI/UX design principles

---

**Enjoy exploring the data! ✈️📊**
