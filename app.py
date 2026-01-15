import streamlit as st
import google.generativeai as genai

# ضبط المفتاح
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
except:
    st.error("تأكد من ضبط المفتاح في Secrets")

st.title("🔎 اختبار النماذج المتاحة")

if st.button("عرض النماذج"):
    try:
        models = genai.list_models()
        for m in models:
            st.write("📌 الاسم:", m.name)
            st.write("   الطرق المدعومة:", m.supported_generation_methods)
            st.write("---")
    except Exception as e:
        st.error(f"خطأ أثناء جلب النماذج: {e}") 
