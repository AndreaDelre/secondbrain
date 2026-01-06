```button
name Synchroniser Planning
type command
action Shell Commands: Execute: synch-todo
color blue
```
## Planning
### Today (In Progress) (2026-01-07)
- [ ] [Perso] Poser les boitiers de prises
- [ ] [Perso] Tirer les cables des prises
- [ ] [Perso] Reboucher les saignées
### 2026-01-08
- [ ] [Perso] Enduire les murs du garde manger
- [ ] [Perso] Protéger le sol du premier étage
- [ ] [Perso] Enduire les murs du 1er étage
### 2026-01-09
- [ ] [Perso] Poncer les murs
- [ ] [Perso] Passer l'éponge sur les murs
- [ ] [Perso] Passer la deuxième couche d'enduit

## Projects
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

### [Binarii] MiniNote
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

### [Perso] Administratif
**Objective :** Maintenir à jour et organiser les documents administratifs personnels et familiaux.
**Success Criteria :** Documents classés, échéances respectées.
- [ ] Envoyer les fiches médicales pour remboursement mutuelle (Fin janvier 2026)
- [ ] Envoyer les factures d'hopital pour remboursement mutuelle rugby
