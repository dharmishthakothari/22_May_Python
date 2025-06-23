#include<stdio.h>
int main()
{
	
	//array Declaration
	int arrRollno[10];
	//Initilization
	arrRollno[0]=101;
	arrRollno[1]=102;
	arrRollno[2]=103;
	arrRollno[3]=104;
	int i,sum;
	for(i=0;i<5;i++)
	{
		//accessing value
		sum=sum+arrRollno[i];
		printf("\n%d",arrRollno[i]);	
	}
	printf("\nSum=%d",sum);	
}
