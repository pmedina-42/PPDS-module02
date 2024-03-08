import matplotlib.pyplot as plt
from load_csv import load
import sys


def plot_life_expectancy(data, country_name):
    """chupame el huevo con esperanza"""
    country_data = data[data['country'] == country_name]
    years = country_data.columns[1:]
    life_expectancy = country_data.values.ravel()[1:]
    plt.plot(years, life_expectancy)
    plt.title(f"{country_name} life expectancy projection")
    plt.xlabel("Year")
    plt.xticks(years[::40])
    plt.ylabel("Life Expectancy")
    plt.show()


def main():
    """la esperanza de vida de tu abuela"""
    try:
        dataset = load("life_expectancy_years.csv")
        if len(sys.argv) == 1:
            if dataset is not None:
                spain_data = dataset[dataset['country'] == 'Spain']
                if not spain_data.empty:
                    plot_life_expectancy(dataset, 'Spain')
                else:
                    print("Spain data not found in the dataset.")
        elif len(sys.argv) == 2:
            country = sys.argv[1]
            country_data = dataset[dataset['country'] == country]
            if not country_data.empty:
                plot_life_expectancy(dataset, country)
            else:
                print(f"{country} data not found in the dataset.")
    except Exception:
        print('Gestioname esta')


if __name__ == "__main__":
    """la main de tu puta madre"""
    main()
