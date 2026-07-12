import streamlit as st
import pandas as pd
from inferencing.predict_freight import predict_freight_cost
from inferencing.predict_invoice_flag import predict_invoice_flag 

# --- UI CONFIG ---
st.set_page_config(page_title="Vendor Intelligence Portal", layout="wide")

# --- CUSTOM CSS FOR "PERSIAN BLUE & DARK" THEME ---
st.markdown("""
    <style>
    /* Main Background */
    .stApp {
        background-color: #0E1117;
    }
    
    /* Header Styling */
    h1 {
        color: #1E90FF !important; 
        font-family: 'Segoe UI', sans-serif;
        font-weight: 700;
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #0A192F !important; /* Deep Persian Blue Night */
        border-right: 1px solid #1E90FF;
    }

    /* Button Glow Effect */
    div.stButton > button:first-child {
        background-color: #1E90FF;
        color: white;
        border-radius: 10px;
        border: none;
        box-shadow: 0 0 15px rgba(30, 144, 255, 0.4);
        transition: all 0.3s ease;
        width: 100%;
        font-weight: bold;
        height: 3em;
    }
    
    div.stButton > button:hover {
        box-shadow: 0 0 25px rgba(30, 144, 255, 0.8);
        transform: translateY(-2px);
        background-color: #2b65ec;
        color: white;
    }

    /* Metric Styling */
    [data-testid="stMetricValue"] {
        color: #1E90FF;
    }
    </style>
    """, unsafe_allow_html=True) # Fixed the argument name here

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.title("⚙️ Control Panel")
    app_mode = st.radio("Navigation", ["Freight Prediction", "Risk Analysis"])
    st.markdown("---")
    st.info("""
    **Intelligence Metrics:**
    * 🚀 Logistics Optimization
    * 🛡️ Fraud Guard AI
    * 📊 Financial Precision
    """)

# --- MAIN HEADER ---
st.title("🏢 Vendor Intelligence Portal")
st.markdown("#### *AI-powered decision support for finance and logistics.*")
st.divider()

# --- APP LOGIC ---

if app_mode == "Freight Prediction":
    st.subheader("📦 Forecast Freight Expenditure")
    col1, col2 = st.columns(2)
    with col1:
        quantity = st.number_input("Item Quantity", min_value=1, value=10)
    with col2:
        dollars = st.number_input("Invoice Total ($)", min_value=1.0, value=500.0)

    if st.button("✨ Calculate Expected Freight"):
        input_dict = {"Quantity": [quantity], "Dollars": [dollars]}
        result_df = predict_freight_cost(input_dict)
        
        if result_df is not None:
            prediction = result_df['Predicted_Freight'].iloc[0]
            st.metric(label="Calculated Freight Cost", value=f"${prediction:,.2f}")
            st.balloons()

elif app_mode == "Risk Analysis":
    st.subheader("🚩 Invoice Risk Profiler")
    col1, col2 = st.columns(2)
    with col1:
        inv_qty = st.number_input("Invoice Quantity", min_value=1, value=50)
        inv_dlrs = st.number_input("Invoice Dollars ($)", min_value=1.0, value=1200.0)
        freight = st.number_input("Freight Component ($)", min_value=0.0, value=45.0)
    
    with col2:
        item_qty = st.number_input("Total Item Quantity", min_value=1, value=50)
        item_dlrs = st.number_input("Total Item Dollars ($)", min_value=1.0, value=1195.0)
    
    st.markdown("---")
    if st.button("🔍 Run AI Risk Assessment"):
        input_risk = {
            "invoice_quantity": [inv_qty],
            "invoice_dollars": [inv_dlrs],
            "Freight": [freight],
            "total_item_quantity": [item_qty],
            "total_item_dollars": [item_dlrs]
        }
        
        risk_result = predict_invoice_flag(input_risk)
        
        if risk_result is not None:
            is_flagged = risk_result['Predicted_Flag'].iloc[0]
            
            if is_flagged == 1:
                st.error("🚨 **HIGH RISK**: Manual review required.")
            else:
                st.success("✅ **LOW RISK**: Invoice cleared for processing.")


















# import streamlit as st

# # ----------------------------------------------------------------------------
# # Page config
# # ----------------------------------------------------------------------------
# st.set_page_config(
#     page_title="Vendor Intelligence Portal",
#     page_icon="🏢",
#     layout="wide",
#     initial_sidebar_state="expanded",
# )

# # ----------------------------------------------------------------------------
# # Global styling
# # ----------------------------------------------------------------------------
# st.markdown(
#     """
#     <style>
#     /* ---- Keyframes ---- */
#     @keyframes fadeInUp {
#         0%   { opacity: 0; transform: translateY(14px); }
#         100% { opacity: 1; transform: translateY(0); }
#     }
#     @keyframes pulseGlow {
#         0%, 100% { box-shadow: 0 0 0 rgba(200, 200, 200, 0); }
#         50%      { box-shadow: 0 0 22px rgba(180, 180, 180, 0.18); }
#     }

#     /* ---- App background: neutral charcoal/slate ---- */
#     .stApp {
#         background: radial-gradient(circle at 20% 0%, #23252b 0%, #17181d 45%, #0d0e11 100%);
#     }

#     /* ---- Hide default streamlit chrome we don't need ---- */
#     #MainMenu, footer {visibility: hidden;}

#     /* ---- Sidebar ---- */
#     section[data-testid="stSidebar"] {
#         background: linear-gradient(180deg, #1c1d22 0%, #121317 100%);
#         border-right: 1px solid rgba(255, 255, 255, 0.06);
#     }
#     section[data-testid="stSidebar"] .block-container {
#         padding-top: 2rem;
#     }

#     /* ---- Hero header ---- */
#     .hero {
#         padding: 1.8rem 2.2rem;
#         border-radius: 18px;
#         background: linear-gradient(120deg, rgba(255, 255, 255, 0.05) 0%, rgba(255, 255, 255, 0.015) 100%);
#         border: 1px solid rgba(255, 255, 255, 0.1);
#         margin-bottom: 1.6rem;
#         animation: fadeInUp 0.5s ease-out;
#         transition: border-color 0.2s ease, box-shadow 0.2s ease;
#     }
#     .hero:hover {
#         border-color: rgba(255, 255, 255, 0.22);
#         box-shadow: 0 8px 30px rgba(0, 0, 0, 0.35);
#     }
#     .hero .eyebrow {
#         display: inline-block;
#         color: #9a9a9a;
#         font-size: 0.78rem;
#         font-weight: 700;
#         letter-spacing: 0.16em;
#         text-transform: uppercase;
#         margin-bottom: 0.5rem;
#     }
#     .hero h1 {
#         font-size: 2.5rem;
#         font-weight: 900;
#         letter-spacing: -0.01em;
#         margin: 0;
#         color: #f5f5f4;
#         text-shadow: 0 2px 24px rgba(255, 255, 255, 0.08);
#     }
#     .hero p {
#         color: #a8a8a8;
#         font-style: italic;
#         margin: 0.5rem 0 0 0;
#         font-size: 1.05rem;
#     }

#     /* ---- Section card ---- */
#     .card {
#         background: rgba(255, 255, 255, 0.03);
#         border: 1px solid rgba(255, 255, 255, 0.08);
#         border-radius: 16px;
#         padding: 1.6rem 1.8rem 1.8rem 1.8rem;
#         margin-bottom: 1.2rem;
#         animation: fadeInUp 0.6s ease-out;
#         transition: transform 0.18s ease, border-color 0.18s ease, box-shadow 0.18s ease;
#     }
#     .card:hover {
#         transform: translateY(-3px);
#         border-color: rgba(255, 255, 255, 0.2);
#         box-shadow: 0 12px 32px rgba(0, 0, 0, 0.4);
#     }
#     .card h3 {
#         margin-top: 0;
#         color: #f0f0ef;
#         font-size: 1.3rem;
#         font-weight: 700;
#     }

#     /* ---- Sidebar metrics box ---- */
#     .metric-box {
#         background: rgba(255, 255, 255, 0.035);
#         border: 1px solid rgba(255, 255, 255, 0.1);
#         border-radius: 14px;
#         padding: 1rem 1.1rem;
#         margin-top: 1.2rem;
#         transition: border-color 0.2s ease, background 0.2s ease;
#     }
#     .metric-box:hover {
#         border-color: rgba(255, 255, 255, 0.24);
#         background: rgba(255, 255, 255, 0.06);
#     }
#     .metric-box h4 {
#         color: #c9c9c9;
#         margin: 0 0 0.6rem 0;
#         font-size: 0.95rem;
#         text-transform: uppercase;
#         letter-spacing: 0.03em;
#         font-weight: 700;
#     }
#     .metric-box ul {
#         margin: 0;
#         padding-left: 1.1rem;
#         color: #d0d0d0;
#         font-size: 0.92rem;
#         line-height: 1.9;
#     }
#     .metric-box li {
#         transition: transform 0.15s ease, color 0.15s ease;
#     }
#     .metric-box li:hover {
#         transform: translateX(3px);
#         color: #ffffff;
#     }

#     /* ---- Nav radio (Freight Prediction / Risk Analysis) ---- */
#     div[role="radiogroup"] label {
#         background: rgba(255, 255, 255, 0.025);
#         border: 1px solid rgba(255, 255, 255, 0.08);
#         padding: 0.55rem 0.8rem;
#         border-radius: 10px;
#         margin-bottom: 0.4rem;
#         width: 100%;
#         transition: all 0.18s ease;
#     }
#     div[role="radiogroup"] label:hover {
#         border-color: rgba(255, 255, 255, 0.35);
#         background: rgba(255, 255, 255, 0.07);
#         transform: translateX(2px);
#     }

#     /* ---- Number inputs ---- */
#     div[data-testid="stNumberInput"] input {
#         background-color: rgba(255, 255, 255, 0.04) !important;
#         border: 1px solid rgba(255, 255, 255, 0.12) !important;
#         color: #f0f0f0 !important;
#         border-radius: 10px !important;
#         transition: border-color 0.18s ease, box-shadow 0.18s ease;
#     }
#     div[data-testid="stNumberInput"] input:hover {
#         border-color: rgba(255, 255, 255, 0.3) !important;
#     }
#     div[data-testid="stNumberInput"] input:focus {
#         border-color: rgba(255, 255, 255, 0.5) !important;
#         box-shadow: 0 0 0 3px rgba(255, 255, 255, 0.08) !important;
#     }
#     div[data-testid="stNumberInput"] label {
#         color: #b8b8b8 !important;
#         font-weight: 500;
#     }

#     /* ---- Primary action buttons ---- */
#     div[data-testid="stButton"] button {
#         background: linear-gradient(90deg, #4a4a4a, #6e6e6e, #4a4a4a);
#         background-size: 200% 100%;
#         color: #f5f5f5;
#         font-weight: 700;
#         border: 1px solid rgba(255, 255, 255, 0.15);
#         border-radius: 12px;
#         padding: 0.75rem 1rem;
#         width: 100%;
#         box-shadow: 0 6px 18px rgba(0, 0, 0, 0.35);
#         transition: transform 0.15s ease, box-shadow 0.15s ease, background-position 0.4s ease;
#     }
#     div[data-testid="stButton"] button:hover {
#         transform: translateY(-2px) scale(1.01);
#         box-shadow: 0 10px 26px rgba(0, 0, 0, 0.5);
#         background-position: 100% 0%;
#         border-color: rgba(255, 255, 255, 0.35);
#     }
#     div[data-testid="stButton"] button:active {
#         transform: translateY(0) scale(0.99);
#     }

#     /* ---- Result metric tiles ---- */
#     .result-tile {
#         background: linear-gradient(135deg, rgba(255, 255, 255, 0.07), rgba(255, 255, 255, 0.02));
#         border: 1px solid rgba(255, 255, 255, 0.16);
#         border-radius: 14px;
#         padding: 1.2rem 1.4rem;
#         text-align: center;
#         animation: fadeInUp 0.4s ease-out, pulseGlow 2.8s ease-in-out infinite;
#         transition: transform 0.18s ease;
#     }
#     .result-tile:hover {
#         transform: translateY(-2px);
#     }
#     .result-tile .label {
#         color: #ababab;
#         font-size: 0.85rem;
#         text-transform: uppercase;
#         letter-spacing: 0.04em;
#     }
#     .result-tile .value {
#         color: #ffffff;
#         font-size: 1.9rem;
#         font-weight: 800;
#         margin-top: 0.2rem;
#     }

#     .risk-safe {
#         background: linear-gradient(135deg, rgba(180, 190, 180, 0.14), rgba(180, 190, 180, 0.04));
#         border: 1px solid rgba(190, 200, 190, 0.35);
#         border-radius: 14px;
#         padding: 1.2rem 1.4rem;
#         color: #d9e6d9;
#         font-weight: 700;
#         font-size: 1.1rem;
#         animation: fadeInUp 0.4s ease-out;
#         transition: transform 0.18s ease;
#     }
#     .risk-safe:hover { transform: translateY(-2px); }

#     .risk-flagged {
#         background: linear-gradient(135deg, rgba(210, 190, 190, 0.16), rgba(210, 190, 190, 0.05));
#         border: 1px solid rgba(220, 190, 190, 0.4);
#         border-radius: 14px;
#         padding: 1.2rem 1.4rem;
#         color: #f0d9d9;
#         font-weight: 700;
#         font-size: 1.1rem;
#         animation: fadeInUp 0.4s ease-out;
#         transition: transform 0.18s ease;
#     }
#     .risk-flagged:hover { transform: translateY(-2px); }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# # ----------------------------------------------------------------------------
# # Sidebar
# # ----------------------------------------------------------------------------
# with st.sidebar:
#     st.markdown("### ⚙️ Control panel")
#     st.caption("Navigation")
#     page = st.radio(
#         "Navigation",
#         ["🚚 Freight prediction", "🚩 Risk analysis"],
#         label_visibility="collapsed",
#     )

#     st.markdown(
#         """
#         <div class="metric-box">
#             <h4>Intelligence metrics</h4>
#             <ul>
#                 <li>🚀 Logistics optimization</li>
#                 <li>🛡️ Fraud guard AI</li>
#                 <li>📊 Financial precision</li>
#             </ul>
#         </div>
#         """,
#         unsafe_allow_html=True,
#     )

# # ----------------------------------------------------------------------------
# # Hero header
# # ----------------------------------------------------------------------------
# st.markdown(
#     """
#     <div class="hero">
#         <span class="eyebrow">Project statement</span>
#         <h1>🏢 Vendor Intelligence Portal</h1>
#         <p>AI-powered decision support for finance and logistics.</p>
#     </div>
#     """,
#     unsafe_allow_html=True,
# )

# # ----------------------------------------------------------------------------
# # Page: Freight Prediction
# # ----------------------------------------------------------------------------
# if "Freight" in page:
#     st.markdown('<div class="card"><h3>📦 Forecast freight expenditure</h3>', unsafe_allow_html=True)

#     col1, col2 = st.columns(2)
#     with col1:
#         item_qty = st.number_input("Item quantity", min_value=0, value=10, step=1)
#     with col2:
#         invoice_total = st.number_input("Invoice total ($)", min_value=0.0, value=500.0, step=10.0, format="%.2f")

#     calculate = st.button("✨ Calculate expected freight")
#     st.markdown("</div>", unsafe_allow_html=True)

#     if calculate:
#         # Placeholder logic — swap in your trained regression model here.
#         predicted_freight = round(invoice_total * 0.09 + item_qty * 1.5, 2)
#         st.markdown(
#             f"""
#             <div class="result-tile">
#                 <div class="label">Predicted freight cost</div>
#                 <div class="value">${predicted_freight:,.2f}</div>
#             </div>
#             """,
#             unsafe_allow_html=True,
#         )

# # ----------------------------------------------------------------------------
# # Page: Risk Analysis
# # ----------------------------------------------------------------------------
# else:
#     st.markdown('<div class="card"><h3>🚩 Invoice risk profiler</h3>', unsafe_allow_html=True)

#     col1, col2 = st.columns(2)
#     with col1:
#         invoice_qty = st.number_input("Invoice quantity", min_value=0, value=50, step=1)
#         invoice_dollars = st.number_input("Invoice dollars ($)", min_value=0.0, value=1200.0, step=10.0, format="%.2f")
#     with col2:
#         total_item_qty = st.number_input("Total item quantity", min_value=0, value=50, step=1)
#         total_item_dollars = st.number_input("Total item dollars ($)", min_value=0.0, value=1195.0, step=10.0, format="%.2f")

#     freight_component = st.number_input("Freight component ($)", min_value=0.0, value=45.0, step=5.0, format="%.2f")

#     run_assessment = st.button("🔍 Run AI risk assessment")
#     st.markdown("</div>", unsafe_allow_html=True)

#     if run_assessment:
#         # Placeholder logic — swap in your trained classification model here.
#         discrepancy = abs(invoice_dollars - total_item_dollars)
#         is_risky = discrepancy > 0.05 * invoice_dollars

#         if is_risky:
#             st.markdown(
#                 '<div class="risk-flagged">⚠️ Flagged: this invoice shows an unusual cost discrepancy and warrants audit review.</div>',
#                 unsafe_allow_html=True,
#             )
#         else:
#             st.markdown(
#                 '<div class="risk-safe">✅ Low risk: this invoice falls within expected cost patterns.</div>',
#                 unsafe_allow_html=True,
#             )