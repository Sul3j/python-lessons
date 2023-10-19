# pętla while
i = 1
while i < 6:
    print(i)
    i += 1

# przerwanie iteracji pętli za pomocą słowa kluczowego break
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

# słowo kluczowe continue
# słowo kluczowe continue pomija dalsze instrukcje w pętli i idzie do nastepnego wykonania
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

# else w pętlach while
# instrukcje zawarte w else wykonują się po wykonaniu wszystkich iteracji pętli
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")