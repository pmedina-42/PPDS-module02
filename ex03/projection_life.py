import matplotlib.pyplot as plt
from load_csv import load


def main():
    """proyectame a tu madre la puta"""
    try:
        inc = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        expectancy = load("life_expectancy_years.csv")
        if inc is not None and expectancy is not None:
            gnp_1900 = inc['1900']
            expectancy_1900 = expectancy['1900']

            plt.scatter(gnp_1900, expectancy_1900)
            plt.title("1900")
            plt.xlabel("Gross domestic product")
            plt.ylabel("Life expectancy (Years)")
            plt.xscale("log")
            plt.xticks(ticks=[300, 1000, 10000], labels=['300', '1k', '10k'])
            plt.show()
        else:
            print('Cagaste perra')
    except Exception:
        print('Errorsito pa ti')


if __name__ == "__main__":
    """la main de tu puta madre"""
    main()
