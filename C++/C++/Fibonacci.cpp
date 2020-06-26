/**
		Implementaytion of the fibonnacci algorithm
		author: Ossim Belias
*/

#include <iostream>
#include <string>
#include <vector>

int Fibonnacci(int value)
{
	std::vector<int> vec(value+1);

	if (value == 0) return 0;
	if (value == 1) return 1;

	if (value < 0)
	{
		std::cout << "the value must be non-negative." << std::endl;
		return -1;
	}

	vec[0] = 0;
	vec[1] = 1;

	for (int i = 2; i <= value; i++)
	{
		vec[i] = vec[i - 1] + vec[i - 2];
	}
	
	return vec[value];
}


void RunTestCase(int value, int expected)
{
	int fib = Fibonnacci(value);
	if (fib != expected)
	{
		std::cout << "Failed!! Expected: " << expected << " but got " << fib << std::endl;
	}
	else
	{
		std::cout << "Ok!" << std::endl;
	}
}

int main()
{
	RunTestCase(0,0);
	RunTestCase(1, 1);
	RunTestCase(2, 1);
	RunTestCase(5, 5);
	RunTestCase(8, 21);
	RunTestCase(23, 28657);
}