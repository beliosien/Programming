//#include <bits/stdc++.h>
//#include <iostream>
//
//using namespace std;
//
//// Complete the countingValleys function below.
//int countingValleys(int n, string s) {
//	int valleysNumber = 0;
//	int downNumber = 0; // level of the sea
//	int upNumber = 0;  // level of the sea
//
//	for (int i = 0; i < n; i++) {
//
//		if (s[i] == 'D')
//		{
//			downNumber++;
//			upNumber--;
//		}
//		else {
//			upNumber++;
//			downNumber--;
//			if (upNumber == downNumber)
//			{
//				valleysNumber++;
//			}
//		}
//
//	}
//
//	return valleysNumber;
//}
//
//int main()
//{
//	ofstream fout(getenv("OUTPUT_PATH"));
//
//	int n;
//	cin >> n;
//	cin.ignore(numeric_limits<streamsize>::max(), '\n');
//
//	string s;
//	getline(cin, s);
//
//	int result = countingValleys(n, s);
//
//	fout << result << "\n";
//
//	fout.close();
//
//	return 0;
//}
