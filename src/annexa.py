# -*- coding: utf-8 -*-
"""
ISO/IEC 27001:2022 - Annexe A (93 mesures, 4 thèmes) : évaluation d'écart AgriSouss SARL.

- Les intitulés anglais sont ceux de la norme (ISO/IEC 27001:2022 Annex A / ISO/IEC 27002:2022).
- Les intitulés français sont une traduction de travail NON OFFICIELLE (la version française
  officielle est publiée par l'AFNOR / ISO ; ne pas citer ces libellés comme texte normatif).
- Les niveaux de maturité (0-5) sont des appréciations d'auditeur fondées sur entretiens et
  observations (étude de cas fictive/anonymisée), pas des mesures.

Échelle de maturité (inspirée CMMI) :
 0 Inexistant | 1 Initial / informel | 2 Reproductible, non documenté
 3 Défini et documenté | 4 Géré et mesuré | 5 Optimisé
"""

THEMES = {
    "5": "Organisationnel (5.1-5.37)",
    "6": "Humain (6.1-6.8)",
    "7": "Physique (7.1-7.14)",
    "8": "Technologique (8.1-8.34)",
}
THEMES_SHORT = {"5": "Organisationnel", "6": "Humain", "7": "Physique", "8": "Technologique"}

MATURITY_LABELS = {
    0: "Inexistant", 1: "Initial", 2: "Reproductible",
    3: "Défini", 4: "Géré", 5: "Optimisé",
}

# Contrôles introduits par la version 2022 (11 nouveaux)
NEW_2022 = {"5.7", "5.23", "5.30", "7.4", "8.9", "8.10", "8.11", "8.12", "8.16", "8.23", "8.28"}

_ROWS = []


def C(cid, en, fr, mat, cible, prio, risques, etat, ecart, applicable=True, justif=None):
    _ROWS.append(dict(
        id=cid, title_en=en, titre_fr=fr, maturite=mat, cible=cible, priorite=prio,
        risques=risques, etat=etat, ecart=ecart, applicable=applicable, justif=justif,
    ))


# ---------------------------------------------------------------- 5. ORGANISATIONNEL
C("5.1", "Policies for information security", "Politiques de sécurité de l'information", 0, 3, "P1", "Tous",
  "Aucune politique écrite ; règles transmises oralement par le gérant.",
  "Rédiger une PSSI courte (5-8 pages) validée par la gérance, + charte utilisateur.")
C("5.2", "Information security roles and responsibilities", "Rôles et responsabilités", 1, 3, "P1", "Tous",
  "Le gérant et le prestataire web gèrent 'l'informatique' sans rôles définis.",
  "Nommer un référent sécurité interne (temps partiel) et formaliser une matrice RACI.")
C("5.3", "Segregation of duties", "Séparation des tâches", 1, 3, "P1", "R07",
  "La même personne saisit et valide les virements fournisseurs.",
  "Double validation des virements et des changements de RIB fournisseur.")
C("5.4", "Management responsibilities", "Responsabilités de la direction", 1, 3, "P2", "Tous",
  "Direction favorable mais aucune exigence sécurité communiquée au personnel.",
  "Engagement écrit de la gérance ; rappel des règles en réunion trimestrielle.")
C("5.5", "Contact with authorities", "Relations avec les autorités", 0, 2, "P2", "R03, R09",
  "Aucun contact identifié (CNDP, maCERT/DGSSI, police judiciaire).",
  "Lister les contacts autorités dans la fiche réflexe incident.")
C("5.6", "Contact with special interest groups", "Relations avec des groupes d'intérêt", 0, 1, "P3", "",
  "Aucune veille ni appartenance à un groupe professionnel sécurité.",
  "S'abonner aux bulletins d'alerte maCERT et à la fédération professionnelle.")
C("5.7", "Threat intelligence", "Renseignement sur les menaces", 0, 1, "P3", "R01, R02",
  "Aucune veille menaces.",
  "Veille légère : bulletins maCERT + alertes du prestataire web (pas de CTI payante).")
C("5.8", "Information security in project management", "Sécurité dans la gestion de projet", 0, 2, "P3", "R03, R08",
  "Les évolutions du site sont lancées sans exigences de sécurité.",
  "Ajouter une check-list sécurité à chaque demande d'évolution au prestataire.")
C("5.9", "Inventory of information and other associated assets", "Inventaire des informations et actifs", 1, 3, "P1", "Tous",
  "Pas d'inventaire ; les PC et comptes sont connus 'de mémoire'.",
  "Tenir un inventaire (tableur) : matériels, comptes, logiciels, données, propriétaire.")
C("5.10", "Acceptable use of information and other associated assets", "Utilisation correcte des actifs", 0, 3, "P2", "R01, R02, R12",
  "Pas de charte ; usage personnel des PC et clés USB libre.",
  "Charte informatique signée, annexée au règlement intérieur.")
C("5.11", "Return of assets", "Restitution des actifs", 1, 3, "P2", "R11, R12",
  "Restitution du matériel au départ, mais pas des comptes ni des données.",
  "Check-list de départ (matériel + comptes + données) signée.")
C("5.12", "Classification of information", "Classification de l'information", 0, 2, "P3", "R03",
  "Aucune classification.",
  "Schéma simple à 3 niveaux : Public / Interne / Confidentiel (données clients, RH, finance).")
C("5.13", "Labelling of information", "Marquage de l'information", 0, 1, "P3", "",
  "Aucun marquage.",
  "Marquer 'Confidentiel' les exports clients et documents RH/financiers.")
C("5.14", "Information transfer", "Transfert de l'information", 1, 3, "P2", "R03, R07",
  "Fichiers clients envoyés au transporteur par WhatsApp/Gmail sans règle.",
  "Règles de transfert : canal approuvé, minimisation, lien partagé à durée limitée.")
C("5.15", "Access control", "Contrôle d'accès", 1, 3, "P1", "R01, R05, R11",
  "Accès donnés 'à la demande', pas de règle du moindre privilège.",
  "Politique de contrôle d'accès : besoin d'en connaître + revue semestrielle.")
C("5.16", "Identity management", "Gestion des identités", 1, 3, "P1", "R05, R11",
  "Compte du panneau d'hébergement et compte admin du site partagés par 3 personnes.",
  "Comptes nominatifs uniquement ; suppression des comptes partagés.")
C("5.17", "Authentication information", "Informations d'authentification", 1, 3, "P1", "R01, R05",
  "Mots de passe réutilisés, notés sur papier ; pas de gestionnaire de mots de passe.",
  "Gestionnaire de mots de passe d'équipe + règles de longueur (phrases de passe).")
C("5.18", "Access rights", "Droits d'accès", 1, 3, "P1", "R11",
  "Un ancien stagiaire et l'ancien prestataire disposent encore d'accès.",
  "Procédure arrivée/départ + revue des droits tous les 6 mois.")
C("5.19", "Information security in supplier relationships", "Sécurité dans les relations fournisseurs", 0, 2, "P2", "R05, R06, R11",
  "Fournisseurs (hébergeur, freelance web, transporteur, cabinet comptable) choisis sur le prix.",
  "Liste des fournisseurs critiques + exigences minimales de sécurité.")
C("5.20", "Addressing information security within supplier agreements", "Sécurité dans les accords fournisseurs", 0, 3, "P1", "R03, R09",
  "Pas de contrat écrit avec le freelance web ; CGV standard de l'hébergeur.",
  "Clauses sécurité, confidentialité et sous-traitance 09-08 dans les contrats.")
C("5.21", "Managing information security in the ICT supply chain", "Sécurité dans la chaîne d'approvisionnement TIC", 1, 2, "P3", "R03, R08",
  "Bibliothèques PHP/JS ajoutées par le prestataire sans suivi de versions.",
  "Exiger la liste des composants tiers et leur mise à jour.")
C("5.22", "Monitoring, review and change management of supplier services", "Surveillance et revue des services fournisseurs", 0, 2, "P3", "R06",
  "Aucun suivi de la qualité de service de l'hébergeur.",
  "Revue annuelle des fournisseurs critiques (incidents, SLA, sauvegardes).")
C("5.23", "Information security for use of cloud services", "Sécurité pour l'utilisation des services cloud", 1, 3, "P1", "R01, R09",
  "Comptes Gmail gratuits utilisés pour l'activité ; Drive partagé par liens publics.",
  "Règles d'usage cloud : comptes professionnels, MFA, partage restreint, localisation des données.")
C("5.24", "Information security incident management planning and preparation", "Planification de la gestion des incidents", 0, 2, "P2", "R01, R02, R03",
  "Aucune procédure ; en cas d'incident on 'appelle le prestataire'.",
  "Fiche réflexe incident d'une page (qui appeler, quoi préserver, quoi notifier).")
C("5.25", "Assessment and decision on information security events", "Appréciation des événements de sécurité", 0, 2, "P3", "R01, R02",
  "Pas de critères pour qualifier un événement en incident.",
  "Critères simples de qualification dans la fiche réflexe.")
C("5.26", "Response to information security incidents", "Réponse aux incidents", 0, 2, "P2", "R02, R03",
  "Pas de réponse organisée.",
  "Scénarios de réponse : rançongiciel, compte compromis, fuite de données.")
C("5.27", "Learning from information security incidents", "Tirer des enseignements des incidents", 0, 2, "P3", "",
  "Le phishing reçu en 2025 n'a donné lieu à aucun retour d'expérience.",
  "Registre des incidents + retour d'expérience court après chaque incident.")
C("5.28", "Collection of evidence", "Collecte des preuves", 0, 1, "P3", "R03, R07",
  "Aucune pratique de conservation des preuves.",
  "Consignes de préservation (ne pas éteindre/effacer, captures, en-têtes d'emails).")
C("5.29", "Information security during disruption", "Sécurité pendant une perturbation", 0, 2, "P3", "R02, R06",
  "Aucun mode dégradé prévu.",
  "Mode dégradé : prise de commandes par téléphone/WhatsApp sur formulaire papier.")
C("5.30", "ICT readiness for business continuity", "Préparation des TIC pour la continuité", 0, 2, "P2", "R02, R06",
  "Pas d'objectifs de reprise ; restauration jamais testée.",
  "Définir RTO/RPO simples (ex. site < 24 h, compta < 48 h) et tester la restauration.")
C("5.31", "Legal, statutory, regulatory and contractual requirements", "Exigences légales et contractuelles", 1, 3, "P1", "R09",
  "Obligations 09-08 méconnues ; aucun registre des exigences.",
  "Registre des exigences : loi 09-08, code pénal (STAD), droit de la consommation, contrats.",
  justif="Exigence légale (loi 09-08) et contractuelle")
C("5.32", "Intellectual property rights", "Droits de propriété intellectuelle", 2, 3, "P3", "",
  "Licences Windows OEM ; une copie non licenciée d'un logiciel bureautique sur un poste.",
  "Régulariser les licences ; vérifier les droits sur photos/textes du site.")
C("5.33", "Protection of records", "Protection des enregistrements", 2, 3, "P2", "R02, R06",
  "Factures conservées en papier + logiciel de facturation local non sauvegardé hors site.",
  "Durées de conservation et sauvegarde des enregistrements comptables.",
  justif="Obligations comptables et fiscales de conservation")
C("5.34", "Privacy and protection of PII", "Vie privée et protection des DCP", 0, 3, "P1", "R03, R09",
  "Aucune déclaration CNDP, pas de politique de confidentialité sur le site.",
  "Mise en conformité 09-08 (voir check-list dédiée).",
  justif="Exigence légale (loi 09-08, CNDP) - données clients")
C("5.35", "Independent review of information security", "Revue indépendante de la sécurité", 0, 2, "P3", "",
  "Le présent audit est la première revue.",
  "Revue indépendante tous les 2 ans ou après changement majeur.")
C("5.36", "Compliance with policies, rules and standards for information security", "Conformité aux politiques et normes", 0, 2, "P3", "",
  "Rien à vérifier faute de politique.",
  "Contrôle annuel simple (check-list) par le référent sécurité.")
C("5.37", "Documented operating procedures", "Procédures d'exploitation documentées", 1, 3, "P2", "R06",
  "Le prestataire seul connaît la procédure de mise en ligne et de restauration.",
  "Documenter : sauvegarde/restauration, mise en ligne, création de compte.")

# ---------------------------------------------------------------- 6. HUMAIN
C("6.1", "Screening", "Sélection des candidats", 2, 2, "P3", "R11",
  "Vérification des références pour les postes administratifs.",
  "Maintenir ; proportionner aux postes ayant accès aux données clients/finance.")
C("6.2", "Terms and conditions of employment", "Termes et conditions du contrat de travail", 1, 3, "P2", "R11",
  "Contrats de travail sans clause relative à la sécurité ou à la confidentialité.",
  "Ajouter clause de confidentialité et renvoi à la charte informatique.")
C("6.3", "Information security awareness, education and training", "Sensibilisation, éducation et formation", 0, 3, "P1", "R01, R02, R07",
  "Aucune sensibilisation ; un employé a déjà saisi son mot de passe sur une fausse page.",
  "Session annuelle de 2 h + rappels trimestriels + exercice de phishing simulé.")
C("6.4", "Disciplinary process", "Processus disciplinaire", 1, 2, "P3", "",
  "Règlement intérieur général, rien sur la sécurité.",
  "Référencer la charte informatique dans le règlement intérieur.")
C("6.5", "Responsibilities after termination or change of employment", "Responsabilités après la fin du contrat", 0, 2, "P2", "R11",
  "Aucune obligation rappelée au départ.",
  "Rappel écrit de l'obligation de confidentialité au départ.")
C("6.6", "Confidentiality or non-disclosure agreements", "Engagements de confidentialité", 0, 3, "P2", "R03, R11",
  "Pas d'accord de confidentialité avec le freelance web ni le cabinet comptable.",
  "NDA signé par tous les prestataires ayant accès aux données.")
C("6.7", "Remote working", "Travail à distance", 1, 2, "P3", "R12",
  "Le gérant et le commercial travaillent depuis un PC portable et un smartphone personnels.",
  "Règles télétravail : poste à jour, chiffré, Wi-Fi de confiance, pas de poste partagé.")
C("6.8", "Information security event reporting", "Déclaration des événements de sécurité", 0, 3, "P2", "R01, R02",
  "Les salariés ne savent pas à qui signaler un email suspect.",
  "Canal de signalement unique (référent + adresse dédiée) connu de tous.")

# ---------------------------------------------------------------- 7. PHYSIQUE
C("7.1", "Physical security perimeters", "Périmètres de sécurité physique", 2, 2, "P3", "R12",
  "Bureaux au-dessus de l'entrepôt, porte principale fermée à clé hors horaires.",
  "Maintenir ; définir le périmètre bureau vs. entrepôt.")
C("7.2", "Physical entry", "Contrôles physiques des accès", 2, 2, "P3", "R12",
  "Accueil visible ; visiteurs (livreurs, clients) peuvent accéder aux bureaux.",
  "Visiteurs accompagnés ; clés tracées.")
C("7.3", "Securing offices, rooms and facilities", "Sécurisation des bureaux et locaux", 1, 2, "P3", "R12",
  "Bureau comptable non fermé à clé ; routeur sur une étagère du couloir.",
  "Fermer le bureau comptable ; placer le routeur dans un local fermé.")
C("7.4", "Physical security monitoring", "Surveillance de la sécurité physique", 1, 1, "P3", "R12",
  "Alarme anti-intrusion sur l'entrepôt ; pas de vidéosurveillance des bureaux.",
  "Suffisant au regard des enjeux ; si caméra ajoutée, déclaration CNDP requise.")
C("7.5", "Protecting against physical and environmental threats", "Protection contre les menaces physiques et environnementales", 1, 2, "P3", "R02, R06",
  "Extincteurs présents ; coupures électriques fréquentes en été non traitées.",
  "Onduleur pour le poste comptable et le routeur.")
C("7.6", "Working in secure areas", "Travail dans les zones sécurisées", None, None, "-", "",
  "Aucune zone sécurisée (pas de salle serveur ; hébergement externalisé).",
  "Non applicable.", applicable=False,
  justif="Exclue : aucune zone sécurisée sur site, l'hébergement du site est externalisé (risque traité via 5.19-5.23). À réévaluer si un serveur local est installé.")
C("7.7", "Clear desk and clear screen", "Bureau propre et écran vide", 0, 2, "P3", "R03, R12",
  "Bons de commande avec adresses clients laissés sur les bureaux ; pas de verrouillage auto des sessions.",
  "Verrouillage automatique après 5 min ; rangement des documents clients.")
C("7.8", "Equipment siting and protection", "Emplacement et protection du matériel", 1, 2, "P3", "R06",
  "PC de l'accueil exposé à la poussière de l'entrepôt.",
  "Repositionner les postes sensibles.")
C("7.9", "Security of assets off-premises", "Sécurité des actifs hors des locaux", 1, 2, "P2", "R12",
  "PC portables emmenés chez les clients agricoles sans chiffrement.",
  "Chiffrement des portables (BitLocker) et smartphones (code + chiffrement natif).")
C("7.10", "Storage media", "Supports de stockage", 0, 2, "P3", "R02, R12",
  "Clés USB personnelles utilisées pour échanger avec le cabinet comptable.",
  "Clé chiffrée dédiée ou partage cloud contrôlé ; désactiver l'autorun.")
C("7.11", "Supporting utilities", "Services supports", 1, 2, "P3", "R06",
  "Pas d'onduleur ; une seule connexion Internet (ADSL/fibre).",
  "Onduleur + partage de connexion 4G de secours.")
C("7.12", "Cabling security", "Sécurité du câblage", 1, 2, "P3", "",
  "Câblage apparent dans le couloir.",
  "Goulottes ; faible enjeu.")
C("7.13", "Equipment maintenance", "Maintenance du matériel", 1, 2, "P3", "R06",
  "Maintenance curative uniquement, par un réparateur local.",
  "Faire signer une clause de confidentialité au réparateur ; retirer les disques si possible.")
C("7.14", "Secure disposal or re-use of equipment", "Élimination ou recyclage sécurisé du matériel", 0, 2, "P3", "R03",
  "Anciens PC donnés/vendus sans effacement des disques.",
  "Effacement sécurisé (outil d'effacement ou destruction) avant cession.")

# ---------------------------------------------------------------- 8. TECHNOLOGIQUE
C("8.1", "User endpoint devices", "Terminaux utilisateurs", 1, 3, "P1", "R02, R12",
  "7 postes Windows (dont 2 portables) hétérogènes ; un poste sous Windows 10 (fin de support oct. 2025).",
  "Standard de configuration des postes ; remplacer/mettre à niveau le poste Windows 10.")
C("8.2", "Privileged access rights", "Droits d'accès privilégiés", 0, 3, "P1", "R02, R05",
  "Tous les utilisateurs sont administrateurs locaux de leur poste.",
  "Comptes utilisateurs standards ; un compte admin séparé par poste.")
C("8.3", "Information access restriction", "Restriction d'accès à l'information", 1, 3, "P2", "R03",
  "Dossier Drive 'Clients' partagé avec tous ; export complet des commandes accessible à tous les comptes du back-office.",
  "Droits par rôle dans le back-office ; partages Drive nominatifs.")
C("8.4", "Access to source code", "Accès au code source", 1, 3, "P1", "R04, R08",
  "Code du site dans un dépôt Git du prestataire ; un secret (clé d'API tierce) présent dans l'historique.",
  "Dépôt privé propriété d'AgriSouss ; secrets hors dépôt ; rotation de la clé.")
C("8.5", "Secure authentication", "Authentification sécurisée", 1, 3, "P1", "R01, R05",
  "MFA activée sur 2 comptes Google sur 9 ; pas de MFA sur l'hébergeur ni le bureau d'enregistrement du domaine.",
  "MFA obligatoire sur messagerie, hébergeur, domaine, back-office.")
C("8.6", "Capacity management", "Dimensionnement", 2, 2, "P3", "R06",
  "Offre mutualisée ; ralentissements signalés lors des promotions de saison.",
  "Surveiller les quotas d'hébergement avant la haute saison.")
C("8.7", "Protection against malware", "Protection contre les programmes malveillants", 2, 3, "P2", "R02",
  "Microsoft Defender actif par défaut sur la plupart des postes, non supervisé.",
  "Vérifier l'activation partout ; macros Office bloquées ; filtrage des pièces jointes.")
C("8.8", "Management of technical vulnerabilities", "Gestion des vulnérabilités techniques", 1, 3, "P1", "R03, R08",
  "Version de PHP en fin de support sur l'hébergement ; mises à jour Windows reportées.",
  "Mises à jour automatiques ; montée de version PHP ; scan de vulnérabilités trimestriel.")
C("8.9", "Configuration management", "Gestion des configurations", 0, 2, "P2", "R08, R10",
  "Routeur avec mot de passe administrateur par défaut ; en-têtes de sécurité HTTP absents.",
  "Configurations de référence (routeur, postes, serveur web).")
C("8.10", "Information deletion", "Suppression des informations", 0, 2, "P2", "R03, R09",
  "Commandes conservées indéfiniment dans la base.",
  "Durées de conservation + purge/anonymisation annuelle des anciennes commandes.")
C("8.11", "Data masking", "Masquage des données", None, None, "-", "",
  "Pas d'environnement de test contenant des données réelles à ce jour.",
  "Non applicable à ce stade.", applicable=False,
  justif="Exclue provisoirement : aucune copie de données de production hors production. À réintégrer si une préproduction est créée (action A21) - lien avec 8.33.")
C("8.12", "Data leakage prevention", "Prévention de la fuite de données", 0, 1, "P3", "R03",
  "Aucune mesure ; exports clients possibles vers comptes personnels.",
  "Mesures légères : restriction des partages externes Drive, pas d'outil DLP dédié.")
C("8.13", "Information backup", "Sauvegarde des informations", 1, 3, "P1", "R02, R06",
  "Sauvegardes automatiques de l'hébergeur (rétention inconnue) ; PC comptable non sauvegardé ; aucun test de restauration.",
  "Règle 3-2-1 : export BDD quotidien + copie hors hébergeur + copie hors ligne ; test trimestriel.")
C("8.14", "Redundancy of information processing facilities", "Redondance des moyens de traitement", 1, 2, "P3", "R06",
  "Dépend entièrement de l'offre mutualisée.",
  "Proportionné : pouvoir redéployer le site chez un autre hébergeur en < 48 h.")
C("8.15", "Logging", "Journalisation", 1, 2, "P2", "R01, R03, R05",
  "Journaux Apache de l'hébergeur (rétention courte) ; aucune journalisation applicative des connexions back-office.",
  "Journaliser connexions et actions d'administration ; conserver selon une durée définie.")
C("8.16", "Monitoring activities", "Activités de surveillance", 0, 2, "P2", "R01, R08",
  "Personne ne consulte les journaux ni les alertes de sécurité Google.",
  "Alertes de connexion, surveillance de disponibilité gratuite, revue mensuelle.")
C("8.17", "Clock synchronization", "Synchronisation des horloges", 3, 3, "P3", "",
  "Postes Windows et hébergeur synchronisés NTP par défaut.",
  "Conforme ; vérifier le fuseau horaire des journaux applicatifs.")
C("8.18", "Use of privileged utility programs", "Utilisation de programmes utilitaires à privilèges", 1, 2, "P3", "R02",
  "Outil d'accès à distance installé par le réparateur, toujours actif.",
  "Désinstaller les outils non utilisés ; prise en main à distance à la demande seulement.")
C("8.19", "Installation of software on operational systems", "Installation de logiciels sur les systèmes en exploitation", 0, 2, "P2", "R02",
  "Chacun installe librement des logiciels (comptes admin).",
  "Installation réservée au compte admin ; liste de logiciels autorisés.")
C("8.20", "Networks security", "Sécurité des réseaux", 1, 3, "P1", "R10",
  "Box FAI : WPS activé, clé Wi-Fi partagée depuis plusieurs années, interface d'administration avec mot de passe par défaut.",
  "Changer le mot de passe admin, désactiver WPS, WPA2/WPA3 avec clé forte, firmware à jour.")
C("8.21", "Security of network services", "Sécurité des services réseau", 1, 2, "P3", "R08",
  "HTTPS actif (certificat gratuit) ; DNS chez le bureau d'enregistrement sans verrou de transfert.",
  "Activer le verrou de domaine ; HSTS ; envisager CDN/WAF gratuit.")
C("8.22", "Segregation of networks", "Cloisonnement des réseaux", 0, 2, "P2", "R10",
  "Un seul réseau pour PC, imprimante, smartphones personnels et visiteurs.",
  "Réseau invité séparé pour visiteurs et appareils personnels.")
C("8.23", "Web filtering", "Filtrage web", 0, 1, "P3", "R02",
  "Aucun filtrage.",
  "DNS filtrant gratuit sur la box (filtrage des domaines malveillants connus).")
C("8.24", "Use of cryptography", "Utilisation de la cryptographie", 1, 2, "P2", "R03, R12",
  "TLS sur le site ; aucun chiffrement des postes ni des sauvegardes.",
  "Chiffrement des portables et des sauvegardes hors site ; règle de gestion des clés.")
C("8.25", "Secure development life cycle", "Cycle de vie de développement sécurisé", 0, 2, "P2", "R03, R08",
  "Modifications faites directement en production par le prestataire.",
  "Processus minimal : dépôt Git, revue, préproduction, mise en ligne tracée.")
C("8.26", "Application security requirements", "Exigences de sécurité des applications", 0, 2, "P2", "R03, R08",
  "Aucune exigence exprimée au prestataire.",
  "Exigences de base (référentiel OWASP ASVS niveau 1 comme base) dans le cahier des charges.")
C("8.27", "Secure system architecture and engineering principles", "Principes d'ingénierie et d'architecture sécurisées", 1, 2, "P3", "R03",
  "Architecture simple ; compte BDD de l'application avec tous les privilèges.",
  "Moindre privilège du compte BDD ; séparation des secrets.")
C("8.28", "Secure coding", "Codage sécurisé", 1, 3, "P1", "R03, R08",
  "Code PHP hétérogène : requêtes préparées sur la plupart des pages, mais quelques concaténations SQL et sorties non échappées.",
  "Requêtes préparées partout, échappement des sorties, jetons CSRF, revue de code.")
C("8.29", "Security testing in development and acceptance", "Tests de sécurité en développement et recette", 0, 2, "P2", "R03, R08",
  "Aucun test de sécurité avant mise en ligne.",
  "Scan automatisé (outil open source) avant chaque mise en ligne majeure.")
C("8.30", "Outsourced development", "Développement externalisé", 0, 3, "P1", "R03, R04, R11",
  "Freelance sans contrat écrit, accès complet, pas de livrable documenté.",
  "Contrat avec exigences sécurité, propriété du code, restitution des accès.")
C("8.31", "Separation of development, test and production environments", "Séparation des environnements", 0, 2, "P3", "R08",
  "Aucune préproduction.",
  "Créer une préproduction (sous-domaine protégé) sans données réelles.")
C("8.32", "Change management", "Gestion des changements", 0, 2, "P3", "R06, R08",
  "Changements non tracés.",
  "Journal des changements (date, auteur, objet, retour arrière).")
C("8.33", "Test information", "Informations de test", 1, 2, "P3", "R03",
  "Tests occasionnels avec de vraies commandes clients.",
  "Données de test fictives ; jamais d'export réel hors production.")
C("8.34", "Protection of information systems during audit testing", "Protection des SI pendant les tests d'audit", 2, 2, "P3", "",
  "Présent audit réalisé sans test intrusif (entretiens + observation + revue documentaire).",
  "Pour tout test technique futur : autorisation écrite, fenêtre, sauvegarde préalable.")


def controls():
    return list(_ROWS)


def theme_of(cid):
    return cid.split(".")[0]


def soa_status(row):
    """Statut de mise en oeuvre pour la DdA (SoA)."""
    if not row["applicable"]:
        return "Non applicable"
    m = row["maturite"]
    if m >= 3:
        return "Mis en oeuvre"
    if m >= 1:
        return "Partiel"
    return "Non mis en oeuvre"


def soa_justification(row):
    if row["justif"]:
        return row["justif"]
    if row["risques"] and row["risques"] != "Tous":
        return "Traitement des risques " + row["risques"]
    if row["risques"] == "Tous":
        return "Socle de gouvernance - tous risques"
    return "Bonne pratique de base (socle)"


def theme_scores():
    """Moyenne de maturité actuelle et cible par thème (mesures applicables)."""
    out = {}
    for t in THEMES:
        rows = [r for r in _ROWS if theme_of(r["id"]) == t and r["applicable"]]
        cur = sum(r["maturite"] for r in rows) / len(rows)
        tgt = sum(r["cible"] for r in rows) / len(rows)
        total = len([r for r in _ROWS if theme_of(r["id"]) == t])
        out[t] = dict(n=total, applicable=len(rows), actuel=round(cur, 2), cible=round(tgt, 2))
    return out


assert len(_ROWS) == 93, len(_ROWS)
assert [len([r for r in _ROWS if theme_of(r["id"]) == t]) for t in "5678"] == [37, 8, 14, 34]
