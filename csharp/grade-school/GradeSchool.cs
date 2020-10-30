using System.Collections.Generic;
using System.Linq;

public class GradeSchool
{
    private class Item
    {
      public string Student;
      public int Grade;
    };

    private readonly List<Item> _items = new List<Item>();

    public void Add(string student, int grade)
    {
      _items.Add(new Item
          {
            Student = student,
            Grade = grade
          }
      );
    }

    public IEnumerable<string> Roster()
    {
      return _items
        .OrderBy(i => i.Grade)
        .ThenBy(i => i.Student)
        .Select(i => i.Student);
    }

    public IEnumerable<string> Grade(int grade)
    {
        return _items
          .Where(i => i.Grade == grade)
          .OrderBy(i => i.Student)
          .Select(i => i.Student);
    }
}
