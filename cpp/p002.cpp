#include <iostream>
#include <vector>

int solution() {
    std::vector<int> fibs {1,1};
    long sum = 0;

    while (fibs.back() < 4000000){
        size_t size = fibs.size();
        long elem = fibs.at(size - 1) + fibs.at(size - 2);
        fibs.push_back(elem);
        if (elem % 2 == 0){
            sum += elem;
        }

    }
    return sum;
}

int main() {
    std::cout << solution() << std::endl;
}