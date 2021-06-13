#include <stdio.h>
#define size 4

  int arr[size];
  int top = - 1;

int stackfull()
 {
     if(top == size - 1)
     {
         return - 1;
     }
     return 0;
 }
 
void push(int val)
 {
     if(stackfull())
     {
         printf("Stack is full %d",val);
     }
     else
     {
         ++top;
         arr[top]=val;
         printf("Push the element into the stack %d \n",arr[top]);
     }
 }
 
int stackfull()
 {
     if(top == size - 1)
     {
         return - 1;
     }
     return 0;
 }
 
void traverse()
 {
     for(int i=0;i<top+1;i++)
     {
         printf("%d",arr[i]);
     }
     printf("\n");
 }
 
void pop(int val)
 {
     if(stackfull())
     {
         printf("Stack is Empty\n");
     }
     else
     {
         printf("pop out the element %d from the stack\n",arr[top]);
         top--;
     }
 }
 
int main() {
	push(1);
	push(2);
	push(3);
	push(4);
	traverse();
	pop();
	pop();
	pop();
	traverse();
	return 0;
}

