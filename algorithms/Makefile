CC = g++
CFLAGS = -Wall 
DEPS = util.o
OBJ = insertionSort.o mergeSort.o countStrings.o reverseStrings.o
BIN = insertionSort.out mergeSort.out countStrings.out reverseStrings.out

all: $(BIN)

util.o: util.cpp
	$(CC) $(GFLAGS) -c util.cpp

mergeSort.o: mergeSort.cpp 
	$(CC) $(GFLAGS) -c mergeSort.cpp

mergeSort.out: mergeSort.o $(DEPS)
	$(CC) $(GFLAGS) $(DEPS) mergeSort.o -o mergeSort.out

insertionSort.o: insertionSort.cpp 
	$(CC) $(GFLAGS) -c insertionSort.cpp

insertionSort.out: insertionSort.o $(DEPS)
	$(CC) $(GFLAGS) $(DEPS) insertionSort.o -o insertionSort.out

countStrings.o: countStrings.cpp
	$(CC) $(GFLAGS) -c countStrings.cpp

countStrings.out: countStrings.o $(DEPS)
	$(CC) $(GFLAGS) countStrings.o -o countStrings.out

reverseStrings.o: reverseStrings.cpp
	$(CC) $(GFLAGS) -c reverseStrings.cpp

reverseStrings.out: reverseStrings.o 
	$(CC) $(GFLAGS) reverseStrings.o -o reverseStrings.out

clean: 
	clear
	rm -f *.o
	rm -f $(BIN)
	rm -f *.out
	rm -rf *.dSYM
