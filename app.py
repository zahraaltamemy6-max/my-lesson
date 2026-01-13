import streamlit as st
import google.generativeai as genai
from PIL import Image

# تأكدي من وضع مفتاحك الخاص هنا بين علامتي التنصيص
genai.configure(api_key="AIzaSyD700uKyNEDC6t-0J00SDEpV4gOv8dUBMU")

st.title("مساعد المعلم الذكي ✨")
uploaded_file = st.file_uploader("اختر صورة الدرس...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='الصورة المرفوعة', use_column_width=True)
   
    if st.button('إعداد التحضير الآن'):
        model = genai.GenerativeModel('gemini-pro-vision')
        response = model.generate_content(["حلل الصورة واستخرج تحضيراً لدرس حالات المادة: أهداف، وسائل، استراتيجيات.", image])
        st.markdown(response.text) 
