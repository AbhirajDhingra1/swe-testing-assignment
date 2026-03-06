# Testing Strategy for Quick-Calc

## What Was Tested
- All core calculator operations: addition, subtraction, multiplication, division.
- Edge cases: division by zero, negative numbers, decimal numbers, large numbers.
- Integration: user interaction sequences and clear/reset functionality.

## What Was Not Tested
- User interface (since this is a command-line app).
- Performance and non-functional aspects.

## Approach & Lecture Concepts

### 1. Testing Pyramid
The test suite reflects the pyramid by focusing mostly on unit tests (8+), with a smaller number of integration tests (2). This ensures a solid foundation of reliable, fast tests.

### 2. Black-box vs White-box Testing
Unit tests use white-box testing, directly verifying function outputs. Integration tests use black-box testing, simulating user actions and checking results.

### 3. Functional vs Non-Functional Testing
All tests are functional, verifying correctness of operations. Non-functional aspects (performance, usability) are not tested.

### 4. Regression Testing
The test suite can be used for regression testing by running it after any code changes to ensure no existing functionality is broken.

## Test Results Summary
| Test Name                  | Type         | Pass/Fail |
|---------------------------|--------------|-----------|
| test_addition             | Unit         | Pass      |
| test_subtraction          | Unit         | Pass      |
| test_multiplication       | Unit         | Pass      |
| test_division             | Unit         | Pass      |
| test_division_by_zero     | Unit         | Pass      |
| test_negative_numbers     | Unit         | Pass      |
| test_decimal_numbers      | Unit         | Pass      |
| test_large_numbers        | Unit         | Pass      |
| test_integration_add_and_clear | Integration | Pass      |
| test_integration_sequence | Integration  | Pass      |
