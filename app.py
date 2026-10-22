import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Откачка септика Абакан — вывоз ЖБО от 1400 ₽ | ИП Качур М.В.",
    page_icon="🚛",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ===== SEO meta + CSS =====
st.markdown(
    """
    <meta name="description" content="Откачка септика в Абакане и Хакасии. Вывоз ЖБО, откачка выгребных ям и колодцев. Цены от 1400 ₽. Работаем более 15 лет. Звоните: +7 (3902) 212-010">
    <meta name="keywords" content="откачка септика Абакан, вывоз ЖБО Абакан, откачка септиков Хакасия, ассенизатор Абакан, откачка выгребных ям Абакан">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://абакансептик.рф/">

    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"], .stMarkdown, p, h1, h2, h3, h4 {
        font-family: 'Outfit', sans-serif !important;
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display: none;}
    div[data-testid="stToolbar"] {display: none;}

    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 1rem !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
        max-width: 1180px;
    }

    .stApp { background-color: #ffffff; }

    @keyframes fadeUp {
        from { opacity: 0; transform: translateY(18px); }
        to   { opacity: 1; transform: translateY(0); }
    }
    @keyframes fadeIn {
        from { opacity: 0; }
        to   { opacity: 1; }
    }
    @keyframes softPulse {
        0%, 100% { box-shadow: 0 4px 14px rgba(232, 93, 4, 0.25); }
        50%      { box-shadow: 0 6px 22px rgba(232, 93, 4, 0.4); }
    }
    @keyframes drive {
        0%   { transform: translateX(0) rotate(0deg); }
        20%  { transform: translateX(6px) rotate(1deg); }
        40%  { transform: translateX(12px) rotate(0deg); }
        60%  { transform: translateX(6px) rotate(-1deg); }
        80%  { transform: translateX(2px) rotate(0.5deg); }
        100% { transform: translateX(0) rotate(0deg); }
    }
    .truck-drive {
        display: inline-block;
        animation: drive 2.2s ease-in-out infinite;
        transform-origin: center bottom;
    }

    .anim-fade-up { animation: fadeUp 0.55s ease-out both; }
    .anim-fade-up-d1 { animation: fadeUp 0.55s ease-out 0.08s both; }
    .anim-fade-up-d2 { animation: fadeUp 0.55s ease-out 0.16s both; }
    .anim-fade-in { animation: fadeIn 0.6s ease-out both; }

    .btn-orange {
        background: linear-gradient(90deg, #e85d04, #f48c06) !important;
        color: white !important;
        padding: 13px 26px !important;
        border-radius: 10px !important;
        font-weight: 600 !important;
        text-decoration: none !important;
        display: inline-block !important;
        margin: 6px 6px !important;
        border: none !important;
        font-size: 1.05rem !important;
        letter-spacing: 0.01em;
        transition: transform 0.2s ease, box-shadow 0.2s ease !important;
    }
    .btn-orange:hover {
        transform: translateY(-3px) scale(1.02);
        box-shadow: 0 8px 22px rgba(232, 93, 4, 0.4);
        color: white !important;
    }

    .btn-yellow {
        background: #ffc107 !important;
        color: #222 !important;
        padding: 14px 28px !important;
        border-radius: 10px !important;
        font-weight: 700 !important;
        text-decoration: none !important;
        display: inline-block !important;
        border: none !important;
        font-size: 1.1rem !important;
        transition: transform 0.2s ease, box-shadow 0.2s ease !important;
        animation: softPulse 2.4s ease-in-out infinite;
    }
    .btn-yellow:hover {
        background: #ffca2c !important;
        color: #222 !important;
        transform: translateY(-3px) scale(1.03);
    }

    .price-card {
        background: white;
        border: 2px solid #ffe0b2;
        border-radius: 16px;
        padding: 26px 20px;
        text-align: center;
        height: 100%;
        box-shadow: 0 4px 14px rgba(0,0,0,0.05);
        transition: transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease;
    }
    .price-card:hover {
        transform: translateY(-6px);
        border-color: #e85d04;
        box-shadow: 0 12px 28px rgba(232, 93, 4, 0.15);
    }
    .price-title {
        font-size: 1.15rem;
        font-weight: 700;
        color: #333;
    }
    .price-value {
        font-size: 2.15rem;
        font-weight: 800;
        color: #e85d04;
        margin: 10px 0;
        letter-spacing: -0.03em;
    }
    .price-details {
        font-size: 1rem;
        color: #555;
        line-height: 1.55;
        margin-bottom: 16px;
    }

    .contact-item {
        font-size: 1.15rem;
        margin: 8px 0;
    }
    .contact-item a {
        color: #e85d04;
        text-decoration: none;
        font-weight: 600;
        transition: color 0.2s ease;
    }
    .contact-item a:hover {
        color: #c2410c;
        text-decoration: underline;
    }

    .section-title {
        font-size: 1.75rem;
        font-weight: 800;
        color: #1a1a1a;
        text-align: center;
        margin: 1.6rem 0 0.35rem 0;
        letter-spacing: -0.02em;
    }
    .section-subtitle {
        text-align: center;
        color: #666;
        margin-bottom: 1.1rem;
        font-size: 1.05rem;
    }

    .footer-box {
        background: linear-gradient(90deg, #e85d04 0%, #f48c06 100%);
        color: white;
        text-align: center;
        padding: 32px 18px;
        border-radius: 14px;
        margin-top: 2rem;
        margin-bottom: 0.4rem;
    }

    .map-wrap {
        border-radius: 16px;
        overflow: hidden;
        box-shadow: 0 8px 28px rgba(0,0,0,0.1);
        border: 2px solid #ffe0b2;
        margin-top: 0.5rem;
    }

    .seo-block {
        background: #fafafa;
        border-radius: 12px;
        padding: 20px 24px;
        margin: 1.2rem 0;
        border: 1px solid #eee;
        font-size: 1.02rem;
        color: #333;
        line-height: 1.65;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ===== HEADER =====
st.markdown(
    """
    <div class="anim-fade-in" style="background: linear-gradient(90deg, #e85d04 0%, #f48c06 100%); 
                padding: 14px 22px; border-radius: 12px; margin-bottom: 18px;
                display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px;">
        <div>
            <div style="font-size: 1.4rem; font-weight: 700; color: white; letter-spacing: -0.01em;">
                <span class="truck-drive">🚛</span> ИП Качур М. В.
            </div>
            <div style="font-size: 0.95rem; color: rgba(255,255,255,0.92);">Откачка септика в Абакане и Хакасии</div>
        </div>
        <a href="tel:+73902212010" 
           style="background: white; color: #e85d04; padding: 10px 18px; border-radius: 10px; 
                  font-weight: 700; text-decoration: none; font-size: 1rem;">
            📞 +7 (3902) 212-010
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

# ===== HERO =====
col1, col2 = st.columns([1.15, 1], gap="medium")

with col1:
    st.markdown(
        """
        <div class="anim-fade-up">
            <h1 style="font-size: 2.2rem; font-weight: 800; color: #e85d04; line-height: 1.18; margin: 0 0 0.85rem 0; letter-spacing: -0.03em;">
                Откачка септика в Абакане — быстро и недорого
            </h1>
            <p style="font-size: 1.1rem; color: #444; line-height: 1.6; margin: 0 0 0.5rem 0;">
                – <strong>Откачка септиков и вывоз ЖБО в Абакане</strong>: объём от 1 до 10 м³ — для частных домов, предприятий и ЖКХ.
            </p>
            <p style="font-size: 1.1rem; color: #444; line-height: 1.6; margin: 0 0 0.5rem 0;">
                – Работаем по Абакану, Республике Хакасия и югу Красноярского края. Приглашаем частных лиц, организации и коммунальные службы.
            </p>
            <p style="font-size: 1.1rem; color: #444; line-height: 1.6; margin: 0 0 1rem 0;">
                – ИП Качур Максим Васильевич — более <strong>15 лет</strong> откачки септиков и вывоза ЖБО. Цены от 1 400 ₽.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="anim-fade-up-d1" style="display: flex; flex-wrap: wrap; justify-content: center; gap: 10px; margin-top: 4px;">
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
    st.markdown('<div class="anim-fade-up-d2">', unsafe_allow_html=True)
    st.image(
        "https://xn--80aaacwsldyvuo.xn--p1ai/wp-content/uploads/2024/11/e2776ed26915ce5a3e586d2b3941fcb7.png",
        use_container_width=True,
        caption="Ассенизатор для откачки септика в Абакане"
    )
    st.markdown('</div>', unsafe_allow_html=True)

# ===== SEO-текст (видим поисковикам) =====
st.markdown(
    """
    <div class="seo-block anim-fade-up">
        <strong>Откачка септика Абакан</strong> — услуга ИП Качур М. В. Выполняем откачку септиков, выгребных ям, колодцев и луж в городе Абакан, по всей Республике Хакасия и на юге Красноярского края.
        Современные ассенизаторы объёмом до 10 м³, оперативный выезд, прозрачные цены. Заказать <strong>откачку септика в Абакане</strong> можно по телефону
        <a href="tel:+73902212010" style="color:#e85d04; font-weight:600;">+7 (3902) 212-010</a>
        или через Telegram. Также оказываем <strong>вывоз ЖБО в Абакане</strong> для частных домов, организаций и ЖКХ.
    </div>
    """,
    unsafe_allow_html=True
)

# ===== ПОЧЕМУ МЫ — АККОРДЕОН =====
st.markdown('<div class="section-title anim-fade-up">Почему выбирают нашу откачку септиков в Абакане</div>', unsafe_allow_html=True)
st.markdown('<div class="section-subtitle">Факты о компании — опыт, цены и качество вывоза ЖБО</div>', unsafe_allow_html=True)

features = [
    ("1", "Очистка сточных вод в Абакане и Хакасии: 15 лет опыта",
     "Мы предлагаем Вам откачку выгребных ям, септиков, колодцев, луж в г.Абакане, по Республике Хакасия и югу Красноярского края, имея опыт в данной сфере более 15 лет"),
    ("2", "Вывоз ЖБО в Абакане: доступные цены, высокая эффективность",
     "Мы оказываем услуги по вывозу ЖБО в г. Абакане по приемлемой цене, являясь при этом конкурентноспособной преуспевающей компанией"),
    ("3", "Санитарная чистота: ваш объект в надёжных руках",
     "Мы всегда готовы помочь содержать Ваше предприятие, объект или частный дом в требуемом санитарно-экологическом состоянии"),
    ("4", "Индивидуальный подход, оперативность, профессионализм: мы гарантируем результат",
     "Проявляя индивидуальный подход, оперативность, профессиональное отношение к делу и клиенту, мы зарекомендовали себя как ответственный исполнитель"),
    ("5", "Освобождение от воды: от остановок до жилых домов",
     "Наши ассенизаторы откачают воду из луж: освободят от воды остановки общественного транспорта, территории у магазинов, торговых центров и жилых домов"),
    ("6", "Команда профессионалов: работаем на результат",
     "У нас работает слаженная команда профессионалов, которые знают и любят свое дело"),
    ("7", "Современная техника: бесперебойная работа, гарантированное качество",
     "Вся техника находится в отличном состоянии и обслуживается в собственных боксах, оборудованных всем необходимым для ремонта"),
]

accordion_items = "".join([
    f"""
    <div class="acc-item" onclick="toggleAcc(this)">
      <div class="acc-header">
        <span class="acc-num">{num}</span>
        <span class="acc-title">{title}</span>
        <span class="acc-arrow">›</span>
      </div>
      <div class="acc-body">{content}</div>
    </div>
    """
    for num, title, content in features
])

accordion_html = f"""
<style>
  .acc-wrap {{ font-family: 'Outfit', sans-serif; max-width: 100%; padding-bottom: 16px; }}
  .acc-item {{
    background: #fff8f0;
    border-left: 5px solid #e85d04;
    border-radius: 12px;
    margin-bottom: 10px;
    cursor: pointer;
    transition: box-shadow 0.25s ease, transform 0.2s ease;
    overflow: hidden;
  }}
  .acc-item:hover {{ box-shadow: 0 6px 18px rgba(232, 93, 4, 0.12); }}
  .acc-item.open {{ box-shadow: 0 6px 20px rgba(232, 93, 4, 0.15); }}
  .acc-header {{
    display: flex;
    align-items: center;
    gap: 14px;
    padding: 16px 18px;
  }}
  .acc-num {{
    font-size: 1.45rem;
    font-weight: 800;
    color: #e85d04;
    min-width: 28px;
    letter-spacing: -0.02em;
  }}
  .acc-title {{
    font-size: 1.05rem;
    color: #222;
    font-weight: 600;
    flex: 1;
    line-height: 1.35;
  }}
  .acc-arrow {{
    font-size: 1.4rem;
    color: #e85d04;
    font-weight: 700;
    transition: transform 0.3s ease;
    transform: rotate(90deg);
  }}
  .acc-item.open .acc-arrow {{ transform: rotate(-90deg); }}
  .acc-body {{
    max-height: 0;
    overflow: hidden;
    transition: max-height 0.35s ease, padding 0.3s ease;
    padding: 0 18px 0 60px;
    font-size: 1rem;
    color: #444;
    line-height: 1.55;
  }}
  .acc-item.open .acc-body {{
    max-height: 220px;
    padding: 0 18px 16px 60px;
  }}
</style>

<div class="acc-wrap">
  {accordion_items}
</div>

<script>
function toggleAcc(el) {{
  const wasOpen = el.classList.contains('open');
  document.querySelectorAll('.acc-item').forEach(i => i.classList.remove('open'));
  if (!wasOpen) el.classList.add('open');
}}
</script>
"""

components.html(accordion_html, height=720)

# ===== ТАРИФЫ =====
st.markdown('<div class="section-title anim-fade-up">Цены на откачку септика в Абакане</div>', unsafe_allow_html=True)
st.markdown('<div class="section-subtitle">Стоимость зависит от объёма, удалённости и сложности. Вывоз ЖБО — от 1 400 ₽</div>', unsafe_allow_html=True)

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
            <div class="price-card anim-fade-up">
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

# ===== ОТЗЫВЫ — КАРУСЕЛЬ =====
st.markdown('<div class="section-title anim-fade-up">Отзывы об откачке септиков в Абакане</div>', unsafe_allow_html=True)
st.markdown('<div class="section-subtitle">Клиенты о вывозе ЖБО и работе ассенизаторов</div>', unsafe_allow_html=True)

reviews = [
    ("Женя", "Очень хорошие ребята! Сразу взяли трубку и даже раньше приехали! Очень довольна. Молодцы! Пользуюсь услугой второй раз! Рекомендую!"),
    ("Василий", "Всё отлично, приехали очень быстро! Цена умеренная!"),
    ("Олеся", "Работа выполнена быстро, качественно, спасибо!"),
    ("Евгения", "Все оперативно, промыли, откачали, спасибо! Рекомендую."),
    ("Глеб", "Работа выполнена оперативно и качественно."),
    ("S13", "Всё отлично! приехали в этот же день как позвонили, откачали как положено. 10 куб."),
]

carousel_html = f"""
<div style="font-family: 'Outfit', sans-serif; max-width: 100%; margin: 0 auto; padding-bottom: 12px;">
  <div id="carousel" style="position: relative; overflow: hidden; border-radius: 16px;">
    <div id="track" style="display: flex; transition: transform 0.45s cubic-bezier(0.25, 0.8, 0.25, 1);">
      {''.join([
        f'''
        <div class="slide" style="min-width: 100%; box-sizing: border-box; padding: 8px 4px;">
          <div style="background: #fafafa; border: 1px solid #eee; border-radius: 16px; padding: 28px 32px; 
                      text-align: center; box-shadow: 0 4px 16px rgba(0,0,0,0.06); min-height: 150px;
                      display: flex; flex-direction: column; justify-content: center;">
            <div style="font-weight: 700; color: #e85d04; font-size: 1.2rem; margin-bottom: 12px;">{name}</div>
            <div style="font-size: 1.08rem; color: #444; font-style: italic; line-height: 1.55;">«{text}»</div>
          </div>
        </div>
        ''' for name, text in reviews
      ])}
    </div>
  </div>

  <div style="display: flex; justify-content: center; align-items: center; gap: 16px; margin-top: 20px; padding-bottom: 8px;">
    <button onclick="prev()" style="
      width: 44px; height: 44px; border-radius: 50%; border: 2px solid #e85d04; background: white;
      color: #e85d04; font-size: 1.3rem; cursor: pointer; display: flex; align-items: center; justify-content: center;
      transition: all 0.2s; font-weight: 700; flex-shrink: 0;
    " onmouseover="this.style.background='#e85d04'; this.style.color='white'"
       onmouseout="this.style.background='white'; this.style.color='#e85d04'">‹</button>

    <div id="dots" style="display: flex; gap: 8px; align-items: center;"></div>

    <button onclick="next()" style="
      width: 44px; height: 44px; border-radius: 50%; border: 2px solid #e85d04; background: white;
      color: #e85d04; font-size: 1.3rem; cursor: pointer; display: flex; align-items: center; justify-content: center;
      transition: all 0.2s; font-weight: 700; flex-shrink: 0;
    " onmouseover="this.style.background='#e85d04'; this.style.color='white'"
       onmouseout="this.style.background='white'; this.style.color='#e85d04'">›</button>
  </div>
</div>

<script>
  const total = {len(reviews)};
  let idx = 0;
  const track = document.getElementById('track');
  const dotsEl = document.getElementById('dots');

  function renderDots() {{
    dotsEl.innerHTML = '';
    for (let i = 0; i < total; i++) {{
      const d = document.createElement('div');
      d.style.cssText = `width:10px;height:10px;border-radius:50%;cursor:pointer;transition:all 0.25s;
        background:${{i === idx ? '#e85d04' : '#ddd'}}; transform:${{i === idx ? 'scale(1.25)' : 'scale(1)'}}`;
      d.onclick = () => {{ idx = i; update(); }};
      dotsEl.appendChild(d);
    }}
  }}

  function update() {{
    track.style.transform = `translateX(-${{idx * 100}}%)`;
    renderDots();
  }}

  function next() {{ idx = (idx + 1) % total; update(); }}
  function prev() {{ idx = (idx - 1 + total) % total; update(); }}

  setInterval(next, 4500);
  update();
</script>
"""

components.html(carousel_html, height=320)

# ===== КАРТА =====
st.markdown('<div class="section-title anim-fade-up">Откачка септика на карте Абакана</div>', unsafe_allow_html=True)
st.markdown('<div class="section-subtitle">Выезжаем по Абакану, Хакасии и югу Красноярского края</div>', unsafe_allow_html=True)

st.markdown('<div class="map-wrap anim-fade-up">', unsafe_allow_html=True)
components.html(
    """
    <iframe 
        src="https://yandex.ru/map-widget/v1/?um=constructor%3A0403aa07c737a80100a91144e0d12fe4712afbaf35a17839453cf0d5f6120f32&source=constructor" 
        width="100%" 
        height="420" 
        frameborder="0" 
        allowfullscreen="true"
        style="display:block; border:0;">
    </iframe>
    """,
    height=430,
)
st.markdown('</div>', unsafe_allow_html=True)

# ===== FAQ для SEO =====
st.markdown('<div class="section-title anim-fade-up">Частые вопросы об откачке септика в Абакане</div>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="seo-block anim-fade-up">
        <p><strong>Сколько стоит откачка септика в Абакане?</strong><br>
        От 1 400 ₽ за объём до 4 м³. Тариф до 6 м³ — 1 700 ₽, от 7 до 10 м³ — 2 400 ₽. Точная цена зависит от удалённости и сложности.</p>
        <p><strong>Как быстро приедет ассенизатор?</strong><br>
        Обычно в день обращения. Звоните: +7 (3902) 212-010 или оставьте заявку в Telegram.</p>
        <p><strong>Работаете ли вы за пределами Абакана?</strong><br>
        Да. Откачка септиков и вывоз ЖБО — по Республике Хакасия и югу Красноярского края.</p>
        <p><strong>Что входит в услугу?</strong><br>
        Откачка септика / выгребной ямы / колодца, вывоз ЖБО, работа оператора. Шланг 10 м, техника до 10 м³.</p>
    </div>
    """,
    unsafe_allow_html=True
)

# ===== КОНТАКТЫ =====
st.markdown('<div class="section-title anim-fade-up">Заказать откачку септика в Абакане</div>', unsafe_allow_html=True)
st.markdown('<div class="section-subtitle">Телефоны и заявка — ответим быстро</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="medium")

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
        <p style="margin:0 0 6px 0; font-size:1.1rem;"><strong>ИП Качур Максим Васильевич</strong></p>
        <p style="margin:0 0 14px 0; font-size:1.05rem;">ИНН <a href="https://www.rusprofile.ru/ip/317190100007117?print=pdf" target="_blank" style="color:#e85d04; font-weight:600;">190116760265</a></p>
        <p style="margin:0 0 14px 0; font-size:1rem; color:#555;">Абакан, Республика Хакасия — откачка септиков и вывоз ЖБО</p>
        <a href="https://t.me/otkachkaabk_bot" target="_blank" class="btn-yellow">
            💬 Оставить заявку в Telegram
        </a>
        """,
        unsafe_allow_html=True
    )

# ===== ФУТЕР =====
st.markdown(
    """
    <div class="footer-box anim-fade-in">
        <div style="font-size: 1.3rem; font-weight: 700; margin-bottom: 5px; letter-spacing: -0.01em;">
            <span class="truck-drive">🚛</span> ИП Качур М. В.
        </div>
        <div style="opacity: 0.92; margin-bottom: 10px; font-size: 1.05rem;">Откачка септика в Абакане · Вывоз ЖБО · Хакасия</div>
        <div style="font-size: 1rem; opacity: 0.9;">
            +7 (3902) 212-010 &nbsp;|&nbsp; septikabakan@mail.ru
        </div>
        <div style="margin-top: 16px; font-size: 0.85rem; opacity: 0.75;">
            © 2026 ИП Качур М. В. — Откачка септиков в Абакане. Все права защищены.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
