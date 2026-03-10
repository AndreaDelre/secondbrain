```button
name Synchroniser Planning
type command
action Shell Commands: Execute: synch-todo
color blue
```
## Planning
### 2026-02-10
- [x] **Grosse Tâche (Frog) :** [Decathlon] Ecrire CR visite en Belgique
- [x] **Grosse Tâche (Frog) :** [Decathlon] [RH] Finaliser projet pro Simon (SIBA) et vision staff/DBT
- [x] [Decathlon] Note de service sur le tracking

### 2026-02-16
- [x] Tâche Secondaire : [Decathlon] Suivre exploration Billel sur Abandonned Browsing
- [ ] Définir les KPIs de Digital Analytics
- [ ] **Grosse Tâche (Frog) :** [Decathlon] [RH] Ecrire 360 Marine Dussaussois
- [ ] Quick Win : [Decathlon] Analyser les demandes d'usages sur Amplitude (Top utilisateurs)
- [ ] [Decathlon] Étudier représentativité du non-consent et KPIs
- [x] Trier le reste du dossier Inbox

### 2026-02-17

### 2026-02-18
- [x] [Decathlon] Prendre les billets de train
- [x] [Decathlon] Mettre à jour l'odj avec Leandro
- [x] [Decathlon] Définir la notion d'anonymisation des données Piano et Amplitude non-consent
- [x] Trier le reste du dossier Inbox

### 2026-02-19
- [x] [Decathlon] Définir les KPIs de Digital Analytics
- [x] Tâche Secondaire : [Decathlon] Synchro Oussama (Data Model) & Leandro (Insights/Tracking)
- [x] Tâche Secondaire : [Decathlon] Discuter avec Leandro de l'organisation de l'équipe tracking

### 2026-02-23
- [x] **Grosse Tâche (Frog) :** [Decathlon] [RH] Ecrire 360 Marine Dussaussois

### 2026-03-09
- [ ] OpenCode Bootstrap
- [ ] Cleaning mail
- [ ] [Decathlon] Briefing Simon Agents Omni Marketing
- [ ] [Decathlon] Mission Chloé
- [ ] [Decathlon] Étudier représentativité du non-consent et KPIs
- [ ] Quick Win : [Decathlon] Analyser les demandes d'usages sur Amplitude (Top utilisateurs)
- [ ] Tâche Secondaire : [Decathlon] Relire plan 2026 de Simon Bazin

### 2026-02-02 (Past)
- [ ] Préparation Roadmap
- [ ] Préparation cadrage abandonned browsing
- [ ] Préparation cadrage streaming
- [x] Trier le dossier Inbox (In Progress)
- [ ] [Decathlon] Présentation Thibault PEETERS
- [ ] [Decathlon] Vision d'équipe 2026
- [ ] [Decathlon] Analyse France pour CA par arbo
- [ ] [Decathlon] Revue des pratiques IA PM
- [ ] [Decathlon] Brief Agent PM
- [ ] [Decathlon] Vision Collection 2026

### 2026-02-03
- [ ] Tâche Secondaire : [Decathlon] Agent Reporting - Cartographier les données (Jira/Databricks)
- [ ] Quick Win : [Decathlon] Daily - Définition des critères de check des périmètres
- [ ] Quick Win : [Decathlon] Daily - Mise à jour sur TiS
- [ ] Quick Win : [Decathlon] Daily - Mise à jour sur DA

### 2026-01-30
- [ ] [Perso] - [CellarCloud] Stratégie de refont v2
- [ ] Quick Win : [Perso] Administratif - Envoyer fiches médicales mutuelle

## Projects
### [Decathlon] Daily Tasks
- [ ] Trier les emails Decathlon
- [ ] Trier les tâches
- [ ] Définition des critères de check des périmètres
- [ ] Mise à jour sur les périmètres
### [Decathlon] Agent Reporting Steering Committee
**Objective :** Automatiser la génération de slides de Steering Committee à partir de données Jira et Databricks via un agent IA.
**Success Criteria :** Obtention d'un deck de slides de qualité attendue sur simple demande à l'agent.
- [ ] Générer un extract Jira quotidien
- [ ] Générer les données de présence équipe et TJS associés
- [ ] Enrichir l'extract Jira avec le coût par ticket par sprint
- [ ] Générer la synthèse de chaque Epic Jira (basée sur les données enrichies)
- [ ] Extraire les informations de coûts des projets depuis Databricks
- [ ] Créer le template de slides
- [ ] Rédiger le prompt agent spécialisé pour la génération des slides

### [Binarii] Infrastructure as Code
**Objective :** Industrialiser l'infrastructure manuelle (Proxmox, K8s, Terraform) pour permettre l'ajout de machines headless et le déploiement automatisé.
**Success Criteria :** Infrastructure entièrement définie en code (IaC), déploiement de clusters K8s automatisé sur Proxmox.
- [X] Définir l'architecture cible et réaliser les schémas d'infrastructure.
- [ ] [Binarii IaC] HTTPS : Mettre en place certificat SSL local

### [Binarii] Minerva (Refonte Outil de veille)
**Objective :** Transformer le PoC actuel en une application robuste de veille collaborative intégrée à Discord.
**Success Criteria :** Code maintenable, flux d'ajout manuel via Discord opérationnel, Recap hebdo automatisé.
- [ ] Fix Minerva fetcher (le script ne tourne pas)
- [ ] Audit du code actuel et définition du plan de refonte
- [ ] Créer un endpoint Webhook pour l'ajout manuel d'articles
- [ ] Intégrer la commande d'ajout d'article dans le Bot Discord
- [ ] Développer la logique de génération du récapitulatif hebdomadaire
- [ ] Automatiser l'envoi du récapitulatif sur Discord

### [Binarii] Binario (Discord Bot)
**Objective :** Interface centrale sur Discord pour lire/enrichir la documentation d'entreprise et interagir avec l'historique des conversations.
**Success Criteria :** Recherche efficace dans l'historique et réponses contextuelles basées sur les échanges passés.
- [ ] Étudier l'API Discord pour récupérer l'historique des messages d'un channel/thread
- [ ] Implémenter l'injection de l'historique dans le contexte du bot

### [Binarii] Gemini Assistant (Local)
**Objective :** Développer une squad d'agents (Alfred, Strategist, Analyst) pour augmenter la productivité (Voir GEMINI_ASSISTANT.md).
**Success Criteria :** Slides automatisés, Cadrage assisté, Gestion tâches fluide.
- [ ] [Alfred] Définir le workflow de travail (Brain Dump, Structurer, Prioriser, Planifier)
- [ ] [Alfred] Ajouter la fonctionnalité de modification de brouillons au MCP Gmail
- [ ] [Strategist] Tester l'agent PM sur un sujet de cadrage réel (Crash Test)
- [ ] [Analyst] Cartographier les données nécessaires (Champs Jira, Tables Databricks) pour les slides
- [ ] [Analyst] Faire un POC technique simple de génération de slide (Python -> PPTX)

### [Binarii] MiniDiairy
**Objective :** Créer un pont de synchronisation bidirectionnel entre les fichiers Markdown locaux (Obsidian/TODO) et Google Tasks, avec une interface d'entrée rapide sur macOS.
**Success Criteria :** Saisie rapide via Mac (<3s), synchronisation bidirectionnelle temps réel Markdown <-> Google Tasks, compatibilité totale avec les agents IA.
- [X] Réaliser le cadrage initial (Besoins, MVP, Stack technique)
- [ ] Configurer l'authentification Google Tasks API (OAuth2)
- [ ] Développer le script de synchronisation (Watcher Markdown -> API Tasks)
- [ ] Implémenter la synchronisation inverse (Polling/Webhook Tasks -> Markdown)

### [Binarii] Organisation
**Objective :** Gérer les tâches transverses et organisationnelles de Binarii.
**Success Criteria :** Coordination fluide des réunions et des échéances trimestrielles.
- [X] Réunion du vendredi - 20260102
- [ ] Envoyer l'invitation de la réunion du vendredi - 20260109
- [ ] Réunion du vendredi - 20260116
- [ ] Réunion mi-janvier pour définition du quarter

### [Binarii] Blog Stratégie
**Objective :** Définir la voix et le contenu de Binarii.io.
**Success Criteria :** Ligne éditoriale posée, planning de 10 articles prêt.
- [ ] Poser les 3 piliers de la ligne éditoriale.
- [ ] Lister les 10 prochains sujets d'articles à traiter.

### [Perso] Travaux Maison
**Objective :** Rénovation complète de la maison (Se référer au fichier TRAVAUX.md pour le détail par pièce).
**Success Criteria :** Travaux terminés selon les standards de qualité définis pour chaque pièce.
- [X] Définir les grandes phases de rénovation et prioriser les pièces.
- Le reste des tâches se trouves dans projects/perso/travaux/_TODO.md

### [Perso] Intendance Maison
**Objective :** Gestion fluide et organisée des tâches quotidiennes et de la logistique du foyer.
**Success Criteria :** Maison entretenue, logistique maîtrisée sans surcharge mentale.
- [ ] Arroser les plantes
- [ ] Lessives Couleurs
- [ ] Lessives Blanches

### [Perso] Administratif
**Objective :** Maintenir à jour et organiser les documents administratifs personnels et familiaux.
**Success Criteria :** Documents classés, échéances respectées.
- [ ] Envoyer les fiches médicales pour remboursement mutuelle (Fin janvier 2026)
- [ ] Envoyer les factures d'hopital pour remboursement mutuelle rugby
- [ ] Rendez-vous dentiste
- [ ] Rendez-vous passeport
- [ ] Rendez-vous ophtalmo