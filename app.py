import streamlit as st

st.set_page_config(
    page_title="ИП Качур М. В. | Откачка септиков в Абакане",
    page_icon="🚛",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ===== CSS =====
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* Скрываем стандартные элементы Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display: none;}
    div[data-testid="stToolbar"] {display: none;}

    /* Общий фон */
    .stApp {
        background-color: #ffffff;
    }

    /* Кнопки */
    .btn-orange {
        background: linear-gradient(90deg, #e85d04, #f48c06) !important;
        color: white !important;
        padding: 12px 24px !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        text-decoration: none !important;
        display: inline-block !important;
        margin: 6px 8px 6px 0 !important;
        border: none !important;
        font-size: 1rem !important;
        transition: all 0.2s !important;
    }
    .btn-orange:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 18px rgba(232, 93, 4, 0.35);
        color: white !important;
    }

    .btn-yellow {
        background: #ffc107 !important;
        color: #222 !important;
        padding: 14px 28px !important;
        border-radius: 8px !important;
        font-weight: 700 !important;
        text-decoration: none !important;
        display: inline-block !important;
        border: none !important;
        font-size: 1.05rem !important;
    }
    .btn-yellow:hover {
        background: #ffca2c !important;
        color: #222 !important;
    }

    /* Карточки */
    .feature-card {
        background: #fff8f0;
        border-left: 5px solid #e85d04;
        padding: 18px 20px;
        border-radius: 10px;
        margin-bottom: 12px;
    }
    .feature-num {
        font-size: 1.5rem;
        font-weight: 800;
        color: #e85d04;
        margin-bottom: 4px;
    }
    .feature-text {
        font-size: 0.98rem;
        color: #333;
        line-height: 1.45;
    }

    .price-card {
        background: white;
        border: 2px solid #ffe0b2;
        border-radius: 16px;
        padding: 24px 20px;
        text-align: center;
        height: 100%;
        box-shadow: 0 4px 12px rgba(0,0,0,0.06);
    }
    .price-title {
        font-size: 1.1rem;
        font-weight: 700;
        color: #333;
    }
    .price-value {
        font-size: 2rem;
        font-weight: 800;
        color: #e85d04;
        margin: 10px 0;
    }
    .price-details {
        font-size: 0.95rem;
        color: #555;
        line-height: 1.55;
        margin-bottom: 16px;
    }

    .review-card {
        background: #fafafa;
        border-radius: 12px;
        padding: 18px;
        margin-bottom: 12px;
        border: 1px solid #eee;
        height: 100%;
    }
    .review-name {
        font-weight: 700;
        color: #e85d04;
        margin-bottom: 6px;
    }
    .review-text {
        font-size: 0.93rem;
        color: #444;
        font-style: italic;
        line-height: 1.45;
    }

    .contact-item {
        font-size: 1.1rem;
        margin: 8px 0;
    }
    .contact-item a {
        color: #e85d04;
        text-decoration: none;
        font-weight: 600;
    }
    .contact-item a:hover {
        text-decoration: underline;
    }

    .section-title {
        font-size: 1.8rem;
        font-weight: 800;
        color: #222;
        text-align: center;
        margin: 2rem 0 0.8rem 0;
    }
    .section-subtitle {
        text-align: center;
        color: #666;
        margin-bottom: 1.5rem;
        font-size: 1rem;
    }

    .footer-box {
        background: linear-gradient(90deg, #e85d04 0%, #f48c06 100%);
        color: white;
        text-align: center;
        padding: 36px 20px;
        border-radius: 12px;
        margin-top: 3rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ===== HEADER =====
st.markdown(
    """
    <div style="background: linear-gradient(90deg, #e85d04 0%, #f48c06 100%); 
                padding: 16px 24px; border-radius: 12px; margin-bottom: 24px;
                display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px;">
        <div>
            <div style="font-size: 1.35rem; font-weight: 700; color: white;">🚛 ИП Качур М. В.</div>
            <div style="font-size: 0.9rem; color: rgba(255,255,255,0.9);">Откачка септиков в Абакане</div>
        </div>
        <a href="tel:+73902212010" 
           style="background: white; color: #e85d04; padding: 10px 20px; border-radius: 8px; 
                  font-weight: 700; text-decoration: none; font-size: 0.95rem;">
            📞 +7 (3902) 212-010
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

# ===== HERO =====
col1, col2 = st.columns([1.15, 1], gap="large")

with col1:
    st.markdown(
        """
        <h1 style="font-size: 2.4rem; font-weight: 800; color: #e85d04; line-height: 1.2; margin-bottom: 1rem;">
            Работаем в любых условиях
        </h1>
        <p style="font-size: 1.05rem; color: #444; line-height: 1.6; margin-bottom: 0.5rem;">
            – Объём ЖБО, вывозимых нашими ассенизаторами, составляет от 1 до 10 м³ — идеально как для частных домов, так и для производственных предприятий и компаний сферы ЖКХ.
        </p>
        <p style="font-size: 1.05rem; color: #444; line-height: 1.6; margin-bottom: 0.5rem;">
            – Приглашаем к сотрудничеству частных лиц, организации и коммунальные службы.
        </p>
        <p style="font-size: 1.05rem; color: #444; line-height: 1.6; margin-bottom: 1.2rem;">
            – ИП Качур Максим Васильевич — ваш надёжный партнёр в сфере услуг вывоза ЖБО. Более 15 лет мы занимаем одну из ключевых позиций в данной сфере.
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="margin-top: 8px;">
            <a href="https://disk.yandex.ru/i/gCeX4X-LeEuxxw" target="_blank" class="btn-orange">
                📄 Скачать договор для юр. лиц
            </a>
            <a href="https://t.me/otkachkaabk_bot" target="_blank" class="btn-orange">
                💬 Оставить заявку в Telegram
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.image(
        "https://xn--80aaacwsldyvuo.xn--p1ai/wp-content/uploads/2024/11/e2776ed26915ce5a3e586d2b3941fcb7.png",
        use_container_width=True
    )

st.markdown("<br>", unsafe_allow_html=True)

# ===== ПОЧЕМУ МЫ =====
st.markdown('<div class="section-title">Почему нужно выбрать нас?</div>', unsafe_allow_html=True)
st.markdown('<div class="section-subtitle">Несколько фактов о нашей компании, которые убедят Вас воспользоваться нашими услугами</div>', unsafe_allow_html=True)

features = [
    ("1", "Очистка сточных вод в Абакане и Хакасии: 15 лет опыта"),
    ("2", "Вывоз ЖБО в Абакане: доступные цены, высокая эффективность"),
    ("3", "Санитарная чистота: ваш объект в надёжных руках"),
    ("4", "Индивидуальный подход, оперативность, профессионализм: мы гарантируем результат"),
    ("5", "Освобождение от воды: от остановок до жилых домов"),
    ("6", "Команда профессионалов: работаем на результат"),
    ("7", "Современная техника: бесперебойная работа, гарантированное качество"),
]

cols = st.columns(2)
for i, (num, text) in enumerate(features):
    with cols[i % 2]:
        st.markdown(
            f"""
            <div class="feature-card">
                <div class="feature-num">{num}</div>
                <div class="feature-text">{text}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

# ===== ТАРИФЫ =====
st.markdown('<div class="section-title">СТОИМОСТЬ РАБОТ АССЕНИЗАТОРА</div>', unsafe_allow_html=True)
st.markdown('<div class="section-subtitle">Цены зависят от удалённости, сложности работы, объёма откачки и прочих условий</div>', unsafe_allow_html=True)

tariffs = [
    {
        "title": "Тариф №1",
        "price": "1 400 ₽",
        "details": "Объём: до 4 м³<br>Минимальное время: 1 час<br>Длина шланга: 10 м<br>Аренда с оператором"
    },
    {
        "title": "Тариф №2",
        "price": "1 700 ₽",
        "details": "Объём: до 6 м³<br>Минимальное время: 1 час<br>Длина шланга: 10 м<br>Аренда с оператором"
    },
    {
        "title": "Тариф №3",
        "price": "2 400 ₽",
        "details": "Объём: от 7 до 10 м³<br>Минимальное время: 1 час<br>Длина шланга: 10 м<br>Аренда с оператором"
    },
]

cols = st.columns(3)
for i, t in enumerate(tariffs):
    with cols[i]:
        st.markdown(
            f"""
            <div class="price-card">
                <div class="price-title">{t['title']}</div>
                <div class="price-value">{t['price']}</div>
                <div class="price-details">{t['details']}</div>
                <a href="https://t.me/otkachkaabk_bot" target="_blank" class="btn-orange" style="width:90%; text-align:center;">
                    Оставить заявку
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )

# ===== ОТЗЫВЫ =====
st.markdown('<div class="section-title">Отзывы наших клиентов на Авито</div>', unsafe_allow_html=True)
st.markdown('<div class="section-subtitle">Вы можете доверять нашим ассенизаторам, профессионализму и качеству работ</div>', unsafe_allow_html=True)

reviews = [
    ("Женя", "Очень хорошие ребята! Сразу взяли трубку и даже раньше приехали! Очень довольна. Молодцы! Пользуюсь услугой второй раз! Рекомендую!"),
    ("Василий", "Всё отлично, приехали очень быстро! Цена умеренная!"),
    ("Олеся", "Работа выполнена быстро, качественно, спасибо!"),
    ("Евгения", "Все оперативно, промыли, откачали, спасибо! Рекомендую."),
    ("Глеб", "Работа выполнена оперативно и качественно."),
    ("S13", "Всё отлично! приехали в этот же день как позвонили, откачали как положено. 10 куб."),
]

cols = st.columns(3)
for i, (name, text) in enumerate(reviews):
    with cols[i % 3]:
        st.markdown(
            f"""
            <div class="review-card">
                <div class="review-name">{name}</div>
                <div class="review-text">«{text}»</div>
            </div>
            """,
            unsafe_allow_html=True
        )

# ===== КОНТАКТЫ =====
st.markdown('<div class="section-title">Свяжитесь с нами</div>', unsafe_allow_html=True)
st.markdown('<div class="section-subtitle">Есть вопросы? Нужно откачать септик? Оставьте заявку — мы свяжемся с вами в ближайшее время.</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("#### 📞 Телефоны")
    st.markdown(
        """
        <div class="contact-item">📞 <a href="tel:+73902212010">+7 (3902) 212-010</a></div>
        <div class="contact-item">📞 <a href="tel:+79130513028">+7 (913) 051-30-28</a></div>
        <div class="contact-item">📞 <a href="tel:+79134467099">+7 (913) 446-70-99</a></div>
        <div class="contact-item">📞 <a href="tel:+79831912010">+7 (983) 191-20-10</a></div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("#### ✉️ Электронная почта")
    st.markdown(
        '<div class="contact-item">📧 <a href="mailto:septikabakan@mail.ru">septikabakan@mail.ru</a></div>',
        unsafe_allow_html=True
    )

with col2:
    st.markdown("#### 🏢 Реквизиты")
    st.markdown(
        """
        <p><strong>ИП Качур Максим Васильевич</strong></p>
        <p>ИНН <a href="https://www.rusprofile.ru/ip/317190100007117?print=pdf" target="_blank" style="color:#e85d04; font-weight:600;">190116760265</a></p>
        <br>
        <a href="https://t.me/otkachkaabk_bot" target="_blank" class="btn-yellow">
            💬 Оставить заявку в Telegram
        </a>
        """,
        unsafe_allow_html=True
    )

# ===== ФУТЕР =====
st.markdown(
    """
    <div class="footer-box">
        <div style="font-size: 1.3rem; font-weight: 700; margin-bottom: 6px;">🚛 ИП Качур М. В.</div>
        <div style="opacity: 0.9; margin-bottom: 12px;">Откачка септиков в Абакане</div>
        <div style="font-size: 0.95rem; opacity: 0.9;">
            +7 (3902) 212-010 &nbsp;|&nbsp; septikabakan@mail.ru
        </div>
        <div style="margin-top: 20px; font-size: 0.85rem; opacity: 0.75;">
            © 2026 ИП Качур М. В. — Откачка септиков в Абакане. Все права защищены.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
