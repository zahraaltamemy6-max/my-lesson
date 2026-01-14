import streamlit as st
import google.generativeai as genai
from PIL import Image

# إعداد المفتاح من الأسرار
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
except:
    st.error("يرجى التأكد من حفظ المفتاح في Secrets")

st.title("💡 مبادرة مساعد المعلم الذكي")
uploaded_file = st.file_uploader("ارفع صورة الدرس (مثل حالات المادة)", type=["jpg", "png", "jpeg"])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="المحتوى المطلوب تحليله")
   
    if st.button("إعداد التحضير والوسائل"):
        try:
            # استخدام الموديل الصحيح لتجاوز خطأ 404
            model = genai.GenerativeModel('gemini-1.5-flash')
            response = model.generate_content(["حلل الصورة تربوياً واقترح أهدافاً وخريطة مفاهيم", img])
            st.success("تم التحليل بنجاح!")
            st.markdown(response.text)
        except Exception as e:
            st.error(f"تنبيه تقني: {e}") 
