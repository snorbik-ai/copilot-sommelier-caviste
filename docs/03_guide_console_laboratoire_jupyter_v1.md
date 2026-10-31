# 🔬 GUIDE DE LA CONSOLE LABORATOIRE JUPYTER
## Banc d'Essai Interactif du Copilote : Copilot Sommelier & Accords Vins

**Localisation du Carnet :** `notebooks/01_console_laboratoire_cycle_de_vie_tour_complet_v1.ipynb`

---

## 🎯 Objectif
Ce carnet Jupyter interactif permet à l'ingénieur et à l'utilisateur de tester, inspecter et visualiser le cycle de vie complet d'un tour de dialogue en conditions réelles, sans dépendance externe.

## 🚀 Démarrage Rapide
1. Lancer Jupyter Lab ou VS Code :
```bash
jupyter lab notebooks/01_console_laboratoire_cycle_de_vie_tour_complet_v1.ipynb
```
2. Exécuter les cellules pas-à-pas (Maj + Entrée).

## 📋 Les Étapes Inspectées dans le Carnet :
1. **Initialisation & Imports :** Chargement propre du package `copilot_sommelier_caviste`.
2. **Formulaire Vivant (DDD) :** Instanciation de `UniversalStateForm`, vérification des 3 slots.
3. **Simulation d'un Tour :** Injection d'un fait utilisateur, calcul du taux de complétion FSM.
4. **Context Engineering S0-S6 :** Assemblage déterministe du prompt système.
5. **Moteur Métier :** Exécution sans IA de l'action déterministe.
6. **Persistance Hybride :** Sauvegarde et rechargement dans le cache SQLite WAL local.
7. **Rendu Visuel HTML/CSS :** Visualisation graphique de la carte d'état et du badge de progression.
