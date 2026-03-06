Hello Joeri,

Comme convenu, je reviens vers toi concernant l'estimation du budget et du planning pour l'intégration des données de tracking de la plateforme C2C dans le datalake. Tous les éléments sont disponibles ici.

Globalement, voici les informations à retenir : 
Budget estimé : 3000€ d'implémentation et 3000€ de maintenance annuelle (ex: gestion des droits et permissions, incidents, support, ajout de pays...).
Planning prévisionnel : on vise une date d'atterrissage au 27 mars 2026 au plus tôt et au 10 avril 2026 au plus tard. Évidemment si cela doit bouger on vous tient informés.
Je te laisse revenir vers moi pour valider tout ça et je reste disponible si besoin.

Bonne fin de journée !
Marine

____

Hello Marine,

Je te remercie pour l'estimation concernant l'intégration des données C2C.

Je souhaiterais toutefois obtenir quelques précisions : confirmez-vous que vous récupérez uniquement les données de traffic ? Pourriez-vous également nous préciser la méthode et l'outil utilisés pour cette récupération ?

De notre côté, nous travaillons actuellement sur l'ingestion des données produits, transactions et vendeurs de la plateforme C2C. Il me semble essentiel de centraliser l'ingestion via un point unique afin de mutualiser les coûts et la maintenance, plutôt que de multiplier les flux depuis un même outil.

Bien à toi,
Ouns BEN KHEDIJA

_____

Hello Ouns,

J'ai besoin de te faire un retour par rapport à ton dernier mail en réponse à Marine. En envoyant ça en réponse, si je m'occupe du sujet C2C, je peux m'imaginer que je me fais double facturer et que les équipes ne travaillent pas conjointement. Tout comme mon message de la semaine dernière, n'hésite pas à pinguer Marine directement pour avoiur les informations et qu'on réponde d'une seule et même voix.

Et donc pour répondre à ton questionnement :

- Nous avons travaillé depuis deux ans à l'uniformisation des données de tracking au travers toute l'entreprise, ça veut dire des pipelines d'ingestion communes, permettant des spécificités au besoin mais restant sur une base commune et permettant de faire bénéficier à tout le monde des évolutions sur une pipeline. Cela permet de diminuer les couts d'ingestion des données de tracking, et de diminuer les couts de maintenance.

S'ajoute à ça le fait que les données entrantes sont obligées de respecter un cahier des charge ce qui fait que la sortie est bien plus propre et homogène permettant une interopérabilité des données. S'ajoute à ça la documentation de la table et des règles en suivants les normes établies pour les données de tracking.

- C'est notamment le rôle des CDP de s'assurer qu'un objet de son domaine est structuré de façon homogène et d'accompagner les producteurs dans cette démarche. Cela rajoute effectivement des coûts mais qui sont négligeables en vus du gain d'homogénéité pour l'entreprise (structure / gouv).

- J'attire donc ton attention sur les ingestions des autres objets que vous allez formater à votre manière sans bénéficier de l'expertise des autres équipes. Exemple : une transaction pour l'entreprise a une définition et un cadre, si l'on souhaite obtenir toutes les transactions je me rends dans la table sales ou orders (quand elle sera consolidée).

En ingérant de votre côté, vous créez un modèle parallèle, certe vous avancez plus vite et répondez plus vite au demande mais en accumulant une dette car vous êtes dans votre tunnel. Je ne dis pas que c'est bien ou mal, juste j'attire ton attention sur les problèmes que ça peut enjendrer à long terme.

Comme je l'ai dit la semaine derière, il faut effectivement avancer en ce sens mais il faut aussi concevoir une modélisation de données avec des gates pour permettre de remplacer ces objets une fois retombés au bon endroit.

- Et donc pour être encore plus précis sur "Il me semble essentiel de centraliser l'ingestion via un point unique afin de mutualiser les coûts et la maintenance, plutôt que de multiplier les flux depuis un même outil." : c'est plutôt en pensant que la centralisation de l'ingestion permet de diminuer les couts qui peut poser problème, car pour ingérer des données de traffic vous allez créer une façon de faire, avec vos normes, vos outils, plutot que de vous appuyer sur ce qui est fait. Donc tu vas ajouter un temps supplémentaire de build, et de run avec des dépendances que même nous avons du mal à gérer (tracking / outils)

- La stratégie de l'entreprise sur la gouvernance de données est de fonctionner en objet afin de garantir une homogénéité de ces derniers, donc tenez bien compte de ça dans votre démarche, vous êtes centrales dans cette capacité à avancer rapidement donc vous allez devoir redoubler d'efforts sur la syncrhonisation avec les autres CDPs afin de tenir un rôle "d'apporteur d'affaires".

Mes attentes pour les prochaines fois :
- Nous sommes censés travailler ensemble, et apporter des réponses ensemble donc n'hésites pas à te synchroniser directement avec les autres PMs sur les sujets pour apporter une réponse commune au sujets.

____

### Version "Cool" (Feedback Direct & Collaboratif)

Hello Ouns,

Petit retour par rapport à ton échange avec Marine. L'idée ici, c'est qu'on parle d'une seule voix pour éviter de donner l'impression au métier qu'on se marche sur les pieds ou qu'on facture deux fois la même chose. Hésite vraiment pas à la pinguer en direct avant de répondre, ça nous simplifiera la vie à tous ! ;)

Sur le fond, voici comment je vois les choses :

1. **Le tracking, c'est notre socle commun :** Ça fait 2 ans qu'on bosse sur des pipelines d'ingestion uniformes. En gros, on a déjà les "rails" et les standards de qualité. S'appuyer dessus, c'est l'assurance d'avoir une donnée propre, documentée et qui coûte moins cher à maintenir sur le long terme.
2. **Éviter les "tunnels" :** Je comprends l'envie d'avancer vite sur les produits ou les transactions de ton côté. C'est top pour l'agilité, mais attention à ne pas créer une "dette" de données. Si chaque équipe fait sa propre cuisine dans son coin, on finit par ne plus pouvoir croiser les infos. L'objectif, c'est que tes objets s'insèrent parfaitement dans le puzzle global de l'entreprise.
3. **Apporteur d'affaires :** Vous avez une super force de frappe pour faire bouger les lignes rapidement. Mon conseil : servez-vous en pour être ceux qui ramènent tout le monde autour de la table. Plus vous serez synchronisés avec les autres CDPs, plus vos solutions seront solides et pérennes.

Bref, l'idée c'est : agilité OUI, mais en restant "branchés" sur le reste de la maison pour éviter de construire des murs qu'on devra casser plus tard.

On se checke quand tu veux si tu veux creuser le sujet !

Andrea