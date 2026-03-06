# L'historique des données Piano France App S2S
## Contexte

## Plan d'action
- [x] Demande d'export d'une journée (pendant les congés de Marine et pas de réponse de l'équipe France sur le mail, indication de si urgence contacter Louise DECOOL pas de demande faite par la France)
    - Boucle de feedback à Piano car données non conformes (4 rounds sur 5 jours)
- [x] Génération du notebook de test (La France était en cc des mails et pas de demandes particulières)
- Demande de la part de France d'un test sur une semaine complète
- [x] Demander l'export de une semaine à Piano - En attente de réponse (1h de délai)
- [ ] Utiliser le notebook de test pour obtenir les KPIs et les résultats de Test
- [ ] Mettre à dispo les KPIs pour la France
- Go / No Go
- [ ] Delande d'export de toutes les données S2S depuis juillet 2024 (Risque de délai)
- [ ] Lancement du recovery (2 jours)

# Modèle unifié
## Contexte
Découverte en Décembre 2024, que les données app de Piano France ne contenaient d'event checkout. Nous ne faisons aucune analyse de qualité de données sur les données Piano, suite à la consigne de 2024 nous indiquant que les efforts devaient être mis sur Amplitude. Les données Piano étaient à disposition des équipes France et donc non utilisées sinon nous nous en serions rendu compte.

## Plan d'action
- [x] Import des données app Piano dans le modèle unifié ()
    - Les données app Piano n'étaient pas ingérées dans le modèle unifié jusque maintenant, car personne n'était en capacité de nous garantir la qualité des données. Suite à une demande de l'ecom d'avoir des données historiques et à cause de mon absence, il n'y a pas eu de stop sur le sujet. Élément d'apprentissage: Toujours chercker les main events avant l'insertion dans un modèle unifié. Mise en place de tests métiers au travers un playbook.
- Warning le 19/01 -> Exploration -> le 21/01 avertissement de la complexité et des différences entre S2S et classic app tracking
- Demande de décision de la part de la France pour savoir quelles données utilisées : S2S ou Classic app tracking
- Notre recommandation est de faire un script temporaire qui combine les données le temps qu'on ne regarde plus que les données Amplitude
- [ ] Supprimer les données app Piano du modèle unifié

# Scenarios

No go revamp
- [ ] Plus de capacité d'acheter
- [ ] Plus possible de voir un produit
- [ ] Parcours X cassé

- [ ] Manque de capacité de dectecter ça
    - [ ] Monitoring des erreurs 500, 400, 401 -> >300 
        - Monitoring déjà là
    - [ ] Bug de trackign -> On perd des données de tracking
        - Comparaison des volumes de données journalières sur les données non consent (données déjà possédées)
    - [ ] Manque d'atractivité -> Pas lavable sur l'app et pilotage valable sur le web