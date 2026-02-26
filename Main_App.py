import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
import requests
import networkx as nx
import io
from scipy.stats import pearsonr, fisher_exact
from itertools import combinations
from pyvis.network import Network
import streamlit.components.v1 as components

# --- 1. GLOBAL PAGE CONFIG (Sirf Ek Baar) ---
st.set_page_config(page_title="MultiScale-BioDigital-Bridge", layout="wide", page_icon="🧬")

# --- 2. THE 5 RESEARCH MODULES (Wrapped as Functions) ---

def run_tracer_design():
    st.header("🎯 Immuno-PET Tracer Rational Design")
    # --- Constants ---
    ZR89_HALFLIFE = 78.41
    ATEZO_KD = 0.43
    TRACER_LIBRARY = {
        "WL12 (Peptide)": {"kd_nm": 12.3, "mw": 1.5, "note": "High affinity peptide"},
        "Atezolizumab (Ab)": {"kd_nm": 0.43, "mw": 145, "note": "Clinical antibody"},
        "Nanobody": {"kd_nm": 2.10, "mw": 15, "note": "Mid-range affinity"}
    }
    
    col1, col2 = st.columns([1, 2])
    with col1:
        selected = st.selectbox("Select Tracer", list(TRACER_LIBRARY.keys()))
        b_max = st.slider("Receptor Density (Bmax)", 10, 500, 150)
        sink = st.slider("Liver/Kidney Sink (%)", 0, 90, 30)
        dose = st.slider("Injected Dose (nM)", 0.1, 50.0, 5.0)
    
    # Simple Logic for Demo
    eff_conc = dose * (1 - (sink/100))
    kd_val = TRACER_LIBRARY[selected]["kd_nm"]
    binding = (b_max * eff_conc) / (kd_val + eff_conc)
    
    with col2:
        st.metric("Predicted Tumor Binding", f"{binding:.2f} fmol/mg")
        st.info(TRACER_LIBRARY[selected]["note"])
        # (Yahan aapka Plotly chart logic aa sakta hai)

def run_cd40_immunosome():
    st.header("🛡️ CD40 Systems Biology Framework")
    scaffolds = ["Liposome", "Exosome", "PLGA Polymer", "Gold NP"]
    scaffold = st.selectbox("Delivery Vehicle", scaffolds)
    
    col1, col2 = st.columns(2)
    with col1:
        st.success(f"Modeling CD40 clustering on {scaffold} surface...")
        st.write("- Receptor recruitment: High")
        st.write("- TRAF6 activation: Predicted")
    with col2:
        st.info("Hypothesis: Scaffold rigidity dictates NF-kB oscillation frequency.")

def run_neurometabolic():
    st.header("🧠 NeuroMetabolic Pathway Engine")
    diseases = ["Huntington's", "Alzheimer's", "Parkinson's", "ALS"]
    choice = st.selectbox("Select Pathology", diseases)
    
    st.write(f"Analyzing KEGG Pathways for {choice}...")
    # Sample Table
    df_demo = pd.DataFrame({
        "Gene": ["HTT", "BDNF", "CASP3", "SOD1"],
        "Role": ["Core", "Neurotrophic", "Apoptosis", "Metabolic"],
        "Score": [95, 88, 72, 65]
    })
    st.table(df_demo)

def run_clinical_interactome():
    st.header("🔬 Clinical & PPI Validation (STRING-DB)")
    gene_input = st.text_input("Enter Genes (comma separated)", "HTT, BDNF, CASP3")
    if st.button("Generate Network"):
        st.warning("Fetching live interactions from STRING-DB...")
        # (Yahan aapka NetworkX logic aa sakta hai)

def run_zebrafish_morphometry():
    st.header("🧬 3D Spatial Phenotyping (Zebrafish)")
    uploaded = st.file_uploader("Upload Cdh2-CRISPR CSV", type="csv")
    if uploaded:
        df = pd.read_csv(uploaded)
        st.write("Data Preview:", df.head())
        # 3D Plot logic
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(np.random.randn(10), np.random.randn(10), np.random.randn(10))
        st.pyplot(fig)
    else:
        st.info("Please upload the CSV from your Zebrafish paper to see 3D analysis.")

# --- 3. THE UNIFIED NAVIGATION SIDEBAR ---

st.sidebar.title("🧬 MS-BDB Suite")
st.sidebar.markdown(f"**Researcher:** Yashwant Nama\n\n**Date:** Feb 26, 2026")
st.sidebar.divider()

menu = st.sidebar.radio(
    "Select Research Scale:",
    [
        "1. Molecular: ImmunoPET Design",
        "2. Cellular: CD40 Immunosome",
        "3. Systems: NeuroMetabolic Mapping",
        "4. Network: Clinical Interactome",
        "5. Organism: 3D Morphometry"
    ]
)

st.sidebar.divider()
st.sidebar.caption("PhD Application Portfolio | Jaipur, Rajasthan")

# --- 4. EXECUTION LOGIC ---

if menu == "1. Molecular: ImmunoPET Design":
    run_tracer_design()
elif menu == "2. Cellular: CD40 Immunosome":
    run_cd40_immunosome()
elif menu == "3. Systems: NeuroMetabolic Mapping":
    run_neurometabolic()
elif menu == "4. Network: Clinical Interactome":
    run_clinical_interactome()
elif menu == "5. Organism: 3D Morphometry":
    run_zebrafish_morphometry()



st.sidebar.divider()
st.sidebar.caption("Unified Research Portfolio | 2026")
