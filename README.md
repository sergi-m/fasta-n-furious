# fasta-n-furious :checkered_flag:
This is a script designed to read specific sequences from contigs in a FASTA file
and output them in a TXT file. For now, the input expected is an Excel file containing
at least four columns with the file name, contig name, start of sequence and end of 
sequence (in that order). Please beware that should you choose to use this script, you might encounter quotes from the movie from which this simple little program takes its name.



## Installation and Requirements

First and foremost, you will need to have Python 3.6 or a later version in your pretty new environment. If that is not the case and you don't know how that can come to happen, I have your back. If you are wise beyond your years and such mundane demonstrations are beneath you, skip the following step.



#### Installing Python 3.8 using conda

1. Activate conda:

   ```bash
   module load conda
   ```

2. Create a new environment with python installed:

   ```bash
   conda create -n py38 python=3.8
   ```

3. Once everything is installed, you can simply activate it with:

   ```bash
   source activate py38
   ```



### Installing fasta-n-furious

There are two options to do this, the lazy one and the proper one. Use whichever one fits you the most but please bear in mind that the recommended one is obvious.

#### Lazy option

1. Download the script and copy it to whichever directory takes your fancy.

2. Change permissions to be able to execute the file:

   ```bash
   chmod 755 fasta-n-furious.py
   ```

3. Install the dependencies with pip:

   ```bash
   pip install pandas
   pip install xlrd
   ```

4. You're good to go!



#### Proper option

The proper option involves cloning the repository and using the requirements.txt to install the requirements with pip. But since for now only Quim is going to be using this script and I know which option he'll choose, I won't bother with this for now. :smiling_imp:



## Using fasta-n-furious

The script comes with its own implemented help menu, which you can access with the following command:

```bash
python fasta-n-furious.py -h
```



I will give you an example to help get you started. All you need is an Excel file containing at least four columns with the file name, contig name, start of sequence and end of sequence (in that order) and the path to the folder containing the FASTA files. Then you quite simply write the following on your pretty little terminal:

```bash
python fasta-n-furious.py -f path/to/fasta_folder -xl path/to/excel_file 
```

And voilà! A file called fasta_sequences.txt was created containing all your precious sequences all ready to be explored to uncover their hidden mysteries. :crystal_ball:

