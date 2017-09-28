#include <bits/stdc++.h>
using namespace std;
int comb(int n , int r , int** a)
{
	if(a[n][r] != -1)
	{
		return a[n][r] ;
	}
	else
	{
		if( n == r || r == 0)
		{
			a[n][r] = 1 ; 
			return 1 ; 
		}
		if( r > n)
		{
			a[n][r] = 0 ; 
			return 0 ; 
		}
		else
		{

			int y = comb(n - 1,r  - 1 ,a) ;
			int x = comb(n - 1, r,a) ;  
			a[n][r] = x + y ; 
			return a[n][r] ; 
		}

	}
}
int main()
{
	int n , r; 
	cin >> n >> r; 
	int** a ;
	a = new int*[n+1] ;  
	for(int i = 0 ; i <= n ; i++)
	{   a[i] = new int[r + 1] ;
		for(int j = 0 ; j <= r ; j++)
		{
			a[i][j] = -1 ; 
		}

	}
	cout << comb(n,r ,a) << endl ; 

}