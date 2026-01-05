#!/bin/bash

PLIST_FILE="com.binarii.sync_todo.plist"
DEST_DIR="$HOME/Library/LaunchAgents"

echo "🛑 Arrêt du service..."
launchctl unload "$DEST_DIR/$PLIST_FILE" 2>/dev/null

echo "🗑️  Suppression du fichier plist..."
if [ -f "$DEST_DIR/$PLIST_FILE" ]; then
    rm "$DEST_DIR/$PLIST_FILE"
    echo "   Fichier supprimé."
else
    echo "   Fichier déjà absent."
fi

echo "🧹 Nettoyage des logs..."
rm /tmp/binarii_sync.log /tmp/binarii_sync.err 2>/dev/null

echo "✅ Désinstallation terminée."