# students = ['Jack', 'Peter', 'David']

# students = [['Jack', 'Python'], ['Peter', 'C++'], ['David', 'Ruby']]

# print(students[2][0] + ' is learning ' + students[1][1] + '.')
# print(students[1][0] + ' is learning ' + students[2][1] + '.')

# print(students[1])

alphabet = [['a', 'i', 'u', 'e','o'], ['q', 'w', 'r', 't', 'y','p', 's', 'd','f','g','h','j','k','l','z','x','c','v','b','n','m']]

# print(alphabet[1][11] + alphabet[0][0] + alphabet[1][16] + alphabet[1][12])

print('Vowels: ', end=" ")
for i in range((len(alphabet[0]))):
    print(str(alphabet[0][i]) + ", ", end="")
print() 
print('Consonants: ', end=" ")
for i in range((len(alphabet[1]))):
    print(str(alphabet[1][i]) + ", ", end="")