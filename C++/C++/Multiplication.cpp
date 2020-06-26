/**
		This code multiply 2 64 bits digits numbers with the karatsuba algorithm
		author: Ossim Belias
*/

#include <string>
#include <iostream>
#include <algorithm>
#include <math.h>

long int Multiply(const long int& a, const long int& b)
{
	long int value = 0;
	if (a == 0 || b == 0)
		return 0;
	else if (a >= b)
	{
		value = a;
		return value += Multiply(a, b - 1);
	}
	else if (a < b)
	{
		value = b;
		return value += Multiply(a - 1, b);
	}
}

void Verify(const long int& realResult, const long int& algoResult)
{
	if (algoResult != realResult)
	{
		std::cout << "Failed!! Expected: " << realResult << " but got instead: " << algoResult << std::endl;
	}
	else
	{
		std::cout << "Passed the result is " << algoResult << " as expected" << std::endl;
	}
}


void subDivide(long int& a, long int& b, long int& c, long int& d, std::string& first, std::string& second)
{
	a = std::stoll(first.substr(0, first.size() / 2));
	b = std::stoll(first.substr(first.size() / 2));
	c = std::stoll(second.substr(0, second.size() / 2));
	d = std::stoll(second.substr(second.size() / 2));
}

long int KarastubaMultiplication(std::string& first, std::string& second)
{
	int n = std::max(first.size(), second.size());
	if (n == 0) return 0;
	if (n == 1) return std::stoll(first) * std::stoll(second);

	long int a , b , c , d;
	subDivide(a, b, c, d, first, second);
	long int ac = Multiply(a, c);
	long int bd = Multiply(b, d);
	long int somme = Multiply(a + b, c + d);

	return ((pow(10, n) * ac) + (pow(10, n / 2) * (somme - ac - bd)) + bd);	
}

void RunTestcases()
{
	std::string a = "1234";
	std::string b = "5678";

	long int result = std::stoll(a) * std::stoll(b);

	std::cout << "Test case 1" << std::endl;
	std::cout << "Input Numbers are: " << a << " " << b << std::endl;
	Verify(result, KarastubaMultiplication(a, b));

	std::cout << std::endl;
	std::cout << "Test case 2" << std::endl;
	a = "1";
	b = "20";
	result = 1 * 20;
	std::cout << "Input Numbers are: " << a << " " << b << std::endl;
	Verify(result, KarastubaMultiplication(a, b));

}

int main()
{
	std::string a, b;
	long int number_1, number_2, realResult, algoResult;
	bool isValidInput = false;
	int option = -1;
	do
	{
		std::cout << "Enter the number corresponding to one of the following options" << std::endl;
		std::cout << "1 - Test with your own numbers" << std::endl;
		std::cout << "2 - Run test cases" << std::endl;
		std::cout << "0 - Exit the program" << std::endl;

		try
		{
			std::string input;
			std::cin >> input;
			option = std::stoi(input);
		}
		catch (const std::exception&)
		{
			std::cout << "Invalid option please try again" << std::endl;
		}
		switch (option)
		{
		case 0:
			std::cout << "Bye bye " << std::endl;
			break;
		case 1:
			do
			{
				try
				{
					std::cout << "Enter your digits " << std::endl;
					std::cin >> a;
					number_1 = std::stoll(a);
					std::cin >> b;
					number_2 = std::stoll(b);
					isValidInput = true;
				}
				catch (const std::exception& e)
				{
					std::cout << "Invalid input or the number is too large try again" << std::endl;
					std::cin.clear();
					isValidInput = false;
				}
			} while (!isValidInput);

			realResult = number_1 * number_2;
			algoResult = KarastubaMultiplication(a, b);
			Verify(realResult, algoResult);
			break;

		case 2:
			RunTestcases();
			break;
		default:
			break;
		}

	} while (option != 0);

	std::cin.get();
}