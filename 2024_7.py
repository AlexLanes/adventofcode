"""
The engineers just need the total calibration result,
which is the sum of the test values from just the equations that could possibly be true
Operators are always evaluated left-to-right, not according to precedence rules
    add (+) and multiply (*).
"""

example = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""
puzzle_input = """12427056279: 3 5 3 8 3 22 1 651 5 3 1 6
554266023266: 835 7 40 9 7 66 323 3 6
156802: 957 23 8 2 5
451396: 2 21 3 3 4 969 8 8 3 11 4
541800: 6 8 8 350 8 7 2 7 4 5 5
502: 43 53 5 397 4
564543133: 3 4 47 54 3 133
185183376789: 47 3 775 7 4 939 202 7
10300720: 359 30 5 16 331
10114285876: 8 80 7 2 19 3 2 861 3 4 6
6658354: 4 62 5 8 354
1679555006712: 7 4 7 9 4 17 8 883 3 2 2 6
3281626: 4 1 8 1 5 6 242 5 7 6 45
646984854: 1 6 767 4 924 50 2 6 9
15435205: 8 6 2 6 97 117 1 5 9 8 1 5
323223: 2 7 6 197 3 381 27 3
14719245: 801 75 4 31 6 163 7 2
384800550: 513 83 590 129 5
843710637122: 71 2 965 5 12 998 4 1 3
2785998: 15 9 1 2 25 70 1
20879049: 2 52 28 6 1 533 9 6 9 9
28589067: 227 894 5 70 51
7231832: 677 763 7 59 2
1131570: 8 64 691 26 8 33 99 9
448728996: 6 82 57 76 80 16 1 35
38586511: 86 437 653 351 511
1017223: 77 4 25 33
20416: 48 78 451 74 46 7 29
56987487: 63 1 2 42 67 8 1 962 9
6098476: 69 63 660 14 5 76
1395810072: 442 510 4 1 5 43 4 6 6
49896817: 557 56 3 81 72 7 88
3849663743508: 3 1 81 2 8 6 373 1 3 51 1
1963977: 9 68 48 74 4 209 8
11735601: 446 49 537
5853: 50 58 3 1 18
2945091: 999 5 7 1 88 4 7 7 3 408
385659: 3 9 1 6 8 5 7 9 2 597 34
13416: 41 9 4 8 6
6845472302: 97 93 215 684 302
1112504: 74 2 87 7 472
54440: 4 2 9 35 8 9
445835058612: 7 43 6 341 9 586 11
6027221856: 41 4 7 882 9 5 9 8 9 888
26490050: 37 8 1 2 8 11 5 1 1 2 4
5200: 2 29 89 1 38
9746919: 6 4 7 78 3 284 945 7 27
1356978: 50 5 89 241 3 4
28681: 75 370 27 8 896
113054413: 226 5 5 43 90 21
1692: 4 49 98 7 635
1789551225: 97 13 5 5 499 7 9 99
152347805: 6 397 4 895 3 353 1 39
655047: 39 145 479 988 3
4835382339: 73 80 468 4 3 2 14 8 29
13503378578: 424 13 309 78 578
932087: 97 834 1 8 2 87
2828: 4 9 4 4 7
2663212860: 329 52 296 1 5 89 90
8879504: 88 1 78 1 501
4992196576175: 21 4 2 9 5 8 5 70 62 81 8
25625354: 1 75 81 1 2 53 54
546379203959: 6 3 3 712 3 8 36 36 3 5 6
41783203: 47 889 167 9 30
7328754: 2 673 9 594 854 3 3 6
391236: 65 5 250 611 1 97 2
225642: 4 40 178 143 469 53
448848: 87 2 8 1 51 69 48
4650: 4 371 169 1 98 8
326690: 8 10 67 2 6 1 3 49 996
27492032: 619 1 33 421 6 51 6 75
191745655: 655 123 4 34 7
25256: 69 8 41 1 8
1440: 74 16 2 395 865
76638936: 5 96 6 7 8 384 2 68 9 6 4
16475979: 63 97 4 7 5 9 79
2948707379: 8 8 102 32 2 23 280 2 5
139295624: 7 6 16 9 2 7 5 9 8 6 32 72
464621: 357 4 26 5 3
237265609378: 61 5 176 442 93 81
67396998: 69 4 941 56 1 6 6 736 4
17731594: 8 7 82 6 6 2 78 4 1 2 3 1
38794833350: 1 5 2 765 74 979 2 7 50
1511975: 70 77 4 1 975
3479377: 369 73 41 94 61
30750833673: 3 349 764 6 1 153 1
3236809: 66 2 40 119 9
218349: 3 42 70 15 7 349
1389960358: 515 5 54 495 87 271
104: 7 93 2
135021376: 2 96 2 973 59 3 28 4
467432: 649 1 276 2 1 25 491
3824775: 4 6 6 33 4 8 7 7 75 573
618569001: 61 856 8 905 96
3510: 177 93 44 5 366
131985: 96 24 57 655 5
16202819: 1 3 926 58 42 861 9 3 1
3411269120: 64 14 932 43 95
36000444: 4 72 6 76 828 47
1633755: 6 62 432 16 127 27
972911772212: 5 4 4 2 5 12 99 9 9 209 4
13240902895: 7 5 2 71 195 16 433 9
122248101: 863 13 392 356 548
56140560365: 783 6 7 32 705 36 6 1
48197812: 7 982 6 4 2 92 406 7 9
23433: 75 3 1 92 5
1732374: 4 1 5 93 590 4 45 3 7 6
36502: 7 8 70 4 129 7 5 1 7 2 22
2510281833807: 715 1 8 13 27 28 5 80 7
5040243: 4 8 7 60 237 3
2332657654: 85 7 6 72 4 6 2 518 1 52
135673: 32 6 4 15 643
1063567: 296 49 681 8 7 5 8
5083677: 105 9 10 2 24
13560481: 64 57 2 3 1 70 291
39721250: 90 947 63 8 76
30247: 13 5 255 29 33 3 1 9 2
2604: 89 4 78 6 1
1483313: 685 482 942 4 6 7 1 3
4072802: 9 93 23 868 74 2
819216581: 1 637 2 6 4 6 8 9 3 5 80 2
367230334: 9 33 62 8 230 332
2398440: 9 1 903 7 33 79 1
1732799: 74 43 68 2 445 4 5 4 2
7084389272: 63 1 1 921 4 7 7 2 3 4 6 1
10959: 6 7 6 576 6 9
13407283: 315 3 51 541 8 83
378826569: 4 8 33 7 52 828 8
14261: 7 7 8 927 9
173854: 6 7 4 8 5 4 6 1 40 1 9 44
57783: 4 1 9 33 256 4 1 1 2 2 6 3
19425406: 2 76 7 326 3 8 6 1 7 805
1619775: 531 8 9 25 3
29867: 9 3 614 88 1 4 8 6 3 7 19
655: 2 51 45 502 6
274409943: 946 241 29 5 3
2518: 247 8 518 17 7
3569675730: 40 46 7 4 47 509 95 62
62041462: 878 7 5 5 557 4 9 1 46 4
51320839626: 252 76 84 35 75 319
4534248981: 83 967 3 85 78 9 6 4 3 3
15568060: 126 22 605 922 5 90
13024055: 5 74 4 88 54
141: 45 92 6
291251791: 6 515 7 6 745
1761366933: 74 23 352 4 294
994404: 4 8 6 48 123 32 8 452 4
76514: 6 7 98 600 14
5058051: 71 482 91 4 185 3 91
2216287993: 9 42 8 936 35 66 61 7 4
12894510: 6 7 1 7 7 307 2 4 4 426
64522175595: 6 452 21 7 497 2 6 602
7303887494: 25 5 609 5 5 84 8 7 49 7
4155: 822 5 46
374608580613: 2 3 616 25 8 58 796 46
23207960: 197 65 4 515 43
443412841610: 479 22 8 40 46 914 9
6789655: 17 254 466 1 92 55
7625964: 76 25 95 5 6
1741: 1 9 1 9 22
180931249: 723 724 5 5 50
3493889717: 41 8 85 6 5 99 1 8 1 883
262770906: 568 976 2 2 79 3
251029: 65 5 26 715 64
3507640: 216 75 6 2 15 642
211904: 13 48 6 344
522: 7 5 3 5
3810: 7 3 379 9 8 8 530
460174478: 6 8 5 2 4 876 6 8 8 9 16
660268231: 77 70 2 5 849 62 870
6128325: 98 5 807 63 75
4669: 3 87 5 6 7 154
37269025921: 374 58 23 83 80 9
44644811817: 7 7 3 6 3 85 786 1 1 8 1 6
16012: 65 4 6 19 8 1 3 7 9 1 8 6
2736304425: 30 841 8 695 3 156
51616: 724 58 2 47 8 2 1 7 7 2 2
270916: 5 8 8 50 172 9 19
3340: 4 679 475 7 142
350635929: 2 5 7 6 73 3 1 796 2 2 5
104348: 1 51 3 8 7 3 8 2 8 6 476 8
49388638: 3 8 6 3 21 4 7 2 8 629 3 5
679606950492: 19 436 446 98 8 83 5 6
90546: 90 53 6 2 5
505494: 1 758 666
1354: 779 443 25 9 98
17895006361: 9 44 65 1 2 6 750 6 361
186277: 2 44 5 7 2 18 23 7 43 1
92249344: 27 192 35 2 47 32 8
6570: 6 155 412
5264531371: 1 657 4 26 5 65 6 2 59
864129820150: 465 94 72 2 45 226 95
73453752: 7 1 4 8 3 76 210 4 831
100776: 1 77 9 7 8 7 775 38 3
341785221: 874 1 13 1 391
6488622: 84 4 356 18 207
146011741: 70 1 2 6 61 486 697
3271: 6 305 16 4 1
582909893: 259 25 8 8 873 892 9 5
780: 9 7 9 9 746
3290654498: 32 90 489 161 4 494 4
12801: 540 35 696 2 89
464472216: 4 1 562 4 4 717 871 9 8
1495: 1 396 440 92 500 66
805473: 80 680 380 706 633
461553: 90 959 6 20 5 43 411
74990463: 4 31 8 1 9 6 931 4 592 5
5768093342: 9 5 7 2 592 688 9 78 5 6
2243: 15 9 87 86 69
11837412709: 785 14 6 9 5 4 698
1291692080932: 92 1 26 372 140 932
1436857560988: 6 4 4 8 357 9 92 1 1 6 43
329661792269: 6 86 7 6 6 4 2 59 5 3 3 90
1839165: 92 5 5 949 19
505911537: 3 69 2 62 8 7 21 470 67
6035327022: 7 5 8 581 8 483 9 5 6 9 2
13893971398: 2 14 6 2 4 3 5 746 900
131628160: 765 22 6 344 5
257664: 18 6 8 2 8 61
5627412: 7 72 2 2 7 95 9 6 3 8 3 12
767366: 95 2 805 760 188 55
577347: 8 9 593 4 863
571: 9 4 66 69 400
13728: 6 5 994 60 215 73 6
519998220: 6 8 8 91 5 9 57 275 8 9 1
343275: 46 4 19 5 995
54549: 20 3 3 250 171
114723458963: 7 3 230 1 6 899 9 89 64
34001983: 5 77 3 69 635 771 2
5310: 29 61 1 3
8917506: 3 5 7 4 315 2 32 9 234
749965: 3 481 6 5 761 6 7 9 3 1 4
6920410040783: 59 87 474 100 40 785
1285810: 43 38 6 30 8 760 75 8
6504567036023: 591 324 276 110 23
39312817: 8 1 4 1 66 2 7 6 1 6 810 7
31945133: 45 557 71 4 75 70 6
14822498693: 162 4 35 80 1 891
20101915756: 235 611 7 7 8 2 9 2 4 2 2
7211517: 13 4 63 9 56 2 5 661 7
486695: 51 2 3 95 7
77338: 5 3 1 3 99 4 8 8 5 285 54
15735: 1 84 1 185 4 6
1308827965: 7 5 1 31 1 90 891 37 56
41036: 496 81 197 6 657
77442240512: 5 1 7 925 886 8 364 8 4
178800585: 2 3 9 4 4 4 10 6 729 2 9 6
191563683819: 87 231 2 6 122 5 3 819
1580: 2 83 88 33 76 7 4 94 6
2524028: 5 38 41 4 9 9 68
1371: 1 6 85 2 1
20180153709061: 6 2 5 89 5 903 9 5 9 3 2 1
5348: 650 46 50 5 6 842
7574880: 152 9 2 9 38 2 3 5 1 86
180263798: 630 8 697 2 41
135637: 451 5 5 895 39
193645: 857 4 5 6 1 9 4 35 2 9 7 4
2209115606: 97 7 360 50 628 9
158736: 6 877 6 399 7 4 9 4 1 8
8191921: 855 5 5 638 3 1
70319106: 80 257 380 433 9 9
300940: 4 686 436 91 8
124: 2 60 4
2054222905284: 7 73 7 532 7 9 1 18 638
3852485577: 804 37 568 4 57 585
7733360: 9 44 7 4 6 3 1 2 6 2 6 292
137876: 40 8 239 5 1 3 1 6 3 3 2 4
8607831: 859 11 162 50 484
495232: 2 1 3 42 786 1 5 6 3 7 4 5
242862437: 62 445 8 8 11 35
6621686: 5 5 5 1 3 922 7 2 8 8 8 6
7604: 6 169 8 7 3 9 6 5 427
89227: 7 932 95 19 2 1
5776: 232 7 3 903 1
45069696: 4 157 9 48 36 18
161643300: 926 4 910 191 1
26868960342: 397 94 800 38 9
333724133: 91 3 79 28 78 3 9 39
4049582505842: 218 86 6 40 28 6 8 60 6
38981085: 1 4 33 1 8 7 29 9 29 7 9 4
88293150: 5 274 2 286 3 66 5 3 5
571913273753: 1 7 563 913 2 7 3 5 2 5 3
255816565: 500 1 15 51 565
22656504: 75 52 155 3 40
5037237: 7 70 3 1 685 30 862 1 9
843118: 4 8 4 3 3 9 8 748 14 6 94
165818013: 7 741 8 74 54
30367: 45 664 3 324 82 78
1248741970: 9 8 46 8 142 680 394 5
121360516: 9 3 8 1 4 6 7 6 8 598 96 1
595928718: 744 8 160 18 931 20 4
229253: 804 4 71 822 4 91
24354727: 722 6 7 4 861 780 6 7
828734019865: 666 36 436 17 39 694
107802: 68 7 9 2 9 8 3 65 1 7 2 9
6909840084: 480 5 5 914 1 9 9 7 21
67574887954: 2 7 9 3 29 485 3 795 1 3
80117581952: 950 38 56 9 843 2
4341626: 9 9 2 268 24
64179026: 49 8 9 7 1 55 3 2 27 7 8 2
39320134: 7 437 4 459 5 833 7
39231675: 4 7 777 855 57
2917615: 7 1 643 7 8 9 8 9 247
76131594: 1 177 627 7 98
69998078: 64 9 6 8 2 367 73 7 8 1
6937280: 4 8 17 15 6 3 2 5 760 8
176737: 8 897 508 23 5
69538171: 13 443 2 8 806 7 1 68
357696643: 46 324 8 3 3 3 4 2
19806500021567: 565 9 625 2 5 7 2 6 9 6 8
1831104: 1 6 809 561 4
90536995: 3 6 8 3 189 14 6 5 2 7 9 5
30610466: 34 9 10 4 67
108330: 4 7 2 2 2 471 5
2078527: 2 7 41 739 6 439 301
2738759568: 7 42 4 2 5 8 3 4 99 7 2 3
2125570: 8 497 4 46 5 2 5 5 54
12120409: 109 18 58 250 24 409
338023: 613 1 67 71 5 2 7 7 3 4
14584: 5 1 8 5 86
116860285: 1 6 3 160 2 50 6 4 72 87
53282559: 5 3 282 5 5 7
46965024966: 757 5 62 2 4 965
308893: 11 2 8 7 69 4 1 82 6 4 7
203220: 27 6 2 94 540 7 4 669
7850309: 9 5 3 36 6 6 21 88 12 5
595056931: 8 36 2 21 616 931
22230: 55 51 884 16 6
68686892: 70 6 722 481 92
123516: 112 9 5 52 2 94
445040: 3 6 5 97 87 7 1 678 5 8
1379473: 7 1 3 9 39 7 7 1 7 8 9 744
577124515: 6 47 892 270 245
1990431900: 998 67 2 793 548 9 3
385832: 82 49 96 91 6 7
42255489: 7 8 939 3 484 4
470: 364 51 6 1 48
97711378199: 977 11 37 1 7 199 1
19493527: 7 2 759 2 39 1 241 51 1
782908337: 8 24 5 5 626 76 19
425193: 1 537 4 77 688 7 2
115915142: 7 5 3 7 208 4 8 1 17 3 6 2
2732: 8 2 29 70 2
48697176: 178 771 6 27 4 7 38 3 8
897561: 5 9 327 8 4 1 57 3 3 567
44027: 95 83 247 3 58
34314052: 75 2 986 4 301 41 8
38591798: 399 10 52 186 518
56857776: 5 4 23 9 61 5 7 76
1495: 6 2 7 8 8 5 5 6 72 54 7 6
1665265: 5 3 89 410 45 331 9 5
145680408675: 4 9 419 4 4 408 674 3
5965317120552: 7 2 1 456 6 56 5 64 554
2419624368: 60 9 7 6 7 8 635 8 7 7 2 3
120212: 26 92 1 5 5 537
1544730757552: 790 143 61 50 391
50250860: 2 7 988 6 84 4 200 2 2
6144650: 67 317 4 4 649
938: 36 24 74
3582735: 562 35 122 6
7130101416: 9 1 8 70 56 2 8 3 5 6 86
114876: 94 3 44 45 2 18 1 627 2
10753200639: 8 5 71 18 52 28 8 2
748: 6 56 90
122935376: 8 96 15 1 9 51 59 4 4 79
30240723944: 12 1 473 6 7 9 9 8 394 2
1132: 32 589 4 500 7 1
523: 49 3 6
10735945123: 2 8 5 8 9 41 2 7 635 12 3
349141893129: 6 550 836 52 5 1 963 3
2970495: 7 847 501 1 57 6
227240795: 553 45 76 5 798
6201: 78 8 540 1 63 9
322171047: 4 9 874 7 27 6 86
342112130: 1 33 211 2 128
527649: 48 4 6 4 13 7 38 8 5 6 3
242559363052: 67 9 4 85 3 9 3 630 5 4
962: 879 35 39 6 1
563393: 8 85 896 6 12 5
212505: 5 16 57 85 8 74 2 20 2 9
1201: 8 3 8 4 789 24 312
259335373: 1 7 4 5 9 3 4 1 3 46 32 8
1497577545545: 3 765 138 725 6 9 7
4446072: 45 50 2 988 72
3916: 46 388 9 8 372
15162562: 4 816 238 3 560
14450297: 4 9 37 78 49 93 2 21 8
2578194502: 54 4 82 36 66 4 875 2
37351: 71 2 7 6 94 5
62832442: 3 6 37 9 7 5 8 7 542 8
38973: 94 6 228 61 75
661997: 66 19 88 6 6
709: 3 27 49 49 73 496 3 9 1
4367700475: 8 4 566 215 3 3 997 2 2
328739: 1 724 24 72 85 2 2
207366: 384 6 3 3 4
104848968: 8 98 4 6 8 66 9 2 6 54 7
127344: 27 44 683 4 168
7932172: 8 38 484 5 2 172
2754000: 234 81 6 4 425 3 51 24
909986: 8 44 4 6 2 5 8 7 6 7 7 7
44597: 445 69 7 12 9
748244: 7 1 99 6 98 8 3 53 4
29674500: 76 885 490 73 6
20135958947: 402 1 7 5 10 85 8 946
139668: 357 1 41 998 68
972: 1 6 59 22 1
809500: 48 5 36 424 466 37 5
15993846: 39 897 8 729 57 45
439929401952: 43 992 93 9 44 75 50
25053: 1 3 2 4 4 3 8
19210481: 74 7 67 236 81
29385628: 5 6 946 307 56 63 65
210880133085: 44 1 8 78 6 4 9 4 2 5 249
91393425: 182 11 62 5 67 2 1 3 9 5
98124: 2 732 67 28 4 4
24650065440: 76 450 2 99 364 4 5
116388725: 1 1 121 2 61 1 3 4 3 8 9 2
7476908378: 747 6 90 78 5 77 1
58420: 7 817 96 19 5 76
10606404: 23 1 6 83 926
178010: 996 1 777 84 623
4954535792640: 435 2 644 5 9 7 92 61 1
1195764: 2 65 9 3 10 412 1 6 397
39193416: 505 9 353 9 216
6654027: 1 70 61 6 39
1130903171: 883 518 1 8 16
1170420: 487 4 30 81 20
253743: 11 17 194 1 9
405720: 7 13 69 311 955 8
1015923: 6 9 47 79 83 68 3
10538269546: 56 8 437 235 4 6
8343: 677 249 9 9 1
2007882: 2 8 74 5 7 8 9 402 2 694
5270243: 20 831 253
16738245: 5 9 184 79 2 5 3 9 5 37
834249: 7 28 360 642 63
108410793: 49 79 753 61 28
32176521: 336 28 4 883 2
570330: 9 4 16 597 339 302 9 2
468520: 67 9 69 2 6
4046008: 66 327 61 55 4
26265204422: 679 742 422 2 73 2 8 6
229: 127 73 22 4 4
288910: 28 8 831 6 73
949182: 58 73 3 224 7 87
55638: 87 634 14 87 3 8 368
3438732966: 9 9 3 9 2 91 6 8 4 312 9
1090577000387: 5 4 52 88 4 3 7 50 9 7 2 2
1367893818: 9 409 59 2 637 9 5 8 3 6
6699: 1 4 4 3 72
9014897: 8 469 76 12 86 62 4 97
46407: 8 3 843 9 8 6 142 85 16
38: 13 6 5 6 8
5472046634994: 21 2 29 367 89 4 99 1
35992250: 4 703 509 1 6 47 6 47 1
437614423219: 972 3 5 8 8 155 93 9 2 1
56110916: 890 5 446 819 6
56479317484: 51 50 247 5 58 4 444 5
384: 6 128 56 2 4
710496: 10 8 740 8 12
532040: 42 548 9 97 943
24095: 41 6 33 9 47 31 2 316
969496385774: 9 9 1 98 92 8 53 4 7 3 72
91959: 3 79 13 90 29
2566398922: 2 7 9 81 6 413 62 853
3425: 70 39 640 53
945989120: 10 161 931 19
99686839: 9 9 6 3 2 3 59 9 27 12
1215180: 40 446 60 6 5
187385: 77 61 61 9 3 825 3
2935383102: 2 257 98 70 130
51339: 4 5 812 7 1 7 4 97 8 7 18
1387980028932: 81 5 918 8 6 994 43 1
14550071987: 92 53 500 71 900 82 6
11932737: 3 7 8 1 819 4 5 614 4 4 8
1888477: 5 9 75 2 559 60 9 7 658
720516: 4 318 6 827 9 619
6346: 27 78 8 3 6
18076176: 1 829 4 3 1 1 4 592 6 6 6
383939244: 5 65 5 73 133 33 9 453
174276: 5 1 967 30 1 157 55 3
54871772: 86 839 1 456 76
62562: 786 95 71 7 4
95673724: 22 2 48 453 4 7 77
1407900: 50 1 19 57 26
188871577: 5 9 8 4 7 129 6 8 257 8 8
29797632: 40 53 136 600 9 6
762624287: 133 9 6 7 9 95 8 9 9 4 1 4
5311278: 46 716 26 2 69 668 9
14390442: 1 1 14 90 7 93 697 90 2
38143333: 17 4 8 8 92 6 8 7 3 8 408
522548: 768 9 87 466 70
8735836482: 429 4 93 7 931 741 9
26425157: 8 373 8 394 229 22 55
61960: 6 4 968 9
13680: 38 99 53 9 8
253971240: 184 695 662 2 518 3
40577051: 84 70 4 8 479
8552: 3 992 5 69 8
6721479438: 3 3 4 94 11 9 5 8 86 5 8
78193003: 9 5 7 9 1 8 183 8 1 763
107829: 4 547 463 301 82
31071077946: 291 841 491 2 722 38
60978: 417 8 3 155 6
85981666: 3 7 170 3 21 2 3 5 2 4 9 5
7362: 7 945 6 38 703
58242: 8 6 828 9 30 3 5 4 66 2
4075: 9 5 352 7 408
2484607586: 637 13 62 7 6 329 3 86
18816: 5 8 2 3 11 43 4 8 2 112
2768866: 8 459 8 67 87 2 73 8 8
4256479: 37 3 98 593 114 4 4 7
13315217: 7 59 9 69 77 5 228 5 2 7
95584639: 9 55 846 32 6
47650502420: 6 1 7 2 2 3 2 2 592 33 7 7
1114026: 17 68 630 98 87
2991360: 591 1 187 64 2 30
75109: 70 5 1 33 64 168 6 7
21908287: 7 33 95 6 661 25 1 4
47090556: 9 869 79 2 9 596
23985780: 46 91 10 573
34076: 8 85 50 69 7
194928707: 18 5 8 1 921 7 6 6 3 9 5 4
1804453: 7 535 3 80 9 5 3 94 781
1161588602: 29 9 733 6 6 53 2
2643840079: 4 6 40 9 1 4 75 34 1 3 78
12231768: 50 96 57 8 3
22053: 315 1 7 3
59127088135: 7 99 74 291 797 132
209537664: 5 5 1 8 4 1 6 92 220 8 8
26634957: 1 85 2 4 2 24 816 3 714
3940518666: 36 3 80 28 442 3 3 1 8 1
12161796610: 49 56 7 998 6 245 43
199948: 61 976 3 192 268
15654: 5 192 3 7 2 6 62
146720: 31 6 58 8 96
1772: 73 6 482 778 74
105802: 4 9 6 226 764 99 73
1410441620754: 671 6 3 8 867 21 51
1278730: 717 4 39 53 216 1 4 2
1755915: 2 178 6 64 3 1 52 6 7 63
111843603828: 2 157 2 341 794 433 3
227276742914: 911 297 551 84 6 5 1 6
188988963: 7 489 8 9 22 8 7 90 6 5 3
2518558236: 94 687 396 39 6 786
179452851: 26 69 50 2 8 11 38 3
4483617753: 771 6 52 55 7 83 2 84
3045905: 5 8 9 319 62 7 3 4 78 1 8
11261535713: 3 250 769 3 5 714
3854: 344 8 2 31 5
1487109: 835 5 356 1 808
2489: 83 176 8 8 6 3 4 388 8
13541635031: 564 234 793 24
29416717243: 462 527 212 14 3
176849: 162 8 2 1 52
73467964416: 868 704 2 258 233
25815023: 1 64 62 5 650 2 8 62 8
98: 4 9 5 42 15
6487913759: 5 6 7 4 9 791 1 2 753 6 1
3527: 45 18 1 7 8
461767: 565 816 99 628
760: 46 9 8 2 3 8 2 3 6 5 318 7
1202974088: 5 39 7 2 2 7 165 632 1 8
24185454: 2 4 442 552 60 94 6
5237162784: 744 1 9 9 6 6 8 8 6 1 7 81
75160511: 1 2 8 75 92 9 9 40 1 5 11
203314725: 681 6 653 85 191 747
165316: 21 4 9 4 74
217: 51 157 9
2985686: 4 5 8 749 59 8 4 864 83
6236226: 8 959 7 9 86 92 8
23190: 6 5 773
3585388362400: 8 936 913 202 5 416
245815119: 76 340 1 7 46
770044: 9 5 550 33 2 6
531732: 63 3 1 928 924 3
53482062: 3 6 716 8 550 9 55
428281604: 7 198 7 85 57 549
102148233: 4 1 6 9 5 907 3 9 4 5 235
156141: 1 11 5 8 2 8 39 8 1 5 1
3406245075: 905 82 68 9 675
8992: 1 40 4 27 48 16
8125201052: 812 5 20 10 52
1186311: 7 2 91 7 8 38 1 7 2 161 3
846893376: 86 8 287 32 981
1260411: 7 9 65 2 21 79 89 194
2137656811665: 44 777 7 41 42 7 3 682
7628618: 9 5 1 2 2 25 8 9 6 728 4 3
4284404: 6 4 352 764 401
1953248008: 9 6 1 619 8 550 62 1 3 6
23217: 59 4 203 61 71
201456: 40 5 872 578 3
1441638: 2 28 4 79 596 6 8 54 33
6923652: 1 47 116 4 847 41 924
80960930: 176 5 92 93 2
1142233984: 8 9 847 406 64
1478491: 29 8 3 9 634
158600757: 996 272 4 4 6 521 23
682984325: 8 2 1 7 860 4 8 8 48 2
426: 7 59 8 5 2
176333692: 732 2 7 2 2 7 5 6 55 64 2
1944: 877 835 2 5 225
14785562880: 76 3 4 22 4 5 89 6 3 23
222447224873: 669 8 2 369 2 9 10 6 1 4
97661641: 6 9 4 1 9 5 2 6 90 40 3
1346404: 732 9 279 132 2
638099: 69 924 8 531
4826320: 2 580 1 1 9 7 1 460 2
5424478: 6 903 6 476 3
174745089: 9 44 932 9 6 4 9 2 5 54 9
49666959984: 8 869 8 798 7 8 10 48 7
13790117510: 3 9 8 93 531 6 7 8 6 7 8
1158: 38 4 1 5 435 289 8
2461918479: 246 1 918 479 1
37175171: 76 5 62 4 97 4 9 792 4
6855: 7 66 15 52 5 42 6 759
10202049: 300 4 907 37 49 6 58
32659503291: 9 7 8 5 3 9 4 2 318 6 3 8
119110203559: 50 9 52 1 62 772 5 6 2 9
286389091119: 1 81 5 7 2 2 9 741 112 2
1729945: 5 616 77 47 4 32
12666905955: 45 1 7 3 29 3 459 985
741595172: 30 78 166 3 22 762 8
1236667: 47 52 506
190: 3 7 9
25153920494: 15 4 3 79 3 24 11 246 2
3990535857: 63 341 839 7 9
4418193: 31 2 177 80 6 267
11286445296: 778 8 23 77 258 56
876672511: 7 2 122 575 3 64 2 55 2
10080485: 29 62 2 4 5 7 16 5 480 5
193818: 193 1 17 701
4322: 33 64 44 7 47
10731634711: 50 3 32 17 685 86 8
3734528: 9 59 32 5 9 8 2 8 7 512
1912249: 237 8 1 9 8 5 3 269 2 7
986442912: 586 25 2 57 75 882 38
2052: 57 5 9 68 84 5 9
360552: 24 6 6 67 35 54
50657277: 388 2 85 768
831901772: 83 2 37 79 9 3 5 62 72
132361: 4 61 2 2 361
27312518714: 9 3 2 11 8 93 51 8 717
86741323257: 18 408 6 124 38 56
56676545931: 3 4 227 5 7 429 3 8 4 9
3595708: 2 9 274 9 9 3 3 275 4 1
5175468: 5 4 3 8 85 5 1 729 8 4 4 6
73015409730: 6 5 838 2 88 223 6 74 6
197559600: 379 594 20 58 7 5
1980192: 6 6 30 18 4 8
246000: 4 4 70 47 25 38 200
429: 5 9 378 6
48175277: 29 769 45 98 8 9 59 6 5
1646: 1 5 538 9 643 4 439 8
168824: 18 91 50 13 8
78074: 747 28 55 1 516
2605050: 1 826 90 7 5
464453: 2 75 1 5 708 8 5
85549: 94 27 9 9 626
3593392: 4 795 9 44 17
8929787: 924 36 93 12 9 49 5
204815029: 204 8 150 28
441987: 1 626 992 7 39
1104672465971: 5 5 2 6 4 672 460 5 9 70
187704: 7 975 91 36 27
4074: 97 6 7
137722: 8 2 86 70 50
1988: 283 7 5
514083842: 918 8 7 380 2 43
1638: 3 6 46 459 32 3
74762172: 70 4 1 762 172
1779191747: 355 5 4 191 749
220802: 2 3 4 80 30
26027520: 229 8 3 457 18 399 80
34859430: 1 3 311 3 2 261 6 7 7 5 5
10896747904: 19 11 71 57 905
6046305385: 920 2 9 657 8 3
65477902626: 7 1 2 3 3 680 5 7 1 1 39 8
18668556: 27 942 734
35140: 389 9 13 2 5
41271300835140: 733 581 2 4 97 33 580
58892856: 396 627 649 177 199
8702400028: 440 4 4 222 875 29
708207: 3 4 63 73 42 68
2267548393: 35 55 7 25 483 48 8 34
158740626: 623 52 7 32 7
37165412: 447 975 1 99 22 3 4 1 4
87584: 8 391 31 135 1 8 7
1438547106: 45 38 317 161 945
504983: 8 4 6 1 604 8 371
14519220930: 93 1 14 159 90 97
949379: 9 58 991
300867840: 81 8 963 6 62 65 3 3
50593616: 4 20 9 71 98 413 9 8 1 6
15598080: 326 497 62 396 96
8680959: 96 4 549 2 9
1354365818046: 7 93 16 9 9 47 1 940 46
2365: 4 7 9 9 431 687 347 6 3
37026: 9 2 2 18 422 4 3 1 5 5 2 3
72608: 8 254 3 2 137
395449: 7 8 4 1 24 1 2 5 21 144 1
23639040: 5 76 33 6 608 324
28177014753: 505 871 557 5 3
66765514217: 3 179 3 1 5 2 1 3 3 7 1 5
275038: 53 4 51 27 9 94 3 6 79
4059426114: 7 4 4 90 9 7 2 258 3 15
1558696408: 7 773 6 77 90 37
72339600: 4 209 1 4 6 1 5 9 3 2 5 40
654: 6 6 7 42 7 5 44
15902: 691 154 38 18 6
991782: 991 22 7 1 552
60835: 60 8 38
924485: 37 3 33 642 5
4249823: 11 2 6 33 828 3 3 23
47841349: 4 4 70 44 7 353 318
74786945: 63 9 24 4 63 7 744 8 65
25553824: 25 5 527 6 8 34 9 92
244489: 116 4 3 7 7
232787240: 3 91 95 931 28
168883: 2 61 1 2 40 8 84
10517265: 156 62 5 766 8 9 8 72
21531469614: 2 976 729 57 302
498: 1 53 2 9 3
35119420617: 2 5 7 949 499 5 5 2 3 4 5
51053418: 4 1 79 8 488 8 69 42
9064910: 866 428 982 7 37
101985094351: 4 400 7 2 7 37 8 7 7 5 3 6
284804116: 678 3 2 5 6 2 67 7 6 2 3 3
3304056: 550 4 4 7 213
105853334787: 43 2 5 2 6 9 7 9 7 90 78 7
8881534: 25 71 5 6 531
1433046: 1 21 270 9 545 27 759
13727957: 8 324 4 1 79 9 1 57 2 9 6
10591349: 37 162 30 22 3 462
49205: 8 4 1 6 422 500 51 245
812346909: 77 797 1 5 125 58 4 6 3
56448843: 56 7 144 84 3
86848: 7 7 7 7 56 8 1 1 4 4 2 32
5763: 10 7 4 7 65 35 6
7147742595255: 12 5 6 3 73 73 91 9 29 5
5946090: 16 6 25 192 86 85 3
1950322773: 16 8 3 15 61 8 5 9 335 7
80001341: 41 7 302 13 4 71 955
189269: 249 758 325 9 193
24353171198: 74 3 8 36 5 13 249 3 3 3
21988928: 7 22 4 8 5 26 19 169 8
8857: 393 3 77 7 68
87464047546: 57 4 9 3 28 5 4 53 22 45
576270130: 38 7 4 98 22 2 6 1 50 12
1038237: 2 5 38 227 10
16437242: 1 8 8 6 1 118 19
118533: 238 6 88 357 8
55755: 4 8 3 2 1 4 94 6 55 5 59
1878: 46 30 20 470 8
188107538: 9 3 7 369 3 4 9 2 4 7 253
6986478: 847 5 41 2 49 22 4 1
56073: 576 1 7 462 9
16147623: 299 6 9 927 696
172299: 6 6 8 39 8 4 420 7 4 8 2 9
19707121: 14 8 80 277 72 542
4807047: 85 84 1 56 8
103399: 4 4 93 614 944 842
415241080: 2 40 2 4 8 48 3 7 877
39496683225: 99 941 494 8 25
65523806: 284 958 81 49 651 5
10531660: 8 8 609 4 3 9 9 40 2 578
251905: 57 8 38 702 3 70 2 745
54818482: 137 81 4 251 82
1318: 993 314 13
797843199: 92 271 6 128 25
253960: 9 1 8 47 300 55 3 8 94
312486050: 4 3 93 8 6 60 3 5 8 7
20412576: 68 790 237 779 76
32860: 4 804 203 4 8 81 8 6 4
6763: 31 3 4 7 2 6 7 7 140 4 8 7
125419236697: 6 7 53 7 9 7 67 2 2 468 2
480424: 71 9 5 2 373
26062600: 548 3 42 4 6 732 474
66809704: 5 78 89 9 9 5 5 1 67 3 6
704520: 5 8 710 6 2
5532597: 6 2 7 5 6 3 7 3 3 5 2 485
90883: 32 28 8 4 80
5795286550: 5 1 795 286 549
351162: 43 8 2 44 474 9
2179214380: 2 4 609 1 57 505 7 916
828: 46 47 558 67 6 99 5
26940060: 614 4 365 86 80 4 5 63
75738: 31 5 2 6 4 89
138382641: 45 3 6 51 198 72 8 10
7881700869: 36 9 349 83 243
48585: 59 423 17 7 361
2649371051236: 306 5 5 9 6 4 4 9 2 809 4
1599: 599 618 1 5 375 2 1
11245: 849 83 80 112 4
20025747125: 9 1 12 9 39 873 125
304159954: 2 6 7 9 7 7 8 15 995 5
174669224220: 6 5 684 442 81 12 159
27806031: 5 3 7 590 702 77 749 1
7817: 7 21 52 168 5
176057: 55 32 57
319278: 48 67 3 3 11 894
4064102: 200 1 4 66 2 36 301
1294: 8 4 2 3 1 663 1 5 515 3 6
40524: 40 69 617 2 6
14779018942: 5 78 29 3 4 9 932 7 61 3
113488760: 4 1 648 4 18 947 815 8
41492589: 514 468 684 43 4
4857: 8 76 4 52 25 256
470973600: 2 7 778 6 1 60 5 9 5 32
500361: 61 82 1 20 44
22257: 7 2 32 32 14 2 753 6
34936254697: 698 7 2 5 5 37 2 7 72 8
6130747: 28 252 7 31 63
621094920: 24 815 93 8 995
25081134120: 91 3 352 31 5 8 5 343
575932900: 57 9 81 5 3 36 77 3 1
7237736: 714 7 57 7 26 66 8 5 63
8371616: 157 845 9 82 9 805 1 6
2270829: 415 7 7 652 21 7 29
291305: 6 85 67 72 10 49 6 6 7
909249513: 35 1 9 73 4 5 7 8 187 6 3
7452225: 6 360 5 5 3 1 5 8 5 5 33 1
92774412762: 4 89 3 10 302 4 1 595 8
186042: 949 4 49 36 2
10280455589: 4 5 9 3 804 1 554 92 96
4222018: 7 4 9 3 4 3 1 467 5 2 337
517625: 95 22 1 46 2 96 753 3 5
5126817530: 2 439 493 8 3 7 47 4 3 2
28996334: 57 909 54 44 3
35154: 4 9 31 1 87 6
26120: 6 71 6 5 3 6 30 2 6 1 5 4
381682302: 50 76 6 84 589 3 4 3 4 3
7152040: 74 17 3 6 4 5 9 8 5 1 89
84383: 6 8 7 43 36 743 83
938542735821: 521 412 3 18 59 58 21
296700: 1 1 3 856 345
1565677140234: 392 4 42 12 95 234
102060855978: 462 319 13 2 2 7 761 3
23908402876: 90 388 5 840 287 6
8716682: 454 534 165 63 120 2
36326: 34 95 402 6
38384656: 1 97 2 94 2 8 833 9 7
1457826837: 10 70 2 589 308 98 5
1344414: 322 5 2 834 6
12427020: 7 789 75 9 5 6
722534456: 2 8 8 9 9 3 9 980 3 3 3 3
885: 2 6 5 68 1
82339793544: 8 2 33 9 7 93 5 44
56161976: 11 66 47 463 75"""

class Equations:

    equations: dict[int, list[list[int]]]

    def __init__ (self, s: str) -> None:
        self.equations = {}
        for line in s.split("\n"):
            left, right = line.split(": ")
            total, values = int(left), [*map(int, right.split(" "))]

            if total not in self.equations: self.equations[total] = []
            self.equations[total].append(values)

    @staticmethod
    def is_valid (total: int, values: list[int]) -> bool:
        def recursion (current: int, waiting: tuple[int]) -> bool:
            if not waiting: return total == current
            value, *waiting = waiting
            return recursion(current + value, waiting) or recursion(current * value, waiting)

        return recursion(0, tuple(values))

    def sum_of_valids (self) -> int:
        return sum (
            total
            for total, all_values in self.equations.items()
            for values in all_values
            if self.is_valid(total, values)
        )

assert Equations(example).sum_of_valids() == 3749
# print(Equations(puzzle_input).sum_of_valids())