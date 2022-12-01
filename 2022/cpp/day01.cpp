#include <fstream>
#include <functional>
#include <iostream>
#include <queue>
#include <string>
#include <vector>

int part1() {
  std::ifstream inputFile("input.txt");
  int max = 0, sum = 0;
  if (inputFile.is_open()) {
    std::string line;

    while (std::getline(inputFile, line)) {
      if (line == "") {
        if (sum > max) {
          max = sum;
        }
        sum = 0;
        continue;
      }

      sum += std::stoi(line);
    }
  }

  inputFile.close();

  return max;
}

int part2() {
  std::ifstream inputFile("input.txt");

  std::priority_queue<int, std::vector<int>, std::greater<int>> elves;

  std::string line;

  int sum = 0;
  if (inputFile.is_open()) {
    while (std::getline(inputFile, line)) {
      if (line == "") {
        if (sum > elves.top()) {
          if (elves.size() == 3) {
            elves.pop();
          }
          elves.push(sum);
        }
        sum = 0;
        continue;
      }

      sum += std::stoi(line);
    }
  }

  inputFile.close();

  int bigSum = 0;

  for (int i = 1; i <= 3; ++i) {
    bigSum += elves.top();
    elves.pop();
  }

  return bigSum;
}

int main() {
  std::cout << part1();

  std::cout << part2();

  return 0;
}
