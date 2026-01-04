# Improvements - 2026-01-02

## 🛠 Process & Interaction
- **Rigueur Nettoyage TODO :** Règle absolue : une fois le Logbook généré, la section des tâches terminées ("Done") **DOIT** être supprimée du fichier `_TODO.md`. Ce fichier ne doit contenir que les tâches à venir.
- **Formatage Date :** Ajouter systématiquement la date cible dans le titre de la section quotidienne (ex: `## Today (Defined) (2026-01-03)`) pour éviter toute ambiguïté sur la journée planifiée.
- **Recherche Contacts Flexible :** Si une recherche de contact par "Prénom Nom" échoue, tenter automatiquement une recherche plus large (juste le "Prénom" ou des variations orthographiques) avant de conclure à l'absence du contact.
