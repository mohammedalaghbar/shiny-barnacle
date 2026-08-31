import streamlit as st

st.set_page_config(page_title="مؤلف الروايات الذكي", page_icon="✍️", layout="wide")

st.markdown("<h1 style='text-align: center; color: #4A90E2;'>منصة تأليف الروايات والقصص الذكية</h1>", unsafe_allow_html=True)
st.write("اصنع قصتك الفنية، اكتب فصولها بذكاء، وأنشئ صوراً تعبيرية مذهلة لمشاهدك.")

with st.sidebar:
    st.header("إعدادات الذكاء الاصطناعي")
    api_key = st.text_input("أدخل مفتاح الـ API (Gemini / OpenAI)", type="password")
    st.info("قم بإدخال المفتاح لتفعيل التوليد الحقيقي للفصول والصور.")

col1, col2 = st.columns(2)

with col1:
    story_title = st.text_input("عنوان الرواية", placeholder="مثال: حارس البوابة القديمة")
    story_genre = st.selectbox("نوع القصة", ["خيالي واسع", "درامي وتشويق", "تاريخي وأساطير", "خيال علمي"])

with col2:
    art_style = st.selectbox("نمط صور Nano Banana", ["سينمائي واقعي", "أنمي وفانتازيا", "لوحة زيتية كلاسيكية", "رقمي حديث"])
    target_chapters = st.slider("عدد الفصول المستهدفة", min_value=1, max_value=10, value=3)

story_prompt = st.text_area("وصف الحبكة والشخصيات والأحداث", placeholder="اكتب ملخصاً تفصيلياً لأحداث القصة لتوجيه الذكاء الاصطناعي...")

if st.button("🚀 ابدأ توليد الفصول والصور", use_container_width=True):
    if not api_key:
        st.warning("⚠️ يرجى إدخال مفتاح الـ API في الشريط الجانبي أولاً للمتابعة.")
    elif not story_prompt.strip():
        st.error("يرجى إدخال وصف الحبكة أولاً لكي يتمكن الذكاء الاصطناعي من البدء.")
    else:
        with st.spinner("جاري التواصل مع نماذج الذكاء الاصطناعي وتجهيز لوحات Nano Banana..."):
            st.success(f"تم بنجاح إنشاء هيكل رواية: {story_title}")
            for i in range(1, target_chapters + 1):
                with st.expander(f"الفصل {i}: بداية الحكاية"):
                    st.write(f"هنا سيظهر النص المولّد تلقائياً للفصل {i} بناءً على الحبكة المكتوبة وبأسلوب الـ {story_genre}...")
                    st.markdown(f"🎨 **صورة تعبيرية مقترحة (نمط {art_style}):**")
                    st.info("سيتم عرض صورة مشهد القصة المولدة عبر محرك Nano Banana هنا.")
                    
