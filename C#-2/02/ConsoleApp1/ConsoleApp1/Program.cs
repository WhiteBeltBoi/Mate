using System.Diagnostics;
using System.Reflection.Metadata.Ecma335;
using System.Security.Cryptography.X509Certificates;

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

class Class1{
    protected int n = 0;

    public int N 
    {         
        get { return n; }
        set { n = value; }
    }
    
    public virtual void A() {
        n = 10;
        
    }
}

class Class2 : Class1{
    public override void A() {
        n = 20;
       
    }
}

class Class3 : Class2{
    public override void A() {
        n = 30;
        
    }
}


class Program
{
    static void Main(string[] args)
    {
        //Viragcsokor v1 = new Viragcsokor("Tulipán", 11);
        //Viragcsokor v2 = new Viragcsokor("Rózsa", 5);
       
        //Console.WriteLine(v1 < v2);
        //Console.WriteLine(v1.ToString());
            
        Class1 c1 = new Class1();
        Class2 c2 = new Class2();
        Class3 c3 = new Class3();

        Console.WriteLine(c3.N);
        c3.A();
        Console.WriteLine(c3.N);

    }
}
