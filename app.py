 import streamlit as st

st.set_page_config(
    page_title="Modern Design | تشطيبات وديكور", page_icon="🏠", layout="wide"
)

# رقم الواتساب الخاص بك
WHATSAPP_NUMBER = "201226424298"

st.markdown(
    """
    <style>
    .main-title { font-size: 36px; color: #1E3A8A; text-align: center; font-weight: bold; }
    .sub-title { font-size: 18px; color: #4B5563; text-align: center; margin-bottom: 30px; }
    .whatsapp-btn {
        display: inline-block;
        background-color: #25D366;
        color: white;
        padding: 12px 24px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: bold;
        text-align: center;
        font-size: 18px;
        margin-top: 15px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.sidebar.title("🛠️ Modern Design")
st.sidebar.markdown("منصتك المتكاملة للتشطيبات والديكور العصري")
menu = st.sidebar.radio(
    "اختر القسـم:",
    [
        "الرئيسية",
        "احسب تكلفة تشطيبك",
        "طلب معاينة / استشارة",
        "معرض أعمالنا",
        "تواصل معنا",
    ],
)

if menu == "الرئيسية":
  st.markdown(
      '<div class="main-title">مرحباً بك في Modern Design</div>',
      unsafe_allow_html=True,
  )
  st.markdown(
      '<div class="sub-title">نحول شقتك أو فيلتك إلى تحفة فنية بأعلى جودة'
      " وأفضل الأسعار</div>",
      unsafe_allow_html=True,
  )

  col1, col2, col3 = st.columns(3)
  with col1:
    st.markdown("### 🎨 تصميم عصري")
    st.write("نقدم أحدث صيحات الديكور المودرن والنيوكلاسيك التي تناسب ذوقك.")
  with col2:
    st.markdown("### ⏱ التزام بالمواعيد")
    st.write("نضمن لك تسليم الوحدة في الموعد المحدد دون تأخير وبأعلى دقة.")
  with col3:
    st.markdown("### 💰 أسعار تنافسية")
    st.write("باقات متنوعة تناسب جميع الميزانيات مع ضمان كامل على التنفيذ.")

  st.write("---")
  st.markdown(
      "<div style='text-align: center;'>"
      f"<a href='https://wa.me/{WHATSAPP_NUMBER}?text=السلام%20عليكم،%20أرغب%20في%20استشارة%20بخصوص%20تشطيب%20وحدة'%20class='whatsapp-btn'%20target='_blank'>💬"
      " تواصل معنا مباشرة عبر واتساب</a></div>",
      unsafe_allow_html=True,
  )

elif menu == "احسب تكلفة تشطيبك":
  st.markdown(
      '<div class="main-title">حاسبة تكلفة التشطيب التقديرية</div>',
      unsafe_allow_html=True,
  )
  space = st.number_input(
      "مساحة الشقة التقريبية (بالمتر المربع):",
      min_value=50,
      max_value=1000,
      value=120,
      step=10,
  )
  finish_type = st.selectbox(
      "اختر مستوى التشطيب:",
      [
          "تشطيب اقتصادي (لوكس)",
          "تشطيب سوبر لوكس",
          "تشطيب ألترا لوكس / ديلوكس",
      ],
  )
  rates = {
      "تشطيب اقتصادي (لوكس)": 2500,
      "تشطيب سوبر لوكس": 4000,
      "تشطيب ألترا لوكس / ديلوكس": 6000,
  }
  if st.button("احسب التكلفة التقديرية", type="primary"):
    cost = space * rates[finish_type]
    st.success(f"🎉 التكلفة التقديرية: **{cost:,} جنيه مصري**")
    wa_msg = f"مرحباً ابو علي، حسبت تكلفة شقتي بمساحة {space} متر لمستوى ({finish_type}) وكانت التكلفة {cost:,} جنيه وأرغب في تأكيد الحجز."
    st.markdown(
        "<div style='text-align: center;'>"
        f"<a href='https://wa.me/{WHATSAPP_NUMBER}?text={wa_msg}'"
        " class='whatsapp-btn' target='_blank'>💬 اطلب هذا العرض عبر"
        " الواتساب</a></div>",
        unsafe_allow_html=True,
    )

elif menu == "طلب معاينة / استشارة":
  st.markdown(
      '<div class="main-title">اطلب معاينة هندسية</div>',
      unsafe_allow_html=True,
  )
  with st.form("req"):
    name = st.text_input("الاسم الكامل:")
    phone = st.text_input("رقم الهاتف:")
    loc = st.text_input("عنوان العقار (المدينة / الحي):")
    submitted = st.form_submit_button("إرسال الطلب عبر الواتساب", type="primary")
    if submitted:
      if name and phone:
        st.success(f"✅ شكراً لك يا {name}! اضغط على الزر أدناه لإرسال طلبك.")
        wa_text = f"السلام عليكم، أنا {name}، رقمي {phone}، وعنوان العقار {loc}، وأرغب في طلب معاينة هندسية."
        st.markdown(
            "<div style='text-align: center;'>"
            f"<a href='https://wa.me/{WHATSAPP_NUMBER}?text={wa_text}'"
            " class='whatsapp-btn' target='_blank'>💬 اضغط هنا للإرسال عبر"
            " الواتساب</a></div>",
            unsafe_allow_html=True,
        )
      else:
        st.error("❌ برجاء إدخال الاسم ورقم الهاتف على الأقل.")

elif menu == "معرض أعمالنا":
  st.markdown(
      '<div class="main-title">معرض أعمال Modern Design</div>',
      unsafe_allow_html=True,
  )
  st.image(
      "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=600",
      caption="تشطيب صالة استقبال مودرن",
  )

elif menu == "تواصل معنا":
  st.markdown(
      '<div class="main-title">تواصل مع Modern Design</div>',
      unsafe_allow_html=True,
  )
  st.markdown(f"📞 **رقم الواتساب الرسمي:** `{WHATSAPP_NUMBER}`")
  st.markdown(
      "<div style='text-align: center;'>"
      f"<a href='https://wa.me/{WHATSAPP_NUMBER}?text=السلام%20عليكم%20ابو%20علي،%20أريد%20الاستفسار%20عن%20خدمات%20التشطيب'%20class='whatsapp-btn'%20target='_blank'>💬"
      " راسلني الآن على الواتساب</a></div>",
      unsafe_allow_html=True,
  )
