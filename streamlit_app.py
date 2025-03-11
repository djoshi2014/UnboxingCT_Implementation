import streamlit as st
import pandas as pd
import datetime

# Title of the App
st.title("📋 Computational Thinking Reflection App")
st.write("Reflect on how you integrated Computational Thinking (CT) into your lesson today.")

# Get Teacher's Name
teacher_name = st.text_input("Your Name")

# Date Selection
date = st.date_input("Date", datetime.date.today())

# Computational Thinking Section
st.subheader("💡 Computational Thinking Integration")
ct_used = st.radio("Did you use Computational Thinking (CT) in your lesson today?", ["Yes", "No"], index=1)
ct_implementation = st.text_area(
    "If yes, how did you implement Computational Thinking? (E.g., Decomposition, Pattern Recognition, Abstraction, Algorithms)")

# Additional Comments
additional_feedback = st.text_area("Additional Comments (Optional)")

# Submit Button
if st.button("Submit Reflection"):
    reflection_data = {
        "Teacher": teacher_name,
        "Date": date,
        "CT Used": ct_used,
        "CT Implementation": ct_implementation if ct_used == "Yes" else "N/A",
        "Comments": additional_feedback
    }

    # Save feedback to a CSV file
    df = pd.DataFrame([reflection_data])
    df.to_csv("ct_reflections.csv", mode="a", header=not pd.io.common.file_exists("ct_reflections.csv"), index=False)

    st.success("✅ Reflection submitted successfully!")
    st.write("Thank you for your input!")

# Show previously submitted reflections (optional)
if st.checkbox("📊 Show Previous Reflections"):
    try:
        df = pd.read_csv("ct_reflections.csv")
        st.dataframe(df)
    except FileNotFoundError:
        st.write("No reflections submitted yet.")
