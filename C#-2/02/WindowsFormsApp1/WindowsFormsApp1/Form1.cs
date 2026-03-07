using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApp1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            double osszeg = 0;
            double szorzat = 1;
            double atlag = 0;

            int n = 0;
            for (int i = 0; i < tbSzamok.Lines.GetLength(0); i++)
            {
                n = int.Parse(tbSzamok.Lines[i]);
                osszeg += n;
                szorzat *= n;
            }
            tbSzamok.Lines.GetLength(0);
            lbOsszeg.Text = $" {osszeg}";
            lbSzorzat.Text = $" {szorzat}";
            lbAtlag.Text = $" {osszeg / tbSzamok.Lines.GetLength(0)}";
        }
        

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void Torol_Click(object sender, EventArgs e)
        {
            tbSzamok.Text = "";
            lbAtlag.Text = "";
            lbOsszeg.Text = "";
        }

        private void btExit_Click(object sender, EventArgs e)
        {
            Close();
        }

        private void tbSzamok_TextChanged(object sender, EventArgs e)
        {

        }
    }
}
