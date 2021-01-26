class BeerSong {
  List<String> recite(int initialBottlesCount, int cntIterations) {
    List<String> result = [];
    var cntBottles = initialBottlesCount;
    for (int i = 0; i < cntIterations; i++) {
      if (result.length > 0) result.add('');
      result.addAll(_iteration(cntBottles));
      cntBottles = _getNextBottlesCount(cntBottles);
    }
    return result;
  }

  String _capitalize(String str) {
    if (str.length == 0) return str;
    return '${str[0].toUpperCase()}${str.substring(1)}';
  }

  String _firstSentence(int cntBottles) {
    var cntBottlesAsStr = _stringifyBottlesCount(cntBottles);
    return '${_capitalize(cntBottlesAsStr)} on the wall, $cntBottlesAsStr.';
  }

  int _getNextBottlesCount(int cntBottles) {
    var next = cntBottles - 1;
    return next >= 0 ? next : 99;
  }

  List<String> _iteration(int cntBottles) {
    return <String>[_firstSentence(cntBottles), _secondSentence(cntBottles)];
  }

  String _secondSentence(int cntBottles) {
    return '${_secondSentenceFirstPart(cntBottles)}, ${_secondSentenceSecondPart(cntBottles)}';
  }

  String _secondSentenceFirstPart(int cntBottles) {
    if (cntBottles == 0) return 'Go to the store and buy some more';
    return 'Take ${cntBottles == 1 ? "it" : "one"} down and pass it around';
  }

  String _secondSentenceSecondPart(int cntBottles) {
    return '${_stringifyBottlesCount(_getNextBottlesCount(cntBottles))} on the wall.';
  }

  String _stringifyBottlesCount(int cntBottles) {
    switch (cntBottles) {
      case 0:
        return "no more bottles of beer";
      case 1:
        return "1 bottle of beer";
      default:
        return "$cntBottles bottles of beer";
    }
  }
}
