sen='a quick brown fox jump over a lazy dog'
split=sen.split()
print(" ".join(sorted(list(set(split)))))  