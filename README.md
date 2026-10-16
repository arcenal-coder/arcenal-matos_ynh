# ARCenal Matos pour YunoHost — preview

Gestion des actifs matériels/logiciels et logistique interne multisite.

Version 0.2.0 : modules EPI et Dosimètres passifs indépendants dans Paramètres → Modules.
EPI actif par défaut ; Dosimètres initialement inactif, logistique sans résultats
de dose. L'assistance IA utilise le MCP existant ; les confirmations physiques restent humaines.
Conserver une sauvegarde YunoHost complète avant mise à jour ; un retour arrière
nécessite sa restauration avec la version précédente, base, médias et configuration.

Le paquet configure PostgreSQL, SSOwat/LDAP, SMTP, le cache du logo d'organisation
YunoHost et le timer de rappels. Connexion exclusivement YunoHost en production.
Un compte YunoHost est choisi comme administrateur lors de l'installation.

Source applicative : https://github.com/arcenal-coder/arcenal-matos
Catalogue de diffusion : https://github.com/arcenal-coder/arcenal-systeme-catalogue

Logiciel propriétaire, LicenseRef-Proprietary ; conditions dans LICENSE.
Le catalogue officiel de logiciels libres YunoHost n'est pas le catalogue ARCenal.

Le canal preview permet la recette sur un serveur d'essai avant usage métier.
Les preuves de cycle de vie réalisées sont décrites dans TEST_REPORT.md.
