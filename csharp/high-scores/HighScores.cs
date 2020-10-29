using System.Collections.Generic;
using System.Linq;


public class HighScores
{
    private readonly List<int> _scores;

    public HighScores(List<int> list) => _scores = list;

    public List<int> Scores() => _scores;

    public int Latest() => _scores.Last();

    public int PersonalBest() => _scores.OrderByDescending(score => score).First();

    public List<int> PersonalTopThree() => _scores.OrderByDescending(score => score).Take(3).ToList();
}
