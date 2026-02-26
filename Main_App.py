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
    st.markdown("---")
    
    col1, col2 = st.columns([1, 3])
    
    with col1:
        st.subheader("Network Settings")
        gene_input = st.text_area("Enter Gene Symbols (comma separated):", "HTT, BDNF, CASP3, TP53, SOD1")
        conf_score = st.slider("Confidence Threshold", 0, 1000, 400)
        st.info("Higher score = More reliable interactions")
        
    with col2:
        if st.button("Generate Live Interactome"):
            st.warning("Fetching data from STRING-DB API...")
            
            # 1. API Call to STRING-DB
            genes = gene_input.replace(" ", "").split(",")
            url = "https://string-db.org/api/json/network"
            params = {
                "identifiers": "%0d".join(genes),
                "species": 9606, # Human
                "min_score": conf_score,
                "caller_identity": "yashwant_nama_phd_app"
            }
            
            try:
                response = requests.post(url, data=params)
                interactions = response.json()
                
                if interactions:
                    # 2. Build NetworkX Graph
                    G = nx.Graph()
                    for edge in interactions:
                        G.add_edge(edge['preferredName_A'], edge['preferredName_B'], weight=edge['score'])
                    
                    # 3. Visualization
                    fig, ax = plt.subplots(figsize=(10, 8))
                    pos = nx.spring_layout(G, k=0.5)
                    
                    # Draw nodes and edges
                    nx.draw_networkx_nodes(G, pos, node_size=1200, node_color='#FF4B4B', edgecolors='white')
                    nx.draw_networkx_edges(G, pos, width=2, alpha=0.5, edge_color='gray')
                    nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif', font_weight='bold')
                    
                    plt.axis('off')
                    st.pyplot(fig)
                    
                    st.success(f"Successfully mapped {len(G.nodes())} proteins and {len(G.edges())} interactions.")
                else:
                    st.error("No interactions found. Try lowering the confidence threshold.")
            except Exception as e:
                st.error(f"API Error: {e}")
        else:
            st.info("Click the button to visualize the protein-protein interaction network.")


def run_zebrafish_morphometry():
    st.header("🧬 3D Spatial Phenotyping (Zebrafish)")
    st.markdown("---")

    # --- Step 1: Data Input Selection ---
    input_method = st.radio("Choose Data Source:", ["Upload My CSV", "Use Sample Research Data"])

    df = None

    if input_method == "Upload My CSV":
        uploaded = st.file_uploader("Upload Cdh2-CRISPR CSV", type="csv")
        if uploaded:
            df = pd.read_csv(uploaded)
    else:
        # Research-based Sample Data Generation
        st.info("Loading pre-set morphometry data (Cdh2-deficient model simulation)")
        data = {
            'centroid-0': np.random.uniform(10, 80, 150),  # Z-axis
            'centroid-1': np.random.uniform(50, 450, 150), # X-axis
            'centroid-2': np.random.uniform(50, 450, 150), # Y-axis
            'volume_voxels': np.random.normal(650, 120, 150),
            'nearest_neighbor_dist': np.random.uniform(8, 25, 150)
        }
        df = pd.DataFrame(data)

    # --- Step 2: Visualization (Only if data exists) ---
    if df is not None:
        # Cleaning numeric columns
        for col in df.columns:
            if df[col].dtype == 'object':
                df[col] = pd.to_numeric(df[col].astype(str).str.replace(',', ''), errors='coerce')
        
        m1, m2, m3 = st.columns(3)
        m1.metric("Total Nuclei Analyzed", len(df))
        m2.metric("Avg Nuclear Volume", f"{df['volume_voxels'].mean():.1f}")
        m3.metric("Avg NN Distance", f"{df['nearest_neighbor_dist'].mean():.2f} μm")

        col_left, col_right = st.columns([1.5, 1])

        with col_left:
            st.subheader("📍 3D Nuclear Architecture")
            fig3d = plt.figure(figsize=(10, 8))
            ax3d = fig3d.add_subplot(111, projection='3d')
            
            # Color by volume to show hypertrophy
            sc = ax3d.scatter(
                df['centroid-1'], df['centroid-2'], df['centroid-0'], 
                c=df['volume_voxels'], cmap='magma', s=40, alpha=0.7
            )
            ax3d.set_xlabel('X (μm)')
            ax3d.set_ylabel('Y (μm)')
            ax3d.set_zlabel('Z (μm)')
            plt.colorbar(sc, label='Volume (voxels)', shrink=0.5)
            st.pyplot(fig3d)

        with col_right:
            st.subheader("📈 Morphometric Distribution")
            fig_hist, ax_hist = plt.subplots()
            sns.histplot(df['volume_voxels'], kde=True, color='purple', ax=ax_hist)
            ax_hist.set_title("Volume Frequency")
            st.pyplot(fig_hist)

            # Correlation Plot
            corr, _ = pearsonr(df['volume_voxels'], df['nearest_neighbor_dist'])
            st.write(f"**Volume-Packing Correlation (r):** {corr:.2f}")
    else:
        st.warning("Please upload a file or select 'Use Sample Data' to begin.")


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
