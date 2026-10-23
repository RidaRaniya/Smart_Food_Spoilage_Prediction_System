import streamlit as st
import pandas as pd
import joblib
from datetime import datetime

# =========================================================
# 1. PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="FreshGuard AI",
    page_icon="🥬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# 2. CUSTOM UI
# =========================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root {
    color-scheme: light;
}

.stApp,
[data-testid="stAppViewContainer"],
[data-testid="stMain"] {
    background: #F5F8F5 !important;
    color: #1B3025 !important;
    font-family: 'Inter', sans-serif !important;
}

[data-testid="stMainBlockContainer"] {
    max-width: 1450px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Hide default Streamlit decoration */

#MainMenu, footer {
    visibility: hidden;
}

header[data-testid="stHeader"] {
    background: transparent;
}

/* Default text colors */

.stApp p,
.stApp label,
.stApp li,
.stApp small,
.stApp h1,
.stApp h2,
.stApp h3,
.stApp h4,
.stApp span {
    color: #1B3025;
}

.stApp h1,
.stApp h2,
.stApp h3,
.stApp h4 {
    font-weight: 750;
}

/* Sidebar */

[data-testid="stSidebar"] {
    background: #12372A !important;
    border-right: 1px solid #214C3A;
}

[data-testid="stSidebar"] * {
    color: #FFFFFF !important;
}

[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
    color: #E1EFE5 !important;
}

[data-testid="stSidebar"] hr {
    border-color: #355A48;
}

[data-testid="stSidebar"] div[role="radiogroup"] label {
    background: transparent;
    border-radius: 9px;
    padding: 8px 10px;
}

[data-testid="stSidebar"] div[role="radiogroup"] label:hover {
    background: #214C3A;
}

/* Brand */

.brand-box {
    padding: 15px 0 18px 0;
}

.brand-icon {
    font-size: 35px;
}

.brand-name {
    color: #FFFFFF !important;
    font-size: 24px;
    font-weight: 800;
    letter-spacing: -0.7px;
}

.brand-caption {
    color: #B7D6C2 !important;
    font-size: 12px;
    margin-top: 5px;
}

/* Hero */

.hero {
    background: linear-gradient(120deg, #12372A 0%, #176B48 60%, #239665 100%);
    padding: 30px 32px;
    border-radius: 20px;
    margin-bottom: 25px;
    box-shadow: 0 8px 24px rgba(18, 55, 42, 0.12);
}

.hero-eyebrow {
    color: #C7F4D7 !important;
    font-size: 12px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 2px;
}

.hero-title {
    color: #FFFFFF !important;
    font-size: 34px;
    line-height: 1.25;
    font-weight: 800;
    margin: 10px 0;
}

.hero-description {
    color: #E5F4E9 !important;
    font-size: 14px;
    line-height: 1.7;
    max-width: 750px;
}

/* Section heading */

.section-heading {
    color: #12372A !important;
    font-size: 22px;
    font-weight: 800;
    margin: 26px 0 14px 0;
}

.section-subtitle {
    color: #68796E !important;
    font-size: 13px;
    margin-top: -8px;
    margin-bottom: 18px;
}

/* Metrics */

.metric-card {
    background: #FFFFFF;
    border: 1px solid #E1EAE3;
    border-radius: 16px;
    padding: 22px;
    min-height: 145px;
    box-shadow: 0 3px 12px rgba(21, 53, 37, 0.035);
}

.metric-top {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 8px;
}

.metric-label {
    color: #65766A !important;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 0.4px;
}

.metric-icon {
    background: #E9F5EC;
    padding: 8px;
    border-radius: 10px;
    font-size: 19px;
}

.metric-value {
    color: #12372A !important;
    font-size: 34px;
    font-weight: 800;
    margin-top: 13px;
}

.metric-note {
    color: #75847A !important;
    font-size: 12px;
    margin-top: 5px;
}

/* White content cards */

.panel {
    background: #FFFFFF;
    border: 1px solid #E1EAE3;
    border-radius: 16px;
    padding: 23px;
    margin-bottom: 16px;
}

.panel-title {
    color: #12372A !important;
    font-size: 17px;
    font-weight: 750;
    margin-bottom: 8px;
}

.panel-description {
    color: #697A6F !important;
    font-size: 13px;
    line-height: 1.65;
}

/* Input fields */

.stApp input,
.stApp textarea,
[data-testid="stNumberInput"] input {
    background: #FFFFFF !important;
    color: #172B22 !important;
    -webkit-text-fill-color: #172B22 !important;
    border-color: #CFDDD2 !important;
}

[data-testid="stSelectbox"] div[data-baseweb="select"] > div {
    background: #FFFFFF !important;
    border-color: #CFDDD2 !important;
}

[data-testid="stSelectbox"] div[data-baseweb="select"] *,
[data-testid="stMultiSelect"] div[data-baseweb="select"] * {
    color: #172B22 !important;
    -webkit-text-fill-color: #172B22 !important;
}

div[data-baseweb="popover"],
div[data-baseweb="menu"] {
    background: #FFFFFF !important;
}

li[role="option"] {
    background: #FFFFFF !important;
    color: #172B22 !important;
}

li[role="option"] * {
    color: #172B22 !important;
}

[data-testid="stWidgetLabel"] p,
[data-testid="stCaptionContainer"] p {
    color: #344B3C !important;
}

[data-testid="stForm"] {
    background: #FFFFFF;
    border: 1px solid #E1EAE3;
    border-radius: 16px;
    padding: 22px;
}

/* Buttons */

.stButton > button,
[data-testid="stFormSubmitButton"] button {
    background: #198754 !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 10px !important;
    font-weight: 700 !important;
    min-height: 45px;
    transition: 0.2s ease;
}

.stButton > button *,
[data-testid="stFormSubmitButton"] button * {
    color: #FFFFFF !important;
    -webkit-text-fill-color: #FFFFFF !important;
}

.stButton > button:hover,
[data-testid="stFormSubmitButton"] button:hover {
    background: #146C43 !important;
    box-shadow: 0 4px 12px rgba(25, 135, 84, 0.18);
}

[data-testid="stDownloadButton"] button {
    background: #12372A !important;
    color: #FFFFFF !important;
    border-radius: 10px !important;
}

[data-testid="stDownloadButton"] button * {
    color: #FFFFFF !important;
}

/* Prediction result */

.result-card {
    padding: 27px;
    border-radius: 17px;
    margin: 18px 0;
}

.fresh-result {
    background: #E8F7ED;
    border: 1px solid #B9E5C8;
    border-left: 7px solid #198754;
}

.spoiled-result {
    background: #FFF0ED;
    border: 1px solid #F4D0CB;
    border-left: 7px solid #D64545;
}

.result-label {
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 1.2px;
    margin-bottom: 9px;
}

.fresh-result .result-label,
.fresh-result .result-title {
    color: #146C43 !important;
}

.spoiled-result .result-label,
.spoiled-result .result-title {
    color: #B42332 !important;
}

.result-title {
    font-size: 27px;
    font-weight: 800;
    margin-bottom: 8px;
}

.result-description {
    color: #37483D !important;
    font-size: 14px;
    line-height: 1.7;
}

/* Data tables */

[data-testid="stDataFrame"],
[data-testid="stTable"] {
    background: #FFFFFF !important;
}

/* Tabs */

[data-testid="stTabs"] button {
    color: #26392D !important;
}

/* Alerts */

[data-testid="stAlert"] p {
    color: #26392D !important;
}

/* Footer */

.app-footer {
    margin-top: 40px;
    padding: 20px;
    text-align: center;
    border-top: 1px solid #DDE7DF;
    color: #68796E !important;
    font-size: 12px;
    line-height: 1.8;
}

.app-footer strong {
    color: #12372A !important;
}

/* Mobile */

@media (max-width: 768px) {
    .hero {
        padding: 23px;
    }

    .hero-title {
        font-size: 26px;
    }

    .metric-value {
        font-size: 27px;
    }
}
</style>
""", unsafe_allow_html=True)


# =========================================================
# 3. LOAD TRAINED MODEL
# =========================================================

@st.cache_resource
def load_model():
    return joblib.load("food_spoilage_model.pkl")


try:
    model = load_model()
except FileNotFoundError:
    st.error(
        "Model file not found. Put food_spoilage_model.pkl "
        "in the same folder as app.py."
    )
    st.stop()
except Exception as error:
    st.error(f"Could not load model: {error}")
    st.stop()


# =========================================================
# 4. SESSION STATE
# =========================================================

if "prediction_history" not in st.session_state:
    st.session_state.prediction_history = []


# =========================================================
# 5. SIDEBAR
# =========================================================

with st.sidebar:
    st.markdown("""
    <div class="brand-box">
        <div class="brand-icon">🥬</div>
        <div class="brand-name">FreshGuard AI</div>
        <div class="brand-caption">SMART FOOD CONDITION ASSISTANT</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    page = st.radio(
        "MAIN MENU",
        [
            "Dashboard",
            "Food Analysis",
            "Prediction History",
            "About Project"
        ],
        label_visibility="visible"
    )

    st.markdown("---")

    st.markdown("### 🤖 Model Overview")
    st.write("**Algorithm:** Random Forest")
    st.write("**Model type:** Classification")
    st.write("**Inputs:** 5 features")

    st.markdown("---")
    st.caption("FreshGuard AI · ML Project")


# =========================================================
# 6. HELPER FUNCTIONS
# =========================================================

def metric_card(icon, label, value, note):
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-top">
                <div class="metric-label">{label}</div>
                <div class="metric-icon">{icon}</div>
            </div>
            <div class="metric-value">{value}</div>
            <div class="metric-note">{note}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


def section_heading(title, subtitle=None):
    st.markdown(
        f'<div class="section-heading">{title}</div>',
        unsafe_allow_html=True
    )

    if subtitle:
        st.markdown(
            f'<div class="section-subtitle">{subtitle}</div>',
            unsafe_allow_html=True
        )


def get_prediction_label(prediction):
    """
    Existing model mapping:
    Good = 0
    Bad = 1

    Fresh-class and Spoiled-class are display labels only.
    Verify the dataset's original label meaning before
    claiming these are verified freshness predictions.
    """
    if prediction == 0:
        return "Fresh-class", "Fresh-class Prediction"

    if prediction == 1:
        return "Spoiled-class", "Spoiled-class Prediction"

    return str(prediction), f"Model Class: {prediction}"


# =========================================================
# 7. HEADER
# =========================================================

st.markdown("""
<div class="hero">
    <div class="hero-eyebrow">AI-POWERED FOOD MONITORING</div>
    <div class="hero-title">FreshGuard AI Dashboard</div>
    <div class="hero-description">
        Analyze fruit-related environmental conditions using
        Machine Learning. Explore predictions, review your
        history, and visualize classification results.
    </div>
</div>
""", unsafe_allow_html=True)


# =========================================================
# 8. HISTORY DATA
# =========================================================

history_df = pd.DataFrame(
    st.session_state.prediction_history
)

total_predictions = len(history_df)

if total_predictions:
    fresh_count = int(
        (history_df["Prediction"] == "Fresh-class").sum()
    )
    spoiled_count = int(
        (history_df["Prediction"] == "Spoiled-class").sum()
    )
else:
    fresh_count = 0
    spoiled_count = 0


# =========================================================
# 9. DASHBOARD PAGE
# =========================================================

if page == "Dashboard":

    section_heading(
        "Dashboard Overview",
        "Your food-condition prediction activity at a glance."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        metric_card(
            "📊",
            "TOTAL PREDICTIONS",
            total_predictions,
            "Current session"
        )

    with col2:
        metric_card(
            "🌿",
            "FRESH-CLASS",
            fresh_count,
            "Predicted as Fresh-class"
        )

    with col3:
        metric_card(
            "⚠️",
            "SPOILED-CLASS",
            spoiled_count,
            "Predicted as Spoiled-class"
        )

    section_heading(
        "Prediction Analytics",
        "Visual summary of predictions made in this session."
    )

    if total_predictions > 0:

        chart_col, summary_col = st.columns([1.3, 1])

        with chart_col:
            st.markdown("""
            <div class="panel">
                <div class="panel-title">Prediction Distribution</div>
                <div class="panel-description">
                    Number of predictions in each displayed class.
                </div>
            </div>
            """, unsafe_allow_html=True)

            chart_data = pd.DataFrame({
                "Class": ["Fresh-class", "Spoiled-class"],
                "Predictions": [fresh_count, spoiled_count]
            }).set_index("Class")

            st.bar_chart(chart_data)

        with summary_col:
            st.markdown("""
            <div class="panel">
                <div class="panel-title">Class Summary</div>
                <div class="panel-description">
                    Breakdown of the current prediction history.
                </div>
            </div>
            """, unsafe_allow_html=True)

            summary = pd.DataFrame({
                "Prediction Class": ["Fresh-class", "Spoiled-class"],
                "Count": [fresh_count, spoiled_count],
                "Percentage": [
                    f"{fresh_count / total_predictions * 100:.1f}%",
                    f"{spoiled_count / total_predictions * 100:.1f}%"
                ]
            })

            st.dataframe(
                summary,
                use_container_width=True,
                hide_index=True
            )

        section_heading("Recent Activity")

        st.dataframe(
            history_df.tail(5).iloc[::-1],
            use_container_width=True,
            hide_index=True
        )

    else:
        st.markdown("""
        <div class="panel">
            <div class="panel-title">👋 Welcome to FreshGuard AI</div>
            <div class="panel-description">
                You have not made any predictions yet. Start by opening
                Food Analysis in the sidebar and entering the fruit's
                environmental measurements.
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("🔬 Go to Food Analysis"):
            st.session_state.go_to_analysis = True
            st.rerun()

    section_heading("How It Works")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="panel">
            <div style="font-size:30px">🍎</div>
            <div class="panel-title">01. Enter Measurements</div>
            <div class="panel-description">
                Select the fruit and enter temperature, humidity,
                light intensity, and CO₂ readings.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="panel">
            <div style="font-size:30px">🧠</div>
            <div class="panel-title">02. Run the Model</div>
            <div class="panel-description">
                The trained Random Forest model predicts the
                dataset class associated with your measurements.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="panel">
            <div style="font-size:30px">📈</div>
            <div class="panel-title">03. Review Results</div>
            <div class="panel-description">
                Explore your results, review prediction history,
                and export records for further analysis.
            </div>
        </div>
        """, unsafe_allow_html=True)


# =========================================================
# 10. FOOD ANALYSIS PAGE
# =========================================================

elif page == "Food Analysis":

    section_heading(
        "Food Condition Analysis",
        "Enter environmental readings to generate a model prediction."
    )

    st.markdown("""
    <div class="panel">
        <div class="panel-title">🍎 Food Information</div>
        <div class="panel-description">
            Select the fruit you want to analyze.
        </div>
    </div>
    """, unsafe_allow_html=True)

    with st.form("food_analysis_form"):

        fruit = st.selectbox(
            "Fruit Type",
            ["Banana", "Orange", "Pineapple", "Tomato"]
        )

        st.markdown("#### 🌡️ Environmental Measurements")

        col1, col2 = st.columns(2)

        with col1:
            temperature = st.number_input(
                "Temperature (°C)",
                min_value=-20.0,
                max_value=60.0,
                value=24.0,
                step=0.5,
                help="Measured environmental temperature."
            )

            humidity = st.number_input(
                "Humidity (%)",
                min_value=0.0,
                max_value=100.0,
                value=90.0,
                step=1.0,
                help="Relative humidity as a percentage."
            )

        with col2:
            light = st.number_input(
                "Light Intensity (lux)",
                min_value=0.0,
                max_value=10000.0,
                value=10.0,
                step=1.0,
                help="Measured light intensity."
            )

            co2 = st.number_input(
                "CO₂ Level (ppm)",
                min_value=0.0,
                max_value=10000.0,
                value=320.0,
                step=1.0,
                help="Measured CO₂ concentration."
            )

        submitted = st.form_submit_button(
            "🔍 Analyze Food Condition",
            use_container_width=True
        )

    if submitted:

        input_df = pd.DataFrame([{
            "Fruit": fruit,
            "Temp": temperature,
            "Humid (%)": humidity,
            "Light (Fux)": light,
            "CO2 (pmm)": co2
        }])

        try:
            prediction = model.predict(input_df)[0]

            result, display_label = get_prediction_label(prediction)

            probability = None

            if hasattr(model, "predict_proba"):
                probabilities = model.predict_proba(input_df)[0]
                classes = list(model.classes_)

                if prediction in classes:
                    probability = float(
                        probabilities[classes.index(prediction)]
                    ) * 100

            if result == "Fresh-class":

                st.markdown("""
                <div class="result-card fresh-result">
                    <div class="result-label">MODEL PREDICTION</div>
                    <div class="result-title">🌿 Fresh-class</div>
                    <div class="result-description">
                        The model assigned this input to the original
                        Good class in the training dataset.
                    </div>
                </div>
                """, unsafe_allow_html=True)

            elif result == "Spoiled-class":

                st.markdown("""
                <div class="result-card spoiled-result">
                    <div class="result-label">MODEL PREDICTION</div>
                    <div class="result-title">⚠️ Spoiled-class</div>
                    <div class="result-description">
                        The model assigned this input to the original
                        Bad class in the training dataset.
                    </div>
                </div>
                """, unsafe_allow_html=True)

            else:
                st.info(display_label)

            if probability is not None:
                st.markdown("#### Model Output")

                st.progress(
                    min(max(int(round(probability)), 0), 100)
                )

                st.metric(
                    "Estimated probability of the predicted class",
                    f"{probability:.2f}%"
                )

                st.caption(
                    "This is the model's estimated class probability, "
                    "not a percentage measure of freshness or food safety."
                )

            warnings = []

            if not 21 <= temperature <= 27:
                warnings.append(
                    "Temperature is outside the observed training "
                    "range of 21–27°C."
                )

            if not 71 <= humidity <= 95:
                warnings.append(
                    "Humidity is outside the observed training "
                    "range of 71–95%."
                )

            if not 4.22 <= light <= 268.45:
                warnings.append(
                    "Light intensity is outside the observed training "
                    "range of approximately 4.22–268.45 lux."
                )

            if not 20 <= co2 <= 478:
                warnings.append(
                    "CO₂ is outside the observed training "
                    "range of 20–478 ppm."
                )

            if warnings:
                st.warning(
                    "Some measurements are outside the ranges "
                    "observed in the training dataset."
                )

                for warning in warnings:
                    st.write(f"• {warning}")

            record = {
                "Date & Time": datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),
                "Fruit": fruit,
                "Temperature (°C)": temperature,
                "Humidity (%)": humidity,
                "Light (lux)": light,
                "CO2 (ppm)": co2,
                "Prediction": result,
                "Model Probability (%)": (
                    round(probability, 2)
                    if probability is not None
                    else None
                )
            }

            st.session_state.prediction_history.append(record)

            st.success("Prediction added to your session history.")

            st.info(
                "Dataset limitation: Fresh-class and Spoiled-class "
                "are display labels for the original Good and Bad "
                "classes. Their relationship to verified food freshness "
                "or spoilage has not yet been established."
            )

        except Exception as error:
            st.error(
                "Prediction failed. Verify that your model uses the "
                "expected feature names and input format."
            )
            st.exception(error)

    st.markdown("---")

    st.warning(
        "This project is not a validated food-safety test. Do not "
        "use its predictions alone to decide whether food is safe "
        "to eat."
    )


# =========================================================
# 11. PREDICTION HISTORY
# =========================================================

elif page == "Prediction History":

    section_heading(
        "Prediction History",
        "Review and export predictions recorded during this session."
    )

    if not history_df.empty:

        search = st.text_input(
            "🔎 Search by fruit or prediction class",
            placeholder="Example: Banana or Fresh-class"
        )

        filtered_df = history_df.copy()

        if search.strip():
            mask = (
                filtered_df.astype(str)
                .apply(
                    lambda column: column.str.contains(
                        search.strip(),
                        case=False,
                        na=False
                    )
                )
                .any(axis=1)
            )

            filtered_df = filtered_df[mask]

        st.dataframe(
            filtered_df.iloc[::-1],
            use_container_width=True,
            hide_index=True
        )

        csv_data = filtered_df.to_csv(
            index=False
        ).encode("utf-8")

        st.download_button(
            "⬇️ Download CSV",
            data=csv_data,
            file_name="food_prediction_history.csv",
            mime="text/csv",
            use_container_width=True
        )

        st.markdown("")

        if st.button("🗑️ Clear All History"):
            st.session_state.prediction_history = []
            st.rerun()

    else:
        st.info(
            "No predictions have been recorded. Go to Food Analysis "
            "to make your first prediction."
        )


# =========================================================
# 12. ABOUT PROJECT
# =========================================================

elif page == "About Project":

    section_heading(
        "About FreshGuard AI",
        "Project overview, algorithm, features, and limitations."
    )

    st.markdown("""
    <div class="panel">
        <div class="panel-title">🥬 Smart Food Spoilage Prediction System</div>
        <div class="panel-description">
            This machine-learning project classifies fruit-related
            environmental measurements using a trained Random Forest
            model.
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="panel">
            <div class="panel-title">🧠 Algorithm</div>
            <div class="panel-description">
                Random Forest combines predictions from multiple
                decision trees to perform classification.
            </div>
            <br>
            <div class="panel-title">📥 Input Features</div>
            <div class="panel-description">
                • Fruit type<br>
                • Temperature<br>
                • Humidity<br>
                • Light intensity<br>
                • CO₂ concentration
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="panel">
            <div class="panel-title">🎯 Model Output</div>
            <div class="panel-description">
                The model predicts the original Good or Bad class.
                This app displays these classes as Fresh-class and
                Spoiled-class for readability.
            </div>
            <br>
            <div class="panel-title">⚠️ Important Limitation</div>
            <div class="panel-description">
                The dataset labels have not been verified as confirmed
                freshness or spoilage measurements. Predictions are
                not proof that food is fresh, spoiled, or safe to eat.
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("#### Why Random Forest?")

    st.write(
        "Random Forest can learn relationships between multiple input "
        "features and class labels. Its actual performance depends on "
        "the quality, representativeness, and meaning of the training data."
    )


# =========================================================
# 13. FOOTER
# =========================================================

st.markdown("""
<div class="app-footer">
    <strong>🥬 FreshGuard AI</strong><br>
    Smart Food Spoilage Prediction System<br>
    Machine Learning Project
</div>
""", unsafe_allow_html=True)
