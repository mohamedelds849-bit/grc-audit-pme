# -*- coding: utf-8 -*-
"""Registre des risques (EBIOS RM allégé) et plan d'action - AgriSouss SARL (cas fictif).

Échelles (4 niveaux, inspirées des exemples du guide EBIOS Risk Manager de l'ANSSI) :
  Gravité G   : 1 Mineure | 2 Significative | 3 Grave | 4 Critique
  Vraisemblance V : 1 Peu vraisemblable | 2 Vraisemblable | 3 Très vraisemblable | 4 Quasi certain
  Niveau = G x V  -> 1-3 Faible | 4-6 Modéré | 8-9 Élevé | 12-16 Critique
"""

GRAVITE = {1: "Mineure", 2: "Significative", 3: "Grave", 4: "Critique"}
VRAISEMBLANCE = {1: "Peu vraisemblable", 2: "Vraisemblable", 3: "Très vraisemblable", 4: "Quasi certain"}


def niveau(g, v):
    s = g * v
    if s >= 12:
        return s, "Critique"
    if s >= 8:
        return s, "Élevé"
    if s >= 4:
        return s, "Modéré"
    return s, "Faible"


# id, intitulé, source de risque, valeur métier / bien support, G, V, G_res, V_res, mesures Annexe A, actions
RISKS = [
    dict(id="R01", titre="Prise de contrôle du compte Google de la gérance par hameçonnage",
         source="SR1 Cybercriminel opportuniste", cible="VM2/VM3 - Comptes Google (Gmail, Drive)",
         g=4, v=3, g_res=4, v_res=1, mesures="5.17, 5.23, 6.3, 8.5", actions="A01, A03, A12, A16, A18, A19"),
    dict(id="R02", titre="Rançongiciel sur le poste comptable / partage de fichiers",
         source="SR1 Cybercriminel opportuniste", cible="VM3 - PC comptable, logiciel de facturation",
         g=4, v=3, g_res=3, v_res=1, mesures="8.1, 8.2, 8.7, 8.8, 8.13", actions="A04, A09, A12, A16, A20"),
    dict(id="R03", titre="Exfiltration de la base clients via une vulnérabilité du site PHP (injection SQL)",
         source="SR1 Cybercriminel opportuniste / SR5 Concurrent", cible="VM1/VM2 - Site web + base MariaDB",
         g=3, v=3, g_res=3, v_res=1, mesures="8.8, 8.26, 8.28, 8.29", actions="A05, A16, A17, A18, A21, A23"),
    dict(id="R04", titre="Abus d'une clé d'API tierce exposée dans l'historique Git (« denial of wallet »)",
         source="SR1 Cybercriminel opportuniste", cible="VM1 - Dépôt de code du site",
         g=2, v=4, g_res=2, v_res=1, mesures="8.4, 8.24, 8.30", actions="A02"),
    dict(id="R05", titre="Compromission du compte de l'hébergeur / du domaine (identifiants partagés, sans MFA)",
         source="SR1 Cybercriminel / SR4 Ancien prestataire", cible="VM1 - Panneau d'hébergement, DNS",
         g=4, v=2, g_res=4, v_res=1, mesures="5.16, 5.17, 8.2, 8.5", actions="A01, A03, A08, A18"),
    dict(id="R06", titre="Perte durable des données du site faute de sauvegarde exploitable",
         source="Accident / erreur (hors sources intentionnelles EBIOS)", cible="VM1 - Base MariaDB, fichiers du site",
         g=3, v=2, g_res=3, v_res=1, mesures="5.30, 5.37, 8.13, 8.14", actions="A04, A20"),
    dict(id="R07", titre="Fraude au faux fournisseur / changement de RIB par email usurpé",
         source="SR2 Fraudeur", cible="VM3 - Paiements fournisseurs",
         g=3, v=3, g_res=3, v_res=1, mesures="5.3, 5.14, 6.3", actions="A07, A12"),
    dict(id="R08", titre="Défiguration ou injection de contenu malveillant (XSS, SEO spam) sur le site",
         source="SR3 Hacktiviste / défaceur", cible="VM4 - Site web, image de marque",
         g=2, v=3, g_res=2, v_res=1, mesures="8.9, 8.25, 8.28, 8.29", actions="A05, A17, A21, A23"),
    dict(id="R09", titre="Non-conformité à la loi 09-08 (absence de déclaration CNDP, transferts hors Maroc non encadrés)",
         source="Exigence réglementaire (contrôle CNDP, plainte client)", cible="VM2 - Traitements de données clients/RH",
         g=3, v=3, g_res=2, v_res=1, mesures="5.20, 5.31, 5.34, 8.10, 8.11", actions="A10, A13, A14, A15, A19"),
    dict(id="R10", titre="Intrusion sur le réseau local via le Wi-Fi (clé partagée, box non durcie)",
         source="SR4 Ancien employé / SR1 opportuniste à proximité", cible="Réseau local, PC bureau",
         g=2, v=2, g_res=2, v_res=1, mesures="8.9, 8.20, 8.22", actions="A06"),
    dict(id="R11", titre="Accès persistants d'anciens salariés ou prestataires",
         source="SR4 Ancien employé / prestataire mécontent", cible="Comptes Google, back-office, hébergeur",
         g=3, v=3, g_res=3, v_res=1, mesures="5.11, 5.18, 6.5, 8.30", actions="A08, A11, A14, A19"),
    dict(id="R12", titre="Vol ou perte d'un PC portable / smartphone non chiffré contenant des données clients",
         source="SR6 Voleur opportuniste", cible="VM2 - Terminaux mobiles",
         g=2, v=3, g_res=1, v_res=3, mesures="7.9, 8.1, 8.24", actions="A09"),
]

for r in RISKS:
    r["score"], r["niveau"] = niveau(r["g"], r["v"])
    r["score_res"], r["niveau_res"] = niveau(r["g_res"], r["v_res"])

# Plan d'action. Coûts = ESTIMATIONS indicatives en MAD HT (ordre de grandeur, marché marocain,
# hypothèse 1 USD ~ 10 MAD), à confirmer par devis. "j" = jour-homme.
ACTIONS = [
    # ---- Quick wins (0-30 jours)
    dict(id="A01", horizon="30 j", titre="Activer la MFA sur tous les comptes Google, l'hébergeur, le bureau d'enregistrement du domaine et le back-office",
         effort="1 j", cout="0", porteur="Référent sécurité", risques="R01, R05", mesures="8.5, 5.17"),
    dict(id="A02", horizon="30 j", titre="Révoquer et régénérer la clé d'API exposée ; retirer les secrets du dépôt et de son historique ; .env hors dépôt",
         effort="0,5 j", cout="0 - 1 000", porteur="Prestataire web", risques="R04", mesures="8.4, 8.24"),
    dict(id="A03", horizon="30 j", titre="Déployer un gestionnaire de mots de passe d'équipe ; changer les mots de passe partagés",
         effort="1 j", cout="0 - 6 000 / an", porteur="Référent sécurité", risques="R01, R05", mesures="5.17"),
    dict(id="A04", horizon="30 j", titre="Sauvegarde 3-2-1 : export BDD quotidien, copie hors hébergeur, disque externe hors ligne pour la compta ; 1er test de restauration",
         effort="2 j", cout="1 000 - 2 500", porteur="Prestataire web + Référent", risques="R02, R06", mesures="8.13, 5.30"),
    dict(id="A05", horizon="30 j", titre="Monter la version de PHP vers une branche supportée ; ajouter les en-têtes HTTP de sécurité (CSP, HSTS, X-Content-Type-Options, frame-ancestors)",
         effort="1-2 j", cout="1 500 - 4 000", porteur="Prestataire web", risques="R03, R08", mesures="8.8, 8.9"),
    dict(id="A06", horizon="30 j", titre="Durcir la box : mot de passe admin, WPS désactivé, WPA2/WPA3 clé forte, réseau invité séparé",
         effort="0,5 j", cout="0 - 1 500", porteur="Référent sécurité", risques="R10", mesures="8.20, 8.22"),
    dict(id="A07", horizon="30 j", titre="Procédure anti-fraude : double validation des virements, contre-appel sur numéro connu pour tout changement de RIB",
         effort="0,5 j", cout="0", porteur="Gérance", risques="R07", mesures="5.3, 5.14"),
    dict(id="A08", horizon="30 j", titre="Revue des comptes : supprimer les accès des anciens salariés/prestataires, comptes nominatifs, droits admin retirés",
         effort="1 j", cout="0", porteur="Référent sécurité", risques="R05, R11", mesures="5.16, 5.18, 8.2"),
    dict(id="A09", horizon="30 j", titre="Postes : mises à jour automatiques, Defender vérifié, verrouillage d'écran, chiffrement des portables ; remplacer le poste Windows 10",
         effort="2 j", cout="0 - 8 000", porteur="Référent + réparateur", risques="R02, R12", mesures="8.1, 8.7, 8.24"),
    dict(id="A10", horizon="30 j", titre="Site : politique de confidentialité, mentions d'information 09-08 sur les formulaires, bandeau cookies avec choix",
         effort="1-2 j", cout="1 000 - 3 000", porteur="Gérance + Prestataire web", risques="R09", mesures="5.34"),
    # ---- 90 jours
    dict(id="A11", horizon="90 j", titre="PSSI simplifiée + charte informatique signée (annexée au règlement intérieur) + procédure arrivée/départ",
         effort="3-5 j", cout="5 000 - 12 000", porteur="Gérance + consultant", risques="Tous", mesures="5.1, 5.10, 6.2, 6.4"),
    dict(id="A12", horizon="90 j", titre="Sensibilisation (session 2 h) + campagne de phishing simulé interne (outil open source)",
         effort="2 j", cout="3 000 - 6 000", porteur="Consultant", risques="R01, R02, R07", mesures="6.3, 6.8"),
    dict(id="A13", horizon="90 j", titre="Déclarations CNDP des traitements (clients/prospects, RH) et démarche pour les transferts de données hors Maroc",
         effort="2-3 j", cout="0 - 5 000 (accompagnement)", porteur="Gérance", risques="R09", mesures="5.31, 5.34"),
    dict(id="A14", horizon="90 j", titre="Contrats/avenants avec hébergeur, prestataire web, transporteur, cabinet comptable : clauses sécurité, confidentialité, sous-traitance 09-08",
         effort="2 j", cout="3 000 - 8 000 (juriste)", porteur="Gérance + juriste", risques="R09, R11", mesures="5.19, 5.20, 6.6, 8.30"),
    dict(id="A15", horizon="90 j", titre="Inventaire des actifs + registre des traitements + durées de conservation et purge des anciennes commandes",
         effort="2 j", cout="0", porteur="Référent sécurité", risques="R09", mesures="5.9, 5.12, 8.10, 8.11"),
    dict(id="A16", horizon="90 j", titre="Fiche réflexe incident (contacts hébergeur, prestataire, maCERT, CNDP, police) + registre des incidents",
         effort="1 j", cout="0 - 2 000", porteur="Référent + consultant", risques="R01, R02, R03", mesures="5.24, 5.26, 5.5"),
    dict(id="A17", horizon="90 j", titre="Audit de sécurité applicatif du site (revue de code + test d'intrusion autorisé) et correction des injections SQL/XSS",
         effort="5-8 j", cout="25 000 - 50 000", porteur="Prestataire qualifié", risques="R03, R08", mesures="8.28, 8.29, 8.8"),
    dict(id="A18", horizon="90 j", titre="Journalisation : connexions back-office, alertes de connexion Google, surveillance de disponibilité gratuite",
         effort="1-2 j", cout="0 - 3 000", porteur="Prestataire web", risques="R01, R03, R05", mesures="8.15, 8.16"),
    dict(id="A23", horizon="90 j", titre="Mettre le site derrière un CDN/WAF (offre gratuite ou d'entrée de gamme) ; verrou de transfert du domaine",
         effort="0,5 j", cout="0 - 2 500 / an", porteur="Prestataire web", risques="R08, R03", mesures="8.21"),
    # ---- 12 mois
    dict(id="A19", horizon="12 mois", titre="Migrer de Gmail gratuit vers une offre professionnelle administrable (console, MFA imposée, récupération des comptes)",
         effort="3 j", cout="10 000 - 15 000 / an (15 utilisateurs)", porteur="Gérance + prestataire", risques="R01, R09, R11", mesures="5.23, 8.5"),
    dict(id="A20", horizon="12 mois", titre="PCA/PRA simplifié (RTO/RPO, mode dégradé) + test de restauration annuel documenté",
         effort="3 j", cout="3 000 - 8 000", porteur="Référent + consultant", risques="R02, R06", mesures="5.29, 5.30"),
    dict(id="A21", horizon="12 mois", titre="Cycle de développement sécurisé avec le prestataire : dépôt privé, préproduction, revue, journal des changements",
         effort="4 j", cout="5 000 - 12 000", porteur="Prestataire web", risques="R03, R08", mesures="8.25, 8.31, 8.32"),
    dict(id="A22", horizon="12 mois", titre="Revue de direction annuelle avec indicateurs (MFA %, sauvegardes testées, mises à jour) + revue indépendante à 24 mois",
         effort="1 j / an", cout="0 - 5 000", porteur="Gérance", risques="Tous", mesures="5.4, 5.35, 5.36"),
]

HORIZON_ORDER = {"30 j": 0, "90 j": 1, "12 mois": 2}
ACTIONS.sort(key=lambda a: (HORIZON_ORDER[a["horizon"]], a["id"]))


def _bounds(cout):
    """Extrait (min, max) MAD d'une chaîne d'estimation, pour totaux indicatifs."""
    import re
    nums = [int(n.replace(" ", "")) for n in re.findall(r"\d[\d ]*\d|\d", cout.split("(")[0].split("/")[0])]
    if not nums:
        return 0, 0
    return min(nums), max(nums)


def budget_by_horizon():
    out = {}
    for a in ACTIONS:
        lo, hi = _bounds(a["cout"])
        b = out.setdefault(a["horizon"], [0, 0])
        b[0] += lo
        b[1] += hi
    return out
