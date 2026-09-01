import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="مؤلف الروايات الذكي", page_icon="📚", layout="centered")

st.markdown("<h1 style='text-align: center; color: #1f77b4;'>منصة تأليف الروايات والقصص الذكية</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>اصنع قستك الفنية، اكتب فصولها بذكاء، وأنشئ صوراً تعبيرية مذهلة لمشاهدك.</p>", unsafe_allow_html=True)

st.sidebar.header("إعدادات الذكاء الاصطناعي")
api_key = st.sidebar.text_input("أدخل مفتاح الـ API (Gemini)", type="password")

title = st.text_input("عنوان الرواية", placeholder="مثال: حارس البوابة القديمة")
genre = st.selectbox("نوع القصة", ["خيال واسع", "دراما", "غموض وتشويق", "خيال علمي"])
style = st.selectbox("نمط صور Nano Banana", ["سينمائي واقعي", "أنمي", "رسم خيالي"])
num_chapters = st.slider("عدد الفصول المستهدفة", 1, 5, 3)
plot = st.text_area("وصف الحبكة والشخصيات والأحداث", placeholder="اكتب ملخصاً تفصيلياً لأحداث القصة لتوجيه الذكاء الاصطناعي...")

if st.button("🚀 ابدأ توليد الفصول والصور"):
    if not api_key:
        st.error("الرجاء إدخال مفتاح الـ API في الشريط الجانبي أولاً!")
    elif not title or not plot:
        st.warning("الرجاء إدخال عنوان الرواية ووصف الحبكة.")
    else:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        with st.spinner("جاري توليد الفصول الإبداعية عبر الذكاء الاصطناعي..."):
            prompt = f"""
            أنت روائي محترف. قم بتأليف رواية متكاملة بعنوان '{title}'، من نوع '{genre}'.
            وصف الحبكة والشخصيات: {plot}
            قم بكتابة {num_chapters} فصول متسلسلة بتفصيل وإبداع، ولكل فصل ضع عنواناً جذاباً ونصاً سردياً عميقاً، متبوعاً بوصف دقيق لصورة تعبيرية بأسلوب '{style}'.
            """
            try:
                response = model.generate_content(prompt)
                st.success("تم توليد الرواية والفصول بنجاح!")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"حدث خطأ أثناء الاتصال بالذكاء الاصطناعي: {e}")
