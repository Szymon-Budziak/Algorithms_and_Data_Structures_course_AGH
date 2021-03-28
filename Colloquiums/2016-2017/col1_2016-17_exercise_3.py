# Proszę opisać(bez implementacji!) jak najszybszy algorytm, który otrzymuje na
# wejściu pewien ciąg n liter oraz liczbę k i wypisuje najczęściej powtarzający
# się podciąg długości k(jeśli ciągów mogących stanowić rozwiązanie jest kilka,
# algorytm zwraca dowolny z nich). Można założyć, że ciąg składa się wyłącznie
# z liter a i b. Na przykład dla ciągu ababaaaabb oraz k = 3 rozwiązaniem jest zarówno
# ciąg aba, który powtarza się dwa razy(to, że te wystąpienia na siebie nachodzą nie
# jest istotne). Zaproponowany algorytm opisać, uzasadnić jego poprawność oraz oszacować
# jego złożoność.


def count_sort(T, k):
    A = [0]*10
    B = [0]*len(T)
    for i in range(len(T)):
        index = int((T[i][1]/k) % 10)
        A[index] += 1
    for i in range(1, 10):
        A[i] += A[i-1]
    j = len(T)-1
    while j >= 0:
        index = int((T[j][1]/k) % 10)
        B[A[index]-1] = T[j]
        A[index] -= 1
        j -= 1
    for i in range(len(T)):
        T[i] = B[i]


def radix_sort(T):
    maximum = 0
    for i in range(len(T)):
        maximum = max(T[i][1], maximum)
    j = 1
    while maximum/j > 0:
        count_sort(T, j)
        j *= 10


def convert_string(string):
    number = 0
    for i in range(len(string)):
        if string[i] == "b":
            number += 2**(len(string)-i)
    return number


def the_most_common_substring(n, k):
    A = []
    for i in range(0, len(n)-k+1):
        string = n[i:i+k]
        number = convert_string(string)
        A.append((string, number))
    # Complexity of this for loop is O(k*(n-k+1)), because complexity of just
    # this for loop is O(n-k+1) but converting string to a number takes O(k)
    # where n is the length of array and k length of string, so complexity of
    # for loop and string converting is O(k) * O(n-k+1) = O(k*(n-k+1))
    radix_sort(A)
    # Complexity of radix sort in our expected time os O(k*(n-k))
    word = max_word = A[0][0]
    result = max_result = 1
    for i in range(1, len(A)):
        if A[i][0] == word:
            result += 1
            if result > max_result:
                max_result = result
                max_word = A[i][0]
        else:
            result = 1
            word = A[i][0]
    # Complexity of this for lop is O(n-k) where n is the length of array
    # Whole complexity of algorithm is O(k*(n-k+1)) + O(k*(n-k)) + O(n-k)
    # == O(k*(n-k))
    return max_word


string = "ababaaaabbababaaa"
k = 3
print(the_most_common_substring(string, k))
