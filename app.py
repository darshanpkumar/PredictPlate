import joblib
import pandas as pd
import streamlit as st

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="PredictPlate — Delivery Prediction",
    page_icon="🛵",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@400;500;600;700;800&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,400&display=swap');

/* ── Global ── */
html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background-color: #FAF7F2;
    color: #1A1A1A;
    font-size: 16px;
}

.stApp { background-color: #FAF7F2; }

#MainMenu, footer, header { visibility: hidden; }

/* ── Hero ── */
.hero {
    background: #1B4332;
    border-radius: 20px;
    padding: 2.8rem 2.5rem 2.5rem;
    margin-bottom: 2rem;
    position: relative;
    overflow: hidden;
}

.hero::after {
    content: '🛵';
    position: absolute;
    right: 2rem;
    top: 50%;
    transform: translateY(-50%);
    font-size: 5rem;
    opacity: 0.12;
}

.hero-eyebrow {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    background: rgba(255,255,255,0.1);
    border: 1px solid rgba(255,255,255,0.2);
    color: #95D5B2;
    font-family: 'Sora', sans-serif;
    font-size: 0.78rem;
    font-weight: 600;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    padding: 0.35rem 1rem;
    border-radius: 100px;
    margin-bottom: 1.2rem;
}

.hero h1 {
    font-family: 'Sora', sans-serif;
    font-size: 2.8rem;
    font-weight: 800;
    color: #FFFFFF;
    margin: 0 0 0.6rem 0;
    line-height: 1.1;
}

.hero h1 em {
    font-style: normal;
    color: #95D5B2;
}

.hero p {
    color: rgba(255,255,255,0.6);
    font-size: 1.05rem;
    font-weight: 300;
    margin: 0;
    max-width: 480px;
}

/* ── Section Headers ── */
.sect-head {
    font-family: 'Sora', sans-serif;
    font-size: 0.8rem;
    font-weight: 700;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #1B4332;
    border-left: 3px solid #1B4332;
    padding-left: 0.6rem;
    margin: 1.4rem 0 0.8rem 0;
}

/* ── INPUT VISIBILITY & CONTRAST FIXES ── */

/* 1. Labels */
div[data-testid="stWidgetLabel"], 
div[data-testid="stWidgetLabel"] * {
    color: #2D3748 !important;
    -webkit-text-fill-color: #2D3748 !important;
    font-weight: 600 !important;
    font-size: 0.92rem !important;
}

/* 2. Selectbox Field & Dropdown Text */
div[data-testid="stSelectbox"] div[data-baseweb="select"] {
    background-color: #F5F1EB !important;
    border: 1.5px solid #DDD6CC !important;
    border-radius: 10px !important;
}

div[data-testid="stSelectbox"] div[data-baseweb="select"] * {
    color: #1A1A1A !important;
    -webkit-text-fill-color: #1A1A1A !important;
    font-weight: 600 !important;
}

/* Dropdown Menu Popup Items */
ul[data-baseweb="menu"] li,
ul[data-baseweb="menu"] li * {
    color: #1A1A1A !important;
    -webkit-text-fill-color: #1A1A1A !important;
    background-color: #FFFFFF !important;
}

/* 3. Number Input Text & Controls */
div[data-testid="stNumberInput"] input {
    background-color: #F5F1EB !important;
    border: 1.5px solid #DDD6CC !important;
    border-radius: 10px !important;
    color: #1A1A1A !important;
    -webkit-text-fill-color: #1A1A1A !important;
    font-weight: 600 !important;
    font-size: 1rem !important;
}

div[data-testid="stNumberInput"] button {
    background-color: #1B4332 !important;
    border: none !important;
    border-radius: 8px !important;
}

div[data-testid="stNumberInput"] button * {
    color: #FFFFFF !important;
    -webkit-text-fill-color: #FFFFFF !important;
}

/* ── Predict Button ── */
.stButton > button {
    width: 100%;
    background: #E85D4A !important;
    color: #FFFFFF !important;
    -webkit-text-fill-color: #FFFFFF !important;
    font-family: 'Sora', sans-serif !important;
    font-weight: 700 !important;
    font-size: 1rem !important;
    letter-spacing: 0.02em;
    border: none !important;
    border-radius: 12px !important;
    padding: 0.85rem 1.5rem !important;
    transition: all 0.18s ease !important;
    box-shadow: 0 4px 16px rgba(232,93,74,0.3) !important;
    margin-top: 1rem;
}

.stButton > button:hover {
    background: #D44A38 !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 24px rgba(232,93,74,0.4) !important;
}

/* ── Result Section Header ── */
.results-header {
    font-family: 'Sora', sans-serif;
    font-size: 1.15rem;
    font-weight: 700;
    color: #1A1A1A;
    margin-bottom: 1.2rem;
    display: flex;
    align-items: center;
    gap: 0.6rem;
}

.results-header::before {
    content: '';
    width: 4px;
    height: 1.2rem;
    background: #1B4332;
    border-radius: 2px;
    display: inline-block;
}

/* ── Result Cards (Mobile Responsive Grid) ── */
.result-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1rem;
    margin-bottom: 1.25rem;
}

@media (max-width: 768px) {
    .result-grid {
        grid-template-columns: 1fr;
    }
}

.result-card {
    background: #FFFFFF;
    border: 1.5px solid #E8E0D5;
    border-radius: 16px;
    padding: 1.5rem 1.2rem 1.4rem;
    text-align: center;
    box-shadow: 0 2px 12px rgba(0,0,0,0.05);
    transition: box-shadow 0.2s;
}

.result-card:hover { box-shadow: 0 4px 20px rgba(0,0,0,0.09); }

.card-icon { font-size: 1.6rem; margin-bottom: 0.5rem; }

.card-label {
    font-size: 0.78rem;
    font-weight: 600;
    letter-spacing: 0.09em;
    text-transform: uppercase;
    color: #999;
    margin-bottom: 0.6rem;
}

.card-value {
    font-family: 'Sora', sans-serif;
    font-size: 2rem;
    font-weight: 800;
    line-height: 1;
    color: #1A1A1A;
}

.card-value.green-val { color: #1B4332; }
.card-value.red-val   { color: #E85D4A; }
.card-value.slate-val { color: #4A6FA5; }

.card-unit {
    font-size: 1rem;
    font-weight: 400;
    color: #AAA;
}

/* ── Confidence Bar ── */
.conf-track {
    background: #F0EDE8;
    border-radius: 999px;
    height: 7px;
    margin-top: 0.75rem;
    overflow: hidden;
}
.conf-fill {
    height: 100%;
    border-radius: 999px;
    background: linear-gradient(90deg, #1B4332, #52B788);
}

/* ── Status Banner ── */
.status-banner {
    border-radius: 14px;
    padding: 1.1rem 1.5rem;
    display: flex;
    align-items: center;
    gap: 1rem;
    font-family: 'Sora', sans-serif;
    font-weight: 600;
    font-size: 1rem;
}

.status-banner.ontime {
    background: #D8F3DC;
    border: 1.5px solid #95D5B2;
    color: #1B4332;
}

.status-banner.late {
    background: #FDE8E5;
    border: 1.5px solid #F4A79D;
    color: #B83A2A;
}

.pulse-dot {
    width: 11px; height: 11px;
    border-radius: 50%;
    flex-shrink: 0;
    animation: pulse 2s infinite;
}
.pulse-dot.ontime { background: #2D9655; }
.pulse-dot.late   { background: #E85D4A; }

@keyframes pulse {
    0%, 100% { transform: scale(1); opacity: 1; }
    50%       { transform: scale(1.45); opacity: 0.55; }
}

/* ── Idle Placeholder ── */
.idle-wrap {
    background: #FFFFFF;
    border: 1.5px dashed #D6CECC;
    border-radius: 20px;
    padding: 3.5rem 2rem;
    text-align: center;
    margin: 1rem 0 2rem;
}

.idle-wrap .idle-emoji { font-size: 3.5rem; margin-bottom: 1rem; }

.idle-wrap p {
    font-size: 1.05rem;
    color: #888;
    margin: 0;
}

.idle-wrap strong { color: #E85D4A; }

/* ── Expander ── */
details, .streamlit-expanderHeader {
    background: #FFFFFF !important;
    border: 1.5px solid #E8E0D5 !important;
    border-radius: 12px !important;
    font-size: 0.95rem !important;
    color: #555 !important;
}

/* ── About Card ── */
.about-card {
    background: #FFFFFF;
    border: 1.5px solid #E8E0D5;
    border-radius: 16px;
    padding: 1.75rem;
    margin-top: 0.5rem;
}

.about-title {
    font-family: 'Sora', sans-serif;
    font-size: 1.05rem;
    font-weight: 700;
    color: #1A1A1A;
    margin-bottom: 0.75rem;
}

.about-card p {
    color: #555;
    font-size: 0.97rem;
    line-height: 1.75;
    margin-bottom: 1.1rem;
}

.pill {
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
    background: #F5F1EB;
    border: 1px solid #E0D9D0;
    border-radius: 100px;
    padding: 0.3rem 0.85rem;
    font-size: 0.85rem;
    color: #444;
    margin: 0.2rem 0.2rem 0.2rem 0;
    font-weight: 500;
}

/* ── Footer ── */
.footer {
    text-align: center;
    color: #BBB;
    font-size: 0.85rem;
    margin-top: 2.5rem;
    padding-top: 1.5rem;
    border-top: 1px solid #E8E0D5;
}

.footer strong { color: #1B4332; }

/* ── Divider ── */
hr { border-color: #E8E0D5 !important; }
</style>
""",
    unsafe_allow_html=True,
)

# -----------------------------
# Load Models
# -----------------------------
reg_model = joblib.load("model.pkl")
clf_model = joblib.load("classifier.pkl")

# -----------------------------
# Hero Section
# -----------------------------
st.markdown(
    """
<div class="hero">
    <div class="hero-eyebrow">🛵 ML-Powered Logistics</div>
    <h1>Predict<em>Plate</em></h1>
    <p>Estimate delivery time and predict on-time status — before the order leaves the kitchen.</p>
</div>
""",
    unsafe_allow_html=True,
)

# -----------------------------
# Form Inputs in Main Body
# -----------------------------
st.markdown('<div class="sect-head">📦 Order Details</div>', unsafe_allow_html=True)
col_ord1, col_ord2 = st.columns(2)
with col_ord1:
    distance = st.number_input(
        "Distance (km)", min_value=0.5, max_value=30.0, value=5.0, step=0.5
    )
with col_ord2:
    prep_time = st.number_input(
        "Preparation Time (min)", min_value=0, max_value=60, value=15
    )

st.markdown('<div class="sect-head">🧑 Courier</div>', unsafe_allow_html=True)
col_cour1, col_cour2 = st.columns(2)
with col_cour1:
    experience = st.number_input(
        "Experience (years)", min_value=0.0, max_value=20.0, value=2.0, step=0.5
    )
with col_cour2:
    vehicle = st.selectbox("Vehicle Type", ["Bike", "Car", "Scooter"])

st.markdown(
    '<div class="sect-head">🌦 Conditions</div>', unsafe_allow_html=True
)
col_cond1, col_cond2, col_cond3 = st.columns(3)
with col_cond1:
    weather = st.selectbox(
        "Weather", ["Clear", "Foggy", "Rainy", "Snowy", "Windy"]
    )
with col_cond2:
    traffic = st.selectbox("Traffic Level", ["High", "Medium", "Low"])
with col_cond3:
    time_day = st.selectbox(
        "Time of Day", ["Afternoon", "Morning", "Evening", "Night"]
    )

predict = st.button("🚀 Predict Now")

st.markdown("<br>", unsafe_allow_html=True)

# -----------------------------
# Prediction Processing & Results
# -----------------------------
if predict:
    input_data = pd.DataFrame(
        {
            "Distance_km": [distance],
            "Preparation_Time_min": [prep_time],
            "Courier_Experience_yrs": [experience],
            "Weather_Foggy": [1 if weather == "Foggy" else 0],
            "Weather_Rainy": [1 if weather == "Rainy" else 0],
            "Weather_Snowy": [1 if weather == "Snowy" else 0],
            "Weather_Windy": [1 if weather == "Windy" else 0],
            "Traffic_Level_Low": [1 if traffic == "Low" else 0],
            "Traffic_Level_Medium": [1 if traffic == "Medium" else 0],
            "Time_of_Day_Evening": [1 if time_day == "Evening" else 0],
            "Time_of_Day_Morning": [1 if time_day == "Morning" else 0],
            "Time_of_Day_Night": [1 if time_day == "Night" else 0],
            "Vehicle_Type_Car": [1 if vehicle == "Car" else 0],
            "Vehicle_Type_Scooter": [1 if vehicle == "Scooter" else 0],
        }
    )

    delivery_time = reg_model.predict(input_data)[0]
    prediction = clf_model.predict(input_data)[0]
    confidence = clf_model.predict_proba(input_data).max() * 100

    is_late = prediction == 1
    status_text = "Late" if is_late else "On-Time"
    status_class = "late" if is_late else "ontime"
    val_class = "red-val" if is_late else "green-val"
    status_icon = "⚠️" if is_late else "✅"
    status_msg = (
        "Conditions suggest this order may arrive late. Consider proactive communication."
        if is_late
        else "All conditions look good. This order should arrive on time."
    )

    st.markdown(
        '<div class="results-header">Prediction Results</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
    <div class="result-grid">
        <div class="result-card">
            <div class="card-icon">⏱️</div>
            <div class="card-label">Estimated Time</div>
            <div class="card-value slate-val">{delivery_time:.1f}<span class="card-unit"> min</span></div>
        </div>
        <div class="result-card">
            <div class="card-icon">🚦</div>
            <div class="card-label">Delivery Status</div>
            <div class="card-value {val_class}">{status_text}</div>
        </div>
        <div class="result-card">
            <div class="card-icon">🎯</div>
            <div class="card-label">Confidence</div>
            <div class="card-value green-val">{confidence:.0f}<span class="card-unit">%</span></div>
            <div class="conf-track"><div class="conf-fill" style="width:{confidence}%;"></div></div>
        </div>
    </div>

    <div class="status-banner {status_class}">
        <div class="pulse-dot {status_class}"></div>
        {status_icon} &nbsp;{status_msg}
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown("<br>", unsafe_allow_html=True)
    with st.expander("🔍 View Encoded Model Input"):
        st.dataframe(input_data, use_container_width=True)

else:
    st.markdown(
        """
    <div class="idle-wrap">
        <div class="idle-emoji">🛵</div>
        <p>Fill in the order details above and click <strong>Predict Now</strong> to see results.</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

# -----------------------------
# About Section
# -----------------------------
st.markdown(
    """
<div class="about-card">
    <div class="about-title">How It Works</div>
    <p>
        PredictPlate runs two machine learning models on every prediction:
        a <strong>Random Forest Regressor</strong> to estimate how many minutes the delivery will take,
        and a <strong>Random Forest Classifier</strong> to determine whether the order will arrive on time or late.
    </p>
    <div>
        <span class="pill">🌲 RF Regressor — Time Estimate</span>
        <span class="pill">🌲 RF Classifier — On-Time Status</span>
        <span class="pill">🐍 Python</span>
        <span class="pill">📐 Scikit-Learn</span>
        <span class="pill">📊 Pandas</span>
        <span class="pill">⚡ Streamlit</span>
    </div>
</div>
""",
    unsafe_allow_html=True,
)

# -----------------------------
# Footer
# -----------------------------
st.markdown(
    """
<div class="footer">
    Built by <strong>Darshan P Kumar</strong> &nbsp;·&nbsp; PredictPlate v2.0
</div>
""",
    unsafe_allow_html=True,
)
