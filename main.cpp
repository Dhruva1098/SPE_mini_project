//
// Created by Dhruva Sharma on 24/2/25.
//
#include <iostream>
#include "headers/operations.h"

int main() {
  bool loop = true;
  while (loop) {
    std::cout << "Please select a function to perform:\n\t1. Square root\n\t2. Factorial\n\t3. Natural Log\n\t4. Power" << std::endl;
    int temp,temp2;
    auto num1 = 0;
    auto num2 = 0;
    std::cin >> temp;
    switch (temp) {
      case 1:
        std::cout << "Input a number to Square root of:";
        std::cin >> num1;
        std::cout << "Square root of " << num1 << " is: " << sq_root(num1) << "\n Would you like to continue?\n\t1.Yes\n\t2.No" << std::endl;

        std::cin >> temp2;
        check(loop, temp2);
      break;
      case 2:
        std::cout << "Input a number to calculate Factorial of:";
        std::cin >> num1;
        std::cout << "Factorial of " << num1 << " is: " << factorial(num1) << "\n Would you like to continue?\n\t1.Yes\n\t2.No" << std::endl;
        std::cin >> temp2;
        check(loop, temp2);
      break;
      default:
        std::cout << " Invalid Input" << std::endl;
    }
  }
}

