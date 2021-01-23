class ResistorColorDuo {
  final _colors = [
    'black',
    'brown',
    'red',
    'orange',
    'yellow',
    'green',
    'blue',
    'violet',
    'grey',
    'white',
  ];

  int value(List<String> colors) {
    return int.parse(colors
        .take(2)
        .map(_toNumber)
        .map((number) => number.toString())
        .join());
  }

  int _toNumber(String color) {
    var index = _colors.indexOf(color);
    if (index == -1) throw ArgumentError('Unsupported color $color!');
    return index;
  }
}
