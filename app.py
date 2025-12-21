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
            
            {"q": "L'année du BAC avec un taux de résussite de 9%?", 
             "o": ["1998", "2007", "2022", "2003"], 
             "r": "2022"},
            
            {"q": "Niveau d’enseignement après l’école primaire?", 
             "o": ["Université", "Lycée", "Collège", "BTS"], 
             "r": "Collège"},
            
            {"q": "Combien d’années dure l’enseignement général?",
             "o": ["14 ans", "11 ans", "13 ans", "12 ans"], 
             "r": "13 ans"},
            
            {"q": "Examen sanctionnant la fin du Lycée?", 
             "o": ["BEPC", "Baccalauréat", "CEE", "Concours"],
             "r": "Baccalauréat"},
            
            {"q": "Diplôme marquant la fin du Système LMD?", 
             "o": ["Master", "Licence", "Baccalauréat", "Doctorat"],
             "r": "Doctorat"},
            
            {"q": "Principale université publique de Guinée?", 
             "o": ["GLC Sonfonia", "Julius Nyéréré", "Gamal Abdel Nasser", "Koffi Anan"], 
             "r": "Gamal Abdel Nasser"},
            
            {"q": "Objectif principal de l’alphabétisation?", 
             "o": ["Parler et conjuguer", "Lire et à écrire", 
                   "Chanter et réciter", "Déssiner et animer"], 
             "r": "Lire et à écrire"},
            
            {"q": "L’âge officiel d’entrée à l’école primaire?", 
             "o": ["5 ans", "6 ans", "7 ans", "8 ans"],
             "r": "7 ans"},
            
            {"q": "Ministère responsable de la Diplomatie?",
             "o": ["Affaires Sociales", "Défense Nationale", "Affaires Etrangères", "Economie Finance"],
             "r": "Affaires Etrangères"},
            
            {"q": "Plus grand hôpital de référence à Conakry?",
             "o": ["CHU Ignace Deen", "CHU Donka", "Sino-Guinéen", "Clinique Pasteur"], 
             "r": "CHU Donka"},
            
            {"q": "Epidémie ayant touchée la Guinée (2014-2016)?", 
             "o": ["Paludisme", "Choléra", "COVID-19", "Ebola"], 
             "r": "Ebola"},
            
            {"q": "Problème de santé publique en milieu rural?",
             "o": ["Cancer", "Paludisme", "Diabète", "Hypertension"],
             "r": "Paludisme"},
            
            {"q": "Structure sanitaire la plus proche des ruraux?",
             "o": ["Hôpital national", "Clinique privée", "Centre de santé", "CHU"], 
             "r": "Centre de santé"},
            
            {"q": "Qui met en oeuvre la politique de santé?",
             "o": ["Ministre de l'économie", "DG du CHU Ignace Deen", "Réprésentant OMS", "Ministre de la Santé"], 
             "r": "Ministre de la Santé"},
            
            {"q": "Langue principale de l'administration?", 
             "o": ["Soussou", "Peul", "Français", "Malinké"], 
             "r": "Français"},
            
            {"q": "Personnel formé pour les accouchements?", 
             "o": ["Pharmacien", "Sage-femme", "Infirmier", "Laborantin"], 
             "r": "Sage-femme"},
            
            {"q": "Document requis pour le baccalauréat?",
             "o": ["CEE", "Acte de naissance", "BEPC", "Identité"], 
             "r": "BEPC"},
            
            {"q": "Objectif principal de la vaccination?", 
             "o": ["Soigner", "Prévenir", "Diagnostiquer", "Réduire coûts"],
             "r": "Prévenir"},
            
            {"q": "IES formant les enseignants du Sécondaire?",
             "o": ["Université", "ENI", "Lycée", "ISSEG"], 
             "r": "ISSEG"},
            
            {"q": "Rôle principal d’un centre de santé?",
             "o": ["Former", "Soins et prévention", "Opérations", "Chirurgie"], 
             "r": "Soins et prévention"}
        ],
        
        "Géographie et Economie": [
            
            {"q": "Nombre de sous préfecture?", 
             "o": ["33", "318", "333", "323"], 
             "r": "333"},
            
            {"q": "Quelle région est une zone côtière?",
             "o": ["Haute  Guinée", "Moyenne  Guinée", "Basse Guinée", " Guinée Forestière"],
             "r": "Basse Guinée"},
            
            {"q": "L'altitude du mont Kakoulima?", 
             "o": ["1235 mètres", "1134 mètres", "1011 mètres", "1335 mètres"], 
             "r": "1011 mètres"},
            
            {"q": "Lequel de ces résistants est mort en 1897",
             "o": ["Dinah Salifou Camara", "Elhadj Omar Tall", "Almamy Samory Touré", "Kissi Kaba Keita"],
             "r": "Dinah Salifou Camara"},
            
            {"q": "Plus grande ville de la Guinée sur le plan économique?", 
             "o": ["Kankan", "Labé", "Nzérékoré", "Conakry"], 
             "r": "Conakry"},
            
            {"q": "Quel océan borde la Guinée au sud-ouest?",
             "o": ["Indien", "Arctique", "Atlantique", "Méditerranée"], 
             "r": "Atlantique"},
            
            {"q": "Quel fleuve prend sa source en Guinée?",
             "o": ["Le Niger", "Le Sénégal", "Le Congo", "Le Nil"], 
             "r": "Le Niger"},
            
            {"q": "Nombre de pays frontaliers à la Guinée?", 
             "o": ["7", "8", "6", "9"], 
             "r": "6"},
            
            {"q": "Minérai exploité par le projet Simandou?",
             "o": ["Fer", "Bauxite", "Or", "Diamant"], 
             "r": "Fer"},
            
            {"q": "Laquelle n'est pas une région administrative", 
             "o": ["Kindia", "Faranah", "Siguirin", "Labé"],
             "r": "Siguirin"},
            
            {"q": "Quelle ville est la capitale des agrumes?", 
             "o": ["Guékedou", "Kindia", "Pita", "Dabola"], 
             "r": "Kindia"},
            
            {"q": "Quelle prefecture abrite le mont Nimba?",
             "o": ["Lola", "Beyla", "Macenta", "Yomou"], 
             "r": "Lola"},
            
            {"q": "La culture largement pratiquée en Basse Guinée?", 
             "o": ["Café", "Fonio", "Riz", "Coton"],
             "r": "Riz"},
            
            {"q": "Pays non frontalier de la Guinée?", 
             "o": ["Sierra Leone", "Mali", "Sénégal", "Ghana"], 
             "r": "Ghana"},
            
            {"q": "Monnaie nationale de la Guinée?", 
             "o": ["Franc CFA", "Le syli", "Z-mao", "GNF"], 
             "r": "GNF"},
            
            {"q": "La colonisation commence en Guinée en?", 
             "o": ["1900", "1898", "1918", "1858"], 
             "r": "1898"},
            
            {"q": "Laquelle n'est pas une ville cotière?", 
             "o": ["Forécariah", "Fria", "Boké", "Dubréka"], 
             "r": "Fria"},
            
            {"q": "Quel Ministère collecte les impôts?", 
             "o": ["Economie et Finance", "Commerce et Industrie", "Budget", "Banque central"],
             "r": "Budget"},
            
            {"q": "Quel climat domine en Guinée?", 
             "o": ["Désertique", "Méditerranéen", "Tropical", "Tempéré"], 
             "r": "Tropical"},
            
            {"q": "Quelle préfecture abrite la ville de Kamsar?", 
             "o": ["Fria", "Boke", "Dubréka", "Boffa"], 
             "r": "Boffa"}
            
        ],
        
        "Sport et Culture": [
            
            {"q": "Sport le plus populaire en Guinée?", 
             "o": ["Basketball", "Athlétisme", "Football", "Handball"],
             "r": "Football"},
            
            {"q": "Appelation de l’équipe nationale de football?",
             "o": ["Gbin Gbin Soo", "Les Éléphants", "Le Syli National",  "Les Aigles"], 
             "r": "Le Syli National"},
            
            {"q": "Quel joueur guinéen fut Ballon d'or africain?", 
             "o": ["Pascal Feindouno", "Cherif Souleymane", "Naby Keita", "Titi Camara"], 
             "r": "Cherif Souleymane"},
            
            {"q": "Ville considérée comme un centre touristique de montagne?", 
             "o": ["Kankan", "Labé", "Boké", "Nzérékoré"],
             "r": "Labé"},
            
            {"q": "Le massif du Fouta-Djalon est connu pou ses", 
             "o": ["plages", "déserts", "montagnes et cascades", "forêts"], 
             "r": "montagnes et cascades"},
            
            {"q": "Site naturel guinéen célèbre pour ses cascades?",
             "o": ["Îles de Loos", "Voile de la Mariée", "Mont Nimba", "Mont Kakoulima"],
             "r": "Voile de la Mariée"},
            
            {"q": "Archipel situé au large de Conakry?",
             "o": ["Îles de Loos", "Îles Canaries", "Îles Bijagos", "Îles du Cap-Vert"], 
             "r": "Îles de Loos"},
            
            {"q": "Parc naturel partagé entre Guinée, Libéria et Côte d'Ivoire?", 
             "o": ["Parc du Badiar", "Parc national du Mont Nimba", "Parc du Niokolo-Koba", "Parc du W"], 
             "r": "Parc national du Mont Nimba"},
            
            {"q": "Instrument traditionnelle de musique très répandu en Guinée?", 
             "o": ["Tamtam", "Guitare", "Kora", "Kenkedi"],
             "r": "Kora"},
            
            {"q": "Genre musical traditionnel associé à la culture guinéenne?", 
             "o": ["Jazz", "Hip-hop", "Musique mandingue", "Rock"],
             "r": "Musique mandingue"},
            
            {"q": "Artiste guinéen mondialement connu pour son mythique titre Yéké yéké?", 
             "o": ["Mory Kanté", "Sory Kandia Kouyaté", "Sékouba Bambino", "Mory Djély"], 
             "r": "Mory Kanté"},
            
            {"q": "Date anniversaire du NON historique?", 
             "o": ["Le 02 Octobre 1958", "Le 04 Avril 1984", "Le 28 Septembre 1958", "Le 1er Mars 1960"], 
             "r": "Le 28 Septembre 1958"}
            
        ],
        
        "Justice et Sécurité": [
            
            {"q": "Loi fondamentale de l’État guinéen?", 
             "o": ["Le Code civil", "La Constitution", "Le Code pénal", "La Charte nationale"], 
             "r": "La Constitution"},
            
            {"q": "Le Ministre de la Justice exerce le pouvoir?",
             "o": ["exécutif", "législatif", "judiciaire", "administratif"],
             "r": "exécutif"},
            
            {"q": "Institution rendant la justice au nom du peuple?",
             "o": ["Le Gouvernement", "Les tribunaux", "L’Assemblée nationale", "La Cour des comptes"], 
             "r": "Les tribunaux"},
            
            {"q": "Rôle principal de la police nationale?",
             "o": ["Défendre le territoire", "Voter les lois", "Maintenir l’ordre public", "Rendre la justice"], 
             "r": "Maintenir l’ordre public"},
            
            {"q": "Force chargée de la défense territoriale?",
             "o": ["La Police", "La Gendarmerie", "Les Forces armées", "La Protection civile"], 
             "r": "Les Forces armées"},
            
            {"q": "Institution jugeant les infractions économiques?", 
             "o": ["La cour des comptes", "La CRIEF", "Le Trésor public", "Le CENA"], 
             "r": "La CRIEF"},
            
            {"q": "Rôle du ministère de la Justice?", 
             "o": ["Organiser les élections", "Assurer la défense", "Administrer la justice", "Protéger les riches du pays"], 
             "r": "Administrer la justice"},
            
            {"q": "Corps assurant la sécurité en milieu rural et sur les routes?", 
             "o": ["La Police nationale", "La Gendarmerie nationale", "Les Douanes", "La Protection civile"], 
             "r": "La Gendarmerie nationale"},
            
            {"q": "Qui est le chef suprême des Forces armées?", 
             "o": ["Le Prémier Ministre", "Le Ministre Défense", "Le Président de la République", "Le Chef d'État-major"], 
             "r": "Le Président de la République"},
            
            {"q": "Texte définissant les infractions et les peines?",
             "o": ["Le Code civil", "Le Code pénal", "La Constitution", "Le Code du travail"], 
             "r": "Le Code pénal"},
            
            {"q": "Rôle de la Cour suprême?", 
             "o": ["Voter les lois", "Juger en dernier ressort", "Maintenir l’ordre", "Défendre le territoire"], 
             "r": "Juger en dernier ressort"},
            
            {"q": "L'année des prémières élections multipartites?",
             "o": ["2010", "1993", "1958", "2025"], 
             "r": "1993"},
            
            {"q": "Corps chargé de la sécurité civile et des secours?", 
             "o": ["La Police", "La Gendarmerie", "La Protection civile", "Les Forces armées"], 
             "r": "La Protection civile"},
            
            {"q": "Quel est le rôle des douanes?", 
             "o": ["Rendre la justice", "Assurer la défense", "Contrôle aux frontières", "Voler l'argent public"],
             "r": "Contrôle aux frontières"},
            
            {"q": "Juridiction traitant les affaires civiles?",
             "o": ["Tribunal civil", "Tribunal militaire", "Cour martiale", "Haute Cour"], 
             "r": "Tribunal civil"},
            
            {"q": "Quelle institution peut juger le Chef de l'Etat?",
             "o": ["Le tribunal de 1ère instance", "La cour suprême", "La Haute Cour de justice", "Le Conseil constitutionnel"], 
             "r": "La Haute Cour de justice"},
            
            {"q": "Rôle principal de la loi?",
             "o": ["Favoriser les plus forts", "Organiser la vie en société", "Attiser les conflits", "Sanctionner les plus faibles"],
             "r": "Organiser la vie en société"},
            
            {"q": "Principe interdisant de se faire justice soi-même?", 
             "o": ["La liberté", "La solidarité", "L’État de droit", "La souveraineté"],
             "r": "L’État de droit"},
            
            {"q": "Service chargé de la sécurité des frontières?",
             "o": ["Police et la sécurité intérieure", "La Gendarmerie et les Forces armées", "Les Tribunaux", "Les frontaliers"], 
             "r": "La Gendarmerie et les Forces armées"},
            
            {"q": "Institution chargé de voter les lois?", 
             "o": ["La Présidence de la République", "La cour suprëme", "L'assemblée nationale", "Le Ministère de la Justice"],
             "r": "L'assemblée nationale"}
        ],
        
        "Histoire et Politique": [
            
            {"q": "Qui fût le 1er président de l'Assemblée nationale?", 
             "o": ["Siradio Diallo", "Barry 3", "Diallo Télli", "Saifoulaye Diallo"], 
             "r": "Saifoulaye Diallo"},
            
            {"q": "Année de création de l'armée guinéenne?", 
             "o": ["1956", "1960", "1962", "1958"], 
             "r": "1960"},
            
            {"q": "Le nom de l'hymne national de guinéen?", 
             "o": ["Patrie", "Horoya", "Guinéenne", "Liberté"], 
             "r": "Liberté"},
            
            {"q": "La superficie de la Guinée?", 
             "o": ["45.867 km2", "245.857 km2", "845.269 km2", "145.967 km2"], 
             "r": "245.857 km2"},
            
            {"q": "Le quartier abritant le palais Sékhoutouréya?", 
             "o": ["Manquepas", "Boulbinet", "Almamya", "Coronthie"], 
             "r": "Boulbinet"},
            
            {"q": "Qui fût le 1er sécrétaire général du PDG-RDA?",
             "o": ["Amara Soumah", "Ahmed Sékou Touré", "Saifoulaye Diallo", "Madera Keita"], 
             "r": "Madera Keita"},
            
            {"q": "Qui fût le tout 1er des PM en Guinée?", 
             "o": ["Lounceny Fall", "Lansana Béavogui", "Diarra Traoré", "Sidya Touré"], 
             "r": "Lansana Béavogui"},
            
            {"q": "Quel événement majeur s’est produit en Guinée en 2009?",
             "o": ["Révolution populaire", "Coup d’État", "Grêve générale", "Massacre au stade du 28 Sept"],
             "r": "Massacre au stade du 28 Sept"},
            
            {"q": "La dévise de la République de Guinée?", 
             "o": ["Unité-Travail-Amour", "Travail-Justice-Liberté", "Un peuple-Un but-une foi", "Travail-Justice-Solidarité"], 
             "r": "Travail-Justice-Solidarité"},
            
            {"q": "Quel officier était à la tête du CNDD?", 
             "o": ["Mamadi Doumbouya", "Sekouba Konaté", "Moussa Dadis Camara", "Toto Camara"], 
             "r": "Moussa Dadis Camara"},
            
            {"q": "Sidya Touré devint Prémier Ministre en?", 
             "o": ["1993", "2008", "2010", "1996"], 
             "r": "1996"},
            
            {"q": "Officier ayant dirigé le coup du 5 septembre 2021?", 
             "o": ["Sadiba Koulibaly", "Amara Camara", "Mamadi Doumbouya", "Alya Camara"], 
             "r": "Mamadi Doumbouya"},
            
            {"q": "Stade le plus connu de Conakry?", 
             "o": ["Stade Petit Sory", "Stade du 28 septembre", "Stade Général Lansana Conté", "Stade M'ballou Mady Diakité"],
             "r": "Stade du 28 septembre"},
            
            {"q": "La Guinée siège au sein de l'Organisation?", 
             "o": ["UEMOA", "CEEAC", "CEDEAO", "SADC"], 
             "r": "CEDEAO"},
            
            {"q": "Préfecture abritant la sous préfecture de Koba?", 
             "o": ["Pita", "Boffa", "Kérouané", "Kissidougou"], 
             "r": "Boffa"},
            
            {"q": "Le dernier Prémier Ministre de Lansana Conté?",
             "o": ["Kabinet Komara", "Eugène Camara", "Ahmed tidiane Souaré", "Cellou Dalein Diallo"], 
             "r": "Ahmed tidiane Souaré"},
            
            {"q": "Objectif annoncé du coup d'Etat de 2021?",
             "o": ["Changer de Monnaie", "Réformer Constitution", "Quitter la CEDEAO", "Sacralisé la démagogie"], 
             "r": "Réformer la Constitution"}
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
    st.session_state.temps_restant = 12

# --- PAGE D'ACCUEIL ---
if st.session_state.index == -1:
    st.title("🇬🇳 Guinée")
    st.markdown(f"""
    ### QUIZ : culture générale! 
    Testez vos connaissances sur notre nation à travers un tirage aléatoire de QCM.
    
    ---
    **📋 Règles :**
    * **20 QCM** tirées au sort parmi 100 QCM de notre base de données.
    * **12 secondes** par question (Il faut donc connaître et être rapide).
    
    *Chaque partie est unique ! Une seule case à cocher, c'est amusant et instructif.*
    """)
    
    if st.button("🚀 LANCER LE DÉFI (20 Questions)", use_container_width=True):
        st.session_state.index = 0
        st.rerun()
    
    st.info("💡 Conçu par : **Almamy Kalla BANGOURA | Consultant Data & BI**")

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
                st.session_state.temps_restant = 12
                st.rerun()
            else:
                st.session_state.fini = True
                st.rerun()

    # --- CHRONOMÈTRE ---
    while st.session_state.temps_restant > 0:
        with zone_chrono:
            color = "red" if st.session_state.temps_restant < 6 else "green"
            st.markdown(f"### ⏳ Temps : :{color}[{st.session_state.temps_restant}s]")
            st.progress(st.session_state.temps_restant / 12)
        time.sleep(1)
        st.session_state.temps_restant -= 1
        
        if st.session_state.temps_restant <= 0:
            st.warning("⌛ Temps écoulé !")
            time.sleep(1)
            if st.session_state.index < len(st.session_state.questions) - 1:
                st.session_state.index += 1
                st.session_state.temps_restant = 12
                st.rerun()
            else:
                st.session_state.fini = True
                st.rerun()

# --- PAGE DE RÉSULTATS ---
else:
    st.balloons()
    st.header("🏁 Quiz Terminé !")
    
    score = st.session_state.score
    total = 20
    
    # Affichage du score avec un design propre
    st.metric(label="Votre Score Final", value=f"{score} / {total}")
    
    # --- LOGIQUE DES PHRASES DE MOTIVATION ---
    if score == 20:
        st.success("🏆 **Honorable** : Une connaissance parfaite sur la Guinée !")
    elif 18 <= score <= 19:
        st.success("🌟 **Excellent** : Une connaissance presque parfaite sur la Guinée.")
    elif 15 <= score <= 17:
        st.info("👏 **Très Bien** : Une bonne connaissance sur la Guinée.")
    elif 12 <= score <= 14:
        st.info("👍 **Bien** : Une connaissance appréciable sur la Guinée.")
    elif 9 <= score <= 11:
        st.warning("😐 **Passable** : Une connaissance moyenne sur la Guinée.")
    elif 5 <= score <= 8:
        st.warning("📚 **Encouragement** : Je vous encourage à apprendre sur la Guinée.")
    else:
        st.error("❗ **À réviser** : Veuillez apprendre davantage sur la Guinée.")

    st.write("---")
    
    # Boutons d'action
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 Rejouer une partie", use_container_width=True):
            # Reset complet de la session pour un nouveau tirage aléatoire
            for k in list(st.session_state.keys()):
                del st.session_state[k]
            st.rerun()
    
    with col2:
        # Optionnel : Un bouton pour partager (juste visuel ici)
        st.button("🔗 Partager mon score", use_container_width=True, help="Bientôt disponible")

    st.write("")
    st.caption(f"© 2025 - Quiz conçu par **Almamy Kalla BANGOURA** | Consultant Data & BI")
  
