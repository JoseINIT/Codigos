import utils
keys,values= utils.get_population()
print(keys,values)
print(utils.A)
data=[
    {"Country":"colombia","Population":500},
    {"Country":"bolivia","Population":300}
]
pais=input("PAIS:")
result=utils.population_by_country(data,pais)
print(result)