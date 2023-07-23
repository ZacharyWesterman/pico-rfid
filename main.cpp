#include "pico/stdlib.h"
#include <cstdio>
#include "btstack.h"

int main()
{
	stdio_init_all();

	while (true)
	{
		sleep_ms(1000);
		printf("test\n");
	}
}