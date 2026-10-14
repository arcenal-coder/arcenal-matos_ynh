# ARCenal Matos 0.1.0~ynh3 — preview

- RÉUSSI : application, 60 tests locaux et 16 parcours Chromium.
- RÉUSSI : SSO/identité de proxy et refus d'accès testés ; données PostgreSQL locales.
- RÉUSSI : logo du portail YunoHost public réel téléchargé ; absence du logo dans le paquet distribué.
- RÉUSSI : syntaxe des scripts ; analyse statique de la candidate finalisée à effectuer avant publication.
- NON_EXÉCUTÉ : package_check, installation, retrait/réinstallation, upgrade, sauvegarde/restauration sur une instance YunoHost d'essai.
- NON_EXÉCUTÉ : connexion utilisateur réelle YunoHost et délivrance SMTP sur le serveur cible ; SSH port 22 inaccessible dans cette session.
- NON_EXÉCUTÉ : profil Hermès réel et téléphones/étiquettes physiques.

Le canal preview est une distribution de recette. Il ne constitue pas une
preuve de mise en service métier ou de qualification stable.

Premier package_check sur YunoHost 12.1.41.2 : ÉCHEC d'installation, lecture
de current_host sans newline sous errexit. Lecture corrigée et déclaration
Nginx explicite dans install/upgrade ; nouvelle qualification requise.

Deuxième essai : installation exécutée, refus de qualification dû aux nombreux
warnings du téléchargement cosmétique sur certificat autosigné de test.
Sortie de cette opération routée vers stdout, fallback conservé ; aucune
vérification TLS désactivée et aucun scénario exclu.
