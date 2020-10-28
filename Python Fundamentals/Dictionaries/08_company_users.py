import collections

lines = input()

companies = {}

while lines != "End":
    args = lines.split(" -> ")
    company = args[0]
    employer_id = args[1]

    if company not in companies:
        companies[company] = []

    if employer_id not in companies[company]:
        companies[company].append(employer_id)

    lines = input()

sorted_companies = collections.OrderedDict(sorted(companies.items()))

for key, value in sorted_companies.items():
    print(f"{key}")

    for employer_id in value:
        print(f"-- {employer_id}")
