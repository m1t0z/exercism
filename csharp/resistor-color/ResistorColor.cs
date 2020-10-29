using System;
using System.Collections.ObjectModel;

public static class ResistorColor
{
    private static readonly string[] _colors =
      new [] { "black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white" };

    private static readonly ReadOnlyCollection<string> _readOnlyColors =
      new ReadOnlyCollection<string>(_colors);

    public static int ColorCode(string color) => Array.IndexOf(_colors, color);

    public static ReadOnlyCollection<string> Colors() => _readOnlyColors;
}
