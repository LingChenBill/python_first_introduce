print()
print("1")
if 43 > 42:
    print("Don't panic")
movies = ["The Holy Grail",
          "The Life of Brian",
          "The Meaning of Life"]
print(movies)
print(movies[1])
print(movies[0])

cast = ["Cleese", 'Palin', 'Jones', 'Idle']
print(cast)
print(len(cast))
print(cast[1])
cast.append("Gilliam")
print(cast)
# 删除末尾数据
cast.pop()
print(cast)
cast.extend(["Gilliam", "Chapman"])
print(cast)
cast.remove("Chapman")
print(cast)
cast.insert(0, "Chapman")
print(cast)
#cast.pop()
cast.remove("Chapman")
print(cast)
movies.insert(1, 1975)
print(movies)
movies.insert(3, 1979)
#movies.insert(-1, 1983)
#movies.insert(5, 1983)
movies.append(1983)
print(movies)
movies = ["The Holy Grail", 1975, 
          "The Life of Brian", 1979,
          "The Meaning of Life", 1983]
print(movies)
