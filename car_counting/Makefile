CFLAGS=`pkg-config --cflags opencv`
LIBS=`pkg-config --libs opencv`
CC:=g++

BIN:=./bin
SRC:=$(wildcard src/**/*.c src/*.c)
OBJ:=$(SRC:%.c=%.o)


all: $(BIN)/detect

$(BIN)/detect : $(OBJ)
	$(CC) $(<:src/%=$(BIN)/%) -o $(BIN)/detect $(LIBS)

%.o : %.c 
	$(CC) $(CFLAGS) -c $< -o $(@:src/%=$(BIN)/%)
clean:
	rm -rf $(BIN)/*.o
