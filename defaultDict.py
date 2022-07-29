from collections import defaultdict

my_company = 'Teclado'

coworkers = ['Jen', 'Li', 'Charlie', 'Rhys']
other_coworkers = [('Rolf', 'Apple, Inc.'), ('Anna', 'Google')]

coworker_companies = defaultdict(lambda: my_company)


for person, company in other_coworkers:
    coworker_companies[person]

print(coworker_companies[coworkers[0]])
print(coworker_companies['Rolf'])
