OBJS = message_passing.o
DEPS = $(OBJS:.o=.d)
CC = gcc
CFLAGS = -Werror -I../../include -g -Wall -fpic -std=gnu99 -MMD -MP -DDEBUG -O3
MESSAGE = message
LDLIBS =  -pthread

all: $(MESSAGE)

$(MESSAGE): $(OBJS)
	$(CC) $(LDFLAGS) $(LDLIBS) $(OBJS) -o $(MESSAGE) -lm

%.d: %.c

clean:
	-rm -f $(OBJS) $(MESSAGE) *.o
	-rm -f $(OBJS) $(MESSAGE) *.d
