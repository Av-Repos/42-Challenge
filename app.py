import streamlit as st
import json
import os
import ast
from objective import evaluate_solution
import numpy as np

st.set_page_config(
    page_title=":heart:4u2:heart:",
    layout="wide"
)

def set_bg(png_file):
    import base64
    with open(png_file, "rb") as f:
        data = base64.b64encode(f.read()).decode()

    st.markdown(
        f"""
        <style>
        /* Background image */
        [data-testid="stAppViewContainer"] {{
            background-image: url("data:image/avif;base64,{data}");
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
        }}

        /* Main layout */
        [data-testid="stMain"] {{
            min-height: 100vh;
            display: flex;
        }}

        /* Content card */
        .block-container {{
            margin: auto;
            border-radius: 16px;
            padding: 2.5rem 3rem;
            max-width: 95%;
        }}

        /* Light mode */
        @media (prefers-color-scheme: light) {{
            .block-container {{
                background-color: rgba(255, 255, 255, 0.92);
                color: #000;
            }}
        }}

        /* Dark mode */
        @media (prefers-color-scheme: dark) {{
            .block-container {{
                background-color: rgba(20, 20, 20, 0.92);
                color: #fff;
            }}
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_bg("background.avif")

LEADERBOARD_FILE = "data/leaderboard.json"

# Load leaderboard
def load_leaderboard():
    if not os.path.exists(LEADERBOARD_FILE):
        return []
    with open(LEADERBOARD_FILE, "r") as f:
        return json.load(f)

# Save leaderboard
def save_leaderboard(lb):
    with open(LEADERBOARD_FILE, "w") as f:
        json.dump(lb, f, indent=2)

# Submit a new entry only if better
def submit_entry(name, solution):
    score = evaluate_solution(solution)
    leaderboard = load_leaderboard()
    existing_entry = next((entry for entry in leaderboard if entry["name"] == name), None)

    if existing_entry and score <= existing_entry["score"]:
        return False, existing_entry["score"]  # Keep best

    leaderboard = [entry for entry in leaderboard if entry["name"] != name]
    leaderboard.append({"name": name, "solution": solution, "score": score})
    leaderboard = sorted(leaderboard, key=lambda x: x["score"], reverse=True)
    save_leaderboard(leaderboard)
    return True, score


# Load the docs
docs = open('docs/getting_started.md', 'r')
docs_getting_started = docs.read()
docs.close()

docs = open('docs/solution_format.md', 'r')
docs_solution_format = docs.read()
docs.close()

docs = open('docs/about_problem.md', 'r')
docs_about_sop = docs.read()
docs.close()


# Streamlit page config
st.set_page_config(page_title="4u2", layout="wide")

# Title and view-only toggle in top-right
header_col1, header_spacer, header_col2 = st.columns([15, 5, 1])

def toggle_view():
    st.session_state.view_only_mode = not st.session_state.view_only_mode
    button_label = "📄 Documentación" if not st.session_state.get("view_only_mode", True) else "🏠 Página principal"


with header_col1:
    st.title("❤️4u2❤️ Optimization Challenge")
    button_label = "📄 Documentación" if not st.session_state.get("view_only_mode", False) else "🏠 Página principal"
    # if st.button(button_label):
    #     st.session_state.view_only_mode = not st.session_state.view_only_mode
    #     button_label = "📄 Documentación" if not st.session_state.get("view_only_mode", True) else "🏠 Página principal"
    st.button(button_label, on_click=toggle_view)

with header_col2:
    if "view_only_mode" not in st.session_state:
        st.session_state.view_only_mode = False
    # if st.button("📄\nDocs"):
    #     st.session_state.view_only_mode = not st.session_state.view_only_mode

# View-only leaderboard mode
if st.session_state.view_only_mode:
    # st.subheader("🏆 Live Leaderboard")
    # leaderboard = load_leaderboard()
    # if leaderboard:
    #     for i, entry in enumerate(leaderboard):
    #         st.markdown(f"**#{i+1} – {entry['name']}** : {entry['score']:.2f}")
    # else:
    #     st.info("No submissions yet.")

    with st.expander("Problema 🧑‍🏫"):
        st.markdown(docs_about_sop)

    with st.expander("Formato de solución 📤"):
        st.markdown(docs_solution_format)

    with st.expander("Código de apoyo 🚀"):
        st.markdown(docs_getting_started)

    st.stop()


# 2-column layout: left = form, right = leaderboard
col1, col2 = st.columns(2)

# === Left side: Submission form ===
with col1:
    st.header("📤 Envía tu solución")
    with st.form("submission_form"):
        name = st.text_input("Nombre del participante")
        solution_str = st.text_area("Tu solución (e.g., [2, 0, 1, 3])")

        btn_col1, btn_col2 = st.columns([1, 1])
        with btn_col1:
            submitted = st.form_submit_button("🚀 Enviar")
        with btn_col2:
            check_position = st.form_submit_button("🔍 Comprobar mi posición")

        if submitted:
            if not name.strip():
                st.warning("⚠️ Por favor, indica tu nombre antes de enviar.")
            else:
                try:
                    solution = ast.literal_eval(solution_str)
                    if not isinstance(solution, list):
                        st.error("Tu solución debe de ser una lista.")
                    else:
                        success, result = submit_entry(name, solution)
                        if success:
                            st.success("✅ ¡Solución aceptada y clasificación actualizada!")
                        else:
                            st.warning(f"⚠️ Tu nueva solución ({evaluate_solution(solution):.2f}) no es mejor que tu mejor solución hasta el momento ({result:.2f}). No se ha registrado el envío.")
                except Exception as e:
                    st.error(f"❌ Error al procesar la solución: {e}")

        elif check_position:
            if not name.strip():
                st.warning("⚠️ Por favor, indica tu nombre para comprobar tu posición.")
            else:
                leaderboard = load_leaderboard()
                entry = next((entry for entry in leaderboard if entry["name"] == name), None)
                if entry:
                    position = sorted(leaderboard, key=lambda x: x["score"], reverse=True).index(entry) + 1
                    st.info(f"📊 Te encuentras en la posición **#{position}** con una puntuación de **{entry['score']:.2f}**.")
                else:
                    st.warning("❌ Nombre no encontrado en la clasificación.")

with col2:
    st.header("🏆 Clasificación en directo")
    leaderboard = load_leaderboard()

    if leaderboard:
        for i, entry in enumerate(leaderboard):
            if i == 0:
                bg = "#FFD700"   # Gold
                text = "#000000"
                emoji = "🥇"
                size = 40
            elif i == 1:
                bg = "#C0C0C0"   # Silver
                text = "#000000"
                emoji = "🥈"
                size = 40
            elif i == 2:
                bg = "#CD7F32"   # Bronze
                text = "#000000"
                emoji = "🥉"
                size = 40
            else:
                bg = "transparent"
                text = "inherit"
                emoji = ""
                size = 20

            st.markdown(
                f"""
                <div style="
                    background-color: {bg};
                    color: {text};
                    padding: 0.6rem 0.8rem;
                    border-radius: 8px;
                    margin-bottom: 0.4rem;
                    font-weight: 600;
                    font-size: {size}px;
                ">
                    {emoji} #{i+1} – {entry['name']} : {f"{int(entry['score']):,}".replace(",", ".")}
                </div>
                """,
                unsafe_allow_html=True
            )
    else:
        st.info("Sin envíos.")

