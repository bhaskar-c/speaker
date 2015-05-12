Translated from ORiginal Fork
========

the speaker

He speaks using Markov chain. Tkinter interface are also available.

Summarizing software after I have finished, I was working on this software for a while. Now I'm over and I publish. Again I stand with an interesting design ...

This software .txt extension opens a book. Then you specify the number of words per chain (I'll explain later) forms with Markov chains. Then he is ready to talk to you. If you like the "Settings" tab you can change the behavior of the software.

I want to give information about the number of words per the following chain. Because the information I have about this software may be insufficient. Let me explain: the number of words per chain is bölünceg escapes escapes in other words in the text. Thus; inputs, outputs will be supervised escapes escapes, also determine examined. Important information you need to know: 1. This number decreases, the variability of output given by the software randomness increases. Although this can sometimes be more fun software, you drop the meaningless number, you are getting complex output; You should raise this value. 2. This number increases, the software runs slower. This is one of the most important factors affecting the speed. If the software is running slowly, reduce it.

Scripts and tasks: markov.py -> Chain forming, entries that receive output, the script makes a lot of business in short, you do not see behind. konuşucu.py -> make up the Tkinter interface, which opens the script and save the settings.

The directory containing OPERATION OF THE SOFTWARE SHOULD BE A BOOK .txt extension.
