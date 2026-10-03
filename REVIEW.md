# Revue qualité - grc-audit-pme (AgriSouss SARL)

Relecteur : profil auditeur GRC senior (ISO/IEC 27001 Lead Auditor, cadre marocain). Date : octobre 2026.
Périmètre relu : `src/annexa.py`, `src/register.py`, `report/rapport_template.md`, `build.py`, PDF reconstruit (25 pages), XLSX (5 onglets), CSV, `README.md`, `LEARN.md`.

## Verdict

| Critère | Résultat |
|---|---|
| Score technique | **8,5 / 10** |
| Score pédagogique | **9 / 10** |
| Sécurité / anonymisation | **PASS** |
| Cohérence interne | **PASS** (après corrections listées ci-dessous) |
| Décision | **APPROUVÉ** |

## 1. ISO/IEC 27001:2022 Annexe A

- 93 mesures, numérotation exacte, répartition 37 / 8 / 14 / 34 (vérifiée par assertion dans le code). Les intitulés anglais correspondent à la norme ; les 11 mesures nouvelles de 2022 sont correctes.
- Logique de la DdA correcte : justification par risque, par exigence légale ou par socle ; état « mis en oeuvre / partiel / non mis en oeuvre » calculé à partir de la maturité ; actions reliées automatiquement.
- **7.6 (travail dans les zones sécurisées)** : exclusion défendable pour une PME sans salle serveur avec hébergement externalisé, et justifiée. Point de vigilance : la recommandation 7.3 de mettre le routeur dans un local fermé ne crée pas forcément une « zone sécurisée » au sens de la 27002, mais un auditeur de certification pourrait en discuter.
- **8.11 (masquage des données)** : l'exclusion **contredisait le constat 8.33** (« tests occasionnels avec de vraies commandes clients ») et l'action de purge/anonymisation de 8.10. **Corrigé** : la mesure est retenue (maturité 0, cible 2, P3, R03/R09, action A15). La DdA compte maintenant 92 mesures retenues et 1 exclusion.

## 2. EBIOS RM

- Les 5 ateliers sont correctement décrits (valeurs métier, biens supports et événements redoutés à l'atelier 1 ; SR/OV ; écosystème et scénarios stratégiques ; scénarios opérationnels ; traitement). Les échelles G1-G4 et V1-V4 utilisent les libellés du guide ANSSI.
- La gravité des risques est cohérente avec les événements redoutés (ER3/ER6 = 4 correspondent à R02/R01 = 4, etc.). Le fait d'avoir mis les risques accidentels et réglementaires (R06, R09) dans le registre est assumé et expliqué.
- La matrice et le registre sont générés à partir de la même source. Le texte disait que R12 restait « vraisemblable » alors que V résiduelle = 3 (« très vraisemblable ») : **corrigé**.
- **Traçabilité risques ↔ actions ↔ mesures** : 12 liens manquaient entre les deux sens (ex. A16, A18, A23, A19, A21 pointaient vers des risques qui ne les listaient pas ; 8.8 ne listait pas R02 ; 8.24 ne listait pas R04). **Corrigé** ; un contrôle croisé automatique ne trouve plus aucun écart.

## 3. Budget (MAD)

- Les autres postes sont plausibles pour une PME marocaine qui fait appel à des freelances ou à de petits cabinets (messagerie pro ≈ 10-15 kMAD/an pour 15 utilisateurs, gestionnaire de mots de passe, juriste).
- **A17 (revue de code + test d'intrusion, 5-8 j)** : 10 000 à 25 000 MAD revient à environ 1 250 à 5 000 MAD par jour, ce qui est trop bas pour un « prestataire qualifié ». **Corrigé** en 25 000 à 50 000 MAD.
- Budget total de la première année : **57 500 à 154 500 MAD HT**, recalculé automatiquement.
- Les jours de consultant (PSSI 3-5 j pour 5 à 12 kMAD) restent au bas du marché : c'est cohérent avec un freelance, pas avec un Big4. Le dire en entretien.

## 4. Droit marocain (vérifié sur le texte consolidé de la loi 09-08, portail officiel Adala, ministère de la Justice)

| Point | Statut |
|---|---|
| Art. 3 (qualité des données, minimisation, conservation 3 e), 4 (consentement + exceptions), 5 (information), 7-9 (accès, rectification, opposition), 10 (prospection directe), 12 (déclaration / autorisation préalable), 43-44 (transferts, dérogations) | **Exacts** |
| Art. 23 : §1 sécurité, **§2-4 sous-traitant (garanties, contrat écrit, instructions)** | Exact. La mention « à vérifier » a été retirée et le paragraphe précisé |
| Confidentialité : le rapport citait « art. 26 (à vérifier) » | Précisé : **art. 25** (traitement uniquement sur instruction) + **art. 26** (secret professionnel) |
| Pas de DPO, pas d'obligation générale de notifier les violations, aucune disposition sur les cookies | Exact (aucune occurrence dans la loi). La position de la CNDP sur les cookies reste marquée « à vérifier », à juste titre |
| Sanctions pénales (art. 54 et suivants : 20 000 à 200 000 DH, art. 60 pour les transferts) | Le rapport dit « les sanctions existent » sans chiffre, ce qui est prudent et correct |
| Décret 05-20 : n° 2-21-406 du 15 juillet 2021 | **Confirmé** (texte publié sur Adala). La mention « référence à vérifier » a été retirée |
| Champ de 05-20, DGSSI rattachée à l'Administration de la Défense nationale, maCERT, DNSSI 2014 non obligatoire pour une PME privée, loi 07-03 (art. 607-3 à 607-11 du code pénal) | Corrects et formulés avec la prudence voulue |

Aucune affirmation n'est trop sûre d'elle. Les réserves restantes (réforme annoncée de la loi, position de la CNDP sur les cookies) sont pertinentes.

## 5. Cohérence, anonymisation, présentation

- Résumé pour la direction, tableaux, XLSX et README alignés : 0,64 / 5 (le résumé affichait « 0,6 » à 1 décimale, il affiche maintenant 2 décimales), cible 2,3, 2 risques critiques et 6 élevés, 23 actions, 22 mesures P1.
- Aucune trace de « Nour », de domaine réel, d'adresse IP, d'email ou de personne réelle, ni dans le code, ni dans le Markdown, ni dans le PDF, ni dans les métadonnées (auteur = Mohamed Elansari).
- PDF : mise en page propre (page de titre, sommaire, tableaux avec en-tête, en-têtes et pieds de page). Défaut mineur : la page 3 ne contient que deux lignes du sommaire.
- « 92 sont retenues, 1 exclues » : accord grammatical corrigé dans le modèle.

## 6. LEARN.md (15 questions)

- Les réponses sont exactes. Q5 (« les ateliers 3 et 4 donnent la gravité et la vraisemblance ») était imprécise : en EBIOS RM, la gravité vient des événements redoutés (atelier 1) et est reportée à l'atelier 3, la vraisemblance vient de l'atelier 4. **Corrigé.**
- Ajouts : repères d'articles 09-08 vérifiés, date du décret 2-09-165, décret 2-21-406, et l'épisode 8.11 comme exemple de contrôle croisé entre la DdA et les constats (un très bon point à raconter en entretien).
- Ligne de CV : honnête (« académique », « PME fictive », « allégée »). Rien à changer.

## Corrections appliquées

1. `src/annexa.py` : 8.11 retenue au lieu d'exclue, avec constat, recommandation et justification ; 8.8 ajoute R02 ; 8.24 ajoute R04.
2. `src/register.py` : listes d'actions de R01, R02, R03, R05, R08, R09, R11 complétées ; mesures de R09 réordonnées et 8.11 ajoutée ; A15 couvre 8.11 ; coût de A17 passé à 25 000-50 000 MAD.
3. `report/rapport_template.md` : décret 2-21-406 confirmé ; art. 23 §2-4 et art. 25-26 précisés ; réserve juridique reformulée (« relus sur le texte consolidé, à confirmer par un juriste ») ; R12 « très vraisemblable (V3) » ; « coût quasi nul » remplacé par « coût faible » (le budget à 30 jours va de 3,5 à 26 kMAD) ; accord « mesures retenues / exclusion(s) ».
4. `build.py` : score global affiché avec 2 décimales dans le résumé pour la direction.
5. `README.md` : 0,64 ; « à faible coût » ; limites mises à jour.
6. `LEARN.md` : DdA 92/1 + explication de 8.11 ; Q5 ; repères d'articles ; décrets.
7. Reconstruction complète avec `python build.py` (PDF de 25 pages, XLSX, CSV, figures).

## Recommandations restantes (non appliquées, à décider par l'auteur)

1. **Anonymisation par le profil** : secteur (intrants agricoles), région (Souss-Massa) et stack (PHP/MariaDB, hébergement mutualisé) forment un profil précis. Si le cas s'inspire d'un vrai client ou d'un projet de l'auteur, généraliser la région ou le secteur. Des constats comme « concaténations SQL » ou « clé d'API dans l'historique Git » ne doivent pas pouvoir être rattachés à un site réel.
2. 7.6 : préparer une réponse orale (« pas de zone sécurisée définie ; si le local du routeur ou le bureau comptable deviennent des zones sécurisées, 7.6 redevient applicable »).
3. Ajouter une ligne « ER » à la colonne cible du registre (R05 a G = 4 alors que ER1 = 3 : à justifier par ER6, la prise de contrôle du domaine et de la messagerie).
4. Sommaire : supprimer la page 3 presque vide (TOC un peu plus serré).
5. Option : une colonne « propriétaire du risque » et une date d'acceptation formelle du résiduel (clause 6.1.3 f), ce qu'un auditeur Big4 cherchera.
6. Q11 de LEARN : citer la liste des pays « adéquats » publiée par la CNDP plutôt que « au sens de la CNDP », après vérification.
