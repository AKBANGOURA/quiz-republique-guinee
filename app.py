import streamlit as st
import random
import time

# --- CONFIGURATION & CONFIDENTIALITÉ ---
st.set_page_config(
    page_title="Grand Quiz République de Guinée",
    page_icon="🇬🇳",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': None 
    }
)

# Masquage des éléments techniques
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stApp { margin-top: -50px; }
    </style>
    """, unsafe_allow_html=True)

# --- INITIALISATION DES QUESTIONS ---
if 'questions' not in st.session_state:
    data_complete = {
        "Education et Santé": [
            {"q": "En quelle année le BAC guinéen a enrégistré le plus faible taux de résussite (soit 9% d'admis) ?", "o": ["1998", "2007", "2022", "2003"], "r": "2022"},
            {"q": "Quel est le niveau d’enseignement qui suit l’école primaire en Guinée ?", "o": ["Université", "Lycée", "Collège", "Formation professionnelle"], "r": "Collège"},
            {"q": "Combien d’années dure normalement l’enseignement primaire en Guinée ?", "o": ["4 ans", "5 ans", "6 ans", "7 ans"], "r": "6 ans"},
            {"q": "Quel examen sanctionne la fin des études primaires ?", "o": ["BEPC", "Baccalauréat", "CEE", "CAP"], "r": "CEE"},
            {"q": "Quel diplôme marque la fin de l’enseignement secondaire ?", "o": ["BEPC", "Licence", "Baccalauréat", "Master"], "r": "Baccalauréat"},
            {"q": "Quelle est la principale université publique de Guinée ?", "o": ["Université de Kankan", "Université de Labé", "Université Gamal Abdel Nasser de Conakry", "Université de Boké"], "r": "Université Gamal Abdel Nasser de Conakry"},
            {"q": "Quel est l’objectif principal de l’alphabétisation ?", "o": ["Former des médecins", "Apprendre à lire et à écrire", "Formation enseignants", "Emplois"], "r": "Apprendre à lire et à écrire"},
            {"q": "Quel est l’âge officiel d’entrée à l’école primaire ?", "o": ["5 ans", "6 ans", "7 ans", "8 ans"], "r": "7 ans"},
            {"q": "Ministère responsable de la santé publique ?", "o": ["Affaires Sociales", "Défense", "Santé et Hygiène Publique", "Administration"], "r": "Ministère de la Santé et de l’Hygiène Publique"},
            {"q": "Plus grand hôpital de référence à Conakry ?", "o": ["Ignace Deen", "Donka", "Sino-Guinéen", "Kindia"], "r": "Hôpital Donka"},
            {"q": "Maladie ayant touché la Guinée (2014-2016) ?", "o": ["Paludisme", "Choléra", "COVID-19", "Ebola"], "r": "Ebola"},
            {"q": "Problème de santé publique en milieu rural ?", "o": ["Cancer", "Paludisme", "Diabète", "Hypertension"], "r": "Paludisme"},
            {"q": "Structure sanitaire la plus proche des ruraux ?", "o": ["Hôpital national", "Clinique privée", "Centre de santé", "CHU"], "r": "Centre de santé"},
            {"q": "Programme santé maternelle et infantile ?", "o": ["Alimentaire", "Vaccination (PEV)", "Plan minier", "Routier"], "r": "Programme élargi de vaccination"},
            {"q": "Langue principale d’enseignement ?", "o": ["Soussou", "Peul", "Français", "Malinké"], "r": "Le Français"},
            {"q": "Personnel formé pour les accouchements ?", "o": ["Pharmacien", "Sage-femme", "Infirmier", "Laborantin"], "r": "Sage-femme"},
            {"q": "Document requis pour le baccalauréat ?", "o": ["Nationalité", "Acte naissance", "BEPC", "Identité"], "r": "BEPC"},
            {"q": "Objectif principal de la vaccination ?", "o": ["Soigner", "Prévenir", "Diagnostic", "Réduire coûts"], "r": "Prévenir les maladies"},
            {"q": "Établissement formant les enseignants du primaire ?", "o": ["Université", "ENI", "Lycée", "Centre santé"], "r": "ENI"},
            {"q": "Rôle principal d’un centre de santé ?", "o": ["Former", "Soins simples et prévention", "Opérations", "Diplômes"], "r": "Soigner les cas simples et prévenir les maladies"}
        ],
        "Géographie et Economie": [
            {"q": "Combien de régions naturelles compte la République de Guinée ?", "o": ["3", "4", "5", "6"], "r": "4"},
            {"q": "Laquelle de ces régions est une zone côtière ?", "o": ["Haute", "Moyenne", "Basse Guinée", "Forestière"], "r": "Basse Guinée"},
            {"q": "Quelle région naturelle est dominée par le massif du Fouta-Djalon ?", "o": ["Basse", "Moyenne Guinée", "Haute", "Forestière"], "r": "Moyenne Guinée"},
            {"q": "Région considérée comme le principal grenier agricole ?", "o": ["Basse", "Haute Guinée", "Forestière", "Moyenne"], "r": "Haute Guinée"},
            {"q": "Plus grande ville de la Guinée sur le plan économique ?", "o": ["Kankan", "Labé", "Nzérékoré", "Conakry"], "r": "Conakry"},
            {"q": "Quel océan borde la Guinée au sud-ouest ?", "o": ["Océan Indien", "Océan Arctique", "Océan Atlantique", "Mer Méditerranée"], "r": "Océan Atlantique"},
            {"q": "Quel fleuve prend sa source en Guinée ?", "o": ["Le Niger", "Le Sénégal", "Le Congo", "Le Nil"], "r": "Le Niger"},
            {"q": "Quelle activité économique domine en Guinée Forestière ?", "o": ["Élevage", "Pêche", "Agriculture", "Industrie pétrolière"], "r": "Agriculture"},
            {"q": "Quelle est la principale richesse minière de la Guinée ?", "o": ["Fer", "Bauxite", "Or", "Diamant"], "r": "Bauxite"},
            {"q": "La Guinée détient l’une des plus grandes réserves mondiales de :", "o": ["Fer", "Or", "Bauxite", "Cuivre"], "r": "Bauxite"},
            {"q": "Quel secteur emploie le plus grand nombre de Guinéens ?", "o": ["Industrie", "Commerce", "Agriculture", "Mines"], "r": "Agriculture"},
            {"q": "Quel port est le plus important pour le commerce extérieur ?", "o": ["Port de Kamsar", "Port de Conakry", "Port de Maferenya", "Port de Boké"], "r": "Port de Conakry"},
            {"q": "Quelle culture est largement pratiquée en Basse Guinée ?", "o": ["Café", "Cacao", "Riz", "Coton"], "r": "Riz"},
            {"q": "Quel pays ne partage pas de frontière avec la Guinée ?", "o": ["Sierra Leone", "Mali", "Sénégal", "Ghana"], "r": "Ghana"},
            {"q": "Quelle monnaie est utilisée en République de Guinée ?", "o": ["Franc CFA", "Dollar", "Euro", "Franc guinéen"], "r": "Franc guinéen"},
            {"q": "Quelle région naturelle est riche en forêts denses ?", "o": ["Haute", "Basse", "Forestière", "Moyenne"], "r": "Guinée Forestière"},
            {"q": "Quel minerai est exploité principalement dans la région de Boké ?", "o": ["Or", "Diamant", "Bauxite", "Fer"], "r": "Bauxite"},
            {"q": "Quelle activité économique est dominante le long du littoral ?", "o": ["Pêche", "Élevage", "Forêt", "Montagne"], "r": "Pêche"},
            {"q": "Quel est le climat dominant en Guinée ?", "o": ["Désertique", "Méditerranéen", "Tropical", "Tempéré"], "r": "Tropical"},
            {"q": "Quelle ville est un important centre commercial en Haute Guinée ?", "o": ["Labé", "Kindia", "Kankan", "Boké"], "r": "Kankan"}
        ],
        "Sport et Culture": [
            {"q": "Quel sport est le plus populaire en République de Guinée ?", "o": ["Basketball", "Athlétisme", "Football", "Handball"], "r": "Football"},
            {"q": "Comment s’appelle l’équipe nationale de football de la Guinée ?", "o": ["Les Lions", "Le Syli National", "Les Éléphants", "Les Aigles"], "r": "Le Syli National"},
            {"q": "Quel joueur guinéen fut Ballon d'or africain ?", "o": ["Pascal Feindouno", "Cherif Souleymane", "Naby Keita", "Titi Camara"], "r": "Cherif Souleymane"},
            {"q": "Quelle ville est considérée comme un centre touristique de montagne ?", "o": ["Kankan", "Labé", "Boké", "Nzérékoré"], "r": "Labé"},
            {"q": "Le massif du Fouta-Djalon est surtout connu pour :", "o": ["Ses plages", "Ses déserts", "Ses montagnes et cascades", "Ses volcans"], "r": "Ses montagnes et cascades"},
            {"q": "Quel site naturel guinéen est célèbre pour ses cascades ?", "o": ["Îles de Loos", "Voile de la Mariée", "Mont Nimba", "Cap Verga"], "r": "Voile de la Mariée"},
            {"q": "Quel archipel est situé au large de Conakry ?", "o": ["Îles de Loos", "Îles Canaries", "Îles Bijagos", "Îles du Cap-Vert"], "r": "Îles de Loos"},
            {"q": "Quel parc naturel est partagé entre la Guinée, la Côte d’Ivoire et le Libéria ?", "o": ["Parc du Badiar", "Parc national du Mont Nimba", "Parc du Niokolo-Koba", "Parc du W"], "r": "Parc national du Mont Nimba"},
            {"q": "Quel instrument de musique traditionnelle est très répandu en Guinée ?", "o": ["Piano", "Guitare", "Kora", "Violon"], "r": "Kora"},
            {"q": "Quel genre musical traditionnel est associé à la culture guinéenne ?", "o": ["Jazz", "Hip-hop", "Musique mandingue", "Rock"], "r": "Musique mandingue"},
            {"q": "Quel artiste guinéen est mondialement connu ?", "o": ["Mory Kanté", "Sory Kandia Kouyaté", "Sékouba Bambino", "Mory Djély"], "r": "Mory Kanté"},
            {"q": "Quel événement culturel célèbre les arts guinéens ?", "o": ["Panafricain", "Festival National Arts", "Carnaval", "Fête Indep."], "r": "Festival national des arts et de la culture"}
        ],
        "Justice et Sécurité": [
            {"q": "Quelle est la loi fondamentale qui organise l’État guinéen ?", "o": ["Le Code civil", "La Constitution", "Le Code pénal", "La Charte nationale"], "r": "La Constitution"},
            {"q": "Quel pouvoir est chargé de faire respecter les lois en Guinée ?", "o": ["Exécutif", "Législatif", "Le pouvoir judiciaire", "Administratif"], "r": "Le pouvoir judiciaire"},
            {"q": "Quelle institution rend la justice au nom du peuple guinéen ?", "o": ["Le Gouvernement", "Les tribunaux", "L’Assemblée nationale", "La Cour des comptes"], "r": "Les tribunaux"},
            {"q": "Quel est le rôle principal de la police nationale ?", "o": ["Défendre le territoire", "Voter les lois", "Maintenir l’ordre public", "Rendre la justice"], "r": "Maintenir l’ordre public"},
            {"q": "Quelle force est chargée de la défense du territoire national ?", "o": ["La Police", "La Gendarmerie", "Les Forces armées", "La Protection civile"], "r": "Les Forces armées"},
            {"q": "Quelle institution est chargée de juger les infractions économiques ?", "o": ["La cour des comptes", "La CRIEF", "Le Trésor public", "Le Parlement"], "r": "La CRIEF"},
            {"q": "Quel est le rôle du ministère de la Justice ?", "o": ["Organiser les élections", "Assurer la défense", "Admin Justice", "Ordre"], "r": "Administrer la justice"},
            {"q": "Quel corps assure la sécurité en milieu rural et sur les routes ?", "o": ["La Police", "La Gendarmerie nationale", "Les Douanes", "La Protection civile"], "r": "La Gendarmerie nationale"},
            {"q": "Qui est le chef suprême des Forces armées guinéennes ?", "o": ["PM", "Défense", "Président", "État-major"], "r": "Le Président de la République"},
            {"q": "Quel texte définit les infractions et les peines en Guinée ?", "o": ["Le Code civil", "Le Code pénal", "La Constitution", "Le Code du travail"], "r": "Le Code pénal"},
            {"q": "Quel est le rôle de la Cour suprême ?", "o": ["Voter les lois", "Juger en dernier ressort", "Maintenir l’ordre", "Défendre le territoire"], "r": "Juger en dernier ressort"},
            {"q": "En quelle année fut organisée les prémières élections multipartites ?", "o": ["2010", "1993", "1958", "2025"], "r": "1993"},
            {"q": "Quel corps est chargé de la sécurité civile et des secours ?", "o": ["La Police", "La Gendarmerie", "La Protection civile", "Les Forces armées"], "r": "La Protection civile"},
            {"q": "Quel est le rôle des douanes ?", "o": ["Rendre la justice", "Assurer la défense", "Contrôle frontières", "Ordre"], "r": "Contrôler les marchandises aux frontières"},
            {"q": "Quelle juridiction traite principalement les affaires civiles ?", "o": ["Tribunal civil", "Tribunal militaire", "Cour martiale", "Haute Cour"], "r": "Tribunal civil"},
            {"q": "Quelle institution peut juger le Président de la République ?", "o": ["Tribunal", "Suprême", "Haute Cour", "Conseil"], "r": "La Haute Cour de justice"},
            {"q": "Quel est le rôle principal de la loi ?", "o": ["Favoriser", "Organiser société", "Conflits", "Remplacer"], "r": "Organiser la vie en société"},
            {"q": "Quel principe interdit de se faire justice soi-même ?", "o": ["La liberté", "La solidarité", "L’État de droit", "La souveraineté"], "r": "L’État de droit"},
            {"q": "Quel service est chargé de la sécurité des frontières ?", "o": ["Police", "Gendarmerie/Armée", "Tribunaux", "Suprême"], "r": "La Gendarmerie et les Forces armées"},
            {"q": "Quel est le rôle principal de la justice ?", "o": ["Guerre", "Social", "Appliquer/Sanctionner", "Lois"], "r": "Appliquer la loi et sanctionner les infractions"}
        ],
        "Histoire et Politique": [
            {"q": "Qui est le premier président de la République de Guinée ?", "o": ["Almamy Samory Touré", "Lansana Conté", "Diallo Télli", "Ahmed Sékou Touré"], "r": "Ahmed Sékou Touré"},
            {"q": "En quelle année la Guinée a-t-elle obtenu son indépendance ?", "o": ["1956", "1960", "1955", "1958"], "r": "1958"},
            {"q": "Quel est le nom de l'hymne national de la Guinée ?", "o": ["Patrie", "Horoya", "Guinéenne", "Liberté"], "r": "Liberté"},
            {"q": "Quelle est la superficie de la Guinée ?", "o": ["45.867 km2", "245.857 km2", "845.269 km2", "145.967 km2"], "r": "245.857 km2"},
            {"q": "Quel est le nom de la capitale de la Guinée ?", "o": ["Kindia", "Kaloum", "Conakry", "Kankan"], "r": "Conakry"},
            {"q": "Qui fut le premier sécrétaire général du PDG-RDA ?", "o": ["Sékou", "Saifoulaye", "Fodé", "Madera Keita"], "r": "Madera Keita"},
            {"q": "Qui a pris le pouvoir après la mort de Sékou Touré ?", "o": ["Bah Mamadou", "Lansana Béavogui", "Lansana Conté", "Diarra Traoré"], "r": "Lansana Conté"},
            {"q": "Quel événement majeur s’est produit en Guinée en 2009 ?", "o": ["Révolution", "Coup d’État", "Guerre civile", "28 Septembre"], "r": "Des massacres au stade du 28 Septembre"},
            {"q": "Quel est la dévise de la République de Guinée ?", "o": ["Unité", "Travail-Justice-Liberté", "Amour", "Travail-Justice-Solidarité"], "r": "Travail-Justice-Solidarité"},
            {"q": "Syndicalistes des grèves de 2007 ?", "o": ["Amadou Diallo", "Soumah", "Ibrahima Fofana & Rabiatou Serah Diallo", "Sow"], "r": "Ibrahima Fofana & Rabiatou Serah Diallo"},
            {"q": "En quelle année Sidya Touré devint PM ?", "o": ["1993", "2008", "2010", "1996"], "r": "1996"},
            {"q": "Officier ayant dirigé le coup du 5 sept 2021 ?", "o": ["Sadiba", "Amara", "Mamadi Doumbouya", "Alya"], "r": "Mamadi Doumbouya"},
            {"q": "Stade le plus connu de Conakry ?", "o": ["Paix", "28 septembre", "Sékou Touré", "National"], "r": "Stade du 28 septembre"},
            {"q": "À quelle organisation régionale la Guinée appartient-elle ?", "o": ["UEMOA", "CEEAC", "CEDEAO", "SADC"], "r": "CEDEAO"},
            {"q": "Quelle région naturelle abrite la ville de Kankan ?", "o": ["Basse", "Moyenne", "Haute Guinée", "Forestière"], "r": "Haute Guinée"},
            {"q": "Quel leader n’a jamais été président ?", "o": ["Sékou Touré", "Lansana Conté", "Alpha Condé", "Cellou Dalein Diallo"], "r": "Cellou Dalein Diallo"},
            {"q": "Objectif annoncé du coup de 2021 ?", "o": ["Monnaie", "Réformer Constitution", "CEDEAO", "Guerre"], "r": "Réformer la Constitution"}
        ]
    }
    
    all_q = []
    for theme in data_complete:
        all_q.extend(data_complete[theme])
    
    # MÉLANGE ALÉATOIRE ET SÉLECTION DES 20 QUESTIONS
    random.shuffle(all_q)
    st.session_state.questions = all_q[:20] # ICI ON LIMITE À 20 QUESTIONS
    
    st.session_state.score = 0
    st.session_state.index = -1 
    st.session_state.fini = False
    st.session_state.temps_restant = 30

# --- PAGE D'ACCUEIL ---
if st.session_state.index == -1:
    st.title("🇬🇳 Quiz : République de Guinée")
    st.markdown(f"""
    ### Bienvenue !
    Testez vos connaissances sur notre nation à travers un tirage aléatoire.
    
    ---
    **📋 Règles :**
    * **20 questions** tirées au sort parmi notre base de données.
    * **30 secondes** par question.
    
    *Chaque partie est unique !*
    """)
    
    if st.button("🚀 LANCER LE DÉFI (20 Questions)", use_container_width=True):
        st.session_state.index = 0
        st.rerun()
    
    st.info("💡 Conçu par : **Almamy Kalla BANGOURA**")

# --- INTERFACE DU QUIZ ---
elif not st.session_state.fini:
    zone_chrono = st.empty()
    item = st.session_state.questions[st.session_state.index]
    
    st.subheader(f"Question {st.session_state.index + 1} / 20")
    
    with st.form(key=f"q_form_{st.session_state.index}"):
        st.write(f"### {item['q']}")
        choix = st.radio("Votre réponse :", item['o'], index=None)
        
        if st.form_submit_button("Valider"):
            if choix == item['r']:
                st.session_state.score += 1
            
            if st.session_state.index < len(st.session_state.questions) - 1:
                st.session_state.index += 1
                st.session_state.temps_restant = 30
                st.rerun()
            else:
                st.session_state.fini = True
                st.rerun()

    # --- CHRONOMÈTRE ---
    while st.session_state.temps_restant > 0:
        with zone_chrono:
            color = "red" if st.session_state.temps_restant < 6 else "green"
            st.markdown(f"### ⏳ Temps : :{color}[{st.session_state.temps_restant}s]")
            st.progress(st.session_state.temps_restant / 30)
        time.sleep(1)
        st.session_state.temps_restant -= 1
        
        if st.session_state.temps_restant <= 0:
            st.warning("⌛ Temps écoulé !")
            time.sleep(1)
            if st.session_state.index < len(st.session_state.questions) - 1:
                st.session_state.index += 1
                st.session_state.temps_restant = 30
                st.rerun()
            else:
                st.session_state.fini = True
                st.rerun()

# --- PAGE DE RÉSULTATS ---
else:
    st.balloons()
    st.header("🏁 Score Final")
    st.metric(label="Résultat", value=f"{st.session_state.score} / 20")
    
    if st.button("🔄 Rejouer (Nouvelle sélection de questions)", use_container_width=True):
        for k in list(st.session_state.keys()): del st.session_state[k]
        st.rerun()
    
    st.caption(f"© 2025 - Almamy Kalla BANGOURA | Consultant Data & BI")
  
