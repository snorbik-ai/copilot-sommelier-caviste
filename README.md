# copilot-sommelier-caviste

[![Pôle Stratégique](https://img.shields.io/badge/P%C3%B4le-04_POLE_USINE_COPILOTES-blue.svg)](#)
[![Nature Commerciale](https://img.shields.io/badge/Nature-PROTOTYPE-orange.svg)](#)
[![Visibilité](https://img.shields.io/badge/Visibilit%C3%A9-PRODUIT-green.svg)](#)
[![Clean Architecture](https://img.shields.io/badge/Architecture-Clean%20Architecture%20Ports%20%26%20Adapters-teal.svg)](#)
[![Budget Lignes](https://img.shields.io/badge/R%C3%A8gle%20%235-%3C%20350%20Lignes%20Garanti-blueviolet.svg)](#)

> **PROTOTYPE PUBLIC DÉMONSTRATEUR (Marketing Métier)**  
> Démonstrateur vitrine LinkedIn de notre usine logicielle : prouve notre capacité à fabriquer un agent dans un domaine raffiné sans secret industriel.

---

## 1. Fiche d'Identité & Modèle Commercial

| Champ | Valeur Stratégique |
| :--- | :--- |
| **Composant** | `copilot-sommelier-caviste` |
| **Pôle d'Appartenance** | **Pôle 4 : Usine Logicielle de Fabrication d'Agents IA** |
| **Modèle Business** | **PROTOTYPE PUBLIC DÉMONSTRATEUR (Marketing Métier)** |
| **Stratégie de Visibilité** | **PRODUIT DÉMO PUBLIC (Prototype)** |
| **Potentiel Marché** | Démonstrateur vitrine LinkedIn de notre usine logicielle : prouve notre capacité à fabriquer un agent dans un domaine raffiné sans secret industriel. |

---

## 2. Guide d'Installation 1-Clic (Développeur Humain)

```bash
git clone https://github.com/snorbik-ai/copilot-sommelier-caviste.git
cd copilot-sommelier-caviste
python install.py
```

Le script installe automatiquement les dépendances requises et résout les chemins de manière dynamique (**zéro chemin Windows absolu en dur**).

---

## 3. Configuration 1-Clic pour Agents IA (Cursor, Antigravity, Claude Code)

Ajoutez ce bloc à votre fichier `.mcp.json` ou `mcp_config.json` :

```json
{
  "mcpServers": {
    "copilot-sommelier-caviste": {
      "command": "python",
      "args": ["canal_mcp/mcp_server.py"],
      "env": {
        "PYTHONIOENCODING": "utf-8"
      },
      "type": "stdio"
    }
  }
}
```

---

## 4. Catalogue Sémantique des Outils (`tools`)

| Outil (`name`) | Rôle & Fonction | Déclencheur d'Action (Quand l'appeler ?) | Arguments requis | Sortie Observable |
| :--- | :--- | :--- | :--- | :--- |
| `recommend_wine_pairing` | Conseille le cépage, l'appellation et le millésime idéaux selon le plat servi. | **Quand l'utilisateur décrit son menu ou demande un accord vin.** | `dish_name (str), budget (str|optional)` | Fiche de dégustation et recommandations caviste |

---

## 5. Exemples Concrets de Prompts Utilisateur

Vous pouvez déclencher immédiatement ce composant en formulant ces requêtes dans votre IDE :

1. *« Quel vin recommandes-tu pour accompagner un magret de canard aux cerises ? »*
2. *« Propose-moi un vin blanc sec minéral à moins de 25 euros. »*
3. *« Donne-moi les accords parfaits pour un plateau de fromages affinés. »*

---

## 📜 Propriété & Licence
Composant officiel de l'écosystème **SNORBIK AI © 2026**.  
Tous droits réservés.
