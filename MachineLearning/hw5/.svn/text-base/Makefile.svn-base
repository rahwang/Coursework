OBJS = eigP.o ml_utils.o 
SOBJ = svdP.o ml_utils.o
DEPS = $(OBJS:.o=.d)
CC = gcc
CFLAGS = -I../../include -g -Wall -fpic -std=gnu99 -MMD -MP -DDEBUG -O3
EIGP = eigP
SVDP = svdP
LDLIBS =  -pthread

all: $(EIGP) $(SVDP)

$(EIGP): $(OBJS)
	$(CC) $(LDFLAGS) $(LDLIBS) $(OBJS) -o $(EIGP) -lm

$(SVDP): $(SOBJ)
	$(CC) $(LDFLAGS) $(LDLIBS) $(SOBJ) -o $(SVDP) -lm

%.d: %.c

clean:
	-rm -f $(OBJS) $(EIGP) *.o
	-rm -f $(OBJS) $(EIGP) *.d
