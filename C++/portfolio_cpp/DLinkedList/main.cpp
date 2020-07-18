#include "DLinkedList.cpp"
#include <iostream>


int main()
{
	std::cout << "TESTS OF THE CLASS: " << std::endl;
	DLinkedList<std::string> dlinkedList = DLinkedList<std::string>();
	if (dlinkedList.getHead() != nullptr && dlinkedList.getTail() != nullptr)
	{
		std::cout << "TEST#1 FAILED." << std::endl;
		exit(1);
	}
	else
	{
		std::cout << "TEST#1 PASSED." << std::endl;
	}
	dlinkedList.addFirst("1");
	dlinkedList.addFirst("2");
	dlinkedList.addFirst("3");

	std::string result = "";
	Node<std::string>* node = dlinkedList.getHead();
	while (node != nullptr)
	{
		result += node->getItem();
		node = node->getPrev();
	}
	
	if (result != "321")
	{
		std::cout << "TEST#2 FAILED." << std::endl;
		exit(1);
	}
	else
	{
		std::cout << "TEST#2 PASSED." << std::endl;
	}

	dlinkedList.removeFirst();
	result = "";
	node = dlinkedList.getHead();
	while (node != nullptr)
	{
		result += node->getItem();
		node = node->getPrev();
	}

	if (result != "21")
	{
		std::cout << "TEST#3 FAILED." << std::endl;
		exit(1);
	}
	else
	{
		std::cout << "TEST#3 PASSED." << std::endl;
	}

	DLinkedList < std:: string > dl;
	dl.addLast("1");
	dl.addLast("2");
	dl.addLast("3");
	dl.addLast("4");
	dl.addLast("5");
	result = "";
	node = dl.getTail();
	while (node != nullptr)
	{
		result += node->getItem();
		node = node->getNext();
	}
	if (result != "54321")
	{
		std::cout << "TEST#4 FAILED." << std::endl;
		exit(1);
	}
	else
	{
		std::cout << "TEST#4 PASSED." << std::endl;
	}

	result = "";
	node = dl.getHead();
	while (node != nullptr)
	{
		result += node->getItem();
		node = node->getPrev();
	}
	if (result != "12345")
	{
		std::cout << "TEST#5 FAILED." << std::endl;
		exit(1);
	}
	else
	{
		std::cout << "TEST#5 PASSED." << std::endl;
	}

	std::string firstVal = dl.removeFirst();
	if (firstVal != "1")
	{
		std::cout << "TEST#6 FAILED." << std::endl;
		exit(1);
	}
	else
	{
		std::cout << "TEST#6 PASSED." << std::endl;
	}

	std::string lastVal = dl.removeLast();
	if (lastVal != "5")
	{
		std::cout << "TEST#7 FAILED." << std::endl;
		exit(1);
	}
	else
	{
		std::cout << "TEST#7 PASSED." << std::endl;
	}

	result = "";
	node = dl.getHead();
	while (node != nullptr)
	{
		result += node->getItem();
		node = node->getPrev();
	}
	if (result != "234")
	{
		std::cout << "TEST#8 FAILED." << std::endl;
		exit(1);
	}
	else
	{
		std::cout << "TEST#8 PASSED." << std::endl;
	}

	dl.clear();
	if (!dl.isEmpty())
	{
		std::cout << "TEST#9 FAILED." << std::endl;
		exit(1);
	}
	else
	{
		std::cout << "TEST#9 PASSED." << std::endl;
	}

	dl.addFirst("1");
	dl.addLast("2");
	dl.addLast("3");
	dl.remove("2");

	result = "";
	node = dl.getHead();
	while (node != nullptr)
	{
		result += node->getItem();
		node = node->getPrev();
	}
	if (result != "13")
	{
		std::cout << "TEST#10 FAILED." << std::endl;
		exit(1);
	}
	else
	{
		std::cout << "TEST#10 PASSED." << std::endl;
	}
	if (dl.size() != 2)
	{
		std::cout << "TEST#11 FAILED" << std::endl;
		exit(1);
	}
	else
	{
		std::cout << "TEST#11 PASSED." << std::endl;
	}
	
	return 0;
}