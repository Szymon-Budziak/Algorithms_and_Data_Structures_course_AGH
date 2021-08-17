# Dana jest formuła logiczna postaci: C1 ∧ C2 ∧ ... ∧ Cm, gdzie każda C[i] to klauzula będąca
# alternatywą zmiennych i/lub ich zaprzeczeń. Wiadomo, że każda zmienna występuje w formule dokładnie
# dwa razy, raz zanegowana i raz niezanegowana. Na przykład podana formuła stanowi dopuszczalne
# wejście: (x ∨ y ∨ z) ∧ (~y ∨ w) ∧ (~z ∨ v) ∧ (~x ∨ ~w) ∧ (~v). Proszę podać algorytm, który oblicza
# takie wartości zmiennych, że formuła jest prawdziwa.

"""
Rozwiązanie:
Budujemy graf dwudzielny, którego jedną grupą wierzchołków są niezanegowane zmienne występujące
w formule oraz drugą grupą są formuły C1, C2, C3, .... Następnie łączymy krawędzią każdą zmienną
z formułą, w której występuje (zanegowana lub niezanegowana). Dzięki temu otrzymujemy graf
(dwudzielny), którego wierzchołki w zmiennych mają stopień 2, bo każda zmienna występuje dokładnie
2 razy (raz zanegowana i raz niezanegowana). Na tak zbudowanym grafie (dwudzielnym) szukamy
maksymalnego skojarzenia przy pomocy max flow. Jeśli maksymalne skojarzenie jest równe ilości
zmiennych, to oznacza, że istnieje takie wartościowanie, że formuła jest spełniona. Aby określić
wartościowanie wszystkich zmiennych należy w powstałym maksymalnym skojarzeniu sprawdzić, do której
formuły jest skierowana krawędź z wierzchołka zmiennej (czy ma zanegowaną wartość, czy nie). Jeśli
krawędź wskazuje na formułę, w której jest zanegowana wartość, to przypisujemy jej 0, w przeciwnym razie 1.
Rozwiązanie to jest poprawne, ponieważ w maksymalnym skojarzeniu może być maksymalnie jedna krawędź
wychodząca z danej zmiennej, czyli niemożliwe jest, aby któraś zmienna miała przypisaną wartość
0 lub 1.
"""
