🇬🇳 Quiz Interactif : Culture & Histoire de la République de Guinée
 Présentation du Projet
Ce projet est une application web interactive conçue pour tester et renforcer les connaissances sur la République de Guinée. À travers une banque de 100 questions variées (Géographie, Histoire, Culture, Économie), l'application propose des sessions dynamiques de 20 questions tirées aléatoirement, offrant une expérience ludique et éducative.

L'objectif est double : promouvoir le patrimoine guinéen et démontrer une maîtrise technique de l'écosystème Python Data.

 Compétences Techniques & Outils
 Langages & Programmation
Python (Core) : Utilisation avancée des structures de données (listes de dictionnaires) pour la gestion de la base de données de questions.

Logique Algorithmique : Implémentation d'un algorithme de tirage aléatoire sans répétition (random.sample) pour garantir une expérience unique à chaque partie.

 Frameworks & Systèmes
Streamlit : Développement d'une interface utilisateur (UI/UX) réactive et moderne.

Session State Management : Gestion avancée de la mémoire du navigateur pour la persistance du score et de l'index des questions sans base de données externe.

Deployment : Maîtrise du cycle de déploiement continu via Streamlit Cloud synchronisé avec GitHub.

 Architecture du Système
Moteur de Quiz : Système de validation des réponses en temps réel.

Évaluation Qualitative : Algorithme de calcul de score avec feedback automatisé basé sur 7 niveaux de performance (de "À réviser" à "Honorable").

 Impact et Valeur Ajoutée
Éducation & Culture : Création d'un outil numérique valorisant le patrimoine guinéen, accessible à la diaspora et aux locaux.

Design UX : Utilisation d'animations (balloons), de métriques visuelles et de composants interactifs pour maximiser l'engagement.

Scalabilité : Architecture modulaire permettant d'étendre facilement la base de données à des milliers de questions.

 Structure du Projet
Plaintext

├── .streamlit/         # Configuration du thème
├── app.py              # Script principal (Logique & UI)
├── requirements.txt    # Liste des dépendances Python
└── README.md           # Documentation technique (ce fichier)

 Installation Locale
Cloner le dépôt

Bash

git clone https://github.com/votre-username/quiz-guinee.git
cd quiz-guinee
Installer les dépendances

Bash

pip install streamlit
Lancer l'application

Bash

streamlit run app.py

À Propos de l'Auteur
Almamy Kalla BANGOURA Consultant Data & BI 

Passionné par l'intersection entre la technologie, l'éducation et l'analyse de données. Ce projet illustre ma capacité à transformer des concepts complexes en outils numériques intuitifs et performants.

Pour consulter l'interface ou pour jouer https://akb-quiz-gn224.streamlit.app/