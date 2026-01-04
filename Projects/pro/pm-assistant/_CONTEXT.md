# Gemini Assistant (Local) - Product Requirements Document

## 1. Vision & Objectifs
**Vision :** Créer une extension cognitive et un "Chef de Projet Exécutif" artificiel. Le système doit absorber la charge opérationnelle, prémâcher le travail stratégique et automatiser le reporting, permettant à l'utilisateur de switcher entre opérationnel et stratégie sans fatigue mentale.

**Succès (North Star) :**
- Délégation complète de la rédaction des slides de Comité de Pilotage (Data -> Slides).
- Zéro charge mentale sur la gestion des tâches/mails.
- Capacité à cadrer un sujet complexe en <15 min d'interaction avec l'agent PM.

## 2. Architecture : La Squad

### 🤖 Alfred (Assistant Personnel & Orchestrateur)
*Le majordome qui gère le quotidien.*
- **Rôle :** Gestionnaire de flux, gatekeeper, planificateur.
- **Outils Connectés :** Google Tasks, Gmail, Calendrier, Système de fichiers local.
- **Niveau d'autonomie :** Élevé (Tri des mails, gestion des priorités).
- **Fonctionnalités Clés :**
    - "Morning Briefing" & "Evening Review" (Processus actuel).
    - Gestion intelligente des emails (Brouillons, résumés, actions).
    - Planification dynamique des tâches (Time blocking).

### 🧠 The Strategist (PM Agent)
*Le bras droit stratégique.*
- **Rôle :** Aide au cadrage, challenge des idées, rédaction de synthèses.
- **Outils Connectés :** Confluence, Fichiers locaux (Markdown), Web Search.
- **Niveau d'autonomie :** Collaboratif (Chat itératif).
- **Fonctionnalités Clés :**
    - Interview de cadrage (L'agent pose les questions pour extraire le jus).
    - Rédaction de PRD / One-pager / Synthèses.
    - Recherche de marché / Veille concurrentielle.

### 📊 The Analyst (Reporting Agent)
*L'expert data et présentation.*
- **Rôle :** Extraction de données, calculs de KPIs, Génération de supports visuels.
- **Outils Connectés :** Jira (API), Databricks (SQL), Google Slides / PPTX.
- **Niveau d'autonomie :** Exécutant expert (Suit des procédures strictes).
- **Fonctionnalités Clés :**
    - "SteerCo One-Click" : Génération du deck hebdo.
    - Analyse de coûts par ticket/sprint.
    - Consolidation des KPIs d'équipe.

## 3. Roadmap Macro

### Phase 1 : Consolidation d'Alfred (Q1)
- [ ] Finaliser l'intégration MCP Google Tasks & Gmail.
- [ ] Implémenter la gestion avancée des emails (Drafting).

### Phase 2 : Le PM Agent (Q1)
- [ ] Test grandeur nature sur un sujet de cadrage réel.
- [ ] Création des templates de sortie (Markdown/Confluence).

### Phase 3 : Le Reporting Agent (Q2)
- [ ] Connexion sécurisée Jira API & Databricks.
- [ ] POC : Extraction des données brutes vers un format structuré (JSON/CSV).
- [ ] POC : Génération de Slides (via API Google Slides ou Librairie Python python-pptx).
