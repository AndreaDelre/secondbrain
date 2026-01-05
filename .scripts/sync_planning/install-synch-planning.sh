#!/bin/bash

# Définition des variables
PLIST_FILE="com.binarii.sync_todo.plist"
DEST_DIR="$HOME/Library/LaunchAgents"

# 1. Créer le dossier s'il n'existe pas (C'est ce qui manquait)
if [ ! -d "$DEST_DIR" ]; then
    echo "📂 Création du dossier $DEST_DIR..."
    mkdir -p "$DEST_DIR"
fi

# 2. Copier le fichier
echo "📄 Copie du fichier plist..."
cp "./$PLIST_FILE" "$DEST_DIR/"

# 3. Décharger l'ancienne version si elle existe (pour éviter les doublons/erreurs)
launchctl unload "$DEST_DIR/$PLIST_FILE" 2>/dev/null

# 4. Charger la nouvelle version
echo "🚀 Activation de l'agent..."
launchctl load "$DEST_DIR/$PLIST_FILE"

echo "✅ Installation terminée avec succès."