

// Consider the fraction, n/d, where n and d are positive integers.
// If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

// If we list the set of reduced proper fractions for d ≤ 8 in
// ascending order of size, we get:

// 1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

// It can be seen that there are 3 fractions between 1/3 and 1/2.
// It can be seen that there are 15 fractions between 1/7 and 4/5.

// 1/8, 1/7, --- 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, --- 4/5, 5/6, 6/7, 7/8

// How many fractions lie between 1/3 and 1/2 in the sorted set of
// reduced proper fractions for d ≤ 12,000?

#include <iostream>
#include <math.h>
#include <algorithm>

#include <set>

void compute_divisors(int num, std::set<int> &disregard)
{
    auto limit = sqrt(num);
    for (int i = 2; i < limit; i++)
    {
        if (num % i == 0)
        {
            disregard.insert(i);
            disregard.insert(num / i);
        }
    }
}

int main()
{

    int max_denominator = 12000;
    std::set<int> disregard;

    std::set<double> computed_ratios;
    std::set<double> computed_divisors;

    double lower_bound = (1.0 / 3) + 0.000001;
    double upper_bound = 1.0 / 2;

    // double lower_bound = (1.0 / 7) + 0.000001;
    // double upper_bound = 4.0 / 5;


    uint64_t count = 0;
    for (float numerator = 1; numerator < max_denominator; numerator++)
    {
        for (float denominator = std::max(max_denominator, (int)numerator); denominator >= 1; denominator--)
        {
            if (disregard.find(denominator) != disregard.end())
            {
                // std::cout << "skipping because disregard: " << numerator << "/" << denominator << std::endl;
                continue;
            }

            if (computed_divisors.find(denominator) == computed_divisors.end())
            {
                compute_divisors(denominator, disregard);
                computed_divisors.insert(denominator);
            }

            auto rat = numerator / denominator;

            if (computed_ratios.find(rat) != computed_ratios.end()){

                // std::cout << "skipping because computed ratio: " << numerator << "/" << denominator << std::endl;

                continue;
            }

            computed_ratios.insert(rat);

            if (rat > upper_bound)
            {
                // std::cout << "continuing because rat > upper_bound: " << numerator << "/" << denominator << std::endl;
                break;
            }

            if (rat > lower_bound && rat < upper_bound)
            {
                count++;
                // std::cout << numerator << "/" << denominator << std::endl;
            }
        }
    }

    std::cout << count << std::endl;
}