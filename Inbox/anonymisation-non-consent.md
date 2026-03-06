# Description de l'anonymisation des données non-consent Piano et Amplitude

Pour le département légale, suite à une plainde à la CNIL, nous avons besoin de produire un document décrivant les données permettant d'identifier une personne dans la donnée, quelles informations nous provient directement du provider (Piano ou Amplitude) et quelles informations nous avons détruites/encryptées en interne, ainsi que les processus d'anonymisation mis en place pour ces données.

# Short answer

## Amplitude
Côté Amplitude, nous ne possédons pas de member_id pour les données non-consent, les informations disponibles ne sont pas suffisantes pour générer un identifiant unique même en croisant les différentes données disponibles. En revanche, le transaction_id est envoyé en clair à Amplitude, ce qui côté lake.

Les données non-consent côté lake étant protégées, un utilisateur ne peut pas effectuer un traitement pour recouper avec la table transaction et identifier la personne sans que l'équipe soit au courant.

En revanche, une personne pourrait faire un export d'Amplitude et venir croiser avec les données de ventes pour remonter à la personne.

Action à prendre:
- hasher le transaction_id lors de l'envoie à Amplitude

## Piano
Côté Piano, nous recevons beaucoup de données et toutes les informations sont dans la même table.
Piano stoque et nous envoie en clair les member_id et transaction_id des utilisateurs en non consent.
Les données Piano, sont exposées uniquement à l'équipe France Marketing qui n'applique pas de traitement sur les données non-consent, et les données.

Nous exécutons un script régulièrement pour uniquement supprimer les member_id, nous pourrions aussi l'étendre aux transaction_id.

Action à prendre:
- hasher le member_id lors de l'envoie à Piano
- hasher le transaction_id lors de l'envoie à Piano

# Contexte

Ce document est produit dans le cadre des données stockées et mises à disposition par les équipes data dans le Datalake.

Je vous ajoute un glossaire simplifié des éléments à comprendre pour mieux appréhender le document, ainsi que les processus d'ingestion et les colonnes des données Piano et Amplitude :

- Front-end : partie visible d'un site web ou d'une application, avec laquelle les utilisateurs interagissent directement.
- Back-end : partie d'un site web ou d'une application qui gère la logique métier
- Librarie de tracking (Google Tag Manager ou Click Stream) : librairie de code installé sur les sites web, app ou backend qui permet de collecter des données sur les utilisateurs et leurs comportements, ces données sont ensuite envoyées aux différents providers pour traitement si consent donné.
- Un outils d'analyse web (Piano ou Amplitude) collecte des données sur les utilisateurs, ces données sont ensuite stockées dans leur propre espace de stockage, elles sont modélisées au travers une interface web accessible aux collaborateurs qui ont un compte afin de produire des analyses. Ces outils bénéfices de leur propre gestion de droits. Ils mettent ensuite à disposition leurs données au près de Decathlon via des processus d'export.
- Databricks : outil de requêtage, d'analyse de données et de construction de job. Il est utilisé par les équipes data pour analyser les données. Il permet aussi d'éxécuter des jobs qui produisent eux même des données basées sur les données d'autres tables.
- Une donnée stockée est une donnée enregistrée sur un espace de stockage dans le cloud, une donnée stockée ne veut pas dire qu'elle est disponible à l'ensemble de l'entreprise.
- Bucket : espace de stockage dans le cloud, qui peut être structuré en dossiers, il est associé à des droits d'accès.
- Datalake (version simplifié): espace de centralisation de la donnée, qui est structuré en tables ou dossier (bucket). Certaines de ces tables/buckets sont publiques (accessibles par n'importe qui dans l'entreprise), d'autres sont privées (accessibles uniquement par demandes de droits).
- Une donnée exposée est une donnée qui est mise à disposition sur des accès publics (entreprise) ou privés, via des outils de requêtage/analyses comme Databricks ou Tableau. Certains de ces outils permettent d'exporter les données dans un format type CSV.
- Une base de données est un ensemble de tables, souvent regroupées par thématique.
- Une table de données est un ensemble de données structurées, organisées en colonnes et lignes, on peut prendre l'image d'un très gros fichier excel.
- Une table publique est une table accessible par n'importe qui qui possède un accès au Datalake.
- Une table privée est une table accessible uniquement par des personnes qui ont reçu des droits d'accès spécifiques suite à une demande.
- Enrichissement de données : processus d'ajout d'informations à une donnée, par exemple en croisant une donnée avec une autre source d'information, ou en appliquant des règles de transformation.
- Ingestion de données : processus de collecte/récupération et de stockage de données dans un espace de stockage, par exemple en collectant des données via une API ou en les extrayant d'une base de données. Les données nous sont parfois mises à disposition directement dans nos buckets.

# Organisation des données comportementales (tracking data)

Nous possédons 3 zones de données :
- Bronze : bucket avec les données brutes déposées par les providers (Piano et Amplitude).
- Raw (silver) : base de données avec les données brutes mis en forme de table afin de pouvoir être interogées via des outils de requêtage (Databricks).
- Enriched (gold) : base de données avec les données enrichies avec des règles ou croisement de données. C'est sur cette zone que les gens se sourcent ou manipulent les données pour faire des analyses, des algorithmes, etc.

Nous ne détruisons que l'adresse ip, la longitudet et latitude dans les données Amplitude, peut importe consent ou non consent.
Concernant les données Piano, ils nous a été demandé de ne pas faire autre chose que du maintien opérationel sur le sujet vu qu'il devrait être décomissioné. Nous avons donc uniquement créé un job temporaire que nous lançons à la main pour supprimer les member_id des données non-consent.

# Processus d'ingestion et d'exposition
## Piano
- Piano met à disposition dans un bucket dédié les données de tracking collectées sur les sites/app de Decathlon, ces données sont mises à disposition dans des fichiers au format JSON, avec un rafraîchissement quotidien.
    - Ces données ne concernent que la France.
    - Elles sont mises de façon séparée, un dossier/bucket pour les données web consent et non consent mélangées.  Puis un dossier/bucket pour les données app (par librairie dans l'app) consent et non consent. Puis un dossier/bucket pour les données app (par librairie dans le back-end) consent et non consent.
    - Une colonne permet d'identifier le consentement ou non des utilisateurs.
- Nous venons écrire une table dans notre zone raw qui. Cette table est uniquement utilisée par l'équipe Data Marketing FR avec le filtre sur les consents (cookies) + table de consent de solitcitation marketing.
- Il existe une table pour web, une table pour app et une autre table pour app_s2s (back-end). Elles sont toutes strcturées de la même façon.

## Amplitude
- Amplitude met à disposition dans un bucket dédié les données par pays et par platform (web/app)
- Nous créons une table dans notre zone raw qui regroupe tous les pays et platforms.
- Nous créeons ensuite une table dans notre zone enriched qui applique des règles d'enrichissement et de transformation, comme le clacul d'un id de session unique, le calcule du type de device, du canal d'origine (paid marketing, organic, etc). 
- Une colonne coutry_code et platform_name permettent de différencier et filtrer au besoin. Une colonne sur les consentements est aussi présente pour permettre aux gens d'exclure les données non-consent si besoin.

## Modèle unifié
Afin de facilité l'utilisation des données, et de permettre une robustesse face à l'évolution des porvider, nous avons conçu un modèle unifié des données de tracking, il simplifie le modèle de données, diminue la volumétrie et utilise le vocabulaire Decathlon.
Il permet de croiser différents types de provider sans effort, mais surtout permet à aux utilisateurs hors scope outils d'analytics web de ne pas avoir à se soucier des différences de structure et de vocabulaire entre les différents providers. Il possède aussi une colonne sur les consentements.

Nous y retrouvons, à la fois les données Piano et Amplitude mais cette fois ci sous le même format. Aucune donnée non-consent n'est mise dans ce modèle.

# Données permettant d'identifier une personne

## Consent :

amplitude_id → persistent across sessions on a same device
unique_amplitude_id → persistent across devices
user_id (member_id)
Country
Region
City
device_id
os_name
os_version
device_family
device_type
device_category
ip_address → Deleted on accessible data, kept in archive data (not accessible)
location_lat → Deleted on accessible data, kept in archive data (not accessible)
location_lng → Deleted on accessible data, kept in archive data (not accessible)

## No consent

amplitude_id → persistent across sessions on a same device
unique_amplitude_id → persistent across devices
user_id (member_id) → Not available
Country
Region
City
device_id
os_name
os_version
device_family
device_type
device_category
ip_address → Deleted on accessible data, kept in archive data (not accessible)
location_lat → Deleted on accessible data, kept in archive data (not accessible)
location_lng → Deleted on accessible data, kept in archive data (not accessible)

# Piano (consent and non-consent in a same table) :

visit_id
visitor_id → persistent across sessions on a same device
user_id → Deleted manually because available even without consent
browser
browser_group
browser_language
browser_version
connection_isp
connection_organisation
device_brand
device_name
device_name_tech
device_screen_digonal
device_screen_height
device_screen_width
device_type
geo_city
geo_continent
geo_country
geo_latitude
geo_longitude
geo_metro
geo_region
os
os_group
os_version
os_name
os_version_name
page_country_code
page_language_code
user_store_id

