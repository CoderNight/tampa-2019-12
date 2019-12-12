#!/usr/bin/env python3

in1 = """
Shady +?? +?? +?? +??
Rocky +QH +KD +8S +9C
Danny +?? +?? +?? +??
Lil +8H +9H +JS +6H
Shady -QD:discard -2S:discard
Rocky -KD:Shady +7H
Danny -QC:Rocky +?? +??
Lil -6H:Rocky -??:Shady -8H:discard +?? -10S:discard +??
* -JS:Shady +10S +QS
Shady +KD:Rocky +??:Lil -KD:discard -??:Lil
Rocky +QC:Danny +6H:Lil -9C:Danny -6H:discard -7H:discard +3D +3H
Danny +9C:Rocky -AD:discard +??
Lil +??:Shady +?? -??:Danny -??:Shady +??
* +AH:Shady +8D -8D:Danny -QS:Shady +8C
Shady +??:Lil -7S:discard +?? -10H:discard
Rocky -QH:Lil +5D -8S:Shady -3H:discard -QC:discard
Danny +??:Lil +?? +?? -??:Lil -3S:Rocky -??:Shady
Lil +QH:Rocky +??:Danny -AH:Rocky -QH:discard
* +4D:Danny
Shady +8S:Rocky +??:Danny -JS:discard +?? +?? +?? +??
Rocky +3S:Danny +AH:Lil +AS +4H
Danny -10D:discard +?? -6S:discard -JC:discard -8D:discard
Lil -8C:discard -??:Shady +?? -??:Danny
* -4D:Shady +KH -KH:Danny
Shady +??:Lil -??:Danny +?? -2H:discard
Rocky +5C -5D:discard +3C -3D:discard -5C:discard +KS
Danny +??:Lil +??:Shady -??:Lil -6D:discard +??
Lil +??:Danny -??:Shady -??:Danny
* +KH:Danny -9H:Shady -KH:Danny
"""


#           Lil
# Danny             Shady
#          Rocky

# Lil gives signals
# Danny & Shady give false signals
# Rocky sees Lil's initial hand
# All input comes from Nell watching over Rocky's shoulder
# Print out the cards in Lil's hand after each of her turns
# "discard" is a "player" If listed as draws, it indicates discarded cards

# Initial: 4 cards per player
# Cards: 52 cards
# Moves: Draw, Pass, Discard
# a card is done after discard

# Input Format:
# Cards  <value><suit>, where
#        Values = [2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A]
#        Suits = [C, D, S, H]
#        unknown = ??
# Name <moves>
# +??  a draw
# -??:Name   pass to Name
# +??:Name   receive from Name
# -??:discard  a discarded card (will be visible)
# * <signals>    <-- same as moves from Lil's point of view

# all discards are visible
# all passes between Lil & Rocky are visible
# signals are only for invisible moves: draws and passes to/from opponents
# signals only come after Lil's turns

# Algorithm:
# initialize state for 4 players and discard pile
# track changes
# for Lil's turn, track changes, then process 0+ signals, then print her cards in order received

in_final = """
Shady +?? +?? +?? +??
Rocky +5S +QH +6H +JC
Danny +?? +?? +?? +??
Lil +7C +3S +8D +9H
Shady -4H:discard -??:Danny +??
Rocky +10D -10D:Danny +4S +2D -4S:discard -JC:Lil
Danny +??:Shady +10D:Rocky +?? +?? +?? -4D:discard
Lil +JC:Rocky +?? -??:Shady +??
*  +JH -7C:Shady +10C
*  +JH -8D:Shady +9S
*  +JH -8D:Shady +10C   [ this one ]
Shady +??:Lil -8D:Rocky +??
Rocky +8D:Shady +9S -2D:discard -5S:Lil
Danny +?? -KS:discard -10D:discard +?? +??
Lil +5S:Rocky +?? -7C:discard -10C:discard -5S:discard
* +KC
* +6S  [ this one ]
* +9S

3S 9H JC JH 6S

Shady -??:Lil +?? -??:Lil -??:Danny +??
Rocky +7D -9S:Shady -7D:discard -6H:Lil +2S -8D:Lil
Danny +??:Shady +?? -6C:discard -??:Lil -7S:discard -KD:discard -5C:discard
Lil +??:Shady +??:Shady +6H:Rocky +8D:Rocky +??:Danny -??:Danny +?? +??
x1   * +2H:Shady +QC:Shady +3D:Danny -3S:Danny +JD +8S
x2   * +3C:Shady +3D:Shady +10S:Danny -3C:Danny +AH +3H
x3   * +QC:Shady +JD:Shady +10S:Danny -6S:Danny +7H +8H  [+] only path possible to z's

3S 9H JC JH QC JD 6H 8D 10S 7H 8H

Shady +9S:Rocky -9S:discard -QD:discard -10H:discard
Rocky +9D -9D:discard -2S:Lil
Danny +??:Lil -AD:discard +?? +?? +??
Lil +2S:Rocky +?? -??:Shady +?? -8D:discard
y1   * +3D -9H:Shady +AH   y1 req: !x1 !x2 ?x3
y2   * +3C -3C:Shady +AS   y2 req: ?x1 !x2 ?x3
y3   * +3D -2S:Shady +AS   y3 req: !x1 !x2 ?x3  [x] only path giving shady the 2S needed next

3S 9H JC JH QC JD 6H 10S 7H 8H 3D AS

Shady +??:Lil +?? -2S:Rocky -5H:discard -??:Danny
Rocky +2S:Shady +KC -KC:discard +2C
Danny +??:Shady +?? +?? -KH:discard +?? -9C:discard -4C:discard
Lil -9H:discard -JH:Rocky -JC:discard +?? -3D:discard
z1   * +AS   req: ?y1 !y2 !y3    ?x1 ?x2 ?x3  ?y1x3
z2   * +3D   req: !y1 ?y2 !y3    !x1 !x2 ?x3         ?y2x3
z3   * +3C   req: ?y1 !y2 ?y3    ?x1 !x2 ?x3  ?y1x3         ?y3x3  [x]  only path with y3

3S QC JD 6H 10S 7H 8H AS 3C
"""
