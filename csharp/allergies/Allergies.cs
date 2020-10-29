using System;
using System.Linq;

public enum Allergen
{
    Eggs          = 1 << 0,
    Peanuts       = 1 << 1,
    Shellfish     = 1 << 2,
    Strawberries  = 1 << 3,
    Tomatoes      = 1 << 4,
    Chocolate     = 1 << 5,
    Pollen        = 1 << 6,
    Cats          = 1 << 7
}

public class Allergies
{
    private int _mask;

    public Allergies(int mask) => _mask = mask;

    public bool IsAllergicTo(Allergen allergen)
    {
      return (_mask & (int)allergen) != 0;
    }

    public Allergen[] List()
    {
      return Enum
        .GetValues(typeof(Allergen))
        .Cast<Allergen>()
        .Where(a => IsAllergicTo(a))
        .ToArray();
    }
}
