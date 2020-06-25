/**
		This code multiply 2 64 bits digits numbers with the karatsuba algorithm

		author: Ossim Belias
*/

#include <string>
#include <iostream>
#include <math.h>

int64_t Multiply(const std::int64_t& a, const std::int64_t& b)
{
	int64_t value = 0;
	if (a == 0 || b == 0)
		return 0;
	else if (a >= b)
	{
		value = a;
		return value += Multiply(a, b - 1);
	}
	else if ( a < b)
	{
		value = b;
		return value += Multiply(a - 1, b);
	}
}

void Verify(const std::int64_t& realResult, const std::int64_t algoResult)
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

void RunTestcases()
{
	std::cout << "Test case 1" << std::endl;

	std::cout << "Test case 2" << std::endl;

}

void subDivide(int64_t& a, int64_t& b, int64_t& c, int64_t& d, std::string& first, std::string& second)
{
	a = std::stoll(first.substr(0, first.size() / 2));
	b = std::stoll(first.substr(first.size() / 2));
	c = std::stoll(second.substr(0, second.size() / 2));
	d = std::stoll(second.substr(second.size() / 2));
}

int64_t KarastubaMultiplication(std::string& first, std::string& second)
{
	if (first.size() == 1 && second.size() == 1)
	{
		return std::stoll(first) * std::stoll(second);
	}
	else
	{
		int64_t a, b, c, d;
		unsigned int n = 0;
		subDivide(a, b, c, d, first, second);
		int64_t ac = Multiply(a,c);
		int64_t bd = Multiply(b,d);	
		int64_t somme = Multiply(a,d) + Multiply(b,c);


		if (first.size() > second.size())
		{
			n = first.size();
		}
		else
		{
			n = second.size();
		}

		return (int64_t)((pow(10,n) * ac) + ( pow(10,n/2) * somme)+ bd);
	}
}


int main()
{
	std::string a, b;
	int64_t number_1, number_2, realResult, algoResult;
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