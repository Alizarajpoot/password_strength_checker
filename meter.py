import streamlit as st
import re

def check_password_strength(password):
    score = 0
    feedback = []
    
    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")
    
    # Strength Rating
    if score == 4:
        strength = "✅ Strong Password!"
        css_class = "strong"
    elif score == 3:
        strength = "⚠️ Moderate Password - Consider adding more security features."
        css_class = "moderate"
    else:
        strength = "❌ Weak Password - Improve it using the suggestions below."
        css_class = "weak"

    return strength, feedback, css_class

# Streamlit App UI
st.markdown("<h1 class='title'>🔒 Password Strength Meter</h1>", unsafe_allow_html=True)

password = st.text_input("Enter your password 🔍", type="password")

if password:
    strength, feedback, css_class = check_password_strength(password)
    
    st.markdown(f"<h3 class='{css_class}'>{strength}</h3>", unsafe_allow_html=True)
    
    if feedback:
        st.markdown("<h4 class='suggestions'>Suggestions to improve your password 🔍</h4>", unsafe_allow_html=True)
        for suggestion in feedback:
            st.write(f"- {suggestion}")
