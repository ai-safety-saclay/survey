Ce sondage est séparé en une partie connaissances et une partie opinion.

Pour la partie connaissances, voici les réponses attendues avec les explications.

NE LISEZ PAS LES RÉPONSES se vous voulez passer le sondage et que vous ne l'avez pas fait.


# Réponses

# 1)

**Lesquelles de ces tâches ont été résolues par des IA à un niveau similaire à un humain ?**

> Jouer à Minecraft

C'est vrai: [Voyager](https://perso.telecom-paristech.fr/aperonnet-23/voyager.html) est un système construit autour de GPT4 qui lui permet de jouer à minecraft. 
Il y a plusieurs limitations cependant:
- Voyager communique directement avec l'API minecraft en écrivant du code. Cela rend la tâche plus simple sur certains aspects (pas de traitement d'image) mais plus complexe sur d'autres (pas accès aux blocs visibles autour de soi)
- La force de Voyager se base sur la connaissance de GPT4 sur le sujet, extrait de bases de données humaines. Voyager s'adapte, mais n'apprend pas vraiment.


> Résoudre des problèmes des Olympiades Internationales de Mathématiques

C'est vrai: [AlphaGeometry](https://deepmind.google/discover/blog/alphageometry-an-olympiad-level-ai-system-for-geometry/) est une IA développée par Google DeepMind pour résoudre des problèmes de géométrie.
Le système dépasse le niveau des médaillés d'argent.


> Décrire et interpréter un meme

C'est vrai: Il n'y a pas eu d'étude poussée sur le sujet, mais la compréhension d'images de GPT4 Vision lui permet d'interpréter une grande partie des memes. Un exemple:

![](https://res.cloudinary.com/lesswrong-2-0/image/upload/f_auto,q_auto/v1/mirroredImages/B8Djo44WtZK6kK4K5/l6ylq6om2dyxq32212o8)

Exemple tiré de [ce blog](https://www.lesswrong.com/posts/B8Djo44WtZK6kK4K5/outreach-success-intro-to-ai-risk-that-has-been-successful#AI_capabilities)


> Identifier l'émotion principale d'une musique

C'est vrai. Vous pouvez voir ce qu'on arrive à faire [ici](https://www.bridge.audio/blog/benchmark-of-the-best-ai-for-music-analysis-in-2024/)


# 2)

**GPT3.5, dont l’architecture permet uniquement de prédire le mot suivant dans un texte, a
été entraîné sur des jeux de données de parties d’échecs après son entraînement principal.
Quel est son score Elo évalué ?**

La bonne réponse est 1800 Elo, un bon niveau en club.

Alors que GPT3 n'a jamais été conçu pour jouer aux échecs: juste pour prédire efficacement le prochain token dans un texte.

Une [vidéo explicative](https://www.youtube.com/watch?v=6D1XIbkm4JE&pp=ygUUbW9uc2lldXIgcGhpIGNoYXRncHQ%3D)
Un [article](https://blog.mathieuacher.com/GPTsChessEloRatingLegalMoves/) sur le sujet.

# 3)

**Parmi ces aspects des LLM, pour lesquels les chercheurs ont une bonne compréhension
basée sur des fondements théoriques, et qui permet de prédire des comportements ?**


> le lien entre taille du modèle et performances

Non: on a des lois empiriques qui montrent que plus un modèle est gros, plus il est performant, mais on ne comprend pas bien pourquoi. Et les chercheurs sont souvent surpris de l'apparition de capacités émergentes, comme dans [ce papier](https://arxiv.org/pdf/2206.07682)


> Le comportement de refus de réponse

Oui: on a réussi à faire en sorte qu'un LLM accepte toujours de répondre à une question, même "comment construire une bombe artisanale" ou "comment dissoudre un cadavre"

Il a suffit de modifier un vecteur dans une des couches du réseau: [article ici](https://www.lesswrong.com/posts/jGuXSZgv6qfdhMCuJ/refusal-in-llms-is-mediated-by-a-single-direction)

> La capacité à effectuer un raisonnement logique

Non: Les chercheurs ont vraiment très peu d'idées de comment un LLM raisonne

> Comment sont stockés les connaissances factuelles

Non: on connait quelques techniques pour modifier des connaissances très spécifiques d'un LLM, mais on ne sait pas où elles sont stockées.


# 4)

**RLHF**

RLHF ([wiki](https://fr.wikipedia.org/wiki/Apprentissage_par_renforcement_%C3%A0_partir_de_r%C3%A9troaction_humaine) signifie "Reinforcement Learning by Human Feedback"

C'est une technique introduite par openAI pour faire en sorte qu'un modèle type GPT change son comportement pour être en accord avec des préférences humaines.

C'est un champ de recherche qui se développe très vite. Il y a une explication assez technique [ici](https://ibrahimciko.github.io/posts/deepdive-rlhf/)


# 5) 

**OpenAI, l’entreprise ayant créé ChatGPT, a comme objectif public de créer une IA générale.
Cela signiﬁe que cette IA fera aussi bien qu’un humain dans essentiellement toutes les tâches,
y compris lorsque cela demande des capacités de planiﬁcation. Dans combien de temps
prévoient-ils d’atteindre cet objectif ?**

La bonne réponse est: 4 ans.
Il y a quelques années, OpenAI communiquait beaucoup plus sur sa feuille de route. Aujourd'hui, l'entreprise est devenue de moins en moins transparente, et leurs objectifs sont assez difficiles à connaitre.

Le cofondateur d'openAI, John Schulman, a expliqué quel était le plan pour arriver à une intelligence artificielle générale en 2027:

<https://community.openai.com/t/openai-cofounder-john-schulman-interview-reasoning-rlhf-plan-for-2027-agi/754337>

# 6)

**D’après le dernier sondage parmi les chercheurs en IA (2800 chercheurs, janvier 2024),
quelle proportion des chercheurs pensent qu’un scénario catastrophe peut arriver à cause
d’une IA incontrôlable ? Spéciﬁquement, la question était: « je pense que la probabilité d’un
scénario qui cause l’extinction de l’espèce humaine ou conséquence similaire est supérieure à
1/10 »**

Bonne réponse: 50%

Les résultats du sondage en question sont [ici](https://arxiv.org/pdf/2401.02843)

Cette question spécifique est répondue en page 15

