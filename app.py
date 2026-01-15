import streamlit as st
import google.generativeai as genai
from PIL import Image

# إعداد المفتاح السري
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
except:
    st.error("⚠️ تأكد من ضبط المفتاح في Secrets")

st.set_page_config(page_title="مساعد المعلم الذكي", layout="centered")
st.title("💡 مبادرة مساعد المعلم الذكي")
st.markdown("ارفع صورة الدرس وسيتم إعداد التحضير تلقائيًا ✨")

uploaded_file = st.file_uploader("📎 ارفع صورة الدرس هنا", type=["jpg", "png", "jpeg"])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="✅ الصورة جاهزة للتحليل")

    if st.button("🔍 إعداد التحضير والوسائل"):
        try:
            model = genai.GenerativeModel(model_name="models/gemini-2.0-flash-lite")
            response = model.generate_content([
                "بناءً على الصورة، قدم تحضيراً تربوياً وأهدافاً وخريطة مفاهيم",
                {"mime_type": "image/jpeg", "data": uploaded_file.getvalue()}
            ])
            st.success("🎉 تم التحليل بنجاح!")
            st.markdown(response.text)
        except Exception as e:
            st.error("⚠️ حدث خطأ أثناء التحليل، قد تكون الحصة اليومية انتهت أو هناك مشكلة في النموذج.")
            st.code(str(e), language="bash") 
