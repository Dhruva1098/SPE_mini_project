//
// Created by Dhruva Sharma on 24/2/25.
//

#include "headers/operations.h"
#include <gtest/gtest.h>

TEST(calculator, root) {
  EXPECT_EQ(sq_root(1), 1);
}
TEST(calculator, factorial) {
  EXPECT_EQ(factorial(0), 1);
  EXPECT_EQ(factorial(2), 2);
  EXPECT_EQ(factorial(3), 6);
}

TEST(calculator, power) {
  EXPECT_EQ(power(20,0), 1);
  EXPECT_EQ(power(20,1), 20);
  EXPECT_EQ(power(20,2), 400);
}

int main(int argc, char **argv) {
  ::testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}