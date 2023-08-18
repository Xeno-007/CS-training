#include <stdio.h>
int findSmallestMissing(int nums[], int n)
{
// create an auxiliary array of size `n+1` to mark all positive elements
    int aux[n + 1];
    for (int i = 0; i < n + 1; i++) {
        aux[i] = 0;
    }
 
    // iterate over the array and mark all positive elements in range `[1, n]`
    for (int i = 0; i < n; i++)
    {
        // ignore all non-positive elements and elements greater than `n`
        if (nums[i] > 0 && nums[i] <= n) {
            aux[nums[i]] = 1;
        }
    }
 
    // check for the smallest missing number between 1 and `n`
    for (int i = 1; i <= n; i++)
    {
        if (!aux[i]) {
            return i;
        }
    }
 
    // If numbers from 1 to `n` are present in the array,
    // then the missing number is `n+1`
    return n + 1;
}
 
int main()
{
    int nums[] = { 1, 4, 2, -1, 6, 5 };
    int n = sizeof(nums) / sizeof(nums[0]);
 
    printf("The smallest positive missing number is %d", findSmallestMissing(nums, n));
 
    return 0;
}