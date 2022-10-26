# Take home exercises and additional learning/review material

### 1. Codon optimize a gene sequence for expression in *E. coli*
* Write a function that inputs a RNA or DNA coding sequence and outputs a RNA or DNA sequence where codons are optimized for gene expression in *E. coli*. 
* Here is a link to the codon usage table in *E. coli*: https://www.kazusa.or.jp/codon/cgi-bin/showcodon.cgi?species=83333&aa=1&style=GCG
* Consider using the translate() function we have already written to translate a RNA/DNA sequence, then from the amino acid sequence, convert back to a RNA/DNA sequence with optimal codons. OR feel free to implement your own logic. 
* I have already written for you a python dictionary with the optimal codon associated with each amino acid ID:

```
ecoli_optimal_codons = {
    "Y":"UAU", "W":"UGG", "V":"GUG", "U":"ACC",
    "S":"AGC", "R":"CGC", "Q":"CAG", "P":"CCG",
    "N":"AAC", "M":"AUG", "L":"CUG", "K":"AAA",
    "I":"AUU", "H":"CAU", "G":"GGC", "F":"UUU",
    "E":"GAA", "D":"GAU", "C":"UGC", "A":"GCG"}
```

* Challenge: allow user to specificy a DNA or RNA sequence output. I would watch this youtube video and focus on how the .replace() method could be used to change U to T or vise versa:
https://www.youtube.com/watch?v=HJpiAZDJrRY



### 2. Random sequence generator
* Watch this youtube video about the random package: https://www.youtube.com/watch?v=KzqSDvzOFNA
* Write a function to generate a random sequence of DNA. Allow the user to specify length of random sequence and GC content. Output the random sequence in fasta format


### 3. Describe a sequence
* Write a function to "describe" an input nucleotide sequence.
* Return the following characteristics of the input sequence:
    - type (DNA or RNA)
    - length of the sequence
    - Count how many times each character occurs in the sequence and record the data in a python dictionary. For tips on manipulating dictionaries, watch: https://www.youtube.com/watch?v=daefaLgNkw0
    - GC content. For an extra challenge iterate through the characters dictionary to get the counts for G and C. 

example outout:
if I wrote a function called describe,  this is what I would expect as output:

```> print(describe("AUCGAUCGGGGGG"))```

length: 13\
type: RNA\
GC content: 69.2%\
{'A': 2, 'U': 2, 'C': 2, 'G': 7}
