import streamlit as st
import pandas as pd

from utils import plot_boxplot, plot_bar, top_regions

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

# --- Title ---
st.title("Solar Radiation Comparison Dashboard") 

st.info("No data available yet — please upload or connect a data source.")

uploaded_file = st.file_uploader("Upload Solar Data CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    
    st.markdown("Interactive visualization of solar energy potential across Benin, Togo, and Sierraleone.")

    # --- Boxplot ---
    st.subheader(f"{metric} (W/m²) Distribution by Country")
    plt_box = plot_boxplot(df, metric, countries)
    st.pyplot(plt_box)

    # --- Bar Chart ---
    st.subheader(f"Average {metric} (W/m²) by Country")
    plt_bar = plot_bar(df, metric, countries)
    st.pyplot(plt_bar)

    # --- Top Regions Table ---
    st.subheader(f"Top Regions — Average {metric} (W/m²) by Country")
    st.table(top_regions(df, metric, countries))

else:
    st.warning("Waiting for data upload...")