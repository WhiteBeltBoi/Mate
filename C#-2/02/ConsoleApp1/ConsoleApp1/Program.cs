using System.Diagnostics;

class Viragcsokor
{
    private string nev { get; set; }
    private int szal { get; set; }
    public Viragcsokor(string nev, int szal)
    {
        this.nev = nev;
        this.szal = szal;
    }

    public override string ToString()
    {
        return $" Csokor neve: {this.nev},  {this.szal} szál";
    }

    public static bool operator >(Viragcsokor v1, Viragcsokor v2)
    {
        return v1.szal > v2.szal;
    }

    public static bool operator <(Viragcsokor v1, Viragcsokor v2)
    {
        return v1.szal < v2.szal;
    }

    public static bool operator ==(Viragcsokor v1, Viragcsokor v2)
    {
        return v1.szal == v2.szal;
    }

    public static bool operator !=(Viragcsokor v1, Viragcsokor v2)
    {
        return v1.szal != v2.szal;
    }

    public static implicit operator int(Viragcsokor v)
    {
        return v.szal;
    }

    public static explicit operator double(Viragcsokor v)
    {
        return v.szal;
    }
}

class Program
{
    static void Main(string[] args)
    {
        Viragcsokor v1 = new Viragcsokor("Tulipán", 11);
        Viragcsokor v2 = new Viragcsokor("Rózsa", 5);
       
        Console.WriteLine(v1 < v2);
        Console.WriteLine(v1.ToString());
            
    }
}
