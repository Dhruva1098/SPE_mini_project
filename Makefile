# Compiler
CXX = g++

# Compiler Flags
CXXFLAGS = -Wall -Wextra -std=c++17 -I/usr/include

#google test libraries
GTEST_LIBS = -lgtest -lgtest_main -pthread
# Directories
HEADER_DIR = headers

# Source and Object files
SRC = main.cpp
TEST_SRC = test_calc.cpp
OBJ = obj/main.o

# Output executable
TARGET = calculator_cli
TEST_TARGET = test_calc
# Default target
all: $(TARGET)

# Ensure obj directory exists
$(OBJ_DIR):
	mkdir -p obj

# Compile main.cpp into an object file
$(OBJ): $(SRC) | $(OBJ_DIR)
	$(CXX) $(CXXFLAGS) -I$(HEADER_DIR) -c $(SRC) -o $(OBJ)

# Link to create the final executable
$(TARGET): $(OBJ)
	$(CXX) $(CXXFLAGS) $(OBJ) -o $(TARGET)
	@echo "Build complete. Run './$(TARGET)' to start the CLI calculator."

$(TEST_TARGET) : $(SRC) $(TEST_SRC)
	$(CXX) $(CXXFLAGS) -o $(TEST_TARGET) $(SRC) $(TEST_SRC) $(GTEST_LIBS)
# Clean build files

test: $(TEST_TARGET)
	./$(TEST_TARGET)
clean:
	rm -rf $(TARGET)
	@echo "Cleanup complete."

.PHONY: all clean