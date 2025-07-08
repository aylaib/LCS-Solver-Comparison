# Résolution du Problème de la Plus Longue Sous-Séquence Commune (LCS)

Ce projet, réalisé dans le cadre du module "Éléments d'Optimisation Combinatoire" (Master 1 Bio-Informatique, USTHB), explore et compare deux approches algorithmiques pour résoudre le problème de la plus longue sous-séquence commune (LCS).

L'objectif est d'analyser les performances d'une **méthode exacte (DFS)** par rapport à une **métaheuristique (Recherche Tabou)** en termes de temps d'exécution et de qualité de la solution.

## 📈 Algorithmes Implémentés

Le script `LSC.py` contient l'implémentation des deux méthodes suivantes :

### 1. Méthode Exacte : Recherche en Profondeur (DFS)
- **Principe :** Explore de manière exhaustive toutes les sous-séquences possibles pour garantir la découverte de la solution optimale.
- **Avantages :** Fournit une solution garantie d'être la plus longue.
- **Inconvénients :** La complexité temporelle est exponentielle, ce qui la rend impraticable pour des séquences de grande taille.

### 2. Métaheuristique : Recherche Tabou (Tabu Search)
- **Principe :** Une méthode d'optimisation avancée qui navigue intelligemment dans l'espace des solutions pour trouver une solution de haute qualité en un temps raisonnable.
- **Mécanismes :** Utilise une "liste tabou" pour éviter de revenir sur des solutions récemment visitées, ce qui lui permet d'échapper aux optima locaux.
- **Avantages :** Beaucoup plus rapide que la méthode exacte, surtout pour les grandes instances.
- **Inconvénients :** Ne garantit pas de trouver la solution optimale, mais vise une solution quasi-optimale.

## 🚀 Comment l'utiliser

Le script `LSC.py` est une application en ligne de commande interactive.

1.  **Clonez le dépôt :**
    ```bash
    git clone https://github.com/VOTRE_NOM_UTILISATEUR/LCS-Solver-Comparison.git
    cd LCS-Solver-Comparison
    ```

2.  **Exécutez le script :**
    ```bash
    python LSC.py
    ```

3.  **Suivez les instructions :**
    - Entrez l'alphabet à utiliser (ex: `ACGT` pour l'ADN).
    - Spécifiez le nombre de séquences et leurs longueurs respectives.
    - Choisissez l'algorithme à tester (DFS ou Tabu Search).
    - Indiquez les indices des deux séquences que vous souhaitez comparer.

4.  Le programme affichera la LCS trouvée, le temps d'exécution, le nombre de comparaisons, et un tableau récapitulatif à la fin.

## 📊 Résultats et Analyse

L'analyse comparative montre que :
- **DFS** est très efficace pour les petites séquences mais son temps d'exécution explose rapidement.
- **Tabu Search** maintient un temps d'exécution stable et beaucoup plus faible, même pour des séquences plus longues, tout en fournissant des solutions de haute qualité.

Pour une analyse détaillée, des graphiques comparatifs et une discussion sur la complexité, veuillez consulter le rapport complet.

## 📚 Documents de Référence
- **[Rapport Complet du Projet](./Rapport_Projet_LCS.pdf)** : Ce document contient l'introduction au problème LCS, la description détaillée des algorithmes, les résultats expérimentaux et leur analyse.