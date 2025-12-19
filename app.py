import streamlit as st
import random
import time

# --- CONFIGURATION ---
st.set_page_config(page_title="Grand Quiz Guinée", page_icon="🇬🇳", initial_sidebar_state="collapsed")

# --- BASE DE DONNÉES COMPLÈTE (100 QUESTIONS) ---
if 'questions' not in st.session_state:
    data_complete = {
        "Education et Santé": [
            {"q": "En quelle année le BAC guinéen a enregistré 9% d'admis ?", "o": ["1998", "2007", "2022", "2003"], "r": "2022"},
            {"q": "Niveau d'enseignement après le primaire ?", "o": ["Université", "Lycée", "Collège", "Pro"], "r": "Collège"},
            {"q": "Durée du cycle primaire en Guinée ?", "o": ["4 ans", "5 ans", "6 ans", "7 ans"], "r": "6 ans"},
            {"q": "Examen de fin d'études primaires ?", "o": ["BEPC", "Bac", "CEE", "CAP"], "r": "CEE"},
            {"q": "Diplôme fin d'enseignement secondaire ?", "o": ["BEPC", "Licence", "Baccalauréat", "Master"], "r": "Baccalauréat"},
            {"q": "Principale université publique (Conakry) ?", "o": ["Kankan", "Labé", "Gamal Abdel Nasser", "Boké"], "r": "Université Gamal Abdel Nasser de Conakry"},
            {"q": "But de l'alphabétisation ?", "o": ["Médecine", "Lire et écrire", "Enseigner", "Emploi"], "r": "Apprendre à lire et à écrire"},
            {"q": "Âge officiel d'entrée au primaire ?", "o": ["5 ans", "6 ans", "7 ans", "8 ans"], "r": "7 ans"},
            {"q": "Ministère de la santé publique ?", "o": ["Affaires Sociales", "Défense", "Santé et Hygiène", "Admin"], "r": "Ministère de la Santé et de l’Hygiène Publique"},
            {"q": "Plus grand hôpital de Conakry ?", "o": ["Ignace Deen", "Donka", "Sino-Guinéen", "Kindia"], "r": "Hôpital Donka"},
            {"q": "Épidémie majeure 2014-2016 ?", "o": ["Paludisme", "Choléra", "COVID-19", "Ebola"], "r": "Ebola"},
            {"q": "Maladie infectieuse la plus fréquente ?", "o": ["Cancer", "Paludisme", "Diabète", "Tension"], "r": "Paludisme"},
            {"q": "Structure de santé de base ?", "o": ["Hôpital", "Clinique", "Centre de santé", "CHU"], "r": "Centre de santé"},
            {"q": "Programme de vaccination infantile ?", "o": ["Alimentaire", "PEV", "Minier", "Routier"], "r": "Programme élargi de vaccination"},
            {"q": "Langue officielle d'enseignement ?", "o": ["Soussou", "Peul", "Français", "Malinké"], "r": "Le Français"},
            {"q": "Spécialiste des accouchements ?", "o": ["Pharmacien", "Sage-femme", "Infirmier", "Laborantin"], "r": "Sage-femme"},
            {"q": "Document pour s'inscrire au Bac ?", "o": ["Nationalité", "Acte naissance", "BEPC", "Identité"], "r": "BEPC"},
            {"q": "Objectif de la vaccination ?", "o": ["Soigner", "Prévenir", "Diagnostic", "Coût"], "r": "Prévenir les maladies"},
            {"q": "École normale d'instituteurs ?", "o": ["Université", "ENI", "Lycée", "Santé"], "r": "ENI"},
            {"q": "Rôle du centre de santé ?", "o": ["Diplômes", "Soins simples", "Recherche", "Opérations"], "r": "Soigner les cas simples et prévenir les maladies"}
        ],
        "Géographie et Economie": [
            {"q": "Nombre de régions naturelles ?", "o": ["3", "4", "5", "6"], "r": "4"},
            {"q": "Région côtière de la Guinée ?", "o": ["Haute", "Moyenne", "Basse Guinée", "Forestière"], "r": "Basse Guinée"},
            {"q": "Région du massif du Fouta-Djalon ?", "o": ["Basse", "Moyenne Guinée", "Haute", "Forestière"], "r": "Moyenne Guinée"},
            {"q": "Grenier agricole (Savane) ?", "o": ["Basse", "Haute Guinée", "Forestière", "Moyenne"], "r": "Haute Guinée"},
            {"q": "Capitale économique ?", "o": ["Kankan", "Labé", "Nzérékoré", "Conakry"], "r": "Conakry"},
            {"q": "Océan bordant la Guinée ?", "o": ["Indien", "Arctique", "Atlantique", "Rouge"], "r": "Océan Atlantique"},
            {"q": "Fleuve 'Château d'eau' ?", "o": ["Niger", "Sénégal", "Nil", "Congo"], "r": "Le Niger"},
            {"q": "Région de la forêt dense ?", "o": ["Haute", "Basse", "Forestière", "Moyenne"], "r": "Guinée Forestière"},
            {"q": "Premier minerai exporté ?", "o": ["Fer", "Bauxite", "Or", "Diamant"], "r": "Bauxite"},
            {"q": "La Guinée est le 1er réservoir mondial de :", "o": ["Fer", "Or", "Bauxite", "Cuivre"], "r": "Bauxite"},
            {"q": "Premier secteur d'emploi ?", "o": ["Industrie", "Commerce", "Agriculture", "Mines"], "r": "Agriculture"},
            {"q": "Principal port autonome ?", "o": ["Kamsar", "Conakry", "Boké", "Victoria"], "r": "Port de Conakry"},
            {"q": "Culture de rente en Basse Guinée ?", "o": ["Ananas/Riz", "Cacao", "Coton", "Blé"], "r": "Ananas/Riz"},
            {"q": "Voisin au Nord de la Guinée ?", "o": ["Libéria", "Mali/Sénégal", "Ghana", "Bénin"], "r": "Mali/Sénégal"},
            {"q": "Nom de la monnaie nationale ?", "o": ["CFA", "GNF", "Dollar", "Euro"], "r": "Franc guinéen"},
            {"q": "Montagne la plus haute (1752m) ?", "o": ["Fouta", "Gangan", "Nimba", "Loura"], "r": "Mont Nimba"},
            {"q": "Zone minière de Sangarédi ?", "o": ["Or", "Fer", "Bauxite", "Diamant"], "r": "Bauxite"},
            {"q": "Activité du port de Kamsar ?", "o": ["Pêche", "Tourisme", "Bauxite", "Militaire"], "r": "Bauxite"},
            {"q": "Climat de la Guinée ?", "o": ["Polaire", "Désertique", "Tropical", "Tempéré"], "r": "Tropical"},
            {"q": "Centre du négoce en Haute-Guinée ?", "o": ["Labé", "Dalaba", "Kankan", "Kissidougou"], "r": "Kankan"}
        ],
        "Sport et Culture": [
            {"q": "Sport Roi en Guinée ?", "o": ["Basket", "Boxe", "Football", "Lutte"], "r": "Football"},
            {"q": "Surnom de l'équipe nationale ?", "o": ["Lions", "Syli", "Aigles", "Éléphants"], "r": "Le Syli National"},
            {"q": "Unique Ballon d'or africain guinéen ?", "o": ["Feindouno", "C. Souleymane", "Naby Keita", "Titi"], "r": "Cherif Souleymane"},
            {"q": "Ville carrefour touristique ?", "o": ["Mamou", "Kindia", "Labé", "Boké"], "r": "Labé"},
            {"q": "Site 'Voile de la Mariée' situé à ?", "o": ["Kindia", "Dalaba", "Dubréka", "Coyah"], "r": "Kindia"},
            {"q": "Îles touristiques de Conakry ?", "o": ["Loos", "Gorée", "Canaries", "Bijagos"], "r": "Îles de Loos"},
            {"q": "Auteur de 'L'Enfant Noir' ?", "o": ["Tamsir Niane", "Camara Laye", "Williams Sassine", "Monénembo"], "r": "Camara Laye"},
            {"q": "Danse traditionnelle célèbre ?", "o": ["Salsa", "Doundoumba", "Zouglou", "Mbalax"], "r": "Doundoumba"},
            {"q": "Instrument à 21 cordes ?", "o": ["Balafon", "Kora", "Djembé", "Flûte"], "r": "Kora"},
            {"q": "Chanteur de 'Yéké Yéké' ?", "o": ["Mory Kanté", "Salif Keita", "Sékouba Bambino", "Fodé Baro"], "r": "Mory Kanté"},
            {"q": "Patrimoine mondial de l'UNESCO ?", "o": ["Stade", "Mont Nimba", "Palais", "Marché"], "r": "Mont Nimba"},
            {"q": "Le 'Bembeya Jazz' est un :", "o": ["Livre", "Orchestre", "Film", "Stade"], "r": "Orchestre"},
            {"q": "Masque sacré baga ?", "o": ["Nimba", "Koma", "Yacouba", "Sénoufo"], "r": "Nimba"},
            {"q": "Capitale mondiale du livre 2017 ?", "o": ["Dakar", "Abidjan", "Conakry", "Bamako"], "r": "Conakry"},
            {"q": "Festival célèbre de Dubréka ?", "o": ["Cinéma", "Arts de la rue", "Bauxite", "Jazz"], "r": "Arts de la rue"},
            {"q": "Spécialité culinaire (Basse Guinée) ?", "o": ["Lafidi", "Riz sauce feuille", "Tô", "Soupe"], "r": "Riz sauce feuille"},
            {"q": "Instrument de percussion ?", "o": ["Kora", "Djembé", "Guitare", "Flûte"], "r": "Djembé"},
            {"q": "Artiste 'Le Rossignol' ?", "o": ["Sory Kandia", "Mory Kanté", "Bambino", "Kouyaté Sory"], "r": "Sory Kandia Kouyaté"},
            {"q": "Événement culturel annuel ?", "o": ["FENAC", "CAN", "Foire", "Salon"], "r": "FENAC"},
            {"q": "La Kora est originaire du milieu :", "o": ["Soussou", "Mandingue", "Forestier", "Peul"], "r": "Mandingue"}
        ],
        "Justice et Sécurité": [
            {"q": "Loi suprême du pays ?", "o": ["Code", "Décret", "Constitution", "Arrêté"], "r": "La Constitution"},
            {"q": "Qui nomme les magistrats ?", "o": ["Ministre", "Parlement", "Président", "Conseil"], "r": "Le Président de la République"},
            {"q": "Institution de lutte contre la corruption ?", "o": ["Police", "CRIEF", "Douane", "Armée"], "r": "La CRIEF"},
            {"q": "Force de l'ordre urbaine ?", "o": ["Armée", "Police", "Gendarmerie", "Douane"], "r": "La Police"},
            {"q": "Force de sécurité routière/rurale ?", "o": ["Police", "Gendarmerie", "Pompiers", "Milice"], "r": "La Gendarmerie"},
            {"q": "Défense du territoire ?", "o": ["Police", "Gendarmerie", "Armée", "Douane"], "r": "L'Armée"},
            {"q": "Plus haute juridiction ?", "o": ["TPI", "Cour d'Appel", "Cour Suprême", "CRIEF"], "r": "Cour Suprême"},
            {"q": "Gardien de la Constitution ?", "o": ["Cour Suprême", "Cour Constitutionnelle", "Justice", "Police"], "r": "Cour Constitutionnelle"},
            {"q": "Rôle des sapeurs-pompiers ?", "o": ["Arrêter", "Secours/Incendie", "Justice", "Impôts"], "r": "Secours et Incendie"},
            {"q": "Code gérant les crimes ?", "o": ["Civil", "Pénal", "Travail", "Commerce"], "r": "Code pénal"},
            {"q": "Lieu de détention principal ?", "o": ["Hôtel", "Maison centrale", "Commissariat", "Camp"], "r": "Maison centrale"},
            {"q": "Qui rend le verdict ?", "o": ["Greffier", "Avocat", "Juge", "Procureur"], "r": "Le Juge"},
            {"q": "Défenseur des accusés ?", "o": ["Juge", "Procureur", "Avocat", "Huissier"], "r": "L'Avocat"},
            {"q": "Représentant de la loi au tribunal ?", "o": ["Juge", "Procureur", "Avocat", "Greffier"], "r": "Le Procureur"},
            {"q": "Âge de la majorité pénale ?", "o": ["15 ans", "16 ans", "18 ans", "21 ans"], "r": "18 ans"},
            {"q": "Rôle de la Douane ?", "o": ["Vols", "Frontières/Taxes", "Armée", "Feu"], "r": "Contrôle des frontières et taxes"},
            {"q": "Peine maximale actuelle ?", "o": ["Mort", "20 ans", "Perpétuité", "30 ans"], "r": "Perpétuité"},
            {"q": "Que signifie OPJ ?", "o": ["Officier Police Judiciaire", "Ordre Public", "Organisation", "Office"], "r": "Officier de Police Judiciaire"},
            {"q": "Tribunal pour enfants ?", "o": ["CRIEF", "Tribunal pour mineurs", "Militaire", "Civil"], "r": "Tribunal pour mineurs"},
            {"q": "Symbole de la justice ?", "o": ["Balance", "Fusil", "Livre", "Marteau"], "r": "La Balance"}
        ],
        "Histoire et Politique": [
            {"q": "Date du 'NON' à la France ?", "o": ["25 août", "28 sept", "2 oct", "1 nov"], "r": "28 septembre 1958"},
            {"q": "Date de l'Indépendance ?", "o": ["28 sept", "2 oct 1958", "1 janv", "3 avril"], "r": "2 octobre 1958"},
            {"q": "Père de l'indépendance ?", "o": ["L. Conté", "Sékou Touré", "D. Télli", "Alpha"], "r": "Ahmed Sékou Touré"},
            {"q": "Deuxième président (1984-2008) ?", "o": ["Diarra", "Conté", "Dadis", "Konaté"], "r": "Lansana Conté"},
            {"q": "Président de la transition 2010 ?", "o": ["Dadis", "Konaté", "Doumbouya", "Beavogui"], "r": "Sékouba Konaté"},
            {"q": "Année du premier président élu ?", "o": ["1958", "1993", "2010", "2020"], "r": "2010"},
            {"q": "Devise de la Guinée ?", "o": ["Unité-Progrès", "Travail-Justice-Solidarité", "Paix", "Honneur"], "r": "Travail-Justice-Solidarité"},
            {"q": "Couleurs du drapeau ?", "o": ["Bleu-Blanc-Rouge", "Rouge-Jaune-Vert", "Vert-Blanc-Rouge", "Noir-Jaune"], "r": "Rouge-Jaune-Vert"},
            {"q": "Signification du Rouge ?", "o": ["Forêt", "Or", "Sang/Sacrifice", "Soleil"], "r": "Sang/Sacrifice"},
            {"q": "Signification du Vert ?", "o": ["Sang", "Végétation/Espoir", "Soleil", "Ciel"], "r": "Végétation/Espoir"},
            {"q": "Signification du Jaune ?", "o": ["Or/Soleil", "Forêt", "Sang", "Ciel"], "r": "Or/Soleil"},
            {"q": "Premier Guinéen à l'UA (ex-OUA) ?", "o": ["Sékou", "Diallo Télli", "Sidya", "Lansana"], "r": "Diallo Télli"},
            {"q": "Capitale du Royaume de Samory Touré ?", "o": ["Bissandougou", "Kankan", "Labé", "Kindia"], "r": "Bissandougou"},
            {"q": "Résistant du Fouta-Djalon ?", "o": ["Samory", "Alpha Yaya Diallo", "Zégbéla", "Dinah Salifou"], "r": "Alpha Yaya Diallo"},
            {"q": "Résistant de la Basse-Côte ?", "o": ["Samory", "Dinah Salifou", "Alpha Yaya", "Sékou"], "r": "Dinah Salifou"},
            {"q": "Agression subie par la Guinée ?", "o": ["22 nov 1970", "1 nov 1958", "3 avril 1984", "5 sept 2021"], "r": "22 novembre 1970"},
            {"q": "Le CNRD a pris le pouvoir le :", "o": ["22 nov", "28 sept", "5 sept 2021", "2 oct"], "r": "5 septembre 2021"},
            {"q": "Hymne national titre ?", "o": ["Patrie", "Liberté", "Guinéenne", "Syli"], "r": "Liberté"},
            {"q": "Nombre de communes à Conakry ?", "o": ["5", "6", "10", "13"], "r": "13"},
            {"q": "Chef d'État actuel ?", "o": ["Alpha", "Conté", "Doumbouya", "Dadis"], "r": "Mamadi Doumbouya"}
        ]
    }
    
    # Compilation
    all_q = []
    for theme in data_complete:
        all_q.extend(data_complete[theme])
    
    # Mélange et sélection de 20 questions
    random.shuffle(all_q)
    st.session_state.questions = all_q[:20]
    st.session_state.score = 0
    st.session_state.index = -1 
    st.session_state.fini = False
    st.session_state.temps_restant = 30

# --- INTERFACE ---
if st.session_state.index == -1:
    st.title("🇬🇳 Quiz Guinée (Total 100 Questions)")
    st.write("Chaque partie sélectionne 20 questions aléatoires parmi les 100 disponibles.")
    if st.button("🚀 COMMENCER"):
        st.session_state.index = 0
        st.rerun()
elif not st.session_state.fini:
    item = st.session_state.questions[st.session_state.index]
    st.write(f"### Question {st.session_state.index + 1}/20")
    with st.form("q"):
        st.write(item['q'])
        rep = st.radio("Options", item['o'], index=None)
        if st.form_submit_button("Suivant"):
            if rep == item['r']: st.session_state.score += 1
            if st.session_state.index < 19:
                st.session_state.index += 1
                st.rerun()
            else:
                st.session_state.fini = True
                st.rerun()
else:
    st.success(f"Score : {st.session_state.score} / 20")
    if st.button("Rejouer"):
        del st.session_state['questions']
        st.rerun()
