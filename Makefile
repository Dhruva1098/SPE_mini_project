# Compiler
CXX = g++

# Compiler Flags
CXXFLAGS = -Wall -Wextra -std=c++17

# Directories
HEADER_DIR = headers

# Source and Object files
SRC = main.cpp
OBJ = obj/main.o

# Output executable
TARGET = calculator_cli

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

# Clean build files
clean:
	rm -rf $(TARGET)
	@echo "Cleanup complete."

.PHONY: all clean