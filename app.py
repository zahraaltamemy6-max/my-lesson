import streamlit as st
import google.generativeai as genai
from PIL import Image

genai.configure(api_key="AIzaSyADNXSoyElQcfPSnAzxKr0ZVmdELX16Q0M")

st.set_page_config(page_title="Teacher AI Initiative")
st.title("💡 مبادرة مساعد المعلم الذكي")

uploaded_file = st.file_uploader("ارفع صورة الدرس", type=["jpg", "png", "jpeg"])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img)
    if st.button("إعداد التحضير والوسائل"):
        try:
            model = genai.GenerativeModel('gemini-1.5-flash-latest')
            response = model.generate_content(["حلل الصورة وقدم تحضيراً تربوياً كاملاً", img])
            st.success("تم التحليل بنجاح!")
            st.markdown(response.text)
        except Exception as e:
            st.error(f"Error: {e}") 
