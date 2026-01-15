import streamlit as st
import google.generativeai as genai
from PIL import Image

# ضبط المفتاح السري
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
except:
    st.error("تأكد من ضبط المفتاح في Secrets")

st.title("💡 مبادرة مساعد المعلم الذكي")
uploaded_file = st.file_uploader("ارفع صورة الدرس هنا", type=["jpg", "png", "jpeg"])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="المحتوى المطلوب تحليله")
   
    if st.button("إعداد التحضير والوسائل"):
        try:
            # استخدم اسم نموذج صحيح من القائمة
            model = genai.GenerativeModel(model_name="models/gemini-2.5-pro")
           
            # تمرير الصورة كـ بايتات مع نوعها
            response = model.generate_content([
                "بناءً على الصورة، قدم تحضيراً تربوياً وأهدافاً وخريطة مفاهيم",
                {"mime_type": "image/jpeg", "data": uploaded_file.getvalue()}
            ])
           
            st.success("تم التحليل بنجاح!")
            st.markdown(response.text)
        except Exception as e:
            st.error(f"تنبيه تقني: {e}") 
