import streamlit as st
import google.generativeai as genai
from PIL import Image

# تأكدي من نسخ المفتاح كاملاً من موقع Google AI Studio
genai.configure(api_key="AIzaSyD7O0uKyNEDC6t-0J00SDEpV4gOvBdUBNU")

st.title("مساعد المعلم الذكي ✨")
st.write("جاهز لتحضير درس حالات المادة...")

uploaded_file = st.file_uploader("ارفع صورة الجدول", type=["jpg", "png"])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img)
   
    if st.button("بدء التحضير"):
        try:
            # استخدام موديل الفلاش الأسرع والأكثر توافقاً
            model = genai.GenerativeModel('gemini-1.5-flash')
            response = model.generate_content(["حلل جدول حالات المادة واكتب تحضيراً يشمل الأهداف والوسائل", img])
            st.markdown(response.text)
        except Exception as e:
            st.error(f"حدث خطأ في المفتاح: {e}") 
