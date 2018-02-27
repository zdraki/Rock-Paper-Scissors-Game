# Rock Paper Scissors Game

Game setup. Each game round consists two turns, the first by the com- puter and the second by a human. The computer continues playing rounds until the human chooses to quit.

The computer chooses one of Rock, Paper, and Scissors, but keeps its choice secret.
The computer asks for the human’s input.
The human chooses one of Rock, Paper, and Scissors, or Quit.
Unless the human quits, the computer figures out the result of the game, as follows:

– Rock smashes Scissors, so Rock beats Scissors.
– Scissors can cut up paper, so Scissors beat Paper.  
– Paper covers Rock, so Paper beats Rock.

If both players chose the same, it is a draw. The computer reports theresult of this round.
If the human chooses to quit, the computer reports:

– the number of games played, and  
– the number of times the human won.  

Computer’s brains. We will give the computer some smarts. It must be able to exploit any human biases. For example, if the human seems to prefer Rock, the computer should play Paper (which beats Rock).

Hence, your program should remember how many Rock, Paper, or Scissors were played by the human. Note that we don’t need to remember the order in which the human chooses these; the total counts so far for each choice will be enough.

The approach followed here is "probabilistic". Instead of sipmply tracking the user's preferences and picking the winning tool everytime, the computer picks the winning tool (according to the user's preference) with a probability. This way if the user, realizes the computer's tactic it's going to be more difficult to beat it.
