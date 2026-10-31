# 🧠 ARCHITECTURE DU CONTEXT ENGINEERING (SECTIONS S0 À S6)
## Agent Copilote : Copilot Sommelier & Accords Vins

---

## 🗺️ Découpage Inviolable des 7 Sections du Prompt Système

### Section S0 : Méta-Contexte
Horodatage ISO-8601, identifiant unique de session (`session_id`), canal actif et index du tour de dialogue.

### Section S1 : Identité & Doctrine Strictes
Rôle : *Conseiller caviste expert guidant les clients dans le choix d'un vin selon leurs plats et leur budget.*  
Doctrine de conduite :
- Poser impérativement une seule question à la fois.
- Valider avec bienveillance chaque fait collecté.
- Fournir des réponses concises et structurées.

### Section S2 : État de la Tablette GPS (Faits Confirmés)
Représentation vivante des slots confirmés et des slots manquants, synchronisée en temps réel avec le cockpit React.

### Section S3 : Historique Conversationnel Compressé
Historique condensé du Canal A (<= 150 tokens par tour) pour préserver le contexte sans saturer la fenêtre d'attention du LLM.

### Section S4 : Connaissances Métier & Base Documentaire RAG
Données extraites dynamiquement de la base vectorielle (`vector_retriever.py`) ou catalogue certifié.

### Section S5 : Définition des Outils & Schémas JSON
Outils déterministes exposés via le protocole FastMCP et l'API FastAPI.

### Section S6 : Directive Immédiate du Tour
Consigne impérative imposant de formuler la question prioritaire suivante sans répéter les faits déjà acquis.
