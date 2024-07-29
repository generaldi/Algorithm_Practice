#include<iostream>
using namespace std;
void test_address(){
  int arr[2][3]={
    {123,234,345},
    {456,567,678}
  };
  for (int i =0;i<2;i++){
    for (int j=0;j<3;j++){
      cout<<"Address of arr["<<i<<"]"<<"["<<j<<"]="<<&arr[i][j]<<endl;
    }
  }
  cout<<"Size of int="<<sizeof(int)<<endl;
  cout<<"Size of long="<<sizeof(long)<<endl;
}
int main(){
  test_address();
}