def load_css():
    """Return an HTML <style> string with the dark theme CSS.

    Returns:
        str: A string containing an HTML `<style>` block with dark theme styles. Caller must inject
        this string into the page using `st.markdown(load_css(), unsafe_allow_html=True)`.
    """

    dark = """
    <style>

    /* ===========================
       GOOGLE FONT
    ============================ */

    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

    *{
        font-family:'Inter',sans-serif;
    }

    /* ===========================
       COLOR VARIABLES
    ============================ */

    :root{
        --bg:#0D0D0D;
        --sidebar:#161616;
        --card:#1F1F1F;
        --border:#2E2E2E;
        --text:#E6E6E6; /* main text color */
        --subtext:#9A9A9A; /* secondary text */
        --muted:#7A7A7A;
        --primary:#FFFFFF;
        --hover:#242424;
        --input:#1B1B1B;
        --glow:rgba(255,255,255,.22);
    }

    /* constrain main content and add padding to match design */
    div.block-container{
        max-width:1200px;
        padding-top:2rem;
        padding-left:3rem;
        padding-right:3rem;
        margin:auto;
    }

    .stApp{
        background:var(--bg);
        color:var(--text);
    }

    section[data-testid="stSidebar"]{
        background:var(--sidebar);
        border-right:1px solid var(--border);
        width:320px !important;
        min-width:320px !important;
        max-width:320px !important;
    }

    /* Sidebar extras */
    .sidebar-header{ display:flex; align-items:center; gap:12px; padding:12px 8px; }
    .sidebar-header .logo{ width:44px; height:44px; border-radius:10px; display:flex; align-items:center; justify-content:center; background:rgba(255,255,255,.04); border:1px solid rgba(255,255,255,.06); }

    .model-card{ background:transparent; padding:10px 6px; border-radius:12px; border:1px solid rgba(255,255,255,.03); margin-top:6px; }

    .profile-card{ margin-top:10px; padding:10px; border-radius:12px; border:1px solid rgba(255,255,255,.03); }

    .nav-button{ text-align:left; font-weight:600; display:block; padding:12px 14px; border-radius:12px; }

    header{ visibility:hidden; }
    footer{ visibility:hidden; }
    #MainMenu{ visibility:hidden; }
    /* hide Streamlit multipage nav and collapse header button */
    [data-testid="stSidebarNav"]{ display:none; }
    button[kind="header"]{ display:none; }

    h1{
        font-size:56px;
        font-weight:800;
        color:var(--text);
        margin-bottom:12px;
        line-height:1.05;
    }

    h2{ color:var(--text); font-weight:700; }
    h3{ color:var(--text); }

    p{
        color:var(--subtext);
        font-size:16px;
        margin-bottom:8px;
    }

    /* base text */
    body, .stApp, .stMarkdown, .stText, .stRadio{
        color:var(--text);
        font-size:16px;
    }

    .stButton>button{
        width:100%;
        background:var(--card);
        color:var(--text);
        border:1px solid var(--border);
        border-radius:14px;
        height:64px; /* slightly larger buttons */
        transition:.25s;
        font-size:16px;
        font-weight:600;
        padding:12px 18px;
    }

    .stButton>button:hover{
        background:var(--hover);
        border:1px solid rgba(255,255,255,.18);
        box-shadow:0 8px 30px rgba(0,0,0,.5);
        transform:translateY(-3px);
    }

    .stChatInput{
        position:fixed;
        bottom:20px;
        left:330px;
        right:30px;
        z-index:999;
    }
    .stChatInput textarea{
        background:var(--input)!important;
        color:var(--text)!important;
        border-radius:20px!important;
        min-height:56px;
        padding:12px !important;
    }

    div[data-testid="metric-container"]{
        background:var(--card);
        border:1px solid var(--border);
        border-radius:20px;
        padding:20px;
    }

    .feature-card{
        background:var(--card);
        border:1px solid var(--border);
        border-radius:20px;
        padding:25px;
        transition:.35s;
        cursor:pointer;
        min-height:180px;
    }

    .feature-card:hover{
        transform:translateY(-8px);
        border:1px solid white;
        box-shadow:0 0 30px rgba(255,255,255,.25);
    }

    .nav-button{
        width:100%;
        background:#1D1D1D;
        padding:18px;
        border-radius:15px;
        color:white;
        margin-bottom:12px;
        transition:.35s;
        border:1px solid transparent;
    }

    .nav-button:hover{
        border:1px solid white;
        box-shadow:0 0 20px rgba(255,255,255,.3);
    }

    .user-msg{
        background:#2A2A2A;
        border-radius:18px;
        padding:18px;
        margin:12px 0;
    }

    .bot-msg{
        background:#171717;
        border-radius:18px;
        padding:18px;
        margin:12px 0;
    }

    .hero{
        text-align:center;
        padding:80px 24px 36px; /* more vertical space */
        border:1px solid rgba(255,255,255,.08);
        border-radius:24px;
        background:linear-gradient(135deg, rgba(255,255,255,.06), rgba(255,255,255,.02));
        margin-bottom:28px;
    }

    .hero-icon{
        width:92px; /* larger icon */
        height:92px;
        border-radius:18px;
        display:flex;
        align-items:center;
        justify-content:center;
        font-size:44px;
        margin:0 auto 20px auto;
        background:rgba(255,255,255,.06);
        border:1px solid rgba(255,255,255,.16);
        box-shadow:0 6px 20px rgba(0,0,0,.25);
    }

    .hero-title{
        font-size:clamp(34px, 4.4vw, 56px);
        font-weight:800;
        color:var(--text);
        margin-bottom:12px;
        letter-spacing:-0.02em;
    }

    .hero-subtitle{
        font-size:18px;
        color:#a5a5a5;
        margin:0 auto 8px auto;
        max-width:880px;
        line-height:1.8;
    }

    .divider-line{
        height:1px;
        background:linear-gradient(90deg, transparent, rgba(255,255,255,.35), transparent);
        margin-top:22px;
    }

    .gradient{
        background:linear-gradient(90deg, #ffffff, #cfcfcf, #ffffff);
        background-size:200% auto;
        -webkit-background-clip:text;
        -webkit-text-fill-color:transparent;
        animation:gradientMove 5s linear infinite;
    }

    .quick-actions{
        margin-top:12px;
        display:flex;
        gap:18px;
        justify-content:center;
        flex-wrap:wrap;
    }

    .stButton>button{
        min-height:160px;
        padding:18px 22px;
        white-space:pre-line;
        text-align:center;
        font-size:15px;
        line-height:1.4;
        background:linear-gradient(135deg, rgba(255,255,255,.05), rgba(255,255,255,.02));
        border:1px solid rgba(255,255,255,.08);
        border-radius:18px;
        backdrop-filter:blur(8px);
        box-shadow:0 10px 40px rgba(0,0,0,.45);
        transition:all .28s ease;
        max-width:300px; /* slightly larger */
        min-width:240px;
        margin:8px auto !important;
        display:flex;
        flex-direction:column;
        align-items:center;
        justify-content:center;
    }
    .stButton>button:hover{
        border:1px solid rgba(255,255,255,.36);
        transform:translateY(-8px);
        box-shadow:0 18px 50px rgba(255,255,255,.06);
    }

    .quick-actions .stButton{
        margin-bottom:8px;
    }

    .quick-actions-wrap{ max-width:1200px; margin:0 auto 8px auto; display:flex; justify-content:center; }

    .hero{ padding:48px 24px 28px; }

    @media (min-width:1100px){
        .quick-actions .stButton > button{ min-height:180px; }
    }

    @keyframes gradientMove{
        from{ background-position:0%; }
        to{ background-position:200%; }
    }

    ::-webkit-scrollbar{ width:10px; }
    ::-webkit-scrollbar-thumb{ background:#3A3A3A; border-radius:50px; }
    ::-webkit-scrollbar-thumb:hover{ background:#606060; }

    </style>
    """

    return dark
