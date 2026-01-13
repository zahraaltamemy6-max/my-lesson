import streamlit as st
import google.generativeai as genai
from PIL import Image

# تأكدي من كتابة مفتاحك هنا بدقة
genai.configure(api_key="AIzaSyD700uKyNEDC6t-0J00SDEpV4gOv8dUBMU")

st.title("مساعد المعلم الذكي ✨")
uploaded_file = st.file_uploader("ارفع صورة الدرس", type=["jpg", "png"])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img)
    if st.button("إعداد التحضير"):
        # هذا السطر هو مفتاح الحل
        model = genai.GenerativeModel('gemini-1.5-flash')
        res = model.generate_content(["حلل الصورة واكتب تحضير درس حالات المادة", img])
        st.write(res.text) 
