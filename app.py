import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import time

st.set_page_config(page_title="Agri-Digitalization & Audit Trust", layout="wide")

st.title("Serverless Agri-Digitalization Pipeline")
st.caption("Real-Time Carbon Disclosure & Blockchain Audit Trust Verification Engine")

st.sidebar.header("Middleware Configuration")
selected_region = st.sidebar.selectbox("Select Agricultural Region", ["Southeast Asia (Palm Oil)", "Sub-Saharan Africa (Maize)", "New Zealand (Dairy)"])
audit_interval = st.sidebar.slider("Blockchain Hashing Interval (ms)", 100, 1000, 500)
run_simulation = st.sidebar.button("Initialize FinTech Middleware")

st.sidebar.markdown("---")
st.sidebar.caption("Architecture: AWS Lambda -> Data Normalization -> SHA-256 Ledger Anchor")

if run_simulation:
    st.subheader(f"Active Monitoring Node: {selected_region}")
    
    col1, col2, col3, col4 = st.columns(4)
    metric_emissions = col1.empty()
    metric_yield = col2.empty()
    metric_hash = col3.empty()
    metric_trust = col4.empty()

    chart_placeholder = st.empty()
    log_placeholder = st.empty()

    np.random.seed(101)
    time_steps = pd.date_range(start=pd.Timestamp.now(), periods=100, freq="s")
    
    carbon_values = []
    trust_scores = []
    
    base_carbon = 120.5
    
    for i in range(100):
        if i < 30:
            current_carbon = base_carbon + np.random.uniform(-2.0, 2.0)
            current_trust = np.random.uniform(98.0, 100.0)
        elif i >= 30 and i < 60:
            current_carbon = base_carbon + (i - 30) * 1.5 + np.random.uniform(-5.0, 5.0)
            current_trust = np.random.uniform(90.0, 95.0)
        else:
            current_carbon = base_carbon + 45.0 + np.random.uniform(-3.0, 3.0)
            current_trust = np.random.uniform(99.0, 100.0) 
            
        carbon_values.append(current_carbon)
        trust_scores.append(current_trust)
        
        simulated_hash = f"0x{np.random.bytes(4).hex()}...{np.random.bytes(2).hex()}"
        
        metric_emissions.metric("Carbon Intensity (kg CO2e)", f"{current_carbon:.1f}", f"{(current_carbon - base_carbon):.1f}")
        metric_yield.metric("Logistics Throughput", f"{int(np.random.uniform(1000, 5000))} MT")
        metric_hash.metric("Latest Ledger Hash", simulated_hash)
        
        if current_trust < 95.0:
            metric_trust.metric("Audit Trust Score", f"{current_trust:.1f}%", "Data Variance Detected")
        else:
            metric_trust.metric("Audit Trust Score", f"{current_trust:.1f}%", "Verified on Blockchain")
            
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=time_steps[:i+1], y=carbon_values, mode='lines', name='Carbon Intensity', line=dict(color='green')))
        fig.add_trace(go.Scatter(x=time_steps[:i+1], y=trust_scores, mode='lines', name='Audit Trust Score', yaxis='y2', line=dict(color='purple', dash='dot')))
        
        fig.update_layout(
            title="Real-Time Supply Chain Carbon Tracking vs Audit Trust",
            xaxis=dict(title="Timestamp"),
            yaxis=dict(title="Carbon Intensity (kg CO2e)"),
            yaxis2=dict(title="Trust Score (%)", overlaying='y', side='right', range=[80, 100]),
            height=400,
            margin=dict(l=0, r=0, t=40, b=0)
        )
        
        chart_placeholder.plotly_chart(fig, use_container_width=True)
        
        if current_trust < 95.0:
            log_placeholder.warning(f"AUDIT WARNING: Discrepancy detected in regional carbon reporting at {time_steps[i].strftime('%H:%M:%S')}. Hash reconciliation pending.")
        else:
            log_placeholder.success(f"Log: Node {i} data verified. SHA-256 hash successfully anchored to decentralized ledger.")
            
        time.sleep(audit_interval / 1000.0)
        
    st.info("Simulation Complete. FinTech middleware successfully bridged agricultural sensors with blockchain audit layers.")
else:
    st.info("Click 'Initialize FinTech Middleware' in the sidebar to simulate live data ingestion.")