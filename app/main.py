# import streamlit as st
# from langchain_community.document_loaders import WebBaseLoader
# from chains import Chain
# from portfolio import Portfolio
# from utils import clean_text

# def apply_tailwind_css():
#     st.markdown("""
#         <style>
#             @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

#             body {
#                 font-family: 'Inter', sans-serif;
#                 background: linear-gradient(135deg, #0f172a, #1e3a8a, #6d28d9);
#                 background-size: 400% 400%;
#                 animation: gradientShift 25s ease infinite;
#             }

#             @keyframes gradientShift {
#                 0% { background-position: 0% 50%; }
#                 50% { background-position: 100% 50%; }
#                 100% { background-position: 0% 50%; }
#             }

#             h1, h2, h3 {
#                 font-weight: 700;
#                 text-shadow: 0 2px 6px rgba(0,0,0,0.5);
#             }

#             .text-gradient {
#                 background: linear-gradient(to right, #38bdf8, #34d399, #facc15);
#                 -webkit-background-clip: text;
#                 -webkit-text-fill-color: transparent;
#             }

#             div[data-testid="stTextInput"] input {
#                 background-color: rgba(255, 255, 255, 0.05);
#                 color: #f1f5f9;
#                 border: 1px solid rgba(255, 255, 255, 0.2);
#                 border-radius: 1rem;
#                 padding: 0.75rem 1rem;
#                 font-weight: 500;
#                 transition: all 0.3s ease;
#                 box-shadow: 0 4px 20px rgba(0,0,0,0.2);
#             }

#             div[data-testid="stTextInput"] input:focus {
#                 border-color: #38bdf8;
#                 box-shadow: 0 0 10px rgba(56, 189, 248, 0.6);
#             }

#             div[data-testid="stButton"] button {
#                 background-image: linear-gradient(45deg, #38bdf8, #34d399, #fcd34d);
#                 color: #000;
#                 border-radius: 1rem;
#                 padding: 0.75rem 2rem;
#                 font-weight: 600;
#                 font-size: 1rem;
#                 transition: all 0.3s ease;
#                 box-shadow: 0 6px 20px rgba(0,0,0,0.25);
#             }

#             div[data-testid="stButton"] button:hover {
#                 transform: translateY(-3px) scale(1.05);
#                 box-shadow: 0 12px 30px rgba(0,0,0,0.35);
#             }

#             div[data-testid="stButton"] button:active {
#                 transform: scale(0.98);
#                 box-shadow: 0 4px 10px rgba(0,0,0,0.2);
#             }

#             a {
#                 transition: transform 0.2s, box-shadow 0.2s;
#             }

#             a:hover {
#                 transform: translateY(-4px);
#                 box-shadow: 0 8px 20px rgba(0,0,0,0.4);
#             }

#             .card {
#                 background: rgba(255,255,255,0.05);
#                 border-radius: 1rem;
#                 padding: 1rem 1.5rem;
#                 box-shadow: 0 8px 20px rgba(0,0,0,0.3);
#                 transition: transform 0.3s, box-shadow 0.3s;
#             }

#             .card:hover {
#                 transform: translateY(-5px);
#                 box-shadow: 0 12px 30px rgba(0,0,0,0.5);
#             }

#             #MainMenu, footer, header {visibility: hidden;}
#         </style>
#         <script src="https://cdn.tailwindcss.com"></script>
#     """, unsafe_allow_html=True)


# def create_streamlit_app(llm, portfolio, clean_text):
#     apply_tailwind_css()
#     st.markdown("""
#         <div class="text-center p-8">
#             <h1 class="text-5xl md:text-6xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-sky-400 to-emerald-400 mb-4">
#                 📧 AI Cold Mail Generator
#             </h1>
#             <p class="text-lg text-slate-400">
#                 Enter a job posting URL to craft a personalized cold email.
#             </p>
#         </div>
#     """, unsafe_allow_html=True)
#     st.markdown('<div class="max-w-2xl mx-auto">', unsafe_allow_html=True)
#     url_input = st.text_input(
#         "Enter a URL:",
#         placeholder="Paste a job URL here...",
#         label_visibility="collapsed"
#     )
#     submit_button = st.button("✨ Generate Email")
#     st.markdown('</div>', unsafe_allow_html=True)
#     st.markdown("""
#         <div class="max-w-2xl mx-auto mt-12 text-center">
#             <h2 class="text-xl font-semibold text-slate-300">Or, try one of these examples:</h2>
#             <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mt-6 text-left">
#                 <a href="https://jobs.nike.com/job/R-33460" target="_blank" class="block p-4 bg-slate-800/50 border border-slate-700 rounded-lg hover:bg-slate-700/50 transition-colors">
#                     <p class="font-bold text-slate-200">Nike Careers</p>
#                     <p class="text-sm text-slate-400 truncate">Senior Software Engineer</p>
#                 </a>
#                 <a href="https://careers.microsoft.com/us/en/job/1052388/Software-Engineer" target="_blank" class="block p-4 bg-slate-800/50 border border-slate-700 rounded-lg hover:bg-slate-700/50 transition-colors">
#                     <p class="font-bold text-slate-200">Microsoft Careers</p>
#                     <p class="text-sm text-slate-400 truncate">Software Engineer</p>
#                 </a>
#                 <a href="https://www.amazon.jobs/en/jobs/1958977/software-development-engineer" target="_blank" class="block p-4 bg-slate-800/50 border border-slate-700 rounded-lg hover:bg-slate-700/50 transition-colors">
#                     <p class="font-bold text-slate-200">Amazon Jobs</p>
#                     <p class="text-sm text-slate-400 truncate">Software Development Engineer</p>
#                 </a>
#                 <a href="https://careers.google.com/jobs/results/86333933293699782-software-engineer-core" target="_blank" class="block p-4 bg-slate-800/50 border border-slate-700 rounded-lg hover:bg-slate-700/50 transition-colors">
#                     <p class="font-bold text-slate-200">Google Careers</p>
#                     <p class="text-sm text-slate-400 truncate">Software Engineer, Core</p>
#                 </a>
#             </div>
#             <p class="text-xs text-slate-500 mt-6">
#                 Please note: These are example links provided for demonstration. As they are external, their availability is subject to change by the respective owners and they may not always be active.
#             </p>
#         </div>
#     """, unsafe_allow_html=True)
#     if submit_button and url_input:
#         with st.spinner("Analyzing job, querying portfolio, and writing email... 🤖"):
#             try:
#                 loader = WebBaseLoader([url_input])
#                 data = clean_text(loader.load().pop().page_content)
#                 portfolio.load_portfolio()
#                 jobs = llm.extract_jobs(data)
#                 if not jobs:
#                     st.error("Could not extract job information from the URL. Please try another one.")
#                     return
#                 job_titles = [job.get('title', f'Job {i+1}') for i, job in enumerate(jobs)]
#                 tabs = st.tabs(job_titles)
#                 for i, tab in enumerate(tabs):
#                     with tab:
#                         job = jobs[i]
#                         skills = job.get('skills', [])
#                         links = portfolio.query_links(skills)
#                         email = llm.write_mail(job, links)
#                         st.code(email, language=None)
#             except Exception as e:
#                 st.error(f"An Error Occurred: {e}")

# if __name__ == "__main__":
#     st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")
#     chain = Chain()
#     portfolio = Portfolio()
#     create_streamlit_app(chain, portfolio, clean_text)










import streamlit as st
from langchain.document_loaders import WebBaseLoader  # updated import
from chains import Chain
from portfolio import Portfolio
from utils import clean_text

# ---------------- Tailwind CSS ----------------
def apply_tailwind_css():
    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

            body {
                font-family: 'Inter', sans-serif;
                background: linear-gradient(135deg, #0f172a, #1e3a8a, #6d28d9);
                background-size: 400% 400%;
                animation: gradientShift 25s ease infinite;
            }

            @keyframes gradientShift {
                0% { background-position: 0% 50%; }
                50% { background-position: 100% 50%; }
                100% { background-position: 0% 50%; }
            }

            h1, h2, h3 {
                font-weight: 700;
                text-shadow: 0 2px 6px rgba(0,0,0,0.5);
            }

            .text-gradient {
                background: linear-gradient(to right, #38bdf8, #34d399, #facc15);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }

            div[data-testid="stTextInput"] input {
                background-color: rgba(255, 255, 255, 0.05);
                color: #f1f5f9;
                border: 1px solid rgba(255, 255, 255, 0.2);
                border-radius: 1rem;
                padding: 0.75rem 1rem;
                font-weight: 500;
                transition: all 0.3s ease;
                box-shadow: 0 4px 20px rgba(0,0,0,0.2);
            }

            div[data-testid="stTextInput"] input:focus {
                border-color: #38bdf8;
                box-shadow: 0 0 10px rgba(56, 189, 248, 0.6);
            }

            div[data-testid="stButton"] button {
                background-image: linear-gradient(45deg, #38bdf8, #34d399, #fcd34d);
                color: #000;
                border-radius: 1rem;
                padding: 0.75rem 2rem;
                font-weight: 600;
                font-size: 1rem;
                transition: all 0.3s ease;
                box-shadow: 0 6px 20px rgba(0,0,0,0.25);
            }

            div[data-testid="stButton"] button:hover {
                transform: translateY(-3px) scale(1.05);
                box-shadow: 0 12px 30px rgba(0,0,0,0.35);
            }

            div[data-testid="stButton"] button:active {
                transform: scale(0.98);
                box-shadow: 0 4px 10px rgba(0,0,0,0.2);
            }

            a {
                transition: transform 0.2s, box-shadow 0.2s;
            }

            a:hover {
                transform: translateY(-4px);
                box-shadow: 0 8px 20px rgba(0,0,0,0.4);
            }

            .card {
                background: rgba(255,255,255,0.05);
                border-radius: 1rem;
                padding: 1rem 1.5rem;
                box-shadow: 0 8px 20px rgba(0,0,0,0.3);
                transition: transform 0.3s, box-shadow 0.3s;
            }

            .card:hover {
                transform: translateY(-5px);
                box-shadow: 0 12px 30px rgba(0,0,0,0.5);
            }

            #MainMenu, footer, header {visibility: hidden;}
        </style>
        <script src="https://cdn.tailwindcss.com"></script>
    """, unsafe_allow_html=True)


# ---------------- Main App ----------------
def create_streamlit_app(llm, portfolio, clean_text):
    apply_tailwind_css()
    
    # Header
    st.markdown("""
        <div class="text-center p-8">
            <h1 class="text-5xl md:text-6xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-sky-400 to-emerald-400 mb-4">
                📧 AI Cold Mail Generator
            </h1>
            <p class="text-lg text-slate-400">
                Enter a job posting URL to craft a personalized cold email.
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="max-w-2xl mx-auto">', unsafe_allow_html=True)
    url_input = st.text_input(
        "Enter a URL:",
        placeholder="Paste a job URL here...",
        label_visibility="collapsed"
    )
    submit_button = st.button("✨ Generate Email")
    st.markdown('</div>', unsafe_allow_html=True)

    # Example links
    st.markdown("""
        <div class="max-w-2xl mx-auto mt-12 text-center">
            <h2 class="text-xl font-semibold text-slate-300">Or, try one of these examples:</h2>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mt-6 text-left">
                <a href="https://jobs.nike.com/job/R-33460" target="_blank" class="block p-4 bg-slate-800/50 border border-slate-700 rounded-lg hover:bg-slate-700/50 transition-colors">
                    <p class="font-bold text-slate-200">Nike Careers</p>
                    <p class="text-sm text-slate-400 truncate">Senior Software Engineer</p>
                </a>
                <a href="https://careers.microsoft.com/us/en/job/1052388/Software-Engineer" target="_blank" class="block p-4 bg-slate-800/50 border border-slate-700 rounded-lg hover:bg-slate-700/50 transition-colors">
                    <p class="font-bold text-slate-200">Microsoft Careers</p>
                    <p class="text-sm text-slate-400 truncate">Software Engineer</p>
                </a>
            </div>
            <p class="text-xs text-slate-500 mt-6">
                These are example links provided for demonstration. Availability may change.
            </p>
        </div>
    """, unsafe_allow_html=True)

    if submit_button and url_input:
        with st.spinner("Analyzing job, querying portfolio, and writing email... 🤖"):
            try:
                loader = WebBaseLoader([url_input])
                doc = loader.load().pop()
                data = clean_text(doc.page_content)

                portfolio.load_portfolio()
                jobs = llm.extract_jobs(data)

                if not jobs:
                    st.error("Could not extract job information from the URL. Please try another one.")
                    return

                job_titles = [job.get('title', f'Job {i+1}') for i, job in enumerate(jobs)]
                tabs = st.tabs(job_titles)

                for i, tab in enumerate(tabs):
                    with tab:
                        job = jobs[i]
                        skills = job.get('skills', [])
                        links = portfolio.query_links(skills)
                        email = llm.write_mail(job, links)
                        st.code(email)

            except Exception as e:
                st.error(f"An Error Occurred: {e}")


# ---------------- Entry Point ----------------
if __name__ == "__main__":
    st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")
    chain = Chain()
    portfolio = Portfolio()
    create_streamlit_app(chain, portfolio, clean_text)
