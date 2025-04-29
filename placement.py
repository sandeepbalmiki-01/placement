import streamlit as st
import joblib

# Load model
model = joblib.load("placement.pkl")

def main():
    st.title("Welcome to Placement Predictor")
    
    # Fixing the slider parameter
    cgpa = st.slider("Choose your CGPA from slider", min_value=0.0, max_value=10.0, step=0.1)
    st.write("Entered CGPA:", cgpa)
    
    if st.button("Predict"):
        res = model.predict([[cgpa]])
        st.success(f"Your predicted package would be {res[0]: .2f} LPA")

# This block should be outside the function
if __name__ == "__main__":
    main()
