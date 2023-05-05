#include <iostream>

long fibonacci(long nth) {
    long prev = 0, next, current = 1, i = 2;
    while (i <= nth) {
        next = prev + current;
        prev = current;
        current = next;
        i++;
    }
    return current;
}

int main() {
    long even_fib_sum = 0;
    int limit = 50;
    long current_fib_number = 0;

    for (int i = 0; i < limit; ++i) {
        current_fib_number = fibonacci(
            i); // you can memoize and make computation easier with lookups
        if (current_fib_number % 2 == 0)
            even_fib_sum += current_fib_number;
    }

    std::cout << "sum: " << even_fib_sum;
    return 0;
}