#ifndef OPERATIONS_H
#define OPERATIONS_H

#include <cmath>
#include <iostream>

template <typename T>
double sq_root(T a) {
  return sqrt(static_cast<double>(a));
}

template <typename T>
auto factorial(T a) {
  int temp = static_cast<int>(a);
  if (temp == a && temp >= 0) {
    int out = 1;
    if (temp == 0) { return 1;}
    while(temp){
      out *=temp--;
    } return out;
  } else {
    std::cerr << "Can only perform factorial for positive integers" << std::endl;
  }
}

template <typename T>
auto log(T a) {
  return std::log(a);
}

template <typename T>
auto power(T a, T b) {
  return std::pow(a, b);
}

inline void check(bool& temp, int a) {
  if (a == 1) {temp = true;}
  else {temp = false;}
}

#endif //OPERATIONS_H
