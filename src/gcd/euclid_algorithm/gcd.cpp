#include <iostream>
#include <assert.h>


int gcd(int x, int y) {
    if (y <= 0) return x;
    int divisor = x % y;
    return gcd(y, divisor);
}


int main(void) {
    assert(gcd(20, 30) == 10);
    assert(gcd(112, 42) == 14);
    return 0;
}
