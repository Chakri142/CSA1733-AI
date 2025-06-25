% Define some facts about planets and their properties
planet(mercury, rocky, small, hot, 'closest-to-sun').
planet(venus, rocky, small, hot, 'second-closest-to-sun').

% Define a predicate to look up a planet's properties by name
planet_properties(Name, Type, Size, Temperature, Position) :-
    planet(Name, Type, Size, Temperature, Position).
