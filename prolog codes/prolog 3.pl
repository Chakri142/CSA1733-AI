% Define some facts about teachers and the subjects they teach
teaches(john, math).
teaches(bob, science).
teaches(sue, history).
teaches(tom, art).

% Define some facts about students and the subjects they are taking
takes(alice, math).
takes(alice, science).
takes(bob, science).
takes(bob, english).
takes(carol, history).
takes(carol, art).
takes(dave, math).
takes(dave, english).
takes(dave, art).

% Rule to find all subjects taught by a specific teacher
teaching_subjects(Teacher, Subjects) :-
    findall(Subject, teaches(Teacher, Subject), Subjects).

% Rule to find all students taking a specific subject
taking_students(Subject, Students) :-
    findall(Student, takes(Student, Subject), Students).
