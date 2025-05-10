import matplotlib.pyplot as plt

age_groups = [
    "0-4", "5-9", "10-14", "15-19", "20-24", "25-29",
    "30-34", "35-39", "40-44", "45-49", "50-54",
    "55-59", "60-64", "65-69", "70-74", "75-79", "80-84", "85+"
]

population = [
    11087, 11288, 11109, 10499, 10040, 9244,
    8184, 7233, 6539, 5607, 4972,
    4144, 3381, 2402, 1581, 934, 571, 389
]

plt.figure(figsize=(12,6))
plt.bar(age_groups, population, color='skyblue', edgecolor='black')

plt.xlabel('Age Group')
plt.ylabel('Population')
plt.title('Population by Age Group (2020)')

plt.xticks(rotation=45)

plt.show()
