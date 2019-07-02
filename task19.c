#include<stdio.h>
#define MAX 1000


struct e{
    int v;
    char E[MAX];
  }.*node[100];



typedef struct if{
   char Ec[100];
   char Et;
   char Ef;
 }if_case;


struct v{
  int num;
  int result;
  char boolean;

}bool[2],*n[100];


struct prim{
char arr[100]="{'+','*','/','-','<=','<','=','>','>='};
}*p[100];



int main()
{

 char input;
  printf("Enter the operation to be performed from prmitive:");
  
  
  printf("The list of primitives are as follows:");
  for(int i=0;i<10;i++)
   {
     printf("%s\t", p.arr[i]);
   }
   
   scanf("%s",&input);
 
 switch(input):
    {
      case '+':
          n[3].result=n[1].num + n[2].num;
          break;
      case '-':
          n[3].result=n[1].num - n[2].num;
          break;
      case '*':
          n[3].result=n[1].num * n[2].num;
          break;
      case '/':
          n[3].result=n[1].num / n[2].num;
          break;
      case '<':
          n[3].result=n[1].num < n[2].num;
          break;
      case '>':
          n[3].result=n[1].num > n[2].num;
          break;
      case '=':
          n[3].result=n[1].num == n[2].num;
          break;
      case '<=':
          n[3].result=n[1].num <= n[2].num;
          break;
      case '>=':
          n[3].result=n[1].num >= n[2].num;
          break;
      
       }

printf("The result is: %s\n:" n.result");

return 0;
} 
  
