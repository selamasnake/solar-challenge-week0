import streamlit as st
from utils import load_data, plot_boxplot, plot_bar, top_regions

# --- Sidebar Controls ---
st.sidebar.header("Filters")
countries = st.sidebar.multiselect(
    "Select countries",
    options=['Benin', 'Togo', 'Sierra Leone'],
    default=['Benin', 'Togo', 'Sierra Leone']
)

metric = st.sidebar.selectbox(
    "Select metric",
    options=['GHI', 'DNI', 'DHI']
)

top_n = st.sidebar.slider(
    "Number of top regions to show",
    min_value=5, max_value=5, value=10, step=1
)

# --- Load Data ---
data_path = "data/cleaned/all_cleaned.csv"  
df = load_data(data_path)

# --- Title ---
st.title("MoonLight Solar Investment Dashboard")
st.markdown("Interactive visualization of solar energy potential across Benin, Togo, and Sierraleone.")

# --- Boxplot ---
st.subheader(f"{metric} Distribution by Country")
plt_box = plot_boxplot(df, metric, countries)
st.pyplot(plt_box)

# --- Bar Chart ---
st.subheader(f"Average {metric} by Country")
plt_bar = plot_bar(df, metric, countries)
st.pyplot(plt_bar)

# --- Top Regions Table ---
st.subheader(f"Average {metric} by Country")
st.table(top_regions(df, metric, countries))

