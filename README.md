# Jeu de la Vie - Version Interactive

Ce projet est une implémentation interactive du **Jeu de la Vie** de Conway en Python avec l'utilisation de la bibliothèque Tkinter. Il permet de visualiser et d'interagir avec une grille représentant des cellules vivantes ou mortes, qui évoluent selon des règles spécifiques.

---

## 🎮 Fonctionnalités

- **Interaction avec les cellules :**
  - Ajoutez ou retirez des cellules vivantes en cliquant sur la grille.
- **Contrôle de la simulation :**
  - **Start** : Lance la simulation.
  - **Stop** : Arrête la simulation.
  - **Reset** : Réinitialise la grille à vide.
  - **Random** : Génère une configuration aléatoire de cellules vivantes.
- **Visualisation en temps réel :**
  - Les cellules évoluent selon les règles du Jeu de la Vie.

---

## ⚙️ Règles du Jeu de la Vie

1. Une cellule vivante avec 2 ou 3 voisins vivants reste vivante.
2. Une cellule morte avec exactement 3 voisins vivants devient vivante.
3. Toutes les autres cellules meurent ou restent mortes.

---

## 📦 Installation et Exécution

### Prérequis

- **Python 3.x** installé sur votre machine.
- Bibliothèque Tkinter (fournie par défaut avec Python).

### Étapes pour exécuter le programme

1. Clonez le dépôt ou copiez le fichier Python :
   ```bash
   git clone https://github.com/cdupasquier/python_lifegame.git
   cd python_lifegame
   ```
2. Activez l'environnement virtuel (lf)
3. py main.py

## 🖼️ Aperçu

Une interface simple et interactive où chaque cellule de la grille peut être activée ou désactivée en cliquant dessus.

## 🛠️ Configuration

Les paramètres du jeu sont définis directement dans le code Python et peuvent être modifiés pour ajuster la taille de la grille ou la vitesse de simulation :

1. Taille des cellules : CELL_SIZE = 20
2. Largeur de la grille (colonnes) : GRID_WIDTH = 30
3. Hauteur de la grille (lignes) : GRID_HEIGHT = 20
4. Vitesse de mise à jour (ms) : UPDATE_SPEED = 200

## 📜 Structure du Code

### Classe GameOfLife :

1. Contient la logique du jeu et l'interface utilisateur.

#### Méthodes principales :

1. toggle_cell : Permet d'activer/désactiver une cellule sur la grille.
2. start : Démarre la simulation.
3. stop : Arrête la simulation.
4. reset : Réinitialise la grille.
5. randomize : Génère une configuration aléatoire.
6. update : Met à jour la grille à chaque étape.
7. next_generation : Calcule la grille suivante selon les règles.
8. count_alive_neighbors : Compte les voisins vivants d'une cellule.

## ✨ Crédits

Inspiré du Jeu de la Vie de John Conway. </br>
Développé en Python avec Tkinter pour l'interface graphique par [Christophe Dupasquier](https://christophe.dupasquier.ch)

## 💡 Améliorations possibles

1. Ajout d'une option pour enregistrer et charger des configurations.
2. Modification dynamique de la taille de la grille et de la vitesse.
3. Support pour des thèmes de couleurs.
