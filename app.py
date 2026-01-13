import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. إعداد واجهة المبادرة
st.set_page_config(page_title="Teacher AI Initiative", layout="wide")
st.title("💡 مبادرة مساعد المعلم الذكي")
st.write("أداة تقنية لدعم الهيئة التدريسية في تحليل الدروس وإعداد التحضير")

# 2. وضع المفتاح الذي ينتهي بـ 6Q0M (تأكدي من نسخه كاملاً)
genai.configure(api_key="AIzaSyADNXSoyElQcfPSnAzxKr0ZVmdELX16Q0M")

# 3. واجهة رفع الملفات
uploaded_file = st.file_uploader("ارفع صورة الدرس (مثل حالات المادة)...", type=["jpg", "png", "jpeg"])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="المحتوى المطلوب تحليله")
   
    if st.button("إعداد التحضير والوسائل"):
        try:
            # استخدام الموديل الأحدث
            model = genai.GenerativeModel('gemini-1.5-flash-latest')
            response = model.generate_content(["بناءً على الصورة، اكتب تحضيراً تربوياً يشمل الأهداف، استراتيجيات التدريس، وخريطة مفاهيم.", img])
            st.success("تم توليد المحتوى بنجاح!")
            st.markdown(response.text)
        except Exception as e:
            st.error(f"تنبيه تقني: {e}") 
