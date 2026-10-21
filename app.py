import streamlit as st

st.set_page_config(
    page_title="ИП Качур М. В. | Откачка септиков в Абакане",
    page_icon="🚛",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ===== Кастомные стили (оранжевая тема как на сайте) =====
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    .main {
        background-color: #ffffff;
    }
    
    /* Скрыть стандартные элементы Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display: none;}
    
    /* Хедер */
    .header-bar {
        background: linear-gradient(90deg, #e85d04 0%, #f48c06 100%);
        padding: 12px 0;
        margin: -6rem -6rem 2rem -6rem;
        color: white;
    }
    
    .logo-text {
        font-size: 1.4rem;
        font-weight: 700;
        color: white;
        margin: 0;
    }
    
    .logo-sub {
        font-size: 0.85rem;
        opacity: 0.9;
        margin: 0;
    }
    
    /* Hero */
    .hero-title {
        font-size: 2.8rem;
        font-weight: 800;
        color: #e85d04;
        line-height: 1.15;
        margin-bottom: 1.2rem;
    }
    
    .hero-text {
        font-size: 1.05rem;
        color: #444;
        line-height: 1.6;
        margin-bottom: 0.6rem;
    }
    
    /* Кнопки */
    .btn-orange {
        background: linear-gradient(90deg, #e85d04, #f48c06);
        color: white !important;
        padding: 14px 28px;
        border-radius: 8px;
        font-weight: 600;
        text-decoration: none !important;
        display: inline-block;
        margin: 8px 8px 8px 0;
        border: none;
        font-size: 1rem;
        transition: transform 0.15s;
    }
    .btn-orange:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(232, 93, 4, 0.35);
        color: white !important;
    }
    
    .btn-yellow {
        background: #ffc107;
        color: #333 !important;
        padding: 14px 28px;
        border-radius: 8px;
        font-weight: 700;
        text-decoration: none !important;
        display: inline-block;
        margin: 8px 0;
        border: none;
        font-size: 1.05rem;
    }
    .btn-yellow:hover {
        background: #ffca2c;
        color: #333 !important;
    }
    
    /* Карточки преимуществ */
    .feature-card {
        background: #fff8f0;
        border-left: 5px solid #e85d04;
        padding: 18px 20px;
        border-radius: 10px;
        margin-bottom: 14px;
        height: 100%;
    }
    .feature-num {
        font-size: 1.6rem;
        font-weight: 800;
        color: #e85d04;
        margin-bottom: 6px;
    }
    .feature-text {
        font-size: 0.98rem;
        color: #333;
        line-height: 1.45;
    }
    
    /* Тарифы */
    .price-card {
        background: white;
        border: 2px solid #ffe0b2;
        border-radius: 16px;
        padding: 28px 24px;
        text-align: center;
        height: 100%;
        transition: all 0.2s;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    }
    .price-card:hover {
        border-color: #e85d04;
        box-shadow: 0 8px 25px rgba(232, 93, 4, 0.15);
        transform: translateY(-4px);
    }
    .price-title {
        font-size: 1.15rem;
        font-weight: 700;
        color: #333;
        margin-bottom: 8px;
    }
    .price-value {
        font-size: 2.2rem;
        font-weight: 800;
        color: #e85d04;
        margin: 12px 0;
    }
    .price-details {
        font-size: 0.95rem;
        color: #555;
        line-height: 1.6;
        margin-bottom: 20px;
    }
    
    /* Отзывы */
    .review-card {
        background: #fafafa;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 16px;
        border: 1px solid #eee;
        height: 100%;
    }
    .review-name {
        font-weight: 700;
        color: #e85d04;
        margin-bottom: 8px;
    }
    .review-text {
        font-size: 0.95rem;
        color: #444;
        font-style: italic;
        line-height: 1.5;
    }
    
    /* Контакты */
    .contact-item {
        font-size: 1.15rem;
        margin: 10px 0;
    }
    .contact-item a {
        color: #e85d04;
        text-decoration: none;
        font-weight: 600;
    }
    .contact-item a:hover {
        text-decoration: underline;
    }
    
    /* Секции */
    .section-title {
        font-size: 2rem;
        font-weight: 800;
        color: #222;
        margin: 2.5rem 0 1.5rem 0;
        text-align: center;
    }
    
    .section-subtitle {
        text-align: center;
        color: #666;
        margin-bottom: 2rem;
        font-size: 1.05rem;
    }
    
    /* Футер */
    .footer {
        background: linear-gradient(90deg, #e85d04 0%, #f48c06 100%);
        color: white;
        text-align: center;
        padding: 40px 20px;
        margin: 4rem -6rem -6rem -6rem;
    }
    
    .footer a {
        color: #fff3cd;
        text-decoration: none;
    }
</style>
""")

# ===== HEADER =====
st.markdown("""
<div class="header-bar">
    <div style="max-width: 1200px; margin: 0 auto; padding: 0 2rem; display: flex; justify-content: space-between; align-items: center;">
        <div>
            <p class="logo-text">🚛 ИП Качур М. В.</p>
            <p class="logo-sub">Откачка септиков в Абакане</p>
        </div>
        <div>
            <a href="tel:+73902212010" class="btn-orange" style="padding: 10px 20px; font-size: 0.95rem;">📞 Позвонить</a>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ===== HERO =====
col1, col2 = st.columns([1.1, 1], gap="large")

with col1:
    st.markdown('<h1 class="hero-title">Работаем в любых условиях</h1>', unsafe_allow_html=True)
    st.markdown("""
    <p class="hero-text">– Объём ЖБО, вывозимых нашими ассенизаторами, составляет от 1 до 10 м³ — идеально как для частных домов, так и для производственных предприятий и компаний сферы ЖКХ.</p>
    <p class="hero-text">– Приглашаем к сотрудничеству частных лиц, организации и коммунальные службы.</p>
    <p class="hero-text">– ИП Качур Максим Васильевич — ваш надёжный партнёр в сфере услуг вывоза ЖБО. Более 15 лет мы занимаем одну из ключевых позиций в данной сфере.</p>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="margin-top: 1.5rem;">
        <a href="https://disk.yandex.ru/i/gCeX4X-LeEuxxw" target="_blank" class="btn-orange">📄 Скачать договор для юр. лиц</a>
        <a href="https://t.me/otkachkaabk_bot" target="_blank" class="btn-orange">💬 Оставить заявку в Telegram</a>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.image(
        "https://xn--80aaacwsldyvuo.xn--p1ai/wp-content/uploads/2024/11/e2776ed26915ce5a3e586d2b3941fcb7.png",
        use_container_width=True
    )

st.markdown("<br>", unsafe_allow_html=True)

# ===== ПОЧЕМУ МЫ =====
st.markdown('<h2 class="section-title">Почему нужно выбрать нас?</h2>', unsafe_allow_html=True)
st.markdown('<p class="section-subtitle">Несколько фактов о нашей компании, которые убедят Вас воспользоваться нашими услугами</p>', unsafe_allow_html=True)

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
        st.markdown(f"""
        <div class="feature-card">
            <div class="feature-num">{num}</div>
            <div class="feature-text">{text}</div>
        </div>
        """, unsafe_allow_html=True)

# ===== ТАРИФЫ =====
st.markdown('<h2 class="section-title">СТОИМОСТЬ РАБОТ АССЕНИЗАТОРА</h2>', unsafe_allow_html=True)
st.markdown('<p class="section-subtitle">Наши тарифы. Цены зависят от удалённости, сложности работы, объёма откачки и прочих условий</p>', unsafe_allow_html=True)

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
        st.markdown(f"""
        <div class="price-card">
            <div class="price-title">{t['title']}</div>
            <div class="price-value">{t['price']}</div>
            <div class="price-details">{t['details']}</div>
            <a href="https://t.me/otkachkaabk_bot" target="_blank" class="btn-orange" style="width: 100%; text-align: center;">Оставить заявку</a>
        </div>
        """, unsafe_allow_html=True)

# ===== ОТЗЫВЫ =====
st.markdown('<h2 class="section-title">Отзывы наших клиентов на Авито</h2>', unsafe_allow_html=True)
st.markdown('<p class="section-subtitle">Вы можете доверять нашим ассенизаторам, профессионализму и качеству работ</p>', unsafe_allow_html=True)

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
        st.markdown(f"""
        <div class="review-card">
            <div class="review-name">{name}</div>
            <div class="review-text">«{text}»</div>
        </div>
        """, unsafe_allow_html=True)

# ===== КОНТАКТЫ =====
st.markdown('<h2 class="section-title">Свяжитесь с нами</h2>', unsafe_allow_html=True)
st.markdown('<p class="section-subtitle">Есть вопросы? Нужно откачать септик? Оставьте заявку, и мы свяжемся с вами в ближайшее время.</p>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.markdown("### 📞 Телефоны")
    st.markdown("""
    <div class="contact-item">📞 <a href="tel:+73902212010">+7 (3902) 212-010</a></div>
    <div class="contact-item">📞 <a href="tel:+79130513028">+7 (913) 051-30-28</a></div>
    <div class="contact-item">📞 <a href="tel:+79134467099">+7 (913) 446-70-99</a></div>
    <div class="contact-item">📞 <a href="tel:+79831912010">+7 (983) 191-20-10</a></div>
    """, unsafe_allow_html=True)
    
    st.markdown("### ✉️ Электронная почта")
    st.markdown('<div class="contact-item">📧 <a href="mailto:septikabakan@mail.ru">septikabakan@mail.ru</a></div>', unsafe_allow_html=True)

with col2:
    st.markdown("### 🏢 Реквизиты")
    st.markdown("""
    <p><strong>ИП Качур Максим Васильевич</strong></p>
    <p>ИНН <a href="https://www.rusprofile.ru/ip/317190100007117?print=pdf" target="_blank">190116760265</a></p>
    <br>
    <a href="https://t.me/otkachkaabk_bot" target="_blank" class="btn-yellow">💬 Оставить заявку в Telegram</a>
    """, unsafe_allow_html=True)

# ===== ФУТЕР =====
st.markdown("""
<div class="footer">
    <p style="font-size: 1.3rem; font-weight: 700; margin-bottom: 8px;">🚛 ИП Качур М. В.</p>
    <p style="opacity: 0.9; margin-bottom: 16px;">Откачка септиков в Абакане</p>
    <p style="font-size: 0.95rem; opacity: 0.85;">
        +7 (3902) 212-010 &nbsp;|&nbsp; septikabakan@mail.ru
    </p>
    <p style="margin-top: 24px; font-size: 0.85rem; opacity: 0.7;">
        © 2026 ИП Качур М. В. — Откачка септиков в Абакане. Все права защищены.
    </p>
</div>
""", unsafe_allow_html=True)
