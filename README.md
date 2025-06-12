# 🧮 Calculateur IPv4 – Interface Tkinter

Cette application Python fournit une interface graphique simple permettant de manipuler des adresses IPv4. Vous pouvez convertir entre différents formats, effectuer des calculs de sous-réseaux et déterminer le masque adéquat pour un nombre donné d'appareils.

## 📦 Fonctionnalités

- 🔄 **Conversion IP ↔ Binaire**
- 🔢 **Conversion IP ↔ Entier**
- 🌐 **Calcul d'informations réseau à partir d'une IP et d'un masque**
- 🧠 **Calcul automatique du masque minimal pour un nombre d'appareils donné**

## 🖥️ Interface utilisateur

L'interface est développée avec la bibliothèque **Tkinter** et propose :

- Un champ d'entrée pour saisir une adresse IPv4, une adresse binaire ou un entier
- Un champ pour entrer un masque CIDR (ex. `24`)
- Un champ pour spécifier le nombre d'appareils nécessaires sur le sous-réseau
- Une zone d'affichage des résultats
- Des boutons pour exécuter chaque opération
- Un bouton pour quitter l'application

## ✅ Prérequis

- Python 3.x
- Bibliothèques standard :
  - `tkinter` (inclus avec Python)
  - `ipaddress`

## 🚀 Lancer l'application

1. Clonez ou téléchargez ce dépôt.
2. Lancez le script :

```bash
python ipv4_calculator.py
