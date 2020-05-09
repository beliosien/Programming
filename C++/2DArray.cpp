#include <algorithm>
#include <bits/stdc++.h>

using namespace std;

// Complete the hourglassSum function below.
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

int main()
{
	ofstream fout(getenv("OUTPUT_PATH"));

	vector<vector<int>> arr(6);
	for (int i = 0; i < 6; i++) {
		arr[i].resize(6);

		for (int j = 0; j < 6; j++) {
			cin >> arr[i][j];
		}

		cin.ignore(numeric_limits<streamsize>::max(), '\n');
	}

	int result = hourglassSum(arr);

	fout << result << "\n";

	fout.close();

	return 0;
}