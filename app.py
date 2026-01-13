import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. إعداد المفتاح (تأكد من وضع مفتاحك هنا)
genai.configure(api_key="AIzaSyD700uKyNEDC6t-0J00SDEpV4gOv8dUBMU")

# 2. واجهة المستخدم
st.title("✨ مساعد المعلم الذكي")
template_type = st.selectbox("اختر نوع التحضير:", ["تحضير قياسي", "تعلم نشط", "استقصاء", "خرائط ذهنية"])
uploaded_file = st.file_uploader("اختر صورة الدرس (JPG/PNG)...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="الصورة التي تم رفعها", use_container_width=True)

    if st.button("إعداد التحضير الآن"):
        with st.spinner("جاري تحليل الصورة وإعداد التحضير..."):
            try:
                   # (السطر 26 المعدل (بأخطاء
                model = genai.GenerativeModel('gemini-1.5-flash')
               
                instruction = f"Analyze the image and write a detailed lesson plan in ARABIC language using this style: {template_type}"
                response = model.generate_content([instruction, image])
               
                st.markdown("---")
                st.markdown(f"### ✨ {template_type}")
                st.write(response.text)
               
            except Exception as e:
                st.error(f"حدث خطأ: {e}") 
