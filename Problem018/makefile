all: main

main: main.o Node.o Tree.o
	g++ -o main main.o Node.o Tree.o

main.o: main.cpp Node.h Tree.h
	g++ -c main.cpp

Tree.o: Tree.cpp Node.h
	g++ -c Tree.cpp

Node.o: Node.cpp Node.h
	g++ -c Node.cpp

clean:
	rm -f *.o
	rm -f main
