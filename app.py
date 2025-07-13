import streamlit as st
import pandas as pd
import joblib

# Load the model
model = joblib.load('models/phishing_model.pkl')

st.title("🔐 Phishing Website Detector")

st.write("Enter the values below for the website features:")

# List of features (same order as dataset without Index and class)
feature_names = [
    'UsingIP', 'LongURL', 'ShortURL', 'Symbol@', 'Redirecting//',
    'PrefixSuffix-', 'SubDomains', 'HTTPS', 'DomainRegLen', 'Favicon',
    'NonStdPort', 'HTTPSDomainURL', 'RequestURL', 'AnchorURL',
    'LinksInScriptTags', 'ServerFormHandler', 'InfoEmail', 'AbnormalURL',
    'WebsiteForwarding', 'StatusBarCust', 'DisableRightClick',
    'UsingPopupWindow', 'IframeRedirection', 'AgeofDomain', 'DNSRecording',
    'WebsiteTraffic', 'PageRank', 'GoogleIndex', 'LinksPointingToPage',
    'StatsReport'
]

# Input form
input_data = []
for feature in feature_names:
    val = st.selectbox(f"{feature} (1 = Legitimate, 0 = Suspicious, -1 = Phishing)", [-1, 0, 1], index=1)
    input_data.append(val)

if st.button("Detect"):
    df = pd.DataFrame([input_data], columns=feature_names)
    prediction = model.predict(df)[0]

    if prediction == 1:
        st.success("✅ This website is Legitimate.")
    else:
        st.error("🚨 Warning: This website is Phishing.")
