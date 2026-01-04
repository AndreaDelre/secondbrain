# Improvements - 2026-01-01

## 🛠 Process & Interaction
- **Logbook enrichi :** Intégrer systématiquement la liste brute des tâches terminées (format Markdown check-list) à la fin du logbook quotidien pour conserver le détail des actions atomiques.
- **Investigation de contexte projet :** Lorsqu'un projet possède son propre fichier `_TODO.md` dans un sous-répertoire technique (ex: `../binarii/binarii-iac/`), l'utiliser comme source de vérité pour définir les prochaines actions dans le `_TODO.md` principal.
- **Réactivité Planification :** Si l'utilisateur dépasse les objectifs fixés (ex: migration faite alors que seule l'architecture était prévue), mettre à jour immédiatement les étapes du projet global pour refléter le nouvel état d'avancement (ex: passer à l'étape "Automatisation Hardware").
- **Ménage de fin de journée :** Une fois le logbook généré et validé, s'assurer que le fichier `_TODO.md` principal est nettoyé des sections de tâches terminées pour ne laisser que le futur ("Today Defined" et "Projects").
