# grc-audit-pme - Mini-audit de sécurité d'une PME (ISO 27001:2022 · EBIOS RM · loi 09-08)

> **Étude de cas fictive, réalisée dans un cadre académique.** « AgriSouss SARL » est une
> entreprise **fictive** : il n'y a pas eu de mission réelle, les « entretiens » et « observations » du rapport
> sont simulés pour illustrer la démarche d'un auditeur. Aucun nom, domaine, adresse IP, identifiant ou donnée réelle n'est utilisé.
> Ce livrable n'est ni un audit de certification, ni un avis juridique.

## FR - De quoi s'agit-il ?

Un livrable de **consultant GRC junior** : le mini-audit de sécurité de l'information d'une PME
marocaine (~15 salariés, site e-commerce PHP/MariaDB chez un hébergeur externe, postes Windows,
Wi-Fi, comptes Gmail/Google Drive), rédigé comme pour un cabinet de conseil, une banque ou un Big4.

**Méthode**

| Étape | Référentiel | Résultat |
|---|---|---|
| Cadrage, périmètre | ISO/IEC 27001:2022 (clauses 4-10) | Périmètre, démarche, échelles |
| Applicabilité réglementaire | Loi 09-08 (CNDP), loi 05-20 (DGSSI), DNSSI | Tableau d'applicabilité **honnête** : 09-08 s'applique ; 05-20 et DNSSI = bonnes pratiques pour une PME privée |
| Inventaire | EBIOS RM atelier 1 | 5 valeurs métier, 12 biens supports, 6 événements redoutés |
| Analyse de risques | EBIOS Risk Manager (ANSSI) **allégée**, 5 ateliers | 6 sources de risque, 5 scénarios stratégiques, 4 scénarios opérationnels, **12 risques** cotés G × V |
| Analyse d'écart | ISO/IEC 27001:2022 Annexe A / 27002:2022 | **93 mesures** évaluées (applicabilité, état, maturité 0-5, écart, priorité) + projet de **DdA (SoA)** |
| Conformité | Loi 09-08 | Check-list de 16 exigences (déclaration CNDP, consentement, cookies, conservation, sous-traitants, transferts) |
| Traitement | EBIOS RM atelier 5 | Plan d'action 30 j / 90 j / 12 mois, effort et **coûts estimés en MAD** |
| Restitution | - | Synthèse direction d'une page + graphiques |

**Contenu du dépôt**

```
grc-audit-pme/
├── build.py                      # génère tout (CSV, XLSX, graphiques, Markdown, PDF)
├── src/
│   ├── annexa.py                 # les 93 mesures de l'Annexe A + évaluation (source unique)
│   ├── register.py               # registre des risques EBIOS + plan d'action + budget
│   └── md2pdf.py                 # moteur Markdown -> PDF (reportlab) : page de titre, sommaire, tableaux
├── report/
│   ├── rapport_template.md       # texte rédigé du rapport (avec marqueurs {{...}})
│   └── rapport_audit_AgriSouss.md  # source Markdown complète (générée)
├── outputs/
│   ├── rapport_audit_AgriSouss.pdf # LE RAPPORT FINAL
│   ├── gap_analysis_annexA.xlsx  # 5 onglets : écart, DdA, synthèse thèmes, risques, plan d'action
│   ├── gap_analysis_annexA.csv   # écart Annexe A (séparateur « ; », UTF-8 BOM pour Excel)
│   ├── soa_draft.csv, risk_register.csv, action_plan.csv
│   └── figures/                  # maturité par thème, matrice des risques
├── LEARN.md                      # fiche de révision + 15 questions d'entretien
└── requirements.txt
```

**Régénérer le PDF**

```bash
pip install -r requirements.txt     # reportlab, openpyxl, matplotlib, pypdf
python build.py                     # ou : python build.py --no-pdf
```

Le texte se modifie dans `report/rapport_template.md`, les évaluations dans `src/annexa.py` et
`src/register.py` ; les tableaux, totaux, scores et graphiques du rapport sont recalculés à chaque build
(aucune valeur recopiée à la main). Sans openpyxl, seul le CSV est produit ; sans matplotlib, les
graphiques sont remplacés par une mention. Aucune API, aucun accès réseau.

**Principaux résultats (cas fictif)** : maturité moyenne Annexe A **0,64 / 5** (cible 12 mois ≈ 2,3) ;
2 risques critiques (compromission de la messagerie, rançongiciel), 6 élevés ; conformité 09-08 faible
(aucune déclaration CNDP, transferts hors Maroc non instruits) ; 23 actions, dont 10 « quick wins » à
30 jours à faible coût (MFA, sauvegardes, revue des accès, anti-fraude au RIB).

**Limites / incertitudes assumées** : articles de la loi 09-08 et décret n° 2-21-406 (loi 05-20) relus sur
le portail officiel Adala, à faire confirmer par un juriste ; position CNDP sur les cookies à vérifier ; libellés français des mesures =
traduction de travail non officielle ; coûts = ordres de grandeur ; vulnérabilités applicatives
présumées (pas de test intrusif).

## EN - Summary

A **junior GRC consultant deliverable**: an information-security mini-audit of a fictional Moroccan
SME ("AgriSouss SARL", ~15 staff, PHP/MariaDB e-commerce site on external hosting). It combines an
**ISO/IEC 27001:2022 Annex A gap analysis** (all 93 controls, maturity 0-5, draft Statement of
Applicability), a **lightweight EBIOS Risk Manager** risk assessment (12 risks, likelihood × severity
matrix), a **Moroccan law 09-08** (personal data, CNDP) compliance checklist, an honest applicability
note on **law 05-20** and the **DNSSI** (mainly public bodies / critical operators, used here as
good-practice references), a prioritized 30/90/365-day action plan with **MAD cost estimates**, and a
one-page executive summary. Everything is generated from Python data files by `python build.py`
(reportlab PDF with title page, table of contents and tables; openpyxl workbook; matplotlib charts).

*Fictional case study (no real engagement; interviews and observations are simulated), produced in an academic context. Not a certification audit, not legal advice.*

Auteur / Author : Mohamed Elansari - élève ingénieur en cybersécurité, Universiapolis Agadir.
Licence : MIT (code). Le contenu du rapport est fourni à titre pédagogique.
