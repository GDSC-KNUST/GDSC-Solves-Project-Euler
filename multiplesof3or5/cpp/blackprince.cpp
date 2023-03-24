// Author: @blackprince001

#include <iostream>
#include <vector>

std::vector<int> multiples_of_3and5(int nth) {
    std::vector<int> mul_collection;
    for (int i = 11; i <= nth; ++i)
        // check if number is divisible by 3 or 5 using ternary operations
        mul_collection.push_back((i % 3 == 0 || i % 5 == 0) ? i : 0);
    return mul_collection;
}

int main() {
    // initialize the `sum` and `limit` variables
    int sum = 0;
    int limit = 1000;

    // generate the list of multiples of 3 and 5 and store in `list`
    auto list = multiples_of_3and5(limit);

    // iterate over `list` and add those values to the cumulative `sum`
    for (auto &val : list) sum += val;

    // print the sum
    std::cout << "Sum of values is " << sum;

    return 0;
}