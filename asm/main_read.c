#include <stdio.h>
#include <errno.h>
#include <string.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

int main(int argc, char *argv[])
{
	char buffer[4];
	int fd = 0;
	fd = open("test.txt",O_RDONLY);
	int count = read(fd,buffer,28);
	return 0;
}
