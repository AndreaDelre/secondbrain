# 

## Contexte
Création de status pal automatique qui existe côté Digital Analytics, nous avions besoin de reproduire ce processus sur les données de la search console (API).

Actuellement, régulièrement Google n'expose pas les données, et quand ça arrive c'est plusieurs jours consécutif.

Il fallait faire des évolutions pour adapter au comportement de global analytics, qui peut avoir plusieurs jours d'affilés l'issue.

## La timeline
- Démarrage en mob prog en octobre 2025, sujet pas prioritaire. Pas tjr simple avec le contexte du mob prog
- Un ticket a été créé pour Global Analytics, en novembre/décembre 2025.
- Sujet abordé côté traffic store il y a 3 semaines
- Simon informe que TiS, est sur le sujet et voir comment le faire avec eux car python opertor n'est pas cible. EKS (cluster partagé avec decathlon), usage car pas de databricks dispo en live et trop cher pour ce qu'on fait par rapport à EKS
- Simon indique que l'information n'était pas très tranché de sa part pour utiliser EKS.
- Cadrage avec TiS et Global, où Victor et Matthieu n'etait pas très impliqué. Ils ont donné leurs avis et après quand on a définit les tables
- Document de cadrage partagé sous forme d'ADR
- Ticket pris sprint dernier
- Il a commencé sur airflow, Chloé a aussi continué sur Airflow, ce qui a été dit c'est que ça allait être trop le bazarre de tout faire en même temps.
- Il a été décidé de faire la partie EKS en premier, pour ne pas faire du travail en double, et que ça puisse être réutilisé pour d'autres sujets.
    - Exemple de airflow car trop complexe, j'ai presque fini donc autant que j'aille au bout.
    - Même toi tu as du mal à te relire et maintenable
    - Retour fait le mercredi ou jeudi avant son départ
    - Vendredi PR envoyée avant le départ, vendredi à 20h

## Les conséquences
- Code pas maintenable
- Il faut potentiellement repartir à 0

## Root causes
- Pourquoi on se rend après deux semaines qu'il faut jeter le code (logique métier ok) ?
- Ticket pas assez découpé en amont
- Manque de maturité sur le sujet avant de démarrer l'indus
- On pensait pouvoir reprendre ce qui pouvait être fait sur Digital et ça n'était pas le cas

## Les actions / recommandations
- Redécouper le ticket
- Cadrer la solution technique
- Se mettre des jalons
- 


# Ressentis Victor

- Le timing était pas bon
- Le sujet de status pal auto était prio car on doit avoir status pal rapidement
- Il faudrait avoir une migration vers EKS
- On en discute et je vois que c'est hyper flou
    - Soit je vais à la cible et ça va être long
    - Je peux pas amorcer le sujet car je connais pas le sujet
    - J'en ai parlé avec Skander, comme ça on a quelque chose qui fonctionne et qui répond à notre besoin
- On est prêt a basculé vers la cible dès qu'on est au clair
- 4 jours plein sur le sujet, très gros et beaucoup de code, mais pas encore en prod donc besoin d'une phase de teste pour savoir si on a pas de faux positifs puis repousser en prod donc il reste 1 jour de dev
- Pas présenté à Simon et Pierre

- Pas de ticket qui peuvent pas être fini