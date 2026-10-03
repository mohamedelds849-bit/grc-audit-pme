# LEARN - Fiche de révision GRC (ISO 27001, EBIOS RM, cadre marocain)

Fiche personnelle construite pendant le projet `grc-audit-pme`. Objectif : savoir **expliquer** ce
que j'ai fait en entretien (cabinet de conseil, banque, Big4), sans réciter.

> Prudence : je cite les textes marocains de mémoire de travail ; les numéros d'articles et les
> références de décrets doivent être revérifiés sur le Bulletin officiel / les sites de la CNDP et de
> la DGSSI avant tout usage professionnel.

---

## 1. ISO/IEC 27001 vs ISO/IEC 27002

| | ISO/IEC 27001:2022 | ISO/IEC 27002:2022 |
|---|---|---|
| Nature | **Exigences** (« shall ») pour un SMSI | **Guide** de mise en oeuvre des mesures |
| Certifiable ? | **Oui** (audit par un organisme accrédité) | Non |
| Contenu | Clauses 4 à 10 (contexte, leadership, planification, support, fonctionnement, évaluation, amélioration) + **Annexe A** (liste des 93 mesures, normative) | Pour chaque mesure : objectif, recommandations, informations complémentaires, **attributs** |
| Logique | Cycle PDCA, approche par les risques | Boîte à outils |

- Ce qui est audité en certification : les **clauses 4-10** + la cohérence entre risques, DdA et mesures. L'Annexe A n'est pas une check-list obligatoire : on doit comparer ses mesures à la liste pour ne rien oublier (6.1.3 c).
- Version 2013 → 2022 : 114 mesures / 14 domaines → **93 mesures / 4 thèmes** ; 11 mesures nouvelles (5.7 renseignement sur les menaces, 5.23 cloud, 5.30 préparation TIC à la continuité, 7.4 surveillance physique, 8.9 gestion des configurations, 8.10 suppression d'information, 8.11 masquage, 8.12 prévention des fuites, 8.16 surveillance, 8.23 filtrage web, 8.28 codage sécurisé). Période de transition des certificats 2013 terminée fin octobre 2025.
- Amendement 1:2024 : ajoute la prise en compte du **changement climatique** dans le contexte (clauses 4.1/4.2).
- Normes voisines : **27005** (gestion des risques), **27701** (vie privée), 27017/27018 (cloud), 27035 (incidents).

## 2. Les 4 thèmes de l'Annexe A

| Thème | Mesures | Exemples |
|---|---|---|
| 5 Organisationnel | 37 (5.1-5.37) | Politiques, rôles, inventaire, contrôle d'accès, fournisseurs, cloud, incidents, continuité, conformité, DCP |
| 6 Humain | 8 (6.1-6.8) | Sélection, contrat, sensibilisation, discipline, départ, NDA, télétravail, signalement |
| 7 Physique | 14 (7.1-7.14) | Périmètres, accès, bureau propre, matériel hors site, supports, élimination |
| 8 Technologique | 34 (8.1-8.34) | Terminaux, accès privilégiés, authentification, malware, vulnérabilités, sauvegarde, journalisation, réseau, crypto, développement sécurisé |

Attributs 27002 (pour filtrer les mesures) : type (préventif/détectif/correctif), propriétés DIC,
concepts cybersécurité (Identifier, Protéger, Détecter, Répondre, Rétablir - comme le NIST CSF),
capacités opérationnelles, domaines de sécurité.

## 3. La Déclaration d'applicabilité (DdA / SoA)

Exigée par la **clause 6.1.3 d)**. Pour **chaque** mesure de l'Annexe A : nécessaire ou non,
**justification** de l'inclusion (risque, exigence légale, contrat, bonne pratique) ou de l'exclusion,
et **état de mise en oeuvre**. C'est le document pivot entre l'appréciation des risques et le plan de
traitement ; l'auditeur de certification part souvent de là. Dans ce projet : 92 retenues, 1 exclue
(7.6 pas de zone sécurisée, hébergement externalisé). J'avais envisagé d'exclure 8.11 (masquage), mais
le constat 8.33 montre que de vraies commandes servent aux tests : l'exclusion aurait été incohérente,
la mesure est donc retenue (P3). Bon exemple de vérification croisée DdA ↔ constats.

Erreur fréquente : exclure une mesure « parce qu'elle n'est pas faite ». On exclut seulement si elle
n'est **pas nécessaire** au regard des risques et des exigences.

## 4. EBIOS Risk Manager (ANSSI, 2018) - les 5 ateliers

1. **Cadrage et socle de sécurité** : périmètre, valeurs métier, biens supports, événements redoutés (avec gravité), socle (référentiels applicables, écarts).
2. **Sources de risque** : qui (SR) et pour quoi (objectifs visés, OV) ; on retient les couples SR/OV les plus pertinents.
3. **Scénarios stratégiques** : cartographie de l'**écosystème** (parties prenantes, dangerosité), chemins d'attaque de haut niveau SR → partie prenante → valeur métier ; gravité.
4. **Scénarios opérationnels** : modes opératoires techniques (souvent en kill chain : connaître, rentrer, trouver, exploiter) ; vraisemblance.
5. **Traitement du risque** : stratégie (réduire, transférer, éviter, accepter), plan d'amélioration continue de la sécurité, risques résiduels, suivi.

EBIOS RM se concentre sur les menaces **intentionnelles** ; les risques accidentels sont couverts par
le socle (atelier 1). Dans mon projet, je les ai mis dans le même registre pour la lisibilité - et je
l'ai écrit.

## 5. Formule du risque

- **Risque = Gravité (impact) × Vraisemblance** (EBIOS) ; en ISO 27005 : conséquence × probabilité/vraisemblance.
- Échelles qualitatives à 4 niveaux (évite le « milieu » refuge d'une échelle impaire). Score 1-16 ; seuils d'acceptation fixés **par la direction**.
- **Risque inhérent / brut** (avant mesures) → **résiduel** (après mesures). Le résiduel doit être **accepté formellement** par le propriétaire du risque.
- Limite : le produit de deux échelles ordinales n'est pas une vraie mesure ; c'est un outil de **priorisation**, pas une probabilité. Approches quantitatives : FAIR, ALE = SLE × ARO.

## 6. Cadre marocain - l'essentiel

**Loi n° 09-08 (2009)** - protection des personnes physiques à l'égard du traitement des données à
caractère personnel ; décret d'application n° 2-09-165 du 21 mai 2009 ; autorité : **CNDP** (Commission Nationale de
contrôle de la protection des Données à caractère Personnel).
- S'applique à **toute** entité qui traite des DCP au Maroc, publique ou privée → s'applique à une PME.
- Principes : finalité, proportionnalité, exactitude, durée de conservation limitée ; **consentement** ou autre base légale ; **information** des personnes ; droits d'**accès, rectification, opposition** ; prospection électronique soumise au consentement préalable.
- **Formalités préalables** auprès de la CNDP : déclaration, ou autorisation pour certains traitements (données sensibles, interconnexions, etc.).
- **Sécurité** et **sous-traitance** (art. 23) : mesures techniques et organisationnelles ; sous-traitant offrant des garanties suffisantes, contrat écrit ; art. 25-26 : traitement sur instruction, secret professionnel.
- Repères d'articles : art. 3 qualité des données / conservation ; art. 4 consentement ; art. 5 information ; art. 7-9 accès, rectification, opposition ; art. 10 prospection ; art. 12 déclaration/autorisation ; art. 43-44 transferts.
- **Transferts vers l'étranger** : vers un pays assurant un niveau de protection suffisant, sinon autorisation/dérogation (point très concret dès qu'on utilise Gmail ou un hébergeur hors Maroc).
- Pas d'obligation de DPO ni de notification générale des violations comparable au RGPD dans le texte de 2009 (à ma connaissance) ; une refonte a été évoquée - vérifier l'état du droit.

**Loi n° 05-20 (2020)** - cybersécurité (décret d'application n° 2-21-406 du 15 juillet 2021) ; autorité nationale : **DGSSI** (Administration de la Défense
Nationale), avec le **maCERT** pour la veille/alerte.
- Vise surtout : administrations de l'État, collectivités territoriales, établissements et entreprises publics, **infrastructures d'importance vitale** (IIV), ainsi que certains opérateurs (télécoms) et prestataires (services numériques, cybersécurité) - périmètre exact à relire dans le texte.
- Obligations typiques : politique de sécurité, classification, **déclaration des incidents**, audits (par prestataires qualifiés pour les IIV), homologation de SI sensibles.
- Pour une PME privée hors champ : **référence de bonnes pratiques**, ou exigences reprises contractuellement par un client assujetti.

**DNSSI (DGSSI, 2014)** - Directive Nationale de la Sécurité des Systèmes d'Information : socle de
mesures inspiré de l'ISO/IEC 27001/27002, destiné aux administrations, organismes publics et IIV.
Non obligatoire pour une PME, utile comme grille complémentaire.

**Autres** : code pénal art. 607-3 à 607-11 (loi 07-03, atteintes aux STAD) ; règles comptables de
conservation ; droit de la consommation pour le e-commerce.

---

## 7. 15 questions d'entretien et réponses modèles

**1. Quelle différence entre ISO 27001 et ISO 27002 ?**
27001 fixe les exigences d'un SMSI et se certifie ; 27002 est le guide de mise en oeuvre des 93 mesures. On se certifie 27001, on s'inspire de 27002.

**2. Combien de mesures dans l'Annexe A 2022, et comment sont-elles organisées ?**
93, en 4 thèmes : organisationnel (37), humain (8), physique (14), technologique (34). 11 sont nouvelles par rapport à 2013, par exemple le renseignement sur les menaces, la sécurité du cloud et le codage sécurisé.

**3. Qu'est-ce qu'une DdA et pourquoi est-elle importante ?**
C'est la liste de toutes les mesures de l'Annexe A avec, pour chacune, l'inclusion ou l'exclusion justifiée et l'état de mise en oeuvre (clause 6.1.3 d). Elle relie l'analyse de risques aux mesures et sert de point d'entrée à l'auditeur.

**4. Peut-on exclure une mesure ? Donnez un exemple.**
Oui, si elle n'est pas nécessaire au regard des risques et exigences, avec justification. Ex. : 7.6 « travail en zone sécurisée » pour une PME sans salle serveur, dont l'hébergement est externalisé. On n'exclut jamais une mesure simplement parce qu'elle n'est pas en place.

**5. Expliquez les 5 ateliers d'EBIOS RM.**
1 cadrage et socle, 2 sources de risque et objectifs visés, 3 scénarios stratégiques via l'écosystème, 4 scénarios opérationnels techniques, 5 traitement et risques résiduels. La gravité est évaluée dès l'atelier 1 (événements redoutés) puis reportée sur les scénarios stratégiques (atelier 3) ; la vraisemblance est estimée à l'atelier 4 (scénarios opérationnels).

**6. Pourquoi EBIOS RM plutôt qu'une simple matrice ?**
Elle part des valeurs métier et des attaquants réalistes, intègre les **parties prenantes** (souvent le maillon faible dans une PME : prestataire web, hébergeur) et produit des scénarios compréhensibles par la direction. Une matrice seule ne dit pas *comment* le risque se réalise.

**7. Comment calculez-vous un niveau de risque ?**
Gravité × vraisemblance sur des échelles à 4 niveaux, avec des seuils validés par la direction. Je précise que c'est un outil de priorisation ordinal, pas une mesure exacte.

**8. Risque brut, risque résiduel, appétence au risque ?**
Brut : avant mesures. Résiduel : après mesures. L'appétence est le niveau que la direction accepte ; le résiduel doit être formellement accepté par le propriétaire du risque.

**9. La loi 05-20 s'applique-t-elle à une PME privée ?**
En général non directement : elle vise surtout les administrations, établissements publics, IIV et certains opérateurs/prestataires. Pour une PME, je l'utilise comme référence de bonnes pratiques, et je vérifie si un client assujetti impose des exigences par contrat.

**10. Et la loi 09-08 ?**
Oui, dès qu'il y a des données personnelles (clients, salariés). Conséquences concrètes : déclarations à la CNDP, information et consentement, droits des personnes, sécurité, contrats avec les sous-traitants, encadrement des transferts à l'étranger.

**11. Une PME utilise Gmail et un hébergeur européen. Quel point 09-08 soulevez-vous ?**
Le **transfert de données hors du Maroc** : il faut vérifier que le pays offre un niveau de protection suffisant au sens de la CNDP, ou obtenir une autorisation/s'appuyer sur une dérogation prévue par la loi. Ensuite : contrat de sous-traitance, minimisation, sécurité des comptes (MFA).

**12. Quelles sont vos 3 premières recommandations pour une PME sans sécurité ?**
MFA partout (messagerie, hébergeur, domaine) ; sauvegardes 3-2-1 avec test de restauration ; suppression des comptes partagés/obsolètes et des droits admin. Plus une règle anti-fraude au virement. Gros effet, coût quasi nul.

**13. Comment mesurez-vous la maturité ?**
Échelle 0-5 type CMMI (inexistant → optimisé), fondée sur entretiens, observations et preuves. Je fixe une **cible proportionnée** (2-3 pour une PME) et je mesure l'écart. Je dis clairement que ce sont des jugements d'auditeur.

**14. Comment convaincre un dirigeant non technique ?**
Parler en impacts métier (ventes bloquées, virement perdu, plainte client, sanction), chiffrer grossièrement, montrer des quick wins gratuits, une page de synthèse, une décision claire à prendre.

**15. Quelles limites voyez-vous à votre propre audit ?**
Cas fictif ; pas de test intrusif, donc vulnérabilités applicatives présumées ; références juridiques à faire valider par un juriste ; coûts en ordres de grandeur ; EBIOS appliquée en version allégée (pas de cotation de dangerosité de l'écosystème).

---

## 8. Ligne de CV (honnête)

> **Projet GRC (académique)** - Mini-audit de sécurité d'une PME fictive : analyse d'écart des 93 mesures ISO/IEC 27001:2022 (Annexe A) et projet de DdA, analyse de risques EBIOS RM allégée (12 risques), check-list de conformité loi 09-08, plan d'action chiffré en MAD ; rapport PDF généré en Python (reportlab, openpyxl, matplotlib).
