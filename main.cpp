#include "pico/stdlib.h"
#include <cstdio>

int main()
{
	stdio_init_all();

	while (true)
	{
		sleep_ms(1000);
		printf("test\n");
	}
}