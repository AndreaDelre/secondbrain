---
name: Data Team Budget Management
description: |
  Skill dédié à la gestion du budget de l'équipe data "Interactions".
---

# Data Team Budget Management Skill

## Overview
Ce skill est conçu pour faciliter la gestion du budget de l'équipe data "Interactions" en intégrant les données Jira qui est l'outils de gestion de projet. Ces données sont exportées dans une table Databircks accessible en utilisant le tool Databricks au path suivant `hive_metastore.preprod_digital_analytics_temporary.global_jira_tickets_enriched`.

Le google Sheet qui accompagne la gestion budgétaire pour 2026 est accessible via le tool Google Sheets avec l'ID `1Ll4oxjix5Z5Aufxk5BUsjEORiBFXMyE6HtceO49VDVE` et la feuille ciblée est `Epics` mais il est possible d'utiliser d'autres feuilles du même document si nécessaire.

Le dossier de travail en local est dans `projects/pro/decathlon/collection/global/budget`, tous les fichiers qui doivent être générés ou modifiés pour la gestion budgétaire doivent être créés ou modifiés dans ce dossier.

## When This Skill Applies
Ce skill s'applique automatiquement lorsque l'utilisateur à une demande concernant la gestion budgétaire. Demande confirmation à l'utilisateur avant d'activer le skill.

## Main concepts

La collection "Interactions" se compose de 3 sous équipe appelé Core Data Product (CDP), les analyses peuvent être faites à la fois à la maille collection mais aussi CDP. Les CDP sont les suivantes :
- Online Interactions (Digital Analytics)
- Store Interactions (Traffic In Store)
- Marketing Interactions (Global Analytics)

Le modèle de données Jira dans Databricks est le suivant :
- id -> string
- url -> string
- key -> string
- summary -> string
- issuetype -> string
- creator_email -> string
- created -> timestamp
- updated -> timestamp
- status -> string
- story_points -> double
- labels -> array<string>
- parent_id -> string
- parent_key -> string
- parent_summary -> string
- components -> array<string>
- cdp_name -> string
- activity_type -> string
- domain -> string
- sprints -> array<string>
- last_sprint -> string
- year -> int
- total_story_points_done -> double
- coef_to_story_points -> double
- daily_cost -> string
- ticket_cost -> double
- collection -> string
- dev_start_date -> date
- dev_end_date -> date
- project_code -> string
- support_group_name -> string
- start_date -> date
- due_date -> date
- description -> string

Il est aussi possible d'accéder directement au ticket en utilisant le tool Jira avec `get_ticket` et en utilisant le key du ticket.

Le budget est géré grâce aux Epics qui sont des éléments de travail dans Jira. Chaque Epic représente une initiative ou un projet avec un budget associé. Les données des Epics sont enrichies dans la table Databricks mentionnée ci-dessus, ce qui permet d'analyser les budgets alloués, les dépenses et les prévisions. Toutes les informations budgétaires sont dans la colonne description sous un format json.

## Artefacts

Gsheet de suivi budgétaire : `1Ll4oxjix5Z5Aufxk5BUsjEORiBFXMyE6HtceO49VDVE` (feuille `Epics`)
Il faut vérifier et mettre à jour les différents champs, attention c'est un onglet critique donc il ne faut aucune allucination, il faut donc utiliser des stratégèmes pour être très précis.

Fiche .md par epic par CDP : Il faut générer en local une fiche par Epic dans le dossier de travail `projects/pro/decathlon/collection/global/budget/[cdp_name]/` avec en nom `[epic_key]_[epic_summary].md`. Dans cette fiche il faut indiquer les éléments suivants :
- Budget
    - Exploration
    - Scoping
    - Build
    - Compute
    - Storage
    - Human Run
- Context and Objective
- Project Description
- Benefit for the Company

Tu devrais pouvoir retrouver ces informations dans la colonne description de la requêtes SQL ou directement quand tu utilises le tool jira sur un ticket précis.