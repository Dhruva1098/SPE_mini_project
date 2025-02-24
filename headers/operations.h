#ifndef OPERATIONS_H
#define OPERATIONS_H

#include <cmath>
#include <iostream>

template <typename T>
double sq_root(T a) {
  return sqrt(static_cast<double>(a));
}

inline unsigned long long factorial(int a) {
  int temp = a;
  if (temp == a && temp == 0) { return 1;}
  if (temp == a && temp > 0) {
    unsigned long long out = 1;
    while(temp){
      out *=temp--;
    } return out;
  }
  return -1;
}

template <typename T>
auto logarithm(T a) {
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
