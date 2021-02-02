import 'dart:math';

class DifferenceOfSquares {
  int squareOfSum(int n) {
    var sum = Iterable<int>.generate(n, (x) => x + 1)
        .reduce((value, element) => value + element);
    return pow(sum, 2) as int;
  }

  int sumOfSquares(int n) {
    return Iterable<int>.generate(n, (x) => x + 1)
        .map((x) => pow(x, 2) as int)
        .reduce((value, element) => value + element);
  }

  int differenceOfSquares(int n) {
    return squareOfSum(n) - sumOfSquares(n);
  }
}
