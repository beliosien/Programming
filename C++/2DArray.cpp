#include <algorithm>
#include <vector>
#include <iostream>
#include <fstream>

/**
	Author: Ossim Belias 
*/
using namespace std;

const int max_size = 6;
const int filter_size = 3;
int filterMatrix(int x, int y, int mat[6][6])
{
	int value = 0;
	int pos_x = 0;
	int pos_y = 0;
	int filter[filter_size][filter_size] = { {1,1,1},
						{0,1,0},
						{1,1,1} };

	for (int i = 0; i < filter_size; i++)
	{
		for (int j = 0; j < filter_size; j++)
		{
			if (x + pos_x >= 0 && x + pos_x < max_size &&
				y + pos_y >= 0 && y + pos_y < max_size)
			{
				value += filter[i][j] * mat[x + pos_x][y + pos_y];
			}
			if (pos_y == filter_size - 1)
			{
				pos_y = 0;
			}
			else {
				pos_y++;
			}
		}
		if (pos_x == filter_size - 1)
		{
			pos_x = 0;
		}
		else {
			pos_x++;
		}
	}
	return value;
}

int hourglassSum(vector<vector<int>> arr) {
	int max = -99;
	int matrice[max_size][max_size];

	// on rempli la matrice avec les vecteurs
	for (int i = 0; i < arr.size(); i++)
	{
		for (int j = 0; j < arr.size(); j++)
		{
			matrice[i][j] = arr[i][j];
		}
	}

	// on filtre des  matrices de 3x3
	for (int i = 0; i < arr.size() / 2 + 1; i++)
	{
		for (int j = 0; j < arr.size() - 1; j++)
		{
			int value = filterMatrix(i, j, matrice);
			if (value >= max)
			{
				max = value;
			}
		}
	}

	return max;
}


void TestCases(string testCase)
{
	fstream fs;
	fs.open(testCase);
	int actualResult;
	vector<vector<int>> arr(6);
	for (int i = 0; i < 6; i++) {
		arr[i].resize(6);

		if (fs.is_open())
		{
			for (int j = 0; j < 6; j++)
			{
				fs >> arr[i][j];
				cout << arr[i][j] << " ";
			}
			cout << endl;
		}
		else
		{
			cout << "Erreur lors de l'ouverture du fichier" << endl;
			return;
		}
	}
	fs >> actualResult;
	fs.close();
	int result = hourglassSum(arr);

	if (result == actualResult)
	{
		cout << "PASSED!! Got: " << result << " Expected: " << actualResult << endl;
	}
	else {
		cout << "FAILED!!!Expected: " << actualResult << " but got " << result << endl;
	}

}
int main()
{
	cout << "Given an 6X6 array we define an hourglass in A to be a subset of values with indices falling in this pattern in array graphical representation: " << endl;
	cout << "a b c" << endl;
	cout << "  d  " << endl;
	cout << "e f g" << endl;
	cout << "There are 16 hourglasses in the given array, and an hourglass sum is the sum of an hourglass values. Calculate the hourglass sum for every hourglass in the array, then print the maximum hourglass sum." << endl;
	cout << endl;
	cout << "--------------------------------------------" << endl;
	cout << "HourglassSum Test cases" << endl;
	cout << "--------------------------------------------" << endl;

	cout << "Test case 1" << endl;
	TestCases("2DArrayTest1.txt");
	cout << endl;

	cout << "Test case 2" << endl;
	TestCases("2DArrayTest2.txt");
	cout << endl;

	cout << "Test case 3" << endl;
	TestCases("2DArrayTest3.txt");
	cout << endl;
	
	return 0;
}