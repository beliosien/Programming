#include <vector>
#include <iostream>
#include <string>
#include <fstream>

using namespace std;

/**
	Author: Ossim Belias
*/

void printVector(vector<int> vec)
{
	for (auto it = vec.begin(); it != vec.end(); it++)
	{
		cout << *it << " ";
	}
}


vector<int> rotLeft(vector<int> a, int d) {
	vector<int> resutls(a.size());
	int limit = a.size() - d; // the number of rotations before returning to initial state

	for (int j = 0; j < a.size(); j++)
	{
		int pos = j + limit;
		if (pos > a.size() - 1)
		{
			pos = pos - a.size();
		}
		resutls[pos] = a[j];

	}

	return resutls;
}

void TestCases(string testCase)
{
	fstream fs;
	fs.open(testCase);

	int n = 0;
	int d = 0;
	fs >> n;
	fs >> d;

	vector<int> a(n);
	vector<int> actualResult(n);
	if (fs.is_open())
	{
		for (int i = 0; i < n; i++) {
			fs >> a[i];
		}

		for (int i = 0; i < n; i++)
		{
			fs >> actualResult[i];
		}
	}
	else
	{
		cout << "Erreur lors de l'ouverture du fichier" << endl;
	}

	cout << "Size of the array " << n << endl;
	cout << "Number of rotation we want to do " << d << endl;
	printVector(a);

	vector<int> result = rotLeft(a, d);
	cout << endl;

	for (int i = 0; i < n; i++)
	{
		if (actualResult[i] != result[i])
		{
			cout << "FAILED !! Expected: " << actualResult[i] << " but got " << result[i] << endl;
			break;
		}
		else if (i == n - 1 && actualResult[i] == result[i])
		{
			cout << "PASSED !! Expected: ";
			printVector(actualResult);
			cout << " got ";
			printVector(result);
			cout << endl;
		}
	}
	fs.close();

}

int main()
{
	cout << "A left rotation operation on an array shifts each of the array's elements 1 unit to the left. For example, if 2 left rotations are ";
	cout << "performed on array [1,2,3,4,5], then the array would become [3,4,5,1,2]." << endl;
	cout << endl;
	
	cout << "---------------------------------" << endl;
	cout << "Left Rotation Test case" << endl;
	cout << "---------------------------------" << endl;

	cout << "Test case 1" << endl;
	TestCases("LeftRotationTest1.txt");
	cout << endl;

	cout << "Test case 2" << endl;
	TestCases("LeftRotationTest2.txt");
	cout << endl;

	cout << "Test case 3" << endl;
	TestCases("LeftRotationTest3.txt");
	cout << endl;
	
	return 0;
}
