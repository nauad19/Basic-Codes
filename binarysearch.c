#include<stdio.h>
int main(){
    int arr[100];
    int a, b;
    printf("enter the size of the array");
    scanf("%d",&a);
    printf("enter the elements");
    for(int i=0; i<a;i++){
        scanf("%d", &arr[i]);

    }
    printf("enter the number to find")
    scanf("%d", &b);
    for(int i=0; i=a/2; i++){
        if(arr[i]==b){
            printf("number is found");
        }
    printf("number not found in upper half");
    }
    for(int i=a; i>a/2; i--){
        if(arr[i]==b){
            printf("number is found");
        }
    }
    printf("enter a valid number");
return 0;
}