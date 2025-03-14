import streamlit as st
import re

st.set_page_config(page_title="Password Strenght Checker", page_icon="💯")

st.markdown("""
## Welcome To The Ultimate Password Strenght Checker!
#### Use this simple tool to check the srentght of your password
""")
password = st.text_input ("Enter Your Password", type = "password")

feedback = []

score = 0

if password:
    if len(password) >= 8:
        score += 1
    else:
        feedback.append ("❌ Password Must Have Atleast 8 Characters")

    if re.search(r'[A-Z]', password) and re.search (r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Password Must Have One Uppercase And One Lowercase Letter")

    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append ("❌ Password Must Contain Atleast One Digit")

    if re.search(r'[@-_]', password):
        score += 1
    else:
        feedback.append("❌ Password Must Contain Atleast One Special Character (@-_)")

    if score == 4:
        feedback.append("✅ Your Password Is Strong")
    elif score == 3:
        feedback.append("🟡 Your Password Strenght Is Medium")
    else:
        feedback.append("🔴 Your Password is weak. Please Make It Stronger.")
    if feedback:
        st.markdown("### Improvement Suggestions")
        for tip in feedback:
            st.write(tip)

else:
    st.info("Please Enter Your Password To Get Started")