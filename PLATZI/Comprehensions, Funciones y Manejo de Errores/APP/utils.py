def get_population():
    keys=["col","bol"]
    values=[300,400]
    return keys,values
A="HOLA"
def population_by_country(data, Country):
    result = list(filter(lambda item: item["country"] == Country, data))
    resultado2=result[0]["Population"]
    return resultado2

