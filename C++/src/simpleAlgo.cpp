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




void FibTestCase(int value, int expected)
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

int GCD(int a, int b)
{
	if (b == 0) return a;
	int remainder = a % b;
	return GCD(b, remainder);
}

void GCDTestCase(int a, int b, int expected)
{
	int gdc = GCD(a,b);
	if (gdc != expected)
	{
		std::cout << "Failed!! Expected: " << expected << " but got " << gdc << std::endl;
	}
	else
	{
		std::cout << "Ok!" << std::endl;
	}
}

int main()
{
	std::cout << "Test of fibonnaci function" << std::endl;
	FibTestCase(0,0);
	FibTestCase(1, 1);
	FibTestCase(2, 1);
	FibTestCase(5, 5);
	FibTestCase(8, 21);
	FibTestCase(23, 28657);

	std::cout << std::endl;
	std::cout << "Test of Great commun divisor function" << std::endl;
	GCDTestCase(42, 56, 14);
	GCDTestCase(0, 0, 0);
	GCDTestCase(12, 0, 12);
	GCDTestCase(7966496, 314080416, 32);


}