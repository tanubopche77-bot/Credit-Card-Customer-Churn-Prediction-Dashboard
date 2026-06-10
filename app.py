# import streamlit as st
# import pickle
# import pandas as pd

# # =========================
# # Load Model
# # =========================
# with open("gaussian_nb_model.pkl", "rb") as f:
#     model = pickle.load(f)

# # =========================
# # Page Config
# # =========================
# st.set_page_config(
#     page_title="Credit Card Customer Churn Prediction",
#     page_icon="💳",
#     layout="wide"
# )

# # =========================
# # Custom CSS
# # =========================
# st.markdown("""
# <style>
# .main {
#     background-color: #f4f7fc;
# }

# .title {
#     text-align:center;
#     color:#0A66C2;
#     font-size:40px;
#     font-weight:bold;
# }

# .subtitle {
#     text-align:center;
#     color:gray;
#     font-size:18px;
#     margin-bottom:30px;
# }

# .stButton>button {
#     width:100%;
#     background:linear-gradient(90deg,#0A66C2,#00A8E8);
#     color:white;
#     border:none;
#     border-radius:12px;
#     height:55px;
#     font-size:20px;
#     font-weight:bold;
# }

# .stButton>button:hover{
#     background:linear-gradient(90deg,#004AAD,#0077B6);
# }

# .block-container{
#     padding-top:2rem;
# }

# div[data-baseweb="select"]{
#     border-radius:10px;
# }

# input{
#     border-radius:10px !important;
# }
# </style>
# """, unsafe_allow_html=True)

# # =========================
# # Header
# # =========================
# st.markdown(
#     '<p class="title">💳 Credit Card Customer Churn Prediction</p>',
#     unsafe_allow_html=True
# )

# st.markdown(
#     '<p class="subtitle">Predict whether a customer is likely to stay or leave the bank.</p>',
#     unsafe_allow_html=True
# )

# # =========================
# # Input Section
# # =========================
# col1, col2 = st.columns(2)

# with col1:

#     st.subheader("👤 Customer Information")

#     Customer_Age = st.number_input(
#         "Customer Age",
#         min_value=18,
#         max_value=100,
#         value=40
#     )

#     Gender = st.selectbox(
#         "Gender",
#         ["M", "F"]
#     )

#     Dependent_count = st.number_input(
#         "Dependent Count",
#         min_value=0,
#         max_value=10,
#         value=2
#     )

#     Education_Level = st.selectbox(
#         "Education Level",
#         [
#             "Uneducated",
#             "High School",
#             "College",
#             "Graduate",
#             "Post-Graduate",
#             "Doctorate",
#             "Unknown"
#         ]
#     )

#     Marital_Status = st.selectbox(
#         "Marital Status",
#         [
#             "Single",
#             "Married",
#             "Divorced",
#             "Unknown"
#         ]
#     )

#     Income_Category = st.selectbox(
#         "Income Category",
#         [
#             "Less than $40K",
#             "$40K - $60K",
#             "$60K - $80K",
#             "$80K - $120K",
#             "$120K +",
#             "Unknown"
#         ]
#     )

#     Card_Category = st.selectbox(
#         "Card Category",
#         [
#             "Blue",
#             "Silver",
#             "Gold",
#             "Platinum"
#         ]
#     )

#     Months_on_book = st.number_input(
#         "Months on Book",
#         min_value=1,
#         max_value=100,
#         value=36
#     )

#     Total_Relationship_Count = st.number_input(
#         "Total Relationship Count",
#         min_value=1,
#         max_value=10,
#         value=4
#     )

# with col2:

#     st.subheader("🏦 Banking Activity")

#     Months_Inactive_12_mon = st.number_input(
#         "Months Inactive (Last 12 Months)",
#         min_value=0,
#         max_value=12,
#         value=2
#     )

#     Contacts_Count_12_mon = st.number_input(
#         "Contacts Count (Last 12 Months)",
#         min_value=0,
#         max_value=10,
#         value=2
#     )

#     Credit_Limit = st.number_input(
#         "Credit Limit",
#         value=5000.0
#     )

#     Total_Revolving_Bal = st.number_input(
#         "Total Revolving Balance",
#         value=1000.0
#     )

#     Avg_Open_To_Buy = st.number_input(
#         "Average Open To Buy",
#         value=4000.0
#     )

#     Total_Amt_Chng_Q4_Q1 = st.number_input(
#         "Amount Change Q4-Q1",
#         value=1.0
#     )

#     Total_Trans_Amt = st.number_input(
#         "Total Transaction Amount",
#         value=4000.0
#     )

#     Total_Trans_Ct = st.number_input(
#         "Total Transaction Count",
#         value=60
#     )

#     Total_Ct_Chng_Q4_Q1 = st.number_input(
#         "Count Change Q4-Q1",
#         value=1.0
#     )

#     Avg_Utilization_Ratio = st.number_input(
#         "Utilization Ratio",
#         min_value=0.0,
#         max_value=1.0,
#         value=0.30
#     )

# # =========================
# # Prediction
# # =========================
# st.markdown("---")

# if st.button("🔍 Predict Customer Churn"):

#     input_data = pd.DataFrame([{
#         "Customer_Age": Customer_Age,
#         "Gender": Gender,
#         "Dependent_count": Dependent_count,
#         "Education_Level": Education_Level,
#         "Marital_Status": Marital_Status,
#         "Income_Category": Income_Category,
#         "Card_Category": Card_Category,
#         "Months_on_book": Months_on_book,
#         "Total_Relationship_Count": Total_Relationship_Count,
#         "Months_Inactive_12_mon": Months_Inactive_12_mon,
#         "Contacts_Count_12_mon": Contacts_Count_12_mon,
#         "Credit_Limit": Credit_Limit,
#         "Total_Revolving_Bal": Total_Revolving_Bal,
#         "Avg_Open_To_Buy": Avg_Open_To_Buy,
#         "Total_Amt_Chng_Q4_Q1": Total_Amt_Chng_Q4_Q1,
#         "Total_Trans_Amt": Total_Trans_Amt,
#         "Total_Trans_Ct": Total_Trans_Ct,
#         "Total_Ct_Chng_Q4_Q1": Total_Ct_Chng_Q4_Q1,
#         "Avg_Utilization_Ratio": Avg_Utilization_Ratio
#     }])

#     prediction = model.predict(input_data)

#     st.markdown("## 📊 Prediction Result")

#     if prediction[0] == 1:
#         st.error(
#             "⚠️ High Churn Risk\n\nCustomer is likely to leave the bank."
#         )
#     else:
#         st.success(
#             "✅ Customer Retention Likely\n\nCustomer is likely to stay with the bank."
#         )

# st.markdown("---")
# st.caption("Developed using Streamlit & Gaussian Naive Bayes")








import streamlit as st
import pickle
import pandas as pd

# ==========================================
# PAGE CONFIG
# ==========================================
st.set_page_config(
    page_title="Credit Card Customer Churn Prediction",
    page_icon="💳",
    layout="wide"
)

# ==========================================
# LOAD MODEL
# ==========================================
with open("gaussian_nb_model.pkl", "rb") as f:
    model = pickle.load(f)

# ==========================================
# CUSTOM CSS
# ==========================================
st.markdown("""
<style>

[data-testid="stAppViewContainer"]{
background: linear-gradient(135deg,#0f172a,#1e3a8a,#2563eb);
}

.main{
color:white;
}

h1,h2,h3,h4,h5,h6,p,label{
color:white !important;
}

.stNumberInput label,
.stSelectbox label{
color:white !important;
font-weight:bold;
}

.stButton>button{
width:100%;
height:60px;
font-size:20px;
font-weight:bold;
border-radius:15px;
background:linear-gradient(90deg,#06b6d4,#3b82f6);
color:white;
border:none;
}

.stButton>button:hover{
transform:scale(1.02);
transition:0.3s;
}

.metric-card{
background:rgba(255,255,255,0.12);
padding:20px;
border-radius:18px;
text-align:center;
backdrop-filter:blur(8px);
box-shadow:0 4px 15px rgba(0,0,0,0.3);
}

.input-box{
background:rgba(255,255,255,0.08);
padding:20px;
border-radius:20px;
margin-bottom:15px;
}

.footer{
text-align:center;
color:white;
padding:20px;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# SIDEBAR
# ==========================================
with st.sidebar:

    st.title("🏦 Banking Dashboard")

    st.success("✅ Model Loaded Successfully")

    st.markdown("---")

    st.info("""
    AI Powered Customer Churn Prediction System

    Predict whether a customer is likely
    to leave the bank based on credit
    card activity and customer profile.
    """)

    st.markdown("---")

    st.write("👩‍💻 Developer")
    st.write("Tanu Bopche")

# ==========================================
# HEADER
# ==========================================
st.markdown("""
<div style="
background:linear-gradient(90deg,#0f172a,#1e40af,#3b82f6);
padding:25px;
border-radius:20px;
text-align:center;
color:white;
box-shadow:0px 4px 15px rgba(0,0,0,0.3);
">
<h1>💳 Credit Card Customer Churn Prediction</h1>
<p>AI Powered Banking Analytics Dashboard</p>
</div>
<br>
""", unsafe_allow_html=True)

# ==========================================
# INPUT SECTION
# ==========================================
col1, col2 = st.columns(2)

with col1:

    st.subheader("👤 Customer Information")

    Customer_Age = st.number_input(
        "Customer Age",
        18,100,40
    )

    Gender = st.selectbox(
        "Gender",
        ["M","F"]
    )

    Dependent_count = st.number_input(
        "Dependent Count",
        0,10,2
    )

    Education_Level = st.selectbox(
        "Education Level",
        [
            "Uneducated",
            "High School",
            "College",
            "Graduate",
            "Post-Graduate",
            "Doctorate",
            "Unknown"
        ]
    )

    Marital_Status = st.selectbox(
        "Marital Status",
        [
            "Single",
            "Married",
            "Divorced",
            "Unknown"
        ]
    )

    Income_Category = st.selectbox(
        "Income Category",
        [
            "Less than $40K",
            "$40K - $60K",
            "$60K - $80K",
            "$80K - $120K",
            "$120K +",
            "Unknown"
        ]
    )

    Card_Category = st.selectbox(
        "Card Category",
        [
            "Blue",
            "Silver",
            "Gold",
            "Platinum"
        ]
    )

    Months_on_book = st.number_input(
        "Months on Book",
        1,100,36
    )

    Total_Relationship_Count = st.number_input(
        "Total Relationship Count",
        1,10,4
    )

with col2:

    st.subheader("🏦 Banking Activity")

    Months_Inactive_12_mon = st.number_input(
        "Months Inactive (12 Months)",
        0,12,2
    )

    Contacts_Count_12_mon = st.number_input(
        "Contacts Count (12 Months)",
        0,10,2
    )

    Credit_Limit = st.number_input(
        "Credit Limit",
        value=5000.0
    )

    Total_Revolving_Bal = st.number_input(
        "Total Revolving Balance",
        value=1000.0
    )

    Avg_Open_To_Buy = st.number_input(
        "Average Open To Buy",
        value=4000.0
    )

    Total_Amt_Chng_Q4_Q1 = st.number_input(
        "Amount Change Q4-Q1",
        value=1.0
    )

    Total_Trans_Amt = st.number_input(
        "Total Transaction Amount",
        value=4000.0
    )

    Total_Trans_Ct = st.number_input(
        "Total Transaction Count",
        value=60
    )

    Total_Ct_Chng_Q4_Q1 = st.number_input(
        "Count Change Q4-Q1",
        value=1.0
    )

    Avg_Utilization_Ratio = st.number_input(
        "Utilization Ratio",
        0.0,1.0,0.30
    )

# ==========================================
# SUMMARY CARDS
# ==========================================
st.markdown("---")

c1,c2,c3,c4 = st.columns(4)

c1.metric("👤 Age", Customer_Age)
c2.metric("💳 Credit Limit", f"${Credit_Limit:,.0f}")
c3.metric("📈 Transactions", Total_Trans_Ct)
c4.metric("🏦 Relations", Total_Relationship_Count)

st.markdown("---")

# ==========================================
# PREDICTION BUTTON
# ==========================================
if st.button("🔍 Predict Customer Churn"):

    input_data = pd.DataFrame([{
        "Customer_Age": Customer_Age,
        "Gender": Gender,
        "Dependent_count": Dependent_count,
        "Education_Level": Education_Level,
        "Marital_Status": Marital_Status,
        "Income_Category": Income_Category,
        "Card_Category": Card_Category,
        "Months_on_book": Months_on_book,
        "Total_Relationship_Count": Total_Relationship_Count,
        "Months_Inactive_12_mon": Months_Inactive_12_mon,
        "Contacts_Count_12_mon": Contacts_Count_12_mon,
        "Credit_Limit": Credit_Limit,
        "Total_Revolving_Bal": Total_Revolving_Bal,
        "Avg_Open_To_Buy": Avg_Open_To_Buy,
        "Total_Amt_Chng_Q4_Q1": Total_Amt_Chng_Q4_Q1,
        "Total_Trans_Amt": Total_Trans_Amt,
        "Total_Trans_Ct": Total_Trans_Ct,
        "Total_Ct_Chng_Q4_Q1": Total_Ct_Chng_Q4_Q1,
        "Avg_Utilization_Ratio": Avg_Utilization_Ratio
    }])

    prediction = model.predict(input_data)

    try:
        prob = model.predict_proba(input_data)

        stay_prob = round(prob[0][0] * 100,2)
        churn_prob = round(prob[0][1] * 100,2)

        st.subheader("📊 Prediction Confidence")

        a,b = st.columns(2)

        a.metric(
            "Customer Stay Chance",
            f"{stay_prob}%"
        )

        b.metric(
            "Customer Churn Risk",
            f"{churn_prob}%"
        )

        st.progress(int(churn_prob))

    except:
        pass

    st.markdown("## 📋 Prediction Result")

    if prediction[0] == 1:

        st.markdown("""
        <div style="
        background:#7f1d1d;
        color:white;
        padding:25px;
        border-radius:15px;
        text-align:center;">
        <h1>⚠️ HIGH CHURN RISK</h1>
        <h3>Customer is likely to leave the bank</h3>
        </div>
        """, unsafe_allow_html=True)

    else:

        st.markdown("""
        <div style="
        background:#14532d;
        color:white;
        padding:25px;
        border-radius:15px;
        text-align:center;">
        <h1>✅ CUSTOMER WILL STAY</h1>
        <h3>Low churn probability detected</h3>
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# RETENTION TIPS
# ==========================================
with st.expander("💡 Customer Retention Suggestions"):

    st.write("""
    ✔ Improve customer engagement

    ✔ Increase transaction activity

    ✔ Offer personalized rewards

    ✔ Reduce inactive months

    ✔ Improve customer support
    """)


