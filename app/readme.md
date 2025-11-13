## Solar Radiation Comparison Dashboard

A lightweight Streamlit dashboard for exploring and comparing solar radiation metrics (GHI, DNI, DHI) across Benin, Togo, and Sierra Leone.

### Features

- Upload cleaned solar data (CSV)
- View boxplots and bar charts by country
- See top regions by average solar potential
- Modular design with reusable utilities (`utils.py`)

### How to Use

You can use the dashboard either via the deployed version or locally.

**Deployed version:**  
Visit [https://week0-solar-data-discovery.streamlit.app/](https://week0-solar-data-discovery.streamlit.app/), upload your data, and explore the visualizations.

**Run locally:**

1. Navigate to the project directory:
   cd solar-challenge-week0/
2. Install dependencies:
   pip install -r requirements.txt
3. Run the Streamlit app:
   streamlit run app/main.py
4. Open your browser at http://localhost:8501
