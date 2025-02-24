# Compiler
CXX = g++

# Compiler Flags
CXXFLAGS = -Wall -Wextra -std=c++17

# Directories
OBJ_DIR = obj
HEADER_DIR = headers

# Source and Object files
SRCS = main.cpp operations.cpp
OBJS = $(OBJ_DIR)/main.o $(OBJ_DIR)/operations.o

# Output executable
TARGET = calculator_cli

# Default target
all: $(TARGET)

# Ensure obj directory exists
$(OBJ_DIR):
	mkdir -p $(OBJ_DIR)

# Compile source files into object files
$(OBJ_DIR)/%.o: %.cpp | $(OBJ_DIR)
	$(CXX) $(CXXFLAGS) -I$(HEADER_DIR) -c $< -o $@

# Link object files into final executable
$(TARGET): $(OBJS)
	$(CXX) $(CXXFLAGS) $(OBJS) -o $(TARGET)
	@echo "Build complete. Run './$(TARGET)' to start the CLI calculator."

# Clean build files
clean:
	rm -rf $(OBJ_DIR) $(TARGET)
	@echo "Cleanup complete."

.PHONY: all clean