/**
	@author Ossim Belias
	@brief Test of the implemtation of the doubly linkedlist
*/

#include <iostream>
#include <string>
#include "../src/LinkedList.cpp"


int main()
{
	std::cout << "TEST OF THE CONSTRUCTOR OF THE CLASS" << std::endl;
	LinkedList<int> linkedList = LinkedList<int>();
	if (linkedList.getHead() != nullptr && linkedList.getTail() != nullptr)
	{
		std::cout << "INITIALIZATION OF THE CLASS FAILED" << std::endl;
		exit(1);
	}
	else
	{
		std::cout << "INITIALIZATION OF THE CLASS PASSED" << std::endl;
	}

	return 0;

}