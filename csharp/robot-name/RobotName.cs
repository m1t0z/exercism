using System.Collections.Generic;
using System;

public class Robot
{
    private string _name = RobotNameFactory.GenerateUniqueName();
    public string Name => _name;
    public void Reset() => _name = RobotNameFactory.GenerateUniqueName();
}

public static class RobotNameFactory
{
    private static Random _rand = new Random();
    private static HashSet<string> _history = new HashSet<string>();

    public static string GenerateUniqueName()
    {
      var name = string.Empty;

      do
      {
        name = GenerateRandomName();
      }
      while(_history.Contains(name));

      _history.Add(name);

      return name;
    }

    private static char GenerateRandomLetter()
    {
      return (char)_rand.Next('A', 'Z'); 
    }

    private static string GenerateRandomName()
    {
      return $"{GenerateRandomLetter()}{GenerateRandomLetter()}{_rand.Next(1000):D3}";
    }
};
