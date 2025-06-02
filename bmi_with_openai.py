import streamlit as st
import openai 

# Set OpenAI API key directly
openai.api_key = "OPENAI_API_KEY"  # Replace with your actual OpenAI API key
#Streamlit app for BMI Calculator with GPT Health Tips

st.title("💪 BMI Calculator + GPT Health Tips")

# Description
st.markdown("This app calculates your BMI and provides AI-powered health tips using GPT.")

# Input
height = st.slider("Enter your height (cm):", 100, 250, 170)
weight = st.slider("Enter your weight (kg):", 40, 200, 70)

# BMI Calculation
bmi = weight / ((height / 100) ** 2)
st.write(f"📏 Your BMI is: `{bmi:.2f}`")

# Category
if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal weight"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

st.success(f"🩺 You are **{category}** based on your BMI.")

# GPT Tips
if st.button("🧠 Suggest Ways to Improve My Health"):
    with st.spinner("Generating suggestions..."):
        prompt = f"My BMI is {bmi:.2f}. My height is {height} cm and my weight is {weight} kg. Suggest 3 tips to improve my health."
        
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a certified health advisor."},
                    {"role": "user", "content": prompt}
                ]
            )
            st.subheader("✅ Health Tips from GPT")
            st.write(response['choices'][0]['message']['content'])

        except openai.error.RateLimitError:
            st.error("⚠️ You've hit the rate limit. Wait or upgrade your OpenAI plan.")
        except Exception as e:
            st.error(f"❌ Error: {e}")
