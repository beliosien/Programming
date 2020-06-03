//#include <algorithm>
//#include <bits/stdc++.h>
//#include <cstdio>
//#include <vector>
//
//using namespace std;
//
//// Complete the repeatedString function below.
//
//bool compare(char a, char b)
//{
//	return a < b;
//}
//long repeatedString(string s, long n) {
//	long long value = 0;
//
//	for (int i = 0; i < s.size(); i++)
//	{
//		if (s[i] == 'a')
//		{
//			value++;
//		}
//	}
//
//	value *= n / s.size();
//
//	for (int i = 0; i < n % s.size(); i++)
//	{
//		if (s[i] == 'a')
//		{
//			value++;
//		}
//	}
//
//	return value;
//}
//
//int main()
//{
//	ofstream fout(getenv("OUTPUT_PATH"));
//
//	string s;
//	getline(cin, s);
//
//	long n;
//	cin >> n;
//	cin.ignore(numeric_limits<streamsize>::max(), '\n');
//
//	long result = repeatedString(s, n);
//
//	fout << result << "\n";
//
//	fout.close();
//	return 0;
//}