import matplotlib.pyplot as plt
from load_csv import load
import sys


def preprocess_population(population):
    """preprocesame esta"""
    if population.endswith("B"):
        return float(population[:-1]) * 1e9
    if population.endswith("M"):
        return float(population[:-1]) * 1e6
    elif population.endswith("k"):
        return float(population[:-1]) * 1e3
    else:
        return float(population)


def plot_population(dataset, countries):
    """xD"""
    population_data = {}
    for country in countries:
        country_data = dataset[dataset['country'] == country].iloc[:, 1:]
        population_data[country] = [preprocess_population(pop)
                                    for pop in country_data.values.flatten()]
    years = country_data.columns.astype(int)
    for country, pop_values in population_data.items():
        plt.plot(years, pop_values, label=country)
    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.xticks(range(1800, 2051, 40), range(1800, 2051, 40))
    plt.xlim(1800, 2040)
    y_ticks = [20e6, 40e6, 60e6]
    plt.yticks(y_ticks, ["20M", "40M", "60M"])
    plt.legend(loc="lower right")
    plt.show()


def main():
    """la main de tu puta madre 2.0"""
    try:
        dataset = load("population_total.csv")
        if dataset is not None:
            if len(sys.argv) == 1:
                campus = "Spain"
                other = "Italy"
                plot_population(dataset, [campus, other])
            elif len(sys.argv) == 2:
                campus = "Spain"
                other = sys.argv[1]
                plot_population(dataset, [campus, other])
            elif len(sys.argv) == 3:
                campus1 = sys.argv[1]
                campus2 = sys.argv[2]
                plot_population(dataset, [campus1, campus2])
    except Exception:
        print('Gestioname esta')


if __name__ == "__main__":
    """la main de tu puta madre"""
    main()
