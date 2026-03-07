namespace WindowsFormsApp1
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            this.tbSzamok = new System.Windows.Forms.TextBox();
            this.Szamol = new System.Windows.Forms.Button();
            this.Torol = new System.Windows.Forms.Button();
            this.lb1 = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.lbSzorzat = new System.Windows.Forms.Label();
            this.lbAtlag = new System.Windows.Forms.Label();
            this.lbOsszeg = new System.Windows.Forms.Label();
            this.contextMenuStrip1 = new System.Windows.Forms.ContextMenuStrip(this.components);
            this.btExit = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // tbSzamok
            // 
            this.tbSzamok.Location = new System.Drawing.Point(12, 28);
            this.tbSzamok.Multiline = true;
            this.tbSzamok.Name = "tbSzamok";
            this.tbSzamok.Size = new System.Drawing.Size(162, 257);
            this.tbSzamok.TabIndex = 0;
            this.tbSzamok.TextChanged += new System.EventHandler(this.tbSzamok_TextChanged);
            // 
            // Szamol
            // 
            this.Szamol.Location = new System.Drawing.Point(479, 387);
            this.Szamol.Name = "Szamol";
            this.Szamol.Size = new System.Drawing.Size(75, 23);
            this.Szamol.TabIndex = 1;
            this.Szamol.Text = "Szamol";
            this.Szamol.UseVisualStyleBackColor = true;
            this.Szamol.Click += new System.EventHandler(this.button1_Click);
            // 
            // Torol
            // 
            this.Torol.Location = new System.Drawing.Point(586, 387);
            this.Torol.Name = "Torol";
            this.Torol.Size = new System.Drawing.Size(75, 23);
            this.Torol.TabIndex = 2;
            this.Torol.Text = "Torol";
            this.Torol.UseVisualStyleBackColor = true;
            this.Torol.Click += new System.EventHandler(this.Torol_Click);
            // 
            // lb1
            // 
            this.lb1.AutoSize = true;
            this.lb1.Location = new System.Drawing.Point(344, 54);
            this.lb1.Name = "lb1";
            this.lb1.Size = new System.Drawing.Size(42, 13);
            this.lb1.TabIndex = 3;
            this.lb1.Text = "Osszeg";
            this.lb1.Click += new System.EventHandler(this.label1_Click);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(347, 117);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(31, 13);
            this.label1.TabIndex = 4;
            this.label1.Text = "Atlag";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(347, 180);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(42, 13);
            this.label2.TabIndex = 5;
            this.label2.Text = "Szorzat";
            // 
            // lbSzorzat
            // 
            this.lbSzorzat.AutoSize = true;
            this.lbSzorzat.Location = new System.Drawing.Point(457, 180);
            this.lbSzorzat.Name = "lbSzorzat";
            this.lbSzorzat.Size = new System.Drawing.Size(0, 13);
            this.lbSzorzat.TabIndex = 8;
            // 
            // lbAtlag
            // 
            this.lbAtlag.AutoSize = true;
            this.lbAtlag.Location = new System.Drawing.Point(457, 117);
            this.lbAtlag.Name = "lbAtlag";
            this.lbAtlag.Size = new System.Drawing.Size(0, 13);
            this.lbAtlag.TabIndex = 7;
            // 
            // lbOsszeg
            // 
            this.lbOsszeg.AutoSize = true;
            this.lbOsszeg.Location = new System.Drawing.Point(454, 54);
            this.lbOsszeg.Name = "lbOsszeg";
            this.lbOsszeg.Size = new System.Drawing.Size(0, 13);
            this.lbOsszeg.TabIndex = 6;
            // 
            // contextMenuStrip1
            // 
            this.contextMenuStrip1.Name = "contextMenuStrip1";
            this.contextMenuStrip1.Size = new System.Drawing.Size(61, 4);
            // 
            // btExit
            // 
            this.btExit.Location = new System.Drawing.Point(687, 387);
            this.btExit.Name = "btExit";
            this.btExit.Size = new System.Drawing.Size(75, 23);
            this.btExit.TabIndex = 10;
            this.btExit.Text = "Exit";
            this.btExit.UseVisualStyleBackColor = true;
            this.btExit.Click += new System.EventHandler(this.btExit_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.btExit);
            this.Controls.Add(this.lbSzorzat);
            this.Controls.Add(this.lbAtlag);
            this.Controls.Add(this.lbOsszeg);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.lb1);
            this.Controls.Add(this.Torol);
            this.Controls.Add(this.Szamol);
            this.Controls.Add(this.tbSzamok);
            this.Name = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox tbSzamok;
        private System.Windows.Forms.Button Szamol;
        private System.Windows.Forms.Button Torol;
        private System.Windows.Forms.Label lb1;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label lbSzorzat;
        private System.Windows.Forms.Label lbAtlag;
        private System.Windows.Forms.Label lbOsszeg;
        private System.Windows.Forms.ContextMenuStrip contextMenuStrip1;
        private System.Windows.Forms.Button btExit;
    }
}

