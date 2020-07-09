#include <bits/stdc++.h>
#include <iostream>

using namespace std;

int countingValleys(int n, string s) {
	int valleysNumber = 0;
	int downNumber = 0; // level of the sea
	int upNumber = 0;  // level of the sea

	for (int i = 0; i < n; i++) {

		if (s[i] == 'D')
		{
			downNumber++;
			upNumber--;
		}
		else {
			upNumber++;
			downNumber--;
			if (upNumber == downNumber)
			{
				valleysNumber++;
			}
		}

	}
	return valleysNumber;
}

void TestCases(int stepNumber, string path, int expected)
{
    cout << path << endl;
    int result = countingValleys(stepNumber, path);

    if (result == expected)
    {
        cout << "PASSED!! Expected " << expected << " got " << result << endl;
    } else
    {
        cout << "FAILED!! Expected << " << expected << " but got " << result << endl; 
    }
    
}

int main()
{

    cout << "Test case 1" << endl;
    TestCases(8, "UDDDUDUU", 1);

    cout << endl;
    cout << "Test case 2" << endl;
    TestCases(12, "DDUUDDUDUUUD", 2);


	return 0;
}
