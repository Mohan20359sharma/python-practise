scores = {'Alice': 80, 'Bob': 65, 'Charlie': 90}
filtered_score = {k: v for k, v in scores.items() if v >70}
print(filtered_score)