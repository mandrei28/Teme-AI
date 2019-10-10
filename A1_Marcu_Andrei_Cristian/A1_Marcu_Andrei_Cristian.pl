%EX 1
direct_train(craiova, bucharest).
direct_train(sibiu, craiova).
direct_train(deva, sibiu).
direct_train(brasov, deva).
direct_train(pitesti, brasov).
direct_train(ploiesti, pitesti).
direct_train(constanta, ploiesti).

%base case, direct route from X to Y
alternative_route(X,Y) :- direct_train(X,Y).
%recursive predicate that checks if there is a route between X and Y through other cities
alternative_route(X,Y) :- direct_train(X,Z), alternative_route(Z,Y).

%EX 2
translate(unu, one).
translate(doi, two).
translate(trei, three).
translate(patru, four).
translate(cinci, five).
translate(sase, six).
translate(sapte, seven).
translate(opt, eight).
translate(noua, nine).

%base case with empty lists
convert([],[]).
%predicate that converts a list of Romanian words into their equivalents in English. This predicate takes each word 
%step by step from the list ListOfRomanianWords and saves it's equivalent in the result list(TranslatedWords)
convert([X|ListOfRomanianWords], [Y|TranslatedWords]) :- translate(X, Y), convert(ListOfRomanianWords, TranslatedWords).


%EX 3
duplicate([InitialList], 1, [InitialList]) :- !.
%base case and preventing useless backtracking with cut operator.

duplicate([InitialList], N, [InitialList|X]) :-
        I is N - 1,
        I > 0,
        duplicate([InitialList], I, X).
%taking each element from the list one by one and duplicate it N times


duplicate([InitialList|T], N, X) :-
      duplicate([InitialList], N, Y),
      duplicate(T, N, Z),
      !, append(Y, Z, X).

%EX 4
insertAt(List,0,Val,[Val|List]).
%base case
insertAt([List|Tail],Pos,Val,[List|Rest]):-
    Pos1 is Pos-1,
    insertAt(Tail,Pos1,Val,Rest). 
%Iterates through the first Pos-1 elements and saves them.
%When it reaches position Pos it inserts the Value
%Then it continues copying the next elements from position Pos+1


%EX 5
listLeftRight(L,L,[L]) :- !.
%base case with cut operator
listLeftRight(L,R,[L|Tail]) :-
    L =< R,
    Aux is L+1,
    listLeftRight(Aux,R,Tail).
%we iterate from L to R and we insert each L in the list until it is equal to R