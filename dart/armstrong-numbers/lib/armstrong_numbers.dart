import 'dart:math';

class ArmstrongNumbers {
  bool isArmstrongNumber(int number) {
    final digits = _toDigits(number);
    final sum = digits.fold<int>(
        0, (prev, element) => prev + pow(element, digits.length) as int);
    return number == sum;
  }

  List<int> _toDigits(int number) {
    List<int> digits = [];
    int n = number;
    while (n != 0) {
      var digit = n % 10;
      digits.add(digit);
      n = n ~/ 10;
    }
    return digits;
  }
}
