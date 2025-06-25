% Base case: Move one disk
hanoi(1, From, To, _) :-
    write('Move disk 1 from '), write(From),
    write(' to '), write(To), nl.

% Recursive case: Move N disks
hanoi(N, From, To, Aux) :-
    N > 1,
    M is N - 1,
    hanoi(M, From, Aux, To),
    write('Move disk '), write(N),
    write(' from '), write(From),
    write(' to '), write(To), nl,
    hanoi(M, Aux, To, From).

% Solve the Tower of Hanoi puzzle
solve(N) :-
    hanoi(N, left, right, center).
