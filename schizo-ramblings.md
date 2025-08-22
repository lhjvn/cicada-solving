This file is used to document my efforts to decrypt the liber primus. You can ignore this of obviously.

# Entry I 17.8.25
Looking into `[0,1,2].jpg`, the previous page hinted at a magic square.

**Matrix:**
```
434  1311  312  278  966
204   812  934  280 1071
626   620  809  620  626
1071  280  934  812  204
966   278  312 1311  434
```
All rows and diagonals sum to **3301**.

Attempting to generate matrices that yield prime numbers from the text:

Second intuition: use each nth rune of the words to build separate matrices. Below is the distribution of word lengths:
```json
{
    1: 5,       // Prime -> I/A 
    3: 36,      // 4x4 matrix
    4: 20, 
    5: 13,      // Prime
    6: 18, 
    2: 28,
    7: 17,      // Prime
    8: 9,       // 3x3 matrix
    9: 6,
    10: 4,      // 2x2 matrix
    11: 2,      // Prime
}
```
For reference, sentence lengths (in words) section crosses:
```
[2, 33, 25, 4, 15, 10, 7, 26, 36] 
```
Number of runes per sentence section crosses:
```
[13, 141, 121, 22, 53, 44, 40, 97, 198] sum = 729 = 3**6 = 3**3 * 3**3
```
Since length 11 has only two entries, this theory is likely excluded.
With 729 indices, there are several ways to arrange them into matrices, 

The matrix can be rebuilt using only these values:
```
434 1311 312 278 966
204 812 934 280 1071
626 620 809
```
Or modulo 29:
```
28   9   23   17   10
1    0   6    19   26
17   11  25
```
13 characters. Previously, the first sentence also had 13 runes:
```
First sentence (runes): ᛋᚻᛖᚩᚷᛗᛡᚠ-ᛋᚣᛖᛝᚳ
First sentence (idx): [15, 8, 18, 3, 6, 19, 27, 0, 15, 26, 18, 21, 5]
```


Im currently considering that the first sentence is somehow used to generate a key.
we have 13 chars to deal with thats $2*2 + 3*3$ 
We can also in a similar fashion as the matrix in the previous page use the 5 as a center and mirror the array to complete the matrix 

```
15	8	18	3	6
19	27	0	15	26
18	21	5	21	18
26	15	0	27	19
6	3	18	8	15
```

# Entry II 18.8.25

TODO:
since there is a 4x4 matrix on one of the pages we might want to look into wether it was used to encode some of the `junk` data in the outguess. 

I forgot to take into considiration that there is another previous matrix
Also stating KNOW THIS

```
272		138		SHADOWS		131		151
AETHEREAL	BVFFERS		VOID		CARNAL		18
226		OBSCVRA		FORM		245		MOBIVS
18		ANALOG		VOID		MOVRNFVL	AETHEREAL
151		131		CABAL		138		272
```
Using the GP sums we get the magic square for 1033:
272		138		341		131		151
366     199		130		320		18
226		245		91	        245 		26
18		320	130		199	    366
151		131		341		138		272

But unfortuanatly we get no results trying to get a new magic square using these values. So maybe we first need to 

1033 + H + 3301 


272		138		341		131		151
366     199		130		320		18
226		245		91	    245		226
18		320		130		199	    366
151		131		341		138		272

15	    8	    18  	3	    6
19	    27  	0	    15	    26
18	    21  	5   	21	    18
26	    15  	0	    27	    19
6	    3	    18	    8	    15

434     1311    312     278     966
204     812     934     280     1071
626     620     809     620     626
1071    280     934     812     204
966     278     312     1311    434



272		138		341		131		151
366     199		130		320		18
226		245		91	
15	    8	    18  	3	    6
19	    27  	0	    15	    26
18	    21  	5   

434     1311    312     278     966
204     812     934     280     1071
626     620     809     


In adendum of yesterday I indicated the lines that result in prime values


89              41               47
    +----+----+----+----+----+
    | 15 |  8 | 18 |  3 |  6 |
    +----+----+----+----+----+
    | 19 | 27 |  0 | 15 | 26 |
    +----+----+----+----+----+
83  | 18 | 21 |  5 | 21 | 18 |  83
    +----+----+----+----+----+
    | 26 | 15 |  0 | 27 | 19 |
    +----+----+----+----+----+
    |  6 |  3 | 18 |  8 | 15 |
    +----+----+----+----+----+
47              41               89

maybe use 0 as an input for a decryption function?



## Entry III - 20.8.2025

Maybe the gpSums are used as a maping for the words. 
e.g. The sum for n = 373. Then for all w in lp. dec(373) = n.
ITS WORDS ARE THE MAP
```
Liber Primus is the way.               <-- text do decode
Its words are the map,                 <-- matrix, dictionary
their meaning is the road              <-- decryption
and their numbers are the direction.   <-- words that are primes are the keys
```

# Entry IV - 22.8.2025

I decided to make this github repository public for other people looking into this. Up until now I made a function to detect single character substitution. However this effort seems futile since 3301 decided to skip over (seemingly) random characters when encrypting. The sample size is too small for a programatic approach. Bummer.


