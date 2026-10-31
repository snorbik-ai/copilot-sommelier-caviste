# copilot-sommelier-caviste

[![Pôle Stratégique](https://img.shields.io/badge/P%C3%B4le-04_POLE_USINE_COPILOTES-blue.svg)](#)
[![Nature](https://img.shields.io/badge/Nature-PROTOTYPE-orange.svg)](#)
[![Visibilité](https://img.shields.io/badge/Visibilit%C3%A9-PRODUIT-green.svg)](#)
[![Version](https://img.shields.io/badge/Version-1.0.0-purple.svg)](#)
[![Standard](https://img.shields.io/badge/Standard-V14.1%20Clean%20Architecture-teal.svg)](#)

> **PROTOTYPE PUBLIC DÉMONSTRATEUR (Marketing Métier)**  
> Agent autonome conseillant les accords mets-vins, millésimes et cépages selon le plat choisi par le client.

---

## 1. Carte d'Identité & Rôle Métier

| Champ Stratégique | Valeur Officielle |
| :--- | :--- |
| **Composant Officiel** | `copilot-sommelier-caviste` |
| **Pôle d'Appartenance** | **Pôle 4 : L'Usine Logicielle de Fabrication d'Agents IA** |
| **Modèle Business** | **PROTOTYPE PUBLIC DÉMONSTRATEUR (Marketing Métier)** |
| **Politique de Visibilité** | **PRODUIT DÉMO PUBLIC (Prototype ou Code Démo)** |
| **Mission Principale** | Agent autonome conseillant les accords mets-vins, millésimes et cépages selon le plat choisi par le client. |
| **Architecture** | Clean Architecture Tri-Canal (STDIO / CLI / SDK In-Process) |

---

## 2. Guide d'Installation 1-Clic

### Option A : Installation Automatisée 1-Clic (Recommandée)
Exécutez simplement le script `install.py` à la racine du dépôt :

```bash
python install.py
```

Ce script effectue automatiquement :
1. La vérification de votre environnement Python (>= 3.10).
2. L'installation des dépendances requises en mode éditable (`pip install -e .` ou `npm install`).
3. La détection et l'injection automatique du serveur dans la configuration de Cursor (`%USERPROFILE%/.cursor/mcp.json`) sans écraser vos autres outils.

### Option B : Installation Manuelle Développeur
```bash
pip install -e .
```

---

## 3. Configuration Manuelle (Cursor, Antigravity, Claude Desktop)

Si vous préférez déclarer manuellement ce serveur dans votre fichier `.cursor/mcp.json` ou `mcp_config.json`, ajoutez le bloc suivant :

```json
{
  "mcpServers": {
    "copilot-sommelier-caviste": {
      "command": "python",
      "args": ["main.py"],
      "env": { "PYTHONIOENCODING": "utf-8" },
      "type": "stdio"
    }
  }
}
```

---

## 4. Catalogue Sémantique des Outils (`tools`)

Ce composant expose des outils déterministes prêts à être invoqués par un modèle de langage (LLM) :

| Nom de l'Outil (`tool`) | Rôle & Fonction Technique | Déclencheur d'Action (*Quand l'IA DOIT-ELLE l'appeler ?*) | Paramètres Requis | Sortie Retournée |
| :--- | :--- | :--- | :--- | :--- |
| `sommelier_recommend_pairing` | Propose les 3 meilleurs accords mets-vins selon les ingrédients, la cuisson et la sauce du plat. | **Dès que le client indique son menu ou le type de cuisine dégusté.** | `dish_description (str, requis), budget_range (str, optionnel)` | Recommandation d'appellation, cépage, température de service et note de dégustation. |
| `sommelier_analyze_vintage` | Analyse le potentiel de garde et la maturité d'un millésime pour une région donnée. | **Quand le client demande s'il doit ouvrir une bouteille ou la laisser en cave.** | `appellation (str, requis), vintage_year (int, requis)` | Fenêtre d'apogée (à boire maintenant, à garder 5 ans, à carafer). |

---

## 5. Exemples Concrets de Prompts Utilisateur

Voici 3 exemples réels de requêtes que vous pouvez poser directement dans le chat de Cursor ou Claude Code pour faire travailler cet outil :

1. *« Quel vin rouge servir avec un magret de canard au miel et vinaigre balsamique ? »*
2. *« Est-ce que mon Saint-Émilion Grand Cru 2015 est prêt à être dégusté ? »*
3. *« Propose un vin blanc sec et minéral pour accompagner un plateau de fruits de mer. »*

---

## 🛡️ Propriété Intellectuelle & Sécurité
- **Éditeur :** SNORBIK AI © 2026.
- **Classification :** Conforme à la Directive Maîtresse V14.1 (Recettes d'architecture sanctuarisées dans le Pôle 06).
- **Zéro Régression :** Respect strict des budgets de lignes et des normes de sécurité.
