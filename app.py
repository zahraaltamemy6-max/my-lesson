import streamlit as st
import google.generativeai as genai
from PIL import Image

# إعداد واجهة المبادرة
st.set_page_config(page_title="مبادرة المعلم الذكي", layout="wide")
st.title("💡 مبادرة مساعد المعلم الذكي")

# المفتاح الجديد الذي فعلتيه (تأكدي من صحته)
genai.configure(api_key="AIzaSyADNXSoyElQcfPSnAzxKr0ZVmdELX16Q0M")

uploaded_file = st.file_uploader("ارفع صورة الدرس هنا...", type=["jpg", "png", "jpeg"])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="المحتوى المطلوب تحليله")
   
    if st.button("إعداد التحضير والوسائل"):
        try:
            # استخدام النسخة الأحدث لضمان النجاح
            model = genai.GenerativeModel('gemini-1.5-flash-latest')
            response = model.generate_content(["حلل الصورة وقدم تحضيراً يشمل الأهداف والوسائل وخريطة مفاهيم.", img])
            st.success("تم التحليل بنجاح!")
            st.markdown(response.text)
        except Exception as e:
            st.error(f"تنبيه: {e}") 
