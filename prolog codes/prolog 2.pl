% Define a data structure for date: year, month, day
data(Y, M, D) :-
    integer(Y),
    integer(M),
    integer(D).

% Define some facts about people and their DOBs
dob(john, date(1990, 5, 1)).
dob(johne, date(1985, 12, 10)).
dob(bob, date(1978, 2, 28)).
dob(sue, date(1995, 8, 15)).
dob(tom, date(2000, 4, 22)).

% Define a predicate to look up a person's DOB by name
lookup(Name, DOB) :-
    dob(Name, DOB).
