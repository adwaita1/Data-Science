#include <iostream>
#include <string>
using namespace std;
#define size 11
int main()
{
	int item[size],tx,temp,suppCnt,taken[size],taken1[size];
	cout<<"Enter the number of transactions ";
	cin>>tx;
	int itemTx[tx][size];
	for(int i=0;i<size;i++)
		for(int j=0;j<tx;j++)
		{
			item[i]=taken[i]=taken1[i]=itemTx[j][i]=0;;
		}
	cout<<"Enter the transactions\n";
	for(int i=0;i<tx;i++)
	{
		cout<<"Enter for transaction "<<i+1<<"\n";
		cout<<"1.Mango 2.Onion 3.Apple 4.Corn 5.Eggs 6.Chocolate 7.Nuts 8.Keychain 9.Knife 10.Jar 11.Toothbrush\n";
		cout<<"Enter 0 when transaction is completed\n";
		do{
			cin>>temp;
			if(temp>0 &&temp<size+1)
			{
				itemTx[i][temp-1]=1;
				item[temp-1]++;
			}
		}while(temp>0 &&temp<size+1);
	}
	string str[]={"Mango","Onion","Apple","Corn","Eggs","Chocolate","Nuts","Keychain","Knife","Jar","Toothbrush"};
	cout<<"Item count is as follows: \n";
	for(int i=0;i<size;i++)
	{
		cout<<str[i]<<" : "<<item[i]<<endl;
	}
	cout<<"Enter the minimum Support count ";
	cin>>suppCnt;
	cout<<"Items satisfying minimum support count\n";
	for(int i=0;i<size;i++)
	{
		if(item[i]>=suppCnt)
		{
			cout<<str[i]<<" : "<<item[i]<<endl;
			taken[i]=1;
		}
	}
	cout<<"Two Item Set: "<<endl;
	int cnt;
	for(int j=0;j<size;j++)
	{
		for(int k=j+1;k<size;k++)
		{
			if(taken[j]==1 && taken[k]==1)
			{
				cnt=0;
				for(int i=0;i<tx;i++)
				{
					if(itemTx[i][k]!=0 && itemTx[i][j]!=0)
					{
						cnt++;
					}
				}
				if(cnt>=suppCnt)
				{
					taken1[j]=taken1[k]=1;
					cout<<str[j]<<" and "<<str[k]<<" : "<<cnt<<endl;
				}
			}
		}
	}
	cout<<"Three Item Set "<<endl;
	for(int j=0;j<size;j++)
	{
		for(int k=j+1;k<size;k++)
		{
			for(int l=k+1;l<size;l++)
			{
				if(taken1[j]==1&&taken1[k]==1&&taken1[l]==1)
				{
					cnt=0;
					for(int i=0;i<tx;i++)
					{
						if(itemTx[i][j]!=0 && itemTx[i][k]!=0 && itemTx[i][l]!=0)
						{
							cnt++;
						}
					}
					if(cnt>=suppCnt)
					{
						cout<<str[j]<<", "<<str[k]<<" and "<<str[l]<<" : "<<cnt<<endl;
					}
				}
			}
		}
	}
	return 0;
}
