import random
import time

# Fonction pour générer une chaîne aléatoire
def generate_random_string(length, alphabet):
    """Génère une chaîne aléatoire de longueur donnée en utilisant l'alphabet spécifié."""
    return ''.join(random.choice(alphabet) for _ in range(length))

# Fonction pour générer un ensemble de données de séquences aléatoires
def generate_dataset(alphabet, num_sequences, sequence_lengths):
    """Génère un ensemble de données contenant un certain nombre de séquences aléatoires de longueurs spécifiées, en utilisant l'alphabet donné."""
    dataset = []
    for i in range(num_sequences):
        length = sequence_lengths[i]
        sequence = generate_random_string(length, alphabet)
        dataset.append(sequence)
    return dataset

# Fonction pour trouver la plus longue sous-séquence commune avec DFS
def lcs_dfs(str1, str2):
    """Implémente l'algorithme de recherche en profondeur (DFS) pour trouver la sous-séquence commune la plus longue entre deux chaînes."""
    def dfs(i, j, current_lcs, max_length):
        """Fonction récursive pour explorer toutes les possibilités."""
        nonlocal comparisons
        comparisons += 1
        if i == len(str1) or j == len(str2):
            if len(current_lcs) == max_length:
                if current_lcs not in lcs_results:
                    lcs_results.append(current_lcs)
            elif len(current_lcs) > max_length:
                lcs_results.clear()
                lcs_results.append(current_lcs)
                return len(current_lcs)
            return max_length

        if str1[i] == str2[j]:
            return dfs(i + 1, j + 1, current_lcs + str1[i], max_length + 1)
        else:
            max_length = max(dfs(i + 1, j, current_lcs, max_length), dfs(i, j + 1, current_lcs, max_length))
            return max_length

    comparisons = 0
    lcs_results = []
    max_length = dfs(0, 0, "", 0)
    return max_length, [seq for seq in lcs_results if len(seq) == max_length], comparisons

# Fonction pour la recherche Tabou
def tabu_search_multiple(str1, str2, alphabet, tabu_list_size=10, max_iterations=1000, num_executions=100, stagnation_limit=100):
    """Implémente l'algorithme de recherche Tabou pour trouver la sous-séquence commune la plus longue entre deux chaînes."""
    all_solutions = []
    total_comparisons = 0

    for _ in range(num_executions):
        best_solution = ""
        best_solution_length = 0
        tabu_list = []
        stagnation_count = 0

        for _ in range(max_iterations):
            current_solution = ""
            current_solution_length = 0
            tabu_candidate = ""

            # Construction de la solution courante
            for i in range(len(str1)):
                if i < len(str2) and str1[i] == str2[i]:
                    current_solution += str1[i]
                    current_solution_length += 1
                else:
                    tabu_candidate += str1[i]

            # Mise à jour de la meilleure solution
            if current_solution_length > best_solution_length:
                best_solution = current_solution
                best_solution_length = current_solution_length

            if current_solution_length == best_solution_length:
                all_solutions.append(current_solution)

            # Ajout de la séquence tabou si nécessaire
            if len(tabu_candidate) > 0:
                if len(tabu_list) >= tabu_list_size:
                    tabu_list.pop(0)
                tabu_list.append(tabu_candidate)

            # Perturbation de la séquence
            perturbed_str1 = str1
            for i in range(len(str1)):
                if i not in range(len(str2)) or str1[i] != str2[i]:
                    for c in alphabet:
                        if c != str1[i] and c not in tabu_list:
                            perturbed_str1 = str1[:i] + c + str1[i + 1:]
                            break
                    if perturbed_str1 != str1:
                        break

            str1 = perturbed_str1
            total_comparisons += 1

            # Vérification de la stagnation
            if best_solution_length == current_solution_length:
                stagnation_count += 1
                if stagnation_count >= stagnation_limit:
                    break
            else:
                stagnation_count = 0

    return all_solutions, total_comparisons

# Fonction principale
def main():
    alphabet = input("Veuillez entrer l'alphabet (par exemple, ACGT) : ")
    num_sequences = int(input("Veuillez entrer le nombre de séquences dans S : "))
    sequence_lengths = []
    for i in range(num_sequences):
        length = int(input(f"Veuillez entrer la taille de la séquence {i+1} : "))
        sequence_lengths.append(length)

    dataset = generate_dataset(alphabet, num_sequences, sequence_lengths)

    results_dfs = []
    results_tabu = []

    while True:
        print("\nEnsemble de données généré :")
        for i, sequence in enumerate(dataset, 1):
            print(f"Séquence {i}: {sequence}")

        algorithm_choice = input("\nChoisissez l'algorithme :\n1. DFS\n2. Tabu Search\nq pour quitter\nVotre choix : ").lower()

        if algorithm_choice == '1' or algorithm_choice == 'dfs':
            while True:
                sequence1_index = int(input("\nVeuillez entrer l'indice de la première séquence à comparer (de 1 à {}) : ".format(num_sequences)))
                sequence2_index = int(input("Veuillez entrer l'indice de la deuxième séquence à comparer (de 1 à {}) : ".format(num_sequences)))
                sequence1 = dataset[sequence1_index - 1]
                sequence2 = dataset[sequence2_index - 1]

                start_time = time.time()
                lcs_length, lcs_sequences, comparisons = lcs_dfs(sequence1, sequence2)
                end_time = time.time()

                print("\nNombre total de comparaisons effectuées en DFS :", comparisons)
                print("Temps d'exécution : {:.10f} secondes".format(end_time - start_time))

                print("\nLongueur de la plus longue sous-séquence commune (LCS) entre les séquences {} et {} : {}".format(sequence1_index, sequence2_index, lcs_length))
                print("Les sous-séquences LCS sont :", ", ".join(lcs_sequences))

                results_dfs.append((sequence1_index, sequence2_index, len(sequence1) + len(sequence2), end_time - start_time, comparisons))

                choice = input("\nVoulez-vous comparer d'autres séquences ? (Oui/Non) : ").lower()
                if choice != 'oui':
                    break

        elif algorithm_choice == '2' or algorithm_choice == 'tabu search':
            while True:
                sequence1_index = int(input("\nVeuillez entrer l'indice de la première séquence à comparer (de 1 à {}) : ".format(num_sequences)))
                sequence2_index = int(input("Veuillez entrer l'indice de la deuxième séquence à comparer (de 1 à {}) : ".format(num_sequences)))
                sequence1 = dataset[sequence1_index - 1]
                sequence2 = dataset[sequence2_index - 1]

                start_time = time.time()
                all_solutions, comparisons = tabu_search_multiple(sequence1, sequence2, alphabet)
                end_time = time.time()

                print("\nNombre total de comparaisons effectuées en Tabu Search :", comparisons)
                print("Temps d'exécution : {:.10f} secondes".format(end_time - start_time))

                # Comptage des solutions les plus fréquentes
                solution_counts = {}
                for solution in all_solutions:
                    if solution in solution_counts:
                        solution_counts[solution] += 1
                    else:
                        solution_counts[solution] = 1

                # Trouver la solution la plus fréquente
                most_common_solution = max(solution_counts, key=solution_counts.get)
                most_common_solution_length = len(most_common_solution)

                print("\nLongueur de la plus longue sous-séquence commune (LCS) entre les séquences {} et {} : {}".format(sequence1_index, sequence2_index, most_common_solution_length))
                print("La séquence LCS la plus fréquente est :", most_common_solution)

                results_tabu.append((sequence1_index, sequence2_index, len(sequence1) + len(sequence2), end_time - start_time, comparisons))

                choice = input("\nVoulez-vous comparer d'autres séquences ? (Oui/Non) : ").lower()
                if choice != 'oui':
                    break

        elif algorithm_choice == 'q':
            break

        else:
            print("\nChoix d'algorithme non valide. Veuillez choisir entre DFS et Tabu Search.")

    print("\nRésultats finaux pour DFS :")
    print("----------------------------------------------------------------------------------")
    print("| Séquence 1 | Séquence 2 | Taille globale | Temps d'exécution | Comparaisons |")
    print("----------------------------------------------------------------------------------")
    for result in results_dfs:
        print("| {:^10} | {:^10} | {:^13} | {:^17.10f} | {:^12} |".format(*result))
    print("----------------------------------------------------------------------------------")

    print("\nRésultats finaux pour Tabu Search :")
    print("----------------------------------------------------------------------------------")
    print("| Séquence 1 | Séquence 2 | Taille globale | Temps d'exécution | Comparaisons |")
    print("----------------------------------------------------------------------------------")
    for result in results_tabu:
        print("| {:^10} | {:^10} | {:^13} | {:^17.10f} | {:^12} |".format(*result))
    print("----------------------------------------------------------------------------------")


if __name__ == "__main__":
    main()
