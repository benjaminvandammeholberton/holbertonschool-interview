#include "palindrome.h"

int is_palindrome(unsigned long n)
{
    unsigned long reversed = 0, original = n;
    int remainder;

    while (original != 0)
    {
        remainder = original % 10;
        reversed = reversed * 10 + remainder;
        original = original / 10;
    }
    if (reversed == n)
        return 1;
    return 0;
}
