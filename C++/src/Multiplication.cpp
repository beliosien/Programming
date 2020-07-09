/**
//		This code multiply 2 64 bits digits numbers with the karatsuba algorithm
//		author: Ossim Belias
//*/

#include <string>
#include <algorithm>
#include <iostream>
#include <cmath>

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
	a = std::stoll(first.substr(0, first.size() / 2 ));
	b = std::stoll(first.substr(first.size() / 2 ));
	c = std::stoll(second.substr(0, second.size() / 2 ));
	d = std::stoll(second.substr(second.size() / 2 ));
}


void split_at(long int& a, long int& b, std::string& s, int pos, int size)
{
	if (s.size() < size)
	{
		for (int i = 0; i < size - s.size(); i++)
		{
			s = '0' + s;
		}
	}
	if (pos - 1 > 0)
	{
		a = std::stoll(s.substr(0, pos - 1));
		b = std::stoll(s.substr(pos - 1));
	}
}

long int KarastubaMultiplication(std::string first, std::string second)
{
	if (stoi(first) < 10 || stoi(second) < 10)
		return stoi(first) * stoi(second);

	int max_size = std::max(first.size(), second.size());
	int split_pos = floor((max_size+1) / 2);

	long int a = 0, b = 0, c = 0, d = 0;
	split_at(a, b, first, split_pos, max_size);
	split_at(c, d, second, split_pos, max_size);

	long int bd = KarastubaMultiplication(std::to_string(b), std::to_string(d));
	long int sum = KarastubaMultiplication(std::to_string(a + b), std::to_string(c + d));
	long int ac = KarastubaMultiplication(std::to_string(a), std::to_string(c));

	return (pow(10, 2*split_pos) * ac) + (pow(10, split_pos) * (sum - ac - bd)) + bd;
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
}