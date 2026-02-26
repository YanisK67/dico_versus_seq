
# Comparaison : Recherche Linéaire vs Recherche Dichotomique

Ce projet illustre et compare deux algorithmes fondamentaux de recherche dans une liste :

-  **Recherche linéaire (séquentielle)**
- **Recherche dichotomique (binaire)**

L’objectif est de comprendre leur fonctionnement, leur complexité et leurs performances.

---

## Installation

Assurez-vous d’avoir Python 3 installé.

Installer matplotlib si nécessaire :

pip install matplotlib

---

## Démo : exécution du programme

Lancer le script :

python comparaison_recherche.py

Le programme va :

1. tester les fonctions de recherche  
2. mesurer les temps d’exécution  
3. comparer les performances  
4. afficher un graphique  

---

## Exemple d’utilisation dans Python

```python
from comparaison_recherche import recherche_lineaire, recherche_dichotomique

liste = [2, 5, 8, 12, 16, 23, 38]

print(recherche_lineaire(liste, 23))
print(recherche_dichotomique(liste, 23))
```

Sortie :

5
5

---

##  Visualisation générée

Le script produit un graphique comparant les performances.

L’image `comparaison.png` correspond à la sortie générée automatiquement par le code.  
Elle montre l’évolution du temps d’exécution selon la taille des données.

 Elle permet de visualiser :

- la croissance linéaire de la recherche séquentielle  
- la croissance logarithmique de la recherche dichotomique  

Vous pouvez régénérer cette image en exécutant le script.

---

##  Comment fonctionne le programme ?

Le script :

✔ génère des tableaux triés aléatoires  
✔ recherche un élément avec les deux méthodes  
✔ mesure les temps d’exécution  
✔ trace un graphique comparatif  

---

## Objectifs

- Comprendre le fonctionnement :
  - de la **recherche séquentielle**
  - de la **recherche dichotomique**
- Mettre en évidence l’impact de la **taille du tableau** sur le temps d’exécution
- Comprendre pourquoi la recherche dichotomique est plus efficace sur un tableau **trié**
- Introduire la notion de **complexité algorithmique** (O(n) vs O(log n))

## Auteur

**Yanis K.**  
---


