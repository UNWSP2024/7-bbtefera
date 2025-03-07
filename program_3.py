# Program #3: US_Population
def populationdata():
    data = []
    while (year := int(input("Enter year (0 to stop): "))) != 0:
        state = input("Enter state: ")
        population = int(input("Enter population: "))
        data.append([year, state, population])
    return data

def totalpopulation(data, year):
    return sum(pop for y, _, pop in data if y == year)

#I think this part should work, but if it doesn't, I don't know how to fix it.
if __name__ == "__main__":
    data = populationdata()
    year = int(input("Enter year to calculate population: "))
    print(f"Total population for {year}: {totalpopulation(data, year)}")
