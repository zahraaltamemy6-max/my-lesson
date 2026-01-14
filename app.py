import streamlit as st
import google.generativeai as genai
from PIL import Image

# هذه هي الطريقة الصحيحة الوحيدة لقراءة المفتاح من الـ Secrets
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
except Exception as e:
    st.error("لم يتم العثور على المفتاح في الإعدادات السرية")

st.title("💡 مبادرة مساعد المعلم الذكي")
uploaded_file = st.file_uploader("ارفع صورة الدرس", type=["jpg", "png", "jpeg"])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img)
    if st.button("إعداد التحضير والوسائل"):
        try:
           model = genai.GenerativeModel('gemini-1.5-flash-latest') 
            response = model.generate_content(["بناءً على الصورة، قدم تحضيراً تربوياً وخريطة مفاهيم.", img])
            st.success("تم التحليل بنجاح!")
            st.write(response.text)
        except Exception as e:
            st.error(f"تنبيه تقني: {e}") 

