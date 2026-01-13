import streamlit as st
import google.generativeai as genai
from PIL import Image

# إعداد واجهة الموقع كمبادرة تعليمية
st.set_page_config(page_title="مبادرة المعلم الذكي", layout="wide")

st.title("💡 مبادرة مساعد المعلم الذكي")
st.subheader("تحويل صور الدروس إلى تحضير وخطط دراسية بذكاء")

# مكان وضع المفتاح (تأكدي من صحته)
genai.configure(api_key="AIzaSyADNXSoyEIQcfPSnAzxKr0ZVmdELX16Q0M")

with st.sidebar:
    st.info("هذا الموقع يهدف لتسهيل عمل الهيئة التدريسية عبر تحليل محتوى الصور وتوليد أفكار تعليمية.")

uploaded_file = st.file_uploader("قم برفع صورة من الكتاب أو الجدول الدراسي...", type=["jpg", "png", "jpeg"])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="المحتوى المرفوع")
   
    if st.button("توليد المحتوى التعليمي"):
        try:
            model = genai.GenerativeModel('gemini-1.5-flash')
            # طلب شامل يخدم المعلم في أي مادة
            response = model.generate_content([
                "أنت مساعد تعليمي خبير. حلل هذه الصورة وقدم للمعلم: 1. أهداف الدرس، 2. استراتيجيات تدريس مبتكرة، 3. خريطة مفاهيم، 4. أسئلة تقويمية.",
                img
            ])
            st.success("تم التحليل بنجاح!")
            st.markdown(response.text)
        except Exception as e:
            st.error(f"تنبيه تقني: {e}") 
