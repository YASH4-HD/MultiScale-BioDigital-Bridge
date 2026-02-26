import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Bio-Digital Bridge v1.0", layout="wide", page_icon="🔬")

# --- CUSTOM CSS FOR PROFESSIONAL LOOK ---
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stSidebar { background-color: #1e3c72; color: white; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("🧬 BDB Suite")
st.sidebar.markdown("Applicant: **Yashwant Nama**")
st.sidebar.divider()

menu = st.sidebar.radio(
    "Select Research Scale:",
    [
        "1. Molecular: ImmunoPET Design",
        "2. Cellular: CD40 Immunosome",
        "3. Systems: NeuroMetabolic Mapping",
        "4. Network: Clinical Interactome",
        "5. Organism: 3D Morphometry (Zebrafish)"
    ]
)

# --- LOGIC TO CALL YOUR EXISTING SCRIPTS ---
if menu == "1. Molecular: ImmunoPET Design":
    # Yahan aapka Tracer Optimizer wala code aayega
    st.header("🎯 Tracer Rational Design")
    # (Pasted Code 5 logic)

elif menu == "2. Cellular: CD40 Immunosome":
    # Yahan CD40 Framework wala code
    st.header("🛡️ CD40 Signaling Module")
    # (Pasted Code 1 logic)

elif menu == "3. Systems: NeuroMetabolic Mapping":
    # NeuroMetabolic Framework
    st.header("🧠 Metabolic Pathway Engine")
    # (Pasted Code 2 logic)

elif menu == "4. Network: Clinical Interactome":
    # Clinical Validation Code
    st.header("🔬 Clinical & PPI Validation")
    # (Pasted Code 3 logic)

elif menu == "5. Organism: 3D Morphometry (Zebrafish)":
    # Zebrafish Morphometry Code
    st.header("🧬 3D Spatial Phenotyping")
    # (Pasted Code 4 logic)

st.sidebar.divider()
st.sidebar.caption("Unified Research Portfolio | 2026")
