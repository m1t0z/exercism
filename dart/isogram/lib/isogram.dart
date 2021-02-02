class Isogram {
  static const ALPHABET_SIZE = 26;
  static const ASCII_A = 65;
  static const ASCII_Z = 90;
  static const ASCII_a = 97;
  static const ASCII_z = 122;

  bool isIsogram(String str) {
    var hasLetter = List.filled(ALPHABET_SIZE, false);

    for (var codePoint in str.runes) {
      if (codePoint >= ASCII_A && codePoint <= ASCII_Z) {
        var index = codePoint - ASCII_A;
        assert(index < ALPHABET_SIZE);
        if (hasLetter[index]) return false;
        hasLetter[index] = true;
      } else if (codePoint >= ASCII_a && codePoint <= ASCII_z) {
        var index = codePoint - ASCII_a;
        assert(index < ALPHABET_SIZE);
        if (hasLetter[index]) return false;
        hasLetter[index] = true;
      }
    }
    return true;
  }
}
