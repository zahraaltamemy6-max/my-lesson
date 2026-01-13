Conversation opened. 1 unread message.

Skip to content
Using Gmail with screen readers
1 of 16
(no subject)
Inbox

zoozoo99 am92am77am177 <zamamam74@gmail.com>
4:16 PM (0 minutes ago)
to me

It looks like this message is in Arabic
import streamlit as st
import google.generativeai as genai
from PIL import Image

# إعداد المفتاح (المفتاح الذي وضعتيه سابقاً)
genai.configure(api_key="AIzaSyD700uKyNEDC6t-0J00SDEpV4gOv8dUBMU")

st.title("مساعد المعلم الذكي ✨")
uploaded_file = st.file_uploader("اختر صورة الدرس (حالات المادة)...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='الصورة التي تم رفعها', use_column_width=True)
   
    if st.button('إعداد التحضير الآن'):
        # استخدام الموديل الصحيح لتحليل الصور
        model = genai.GenerativeModel('gemini-pro-vision')
        response = model.generate_content(["قم بتحليل هذه الصورة واستخرج منها تحضيراً كاملاً يشمل: الأهداف، الوسائل، والاستراتيجيات لدرس حالات المادة.", image])
        st.markdown(response.text) 
