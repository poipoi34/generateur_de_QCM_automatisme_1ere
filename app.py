import random
import string
import streamlit as st
from id_uuid_base import *


BASE_URL = "https://coopmaths.fr/alea/?"

categories = {
    "Calcul": Calcul,
    "evolutions": evolutions,
    "fonctions": fonctions,
    "probabilités": probabilités,
    "proportion": proportion,
    "statistiques": statistiques,
}

def random_alea(length=4):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def generate_url(exercises_dict, n, es="01110011"):
    items = list(exercises_dict.items())
    n = min(n, len(items))
    selected = random.sample(items, n)

    parts = []
    for ex_id, uuid in selected:
        parts.append(f"uuid={uuid}&id={ex_id}&i=1&alea={random_alea()}")

    parts.append("v=eleve")
    parts.append(f"es={es}")

    return BASE_URL + "&".join(parts)

st.title("Générateur de QCM CoopMaths")

category = st.selectbox(
    "Choisir une catégorie",
    list(categories.keys()) + ["toutes les catégories"]
)

if category == "toutes les catégories":
    pool = {}
    for d in categories.values():
        pool.update(d)
else:
    pool = categories[category]

max_questions = len(pool)
nb_questions = st.number_input(
    "Nombre de questions",
    min_value=1,
    max_value=max_questions,
    value=min(10, max_questions),
    step=1
)

if st.button("Générer le QCM"):
    url = generate_url(pool, nb_questions)
    st.success("QCM généré")
    st.code(url)
    st.markdown(f"[Ouvrir le QCM]({url})")