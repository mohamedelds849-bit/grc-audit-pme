---
title: Mini-audit de sécurité de l'information
client: AgriSouss SARL (étude de cas anonymisée)
author: Mohamed Elansari - élève ingénieur en cybersécurité, Universiapolis Agadir
version: 1.0
date: {{DATE}}
classification: Confidentiel - diffusion restreinte à la gérance (cas fictif, cadre académique)
---

# Synthèse pour la direction

**À qui s'adresse cette page :** à la gérance d'AgriSouss SARL. Elle résume, sans jargon, ce que l'audit a trouvé et ce qu'il faut faire.

**En une phrase :** l'entreprise fonctionne bien au quotidien, mais sa sécurité repose sur la bonne volonté de quelques personnes et non sur des règles ; **un seul email piégé ou un seul poste infecté pourrait bloquer les ventes et exposer le fichier clients**.

**Niveau actuel :** maturité moyenne **{{SCORE_GLOBAL}} / 5** (cible à 12 mois : **{{SCORE_TARGET}} / 5**, niveau raisonnable pour une PME de cette taille). {{NB_RISK_CRIT}} risques sont jugés **critiques** et {{NB_RISK_HIGH}} **élevés** sur 12.

{{CHART_SMALL}}

**Les 4 dangers principaux**

- **Vol du compte email de la gérance** par un faux message (hameçonnage) : accès aux factures, aux clients et aux autres comptes.
- **Rançongiciel** sur le poste comptable : facturation bloquée, et aujourd'hui **aucune sauvegarde testée** pour repartir.
- **Fuite du fichier clients** via une faille du site web, avec une obligation légale (loi 09-08) qui n'est pas encore respectée (pas de déclaration à la CNDP).
- **Faux changement de RIB** d'un fournisseur par email : un virement envoyé à un escroc.

**Ce qu'il faut faire en priorité (30 jours, coût quasi nul)**

1. Activer la double authentification sur **tous** les comptes (email, hébergeur, nom de domaine).
2. Mettre en place des **sauvegardes** dont une hors ligne, et vérifier une fois qu'on sait les restaurer.
3. Supprimer les accès des anciens salariés et prestataires ; un compte par personne.
4. Règle « deux personnes + un appel » pour tout virement ou changement de RIB.
5. Remplacer la clé d'accès exposée dans le code du site et mettre à jour le site.

**Budget indicatif :** {{BUDGET_30}} MAD sur 30 jours, {{BUDGET_90}} MAD sur 90 jours, {{BUDGET_12}} MAD sur 12 mois (estimations hors taxes, à confirmer par devis). À mettre en regard d'un arrêt des ventes de plusieurs jours en haute saison ou d'une sanction de la CNDP.

**Décision attendue :** valider le plan à 30 jours et désigner un **référent sécurité** interne (2 à 4 heures par semaine).

<!-- pagebreak -->

# 1. Contexte, périmètre et méthodologie

## 1.1 Contexte de la mission

> **Étude de cas anonymisée, réalisée dans un cadre académique.** « AgriSouss SARL » est un nom fictif. Les constats sont plausibles pour une PME de ce profil mais ne décrivent aucune entreprise réelle ; aucune donnée réelle (nom, domaine, adresse IP, identifiant) n'est reproduite.

AgriSouss SARL est une PME d'environ **15 salariés** de la région Souss-Massa qui commercialise des produits agricoles (engrais, oligo-éléments, semences) auprès d'exploitants, en direct et via un **site e-commerce** développé en PHP avec une base **MariaDB** chez un **hébergeur mutualisé externe**. Les commandes en ligne sont majoritairement réglées **à la livraison** (pas de paiement par carte sur le site), ce qui exclut du périmètre les exigences de type PCI DSS.

Système d'information observé : 7 postes Windows (dont 2 portables), une box FAI avec Wi-Fi, une imprimante réseau, des comptes Gmail/Google Drive utilisés pour l'activité, des smartphones (dont certains personnels) utilisant WhatsApp pour les commandes, un logiciel de facturation installé localement sur le poste comptable. Le site est maintenu par un **développeur freelance** ; la comptabilité est tenue par un **cabinet externe** ; les livraisons sont confiées à un **transporteur**.

## 1.2 Objectifs

1. Établir un état des lieux de la sécurité de l'information et de la conformité à la loi 09-08.
2. Identifier et hiérarchiser les risques principaux.
3. Proposer un plan d'action réaliste, proportionné au budget d'une PME.

Il ne s'agit **pas** d'un audit de certification ISO/IEC 27001, ni d'un test d'intrusion.

## 1.3 Périmètre

| Inclus | Exclu |
|---|---|
| Organisation et gouvernance de la sécurité | Systèmes internes de l'hébergeur (hors contrat) |
| Postes de travail, Wi-Fi, comptes cloud | Tests d'intrusion actifs sur le site en production |
| Site e-commerce (revue documentaire, configuration observable, entretien avec le prestataire) | Systèmes du transporteur et du cabinet comptable |
| Traitements de données personnelles (clients, prospects, salariés) | Sécurité des produits et des process agricoles |
| Relations avec les prestataires (contrats, accès) | Entrepôt (hors aspects SI) |

## 1.4 Démarche

| Phase | Activités | Livrables |
|---|---|---|
| 1. Cadrage | Réunion de lancement, périmètre, référentiels, planning | Note de cadrage |
| 2. Collecte | Entretiens (gérant, comptable, commercial, prestataire web), visite des locaux, revue documentaire, observation de configurations (sans test intrusif) | Notes d'entretien |
| 3. Analyse | Inventaire des actifs, analyse de risques EBIOS RM allégée, analyse d'écart Annexe A, check-list 09-08 | Registre des risques, tableau d'écart |
| 4. Restitution | Plan d'action priorisé, synthèse direction, rapport | Le présent rapport, DdA (SoA) projet |

**Preuves :** chaque niveau de maturité repose sur un entretien et, quand c'était possible, une observation. Les évaluations restent des **jugements d'auditeur** ; elles ne remplacent pas une vérification technique.

## 1.5 Référentiels utilisés

- **ISO/IEC 27001:2022** : exigences d'un système de management de la sécurité de l'information (SMSI) - clauses 4 à 10 et **Annexe A** (93 mesures en 4 thèmes : organisationnel, humain, physique, technologique). L'amendement ISO/IEC 27001:2022/Amd 1:2024 (prise en compte du changement climatique dans le contexte) est sans effet notable ici.
- **ISO/IEC 27002:2022** : guide de mise en oeuvre des 93 mesures (objectifs, recommandations, attributs).
- **EBIOS Risk Manager** (ANSSI, 2018) : méthode d'appréciation des risques en 5 ateliers, utilisée ici en **version allégée**.
- **Cadre marocain** : loi 05-20, loi 09-08, DNSSI (voir section 2).

## 1.6 Échelles

**Maturité des mesures (0-5)** : 0 Inexistant · 1 Initial/informel · 2 Reproductible mais non documenté · 3 Défini et documenté · 4 Géré et mesuré · 5 Optimisé. Pour une PME, la cible est généralement **2 à 3** ; viser 4-5 serait disproportionné.

**Risques** : Niveau = **Gravité (1-4) × Vraisemblance (1-4)**, soit 1 à 16. Seuils : 1-3 Faible (acceptable), 4-6 Modéré (à surveiller), 8-9 Élevé (à traiter), 12-16 Critique (à traiter en priorité).

<!-- pagebreak -->

# 2. Cadre réglementaire et normatif - applicabilité

| Texte | Objet | Applicable à AgriSouss ? | Utilisation dans l'audit |
|---|---|---|---|
| **Loi n° 09-08** (2009) relative à la protection des personnes physiques à l'égard du traitement des données à caractère personnel, et son décret d'application n° 2-09-165 | Données personnelles ; autorité de contrôle : **CNDP** | **Oui, directement** : l'entreprise traite des données de clients, prospects et salariés | Check-list de conformité (section 6) |
| **Loi n° 05-20** (2020) relative à la cybersécurité, et son décret d'application (n° 2-21-406, 2021 - référence à vérifier) | Sécurité des SI des administrations, collectivités, établissements et entreprises publics, infrastructures d'importance vitale (IIV), certains opérateurs et prestataires | **Non directement** : une SARL privée qui n'est ni IIV, ni opérateur télécom, ni prestataire de services numériques/cybersécurité visé n'entre pas dans le champ des obligations | **Référence de bonnes pratiques** (déclaration d'incident, homologation, audit) |
| **DNSSI** - Directive Nationale de la Sécurité des Systèmes d'Information (DGSSI, 2014) | Mesures de sécurité de référence, largement inspirées de l'ISO/IEC 27001/27002 | **Non obligatoire** : destinée aux administrations, organismes publics et IIV | Référence complémentaire de bonnes pratiques |
| **Code pénal, art. 607-3 à 607-11** (loi n° 07-03 relative aux atteintes aux systèmes de traitement automatisé des données) | Incrimine l'accès frauduleux, l'entrave, l'altération de données | **Oui** (protège l'entreprise victime) | Base des dépôts de plainte ; conservation des preuves (5.28) |
| **ISO/IEC 27001 / 27002:2022** | Normes volontaires | **Volontaire** ; pas de certification visée | Grille d'analyse d'écart et DdA |

**Points d'attention sur l'applicabilité (honnêteté du diagnostic) :**

- La **loi 05-20** désigne la **DGSSI** (Direction Générale de la Sécurité des Systèmes d'Information, rattachée à l'Administration de la Défense Nationale) comme autorité nationale de cybersécurité ; elle impose aux entités assujetties notamment une politique de sécurité, la classification des actifs, la déclaration des incidents et des audits. AgriSouss n'y est pas assujettie ; nous en retenons l'**esprit** (déclarer, se préparer, auditer). Si AgriSouss devenait fournisseur d'une entité assujettie (par exemple un office public), des exigences contractuelles pourraient en découler.
- La **loi 09-08** s'applique pleinement : fichier clients du site, commandes, données de livraison, fichiers RH, éventuelle vidéosurveillance. Des **transferts hors du Maroc** existent de fait (messagerie Gmail/Google Drive, hébergeur dont les serveurs peuvent être à l'étranger) et relèvent du régime des transferts de la loi, qui suppose un pays offrant un niveau de protection suffisant ou une autorisation/dérogation : **point à instruire avec la CNDP**.
- Les numéros d'articles de la loi 09-08 cités en section 6 sont donnés pour faciliter la lecture ; **ils doivent être vérifiés sur le texte publié au Bulletin officiel** avant toute utilisation juridique. Un projet de réforme du cadre des données personnelles a été évoqué publiquement : **l'état du droit est à vérifier à la date de l'audit**. Ce rapport ne constitue pas un avis juridique.
- Le **RGPD** européen n'est pas applicable a priori (clientèle marocaine, pas de ciblage de résidents de l'UE).

<!-- pagebreak -->

# 3. Inventaire des actifs

## 3.1 Valeurs métier (EBIOS RM - atelier 1)

| Réf. | Valeur métier | Description | Propriétaire | Besoins D / I / C |
|---|---|---|---|---|
| VM1 | Vente en ligne et prise de commande | Catalogue, panier, commandes, suivi des livraisons | Gérant | Élevé / Élevé / Moyen |
| VM2 | Relation client et données clients | Fichier clients/prospects (nom, téléphone, adresse d'exploitation, historique d'achat) | Responsable commercial | Moyen / Élevé / **Élevé** |
| VM3 | Facturation, comptabilité et paiements fournisseurs | Factures, relevés, virements, RIB fournisseurs | Comptable | Élevé / **Élevé** / Élevé |
| VM4 | Image de marque et contenus produits | Fiches techniques, homologations, photos, référencement | Gérant | Moyen / Élevé / Faible |
| VM5 | Gestion du personnel | Contrats, paie, CNSS, dossiers salariés | Gérant | Faible / Moyen / **Élevé** |

D = disponibilité, I = intégrité, C = confidentialité.

## 3.2 Biens supports

| Réf. | Bien support | Type | Valeurs métier | Localisation | Responsable |
|---|---|---|---|---|---|
| BS01 | Site e-commerce PHP + back-office | Logiciel | VM1, VM2, VM4 | Hébergeur mutualisé externe | Prestataire web |
| BS02 | Base de données MariaDB (commandes, clients) | Données | VM1, VM2 | Hébergeur | Prestataire web |
| BS03 | Panneau d'hébergement, compte du nom de domaine, DNS | Service | VM1, VM4 | Fournisseurs externes | Gérant |
| BS04 | Dépôt de code source (Git) | Logiciel | VM1 | Compte du prestataire | Prestataire web |
| BS05 | Comptes Gmail / Google Drive (9 comptes) | Service cloud | VM2, VM3, VM5 | Cloud (hors Maroc) | Gérant |
| BS06 | Poste comptable + logiciel de facturation local | Matériel / logiciel | VM3, VM5 | Bureau comptable | Comptable |
| BS07 | 4 postes fixes bureau + 2 PC portables | Matériel | Toutes | Bureaux / déplacements | Utilisateurs |
| BS08 | Smartphones (WhatsApp Business, dont appareils personnels) | Matériel | VM1, VM2 | Mobiles | Commerciaux |
| BS09 | Box FAI, Wi-Fi, imprimante réseau | Réseau | Toutes | Couloir des bureaux | Gérant |
| BS10 | Archives papier (factures, bons de livraison, dossiers RH) | Papier | VM3, VM5 | Bureau comptable | Comptable |
| BS11 | Prestataires : développeur freelance, cabinet comptable, transporteur, hébergeur | Organisation | Toutes | Externes | Gérant |
| BS12 | Personnel (15 salariés) | Personnes | Toutes | - | Gérant |

## 3.3 Événements redoutés

| Réf. | Événement redouté | Valeur métier | Impacts | Gravité |
|---|---|---|---|---|
| ER1 | Indisponibilité du site et des commandes > 48 h en haute saison | VM1 | Perte de chiffre d'affaires, clients reportés vers la concurrence | 3 Grave |
| ER2 | Divulgation du fichier clients | VM2 | Non-conformité 09-08, atteinte à la réputation, démarchage des clients par un concurrent | 3 Grave |
| ER3 | Perte ou chiffrement des données comptables | VM3 | Arrêt de la facturation, difficultés fiscales, trésorerie | 4 Critique |
| ER4 | Détournement de paiement (faux RIB) | VM3 | Perte financière directe, souvent non récupérable | 3 Grave |
| ER5 | Altération du site (défiguration, contenu malveillant) | VM4 | Réputation, déréférencement | 2 Significative |
| ER6 | Prise de contrôle des comptes de messagerie | VM2, VM3 | Usurpation de l'entreprise, rebond vers clients et fournisseurs | 4 Critique |

## 3.4 Socle de sécurité (synthèse)

Le socle a été évalué par rapport à l'Annexe A de l'ISO/IEC 27001:2022 (section 5) et à la loi 09-08 (section 6). Il est **faible** : pas de politique, pas de MFA généralisée, pas de sauvegarde testée, droits d'administration généralisés. Les points positifs sont réels : HTTPS actif, antivirus natif présent, paiement à la livraison (pas de données de carte), petite surface d'attaque, direction réceptive.

<!-- pagebreak -->

# 4. Analyse de risques (EBIOS Risk Manager allégée)

## 4.1 Ce qui a été allégé

Les 5 ateliers ont été suivis, de façon condensée (une demi-journée d'atelier avec la gérance au lieu de plusieurs séances) : pas de cartographie détaillée de l'écosystème avec cotation de dangerosité, scénarios opérationnels décrits en texte plutôt qu'en graphes d'attaque complets. Les risques **accidentels** (panne, erreur), que l'EBIOS RM traite surtout via le socle de sécurité, sont intégrés au registre pour donner à la direction une vue unique.

## 4.2 Atelier 2 - Sources de risque et objectifs visés

| Réf. | Source de risque | Objectif visé | Motivation / ressources | Pertinence |
|---|---|---|---|---|
| SR1 | Cybercriminel opportuniste | Rançon, revente d'accès ou de données | Élevée / outils automatisés | **Élevée** |
| SR2 | Fraudeur (ingénierie sociale) | Détourner un virement | Élevée / faibles moyens techniques | **Élevée** |
| SR3 | Hacktiviste / défaceur | Visibilité, défiguration | Moyenne / scans de masse | Moyenne |
| SR4 | Ancien salarié ou prestataire mécontent | Nuire, conserver un avantage | Faible à moyenne / **accès légitimes conservés** | Moyenne |
| SR5 | Concurrent peu scrupuleux | Obtenir le fichier clients | Faible / sous-traitance possible | Faible |
| SR6 | Voleur opportuniste | Revente du matériel | Moyenne | Moyenne |

## 4.3 Atelier 3 - Écosystème et scénarios stratégiques

Parties prenantes critiques : **hébergeur** (dépendance totale du site), **développeur freelance** (accès complet, aucun contrat), **Google** (messagerie et documents), **cabinet comptable** (échanges de fichiers par clé USB/email), **transporteur** (reçoit noms, téléphones et adresses des clients).

| Réf. | Scénario stratégique | Chemin | Événement redouté |
|---|---|---|---|
| SS1 | Un cybercriminel prend le contrôle de la messagerie de la gérance et l'utilise pour accéder aux autres comptes et frauder | SR1 → gérant (hameçonnage) → Gmail → réinitialisation hébergeur/domaine | ER6, ER1, ER4 |
| SS2 | Un cybercriminel chiffre le poste comptable via une pièce jointe piégée | SR1 → salarié → poste comptable (admin local) → fichiers de facturation | ER3 |
| SS3 | Un attaquant exploite une faille du site pour extraire la base clients | SR1/SR5 → site PHP (version obsolète, injection) → MariaDB | ER2, ER5 |
| SS4 | Un fraudeur se fait passer pour un fournisseur et obtient un changement de RIB | SR2 → comptable (email usurpé) → virement | ER4 |
| SS5 | Un ancien prestataire réutilise ses accès conservés | SR4 → panneau d'hébergement / dépôt Git | ER1, ER5, ER2 |

## 4.4 Atelier 4 - Scénarios opérationnels (principaux)

**SO1 (pour SS1) - Hameçonnage de la gérance.** (1) Reconnaissance : adresse email publique sur le site. (2) Email imitant une alerte Google ou une facture d'un fournisseur. (3) Saisie du mot de passe sur une fausse page ; absence de MFA. (4) Création d'une règle de transfert discrète dans la boîte. (5) Réinitialisation du mot de passe de l'hébergeur et du domaine via l'adresse compromise. (6) Fraude ou rançon. *Vraisemblance : 3 (très vraisemblable) - un salarié a déjà saisi son mot de passe sur une fausse page.*

**SO2 (pour SS2) - Rançongiciel.** (1) Pièce jointe Office ou archive piégée. (2) Exécution avec des droits d'administrateur local. (3) Désactivation de l'antivirus, chiffrement du disque et des clés USB connectées. (4) Aucune sauvegarde hors ligne → perte ou paiement. *Vraisemblance : 3.*

**SO3 (pour SS3) - Injection SQL.** (1) Scan automatisé du site, détection d'une version PHP en fin de support. (2) Paramètre vulnérable à l'injection SQL (concaténation identifiée lors de l'entretien avec le prestataire). (3) Extraction de la table clients. (4) Revente ou publication. *Vraisemblance : 3 - à confirmer par un test autorisé (action A17).*

**SO4 (pour SS4) - Faux RIB.** (1) Compromission ou imitation de l'adresse d'un fournisseur. (2) Email « nouveau RIB » au comptable. (3) Aucun contre-appel ni double validation. (4) Virement perdu. *Vraisemblance : 3.*

## 4.5 Registre des risques

{{RISK_REGISTER}}

## 4.6 Matrice des risques (avant traitement)

{{RISK_MATRIX_TABLE}}

{{CHART_RISK}}

## 4.7 Atelier 5 - Stratégie de traitement

Tous les risques **critiques et élevés** sont **réduits** par le plan d'action (section 7). Aucun risque n'est transféré à ce stade ; une **cyber-assurance** pourra être étudiée une fois les mesures de base en place (les assureurs exigent généralement MFA et sauvegardes). Le risque résiduel R12 (vol d'un portable) reste « vraisemblable », mais sa gravité devient mineure grâce au chiffrement ; il est **accepté**. Les niveaux résiduels supposent que les actions soient effectivement réalisées et vérifiées.

{{RISK_RESIDUAL_TABLE}}

<!-- pagebreak -->

# 5. Analyse d'écart ISO/IEC 27001:2022 - Annexe A

## 5.1 Clauses 4 à 10 (SMSI) - aperçu

| Clause | Exigence (résumé) | Constat | Maturité |
|---|---|---|---|
| 4 Contexte | Enjeux, parties intéressées, périmètre du SMSI | Non formalisés (ce rapport en fournit une première version) | 0 |
| 5 Leadership | Engagement de la direction, politique, rôles | Direction réceptive, aucune politique ni rôle | 1 |
| 6 Planification | Appréciation et traitement des risques, objectifs, DdA | Première appréciation réalisée par cet audit | 1 |
| 7 Support | Ressources, compétences, sensibilisation, documentation | Pas de sensibilisation ni de documentation | 0 |
| 8 Fonctionnement | Mise en oeuvre du traitement des risques | Mesures ponctuelles non pilotées | 1 |
| 9 Évaluation | Surveillance, audit interne, revue de direction | Inexistant | 0 |
| 10 Amélioration | Non-conformités, actions correctives | Inexistant | 0 |

Une certification n'est **pas recommandée** à court terme : le coût (accompagnement, audit de certification, maintien) serait disproportionné. L'objectif est d'adopter la logique de la norme (risques → mesures → vérification) à l'échelle d'une PME.

## 5.2 Maturité par thème

{{THEME_TABLE}}

{{CHART_MATURITY}}

## 5.3 Principaux écarts (priorité P1)

{{TOP_GAPS}}

Le tableau complet des 93 mesures (état actuel, maturité, écart, priorité, risques liés) est fourni dans `outputs/gap_analysis_annexA.xlsx` / `.csv` ; le projet de Déclaration d'applicabilité figure en annexe A.

<!-- pagebreak -->

# 6. Conformité à la loi 09-08 - check-list

Légende : ✔ conforme · ◐ partiel · ✘ non conforme · ? à vérifier. Références d'articles indicatives (voir réserve en section 2).

| # | Exigence | Réf. indicative | Constat | Statut | Action |
|---|---|---|---|---|---|
| 1 | Recenser les traitements (clients/prospects, commandes, RH/paie, éventuelle vidéosurveillance) | Bonne pratique (préalable aux formalités) | Aucun registre | ✘ | A15 |
| 2 | **Déclaration préalable** à la CNDP (ou demande d'autorisation pour les traitements qui l'exigent) | Art. 12 et s. | Aucune déclaration effectuée | ✘ | A13 |
| 3 | Finalités déterminées, données adéquates et non excessives (minimisation) | Art. 3 | Le formulaire demande la CIN, inutile pour une livraison | ◐ | A10 |
| 4 | **Consentement** de la personne ou autre base légale (exécution du contrat, obligation légale...) | Art. 4 | Commandes : exécution du contrat (OK). Newsletter/WhatsApp promotionnels : pas de consentement recueilli | ◐ | A10 |
| 5 | **Information** des personnes lors de la collecte (identité du responsable, finalités, destinataires, droits) | Art. 5 | Pas de politique de confidentialité ni de mention sur les formulaires | ✘ | A10 |
| 6 | Droits d'accès, de rectification et d'opposition ; point de contact | Art. 7 à 9 | Aucune procédure ni adresse dédiée | ✘ | A10 |
| 7 | Prospection directe par email/SMS/messagerie : consentement préalable | Art. 10 | Messages promotionnels envoyés à tout le fichier | ✘ | A10 |
| 8 | **Cookies** et traceurs : information et choix de l'utilisateur | Pas de disposition spécifique identifiée dans la loi (principes d'information et de consentement) - position CNDP à vérifier | Outil de mesure d'audience déposé sans bandeau | ✘ | A10 |
| 9 | **Durées de conservation** définies et appliquées | Art. 3 | Commandes conservées sans limite | ✘ | A15 |
| 10 | **Sécurité** des traitements (mesures techniques et organisationnelles) | Art. 23 | Voir sections 4 et 5 : MFA, sauvegarde, droits insuffisants | ✘ | A01-A09 |
| 11 | **Sous-traitants** : garanties de sécurité et contrat écrit (hébergeur, prestataire web, transporteur, cabinet comptable) | Art. 23 (sous-traitance - à vérifier) | Aucun contrat avec clauses de protection des données | ✘ | A14 |
| 12 | **Transferts vers l'étranger** (Google, hébergeur) : pays adéquat, ou autorisation/dérogation | Art. 43 et 44 | Localisation des données non connue ; aucune démarche | ? | A13 |
| 13 | Confidentialité : personnel habilité, engagement de confidentialité | Art. 26 (à vérifier) | Pas de clause de confidentialité dans les contrats | ✘ | A11, A14 |
| 14 | Données des salariés (RH) : information, accès restreint | Art. 3 à 5 | Dossiers RH dans un dossier Drive partagé | ◐ | A11, A13 |
| 15 | Vidéosurveillance éventuelle : déclaration et affichage | Formalités CNDP | Pas de caméra dans les bureaux à ce jour | ✔ | Si installation : déclarer |
| 16 | Gestion des violations de données : procédure interne, information de la CNDP si pertinent | Pas d'obligation générale de notification identifiée dans la loi de 2009 (contrairement au RGPD) - bonne pratique | Aucune procédure | ✘ | A16 |

**Lecture :** la conformité 09-08 est **faible mais rapidement améliorable** : la plupart des actions sont documentaires (déclarations, mentions, contrats) et peu coûteuses. La loi 09-08 n'impose pas, à notre connaissance, la désignation d'un délégué à la protection des données ; nommer un **interlocuteur interne** reste recommandé. La sanction la plus probable n'est pas une amende mais une **plainte client** ou une **perte de confiance** ; les sanctions administratives et pénales prévues par la loi existent néanmoins.

<!-- pagebreak -->

# 7. Plan d'action priorisé

**Principes de priorisation :** (1) réduire d'abord les risques critiques ; (2) privilégier les actions à fort effet et faible coût ; (3) rester réaliste pour une équipe sans informaticien interne. Coûts : **estimations indicatives en MAD HT** (prix de marché observés pour des prestations de PME, hypothèse 1 USD ≈ 10 MAD), à confirmer par devis. « j » = jour de travail.

{{ACTION_PLAN}}

**Budget indicatif cumulé** (fourchettes, hors temps interne) :

{{BUDGET_TABLE}}

**Indicateurs de suivi proposés :** % de comptes avec MFA (cible 100 %) ; date du dernier test de restauration réussi (< 3 mois) ; nombre de postes à jour (100 %) ; nombre de comptes d'anciens salariés actifs (0) ; taux de clic à la campagne de phishing (en baisse) ; déclarations CNDP déposées (oui/non).

<!-- pagebreak -->

# 8. Conclusion

AgriSouss SARL présente un profil typique de PME : des outils simples, une forte dépendance à quelques personnes et à des prestataires non encadrés, et une sécurité qui n'a jamais été pilotée. Les risques les plus graves (prise de contrôle de la messagerie, rançongiciel, fuite du fichier clients, fraude au virement) sont **courants et bien documentés**, et les mesures qui les réduisent le plus sont **peu coûteuses** : MFA, sauvegardes testées, suppression des comptes partagés, double validation des paiements, mise à jour du site.

Le plan proposé ne vise pas la certification ISO/IEC 27001 mais une **maturité moyenne d'environ {{SCORE_TARGET}} / 5** en 12 mois (niveau 3 « défini » sur les mesures prioritaires), la **mise en conformité 09-08** et une capacité minimale à réagir à un incident. Un point d'étape à 90 jours est recommandé pour mesurer l'avancement avec les indicateurs ci-dessus.

## Limites de l'audit

- Étude de cas **fictive et anonymisée** réalisée dans un cadre académique ; elle n'a pas la valeur d'un audit réalisé par un prestataire qualifié.
- Aucun test technique intrusif ; les vulnérabilités applicatives (SO3) sont **présumées** à partir d'entretiens et doivent être confirmées par un test autorisé.
- Les références juridiques sont données à titre indicatif et doivent être vérifiées par un juriste ; elles ne constituent pas un avis juridique.
- Les coûts sont des ordres de grandeur.

<!-- pagebreak -->

# Annexe A - Projet de Déclaration d'applicabilité (DdA / SoA)

La DdA, exigée par l'ISO/IEC 27001:2022 (clause 6.1.3 d), liste les mesures nécessaires, la justification de leur inclusion ou exclusion et leur état de mise en oeuvre. Ce projet couvre les 93 mesures de l'Annexe A ; **{{NB_APPLICABLE}} sont retenues, {{NB_EXCLUDED}} exclues** avec justification. Intitulés en anglais (texte de la norme) ; libellés français de l'audit = traduction de travail non officielle.

{{SOA}}

<!-- pagebreak -->

# Annexe B - Fichiers livrés

| Fichier | Contenu |
|---|---|
| `outputs/rapport_audit_AgriSouss.pdf` | Le présent rapport |
| `report/rapport_audit_AgriSouss.md` | Source Markdown complète (générée) |
| `outputs/gap_analysis_annexA.xlsx` | Classeur : écart Annexe A, DdA, synthèse par thème, risques, plan d'action |
| `outputs/gap_analysis_annexA.csv` | Écart Annexe A (93 mesures) |
| `outputs/soa_draft.csv` | Projet de DdA |
| `outputs/risk_register.csv`, `outputs/action_plan.csv` | Registre des risques, plan d'action |
| `outputs/figures/*.png` | Graphiques de maturité et matrice des risques |
