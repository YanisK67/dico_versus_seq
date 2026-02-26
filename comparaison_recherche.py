"""
Comparaison entre recherche séquentielle et recherche dichotomique.
"""

import random
import time
import matplotlib.pyplot as plt


# ============================================================
# Algorithmes de recherche
# ============================================================

def recherche_dichotomique(tab, element):
    """Retourne l'indice de element dans tab trié, ou -1 s'il n'est pas présent."""
    debut = 0
    fin = len(tab) - 1

    while debut <= fin:
        milieu = (debut + fin) // 2

        if element == tab[milieu]:
            return milieu
        if element < tab[milieu]:
            fin = milieu - 1
        else:
            debut = milieu + 1

    return -1


def recherche_lineaire(tab, element):
    """Retourne l'indice de element dans tab, ou -1 s'il n'est pas présent."""
    for i, valeur in enumerate(tab):
        if valeur == element:
            return i
    return -1


# ============================================================
# Outils de mesure
# ============================================================

def creer_tableau(n):
    """Génère un tableau trié de taille n avec valeurs aléatoires."""
    tab = [random.randint(1, n) for _ in range(n)]
    tab.sort()
    return tab


def mesurer_temps(n, nb_mesures):
    """
    Retourne les temps moyens (ms) :
    [temps_recherche_lineaire, temps_recherche_dichotomique]
    """
    temps = [0.0, 0.0]
    tableau = creer_tableau(n)

    for _ in range(nb_mesures):
        element = n  # valeur volontairement en fin ou absente

        # Recherche linéaire
        debut = time.time()
        recherche_lineaire(tableau, element)
        temps[0] += time.time() - debut

        # Recherche dichotomique
        debut = time.time()
        recherche_dichotomique(tableau, element)
        temps[1] += time.time() - debut

    temps[0] = round(1000 * temps[0] / nb_mesures, 6)
    temps[1] = round(1000 * temps[1] / nb_mesures, 6)

    return temps


# ============================================================
# Programme principal
# ============================================================

def main():
    """Fonction principale."""

    # --- Test simple ---
    print("\n=== Test des fonctions ===")
    liste_test = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    print("Dichotomique (23) :", recherche_dichotomique(liste_test, 23))
    print("Dichotomique (50) :", recherche_dichotomique(liste_test, 50))

    # --- Comparaison des temps ---
    nb_mesures = 20
    tailles = [100, 500, 1000, 5000, 10000, 50000, 100000]

    temps_lineaire = []
    temps_dichotomique = []

    print("\n=== Comparaison des temps ===\n")

    for taille in tailles:
        tps = mesurer_temps(taille, nb_mesures)
        temps_lineaire.append(tps[0])
        temps_dichotomique.append(tps[1])

        print(f"Taille {taille} :")
        print(f"  {tps[0]} ms (linéaire)")
        print(f"  {tps[1]} ms (dichotomique)\n")

    # --- Graphique ---
    plt.plot(tailles, temps_lineaire, label="Recherche linéaire")
    plt.plot(tailles, temps_dichotomique, label="Recherche dichotomique")

    plt.xlabel("Taille du tableau")
    plt.ylabel("Temps moyen (ms)")
    plt.legend()
    plt.title("Comparaison des performances")
    plt.show()


# ============================================================
# Point d'entrée
# ============================================================

if __name__ == "__main__":
    main()
