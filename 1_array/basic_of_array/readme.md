# 在C++中数据的存储
## 单位
- 位（bit）：信息的基本单位，代表一个二进制数字（0或1）。
- 字节（byte）：计算机存储的基本单位。**1字节 = 8位**。
- 比特（bit）：通常与位相同，代表一个二进制数字。
## 不同数据类型存储大小
| 数据类型 | 大小（字节） | 描述 |
|----------|--------------|------|
| `char`   | 1            | 通常用于表示字符或8位整数 |
| `bool`   | 1            | 布尔值（通常是 `char` 的大小） |
| `signed char` | 1 | 有符号的 `char` |
| `unsigned char` | 1 | 无符号的 `char` |
| `short`  | 2            | 16位整数 |
| `unsigned short` | 2 | 无符号的 `short` |
| `int`    | 4            | 32位整数 |
| `unsigned int` | 4 | 无符号的 `int` |
| `long`   | 4或8         | 32位或64位整数，依赖于平台 |
| `unsigned long` | 4或8 | 无符号的 `long` |
| `long long` | 8          | 64位整数 |
| `unsigned long long` | 8 | 无符号的 `long long` |
| `float`  | 4            | 单精度浮点数 |
| `double` | 8            | 双精度浮点数 |
| `long double` | 8或16    | 扩展精度浮点数，依赖于平台 |
## int类型大小范围
直接如下声明：
```c++
int a = 2147483647; // 最大值
```
则a是一个有符号的32位整数，最高位要用于表达符号，剩下的31位用于表示数值，
因此a的取值范围是：**$-2^{31}$ ~ $2^{31} - 1$**，大概是**正负20亿**以内。

如果声明无符号int类型，则声明如下：
```c++
unsigned int b = 4294967295; // 最大值
```
则b是一个无符号的32位整数，其取值范围是：**0 ~ $2^{32} - 1$**，大概是**0 ~ 40亿**。

## 二维数组存储的顺序
假如作如下实验：
```c++
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
```
输出结果为：
``` 
Address of arr[0][0]=0x61fdd0
Address of arr[0][1]=0x61fdd4
Address of arr[0][2]=0x61fdd8
Address of arr[1][0]=0x61fddc
Address of arr[1][1]=0x61fde0
Address of arr[1][2]=0x61fde4
Size of int=4
Size of long=4
```
可以看到，数组的存储顺序是按行优先的，
并且按行的顺序是连续的存储，每个地址之间隔了4 bytes的距离。
# 在python中数据的存储
python中的数据一般是动态存储，也就是说，在程序运行过程中，
变量所占用的内存空间是不固定的，这就意味着，python中的数据类型可以是任意的。
例如如下例子：
```python
import sys
an_int = 4242424
print(sys.getsizeof(an_int))
an_int = 4242424424242442424244242424
print(sys.getsizeof(an_int))
a_float = 3.1442424242
print(sys.getsizeof(a_float))
```
输出结果：
```
28
40
24
```
这足以看出数据的存储大小在随着数据大小的增加而增加。
关于python中二维数组的存储，它的地址也是连续的，只要用如下实验：
```python
list_example = [[1,2,3],[1,2,3]]
for row in list_example:
    for element in row:
        print(id(element))
```
输出结果为：
```
3043014344944
3043014344976
3043014345008
3043014344944
3043014344976
3043014345008
```
可以看到，数组的存储顺序是按行优先的，
并且按行的顺序是连续的存储，每个地址之间隔了32bytes的距离。