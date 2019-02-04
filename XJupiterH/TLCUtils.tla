------------------------------ MODULE TLCUtils ------------------------------
(*
Utilities to the TLC standard module.
*)
EXTENDS Naturals, TLC
(*
Help to count how many times TLC evaluates an expression.
It also prints the counter with user-specified description whenever it divides multiplier.

ASSUME (TLCSet(i, <<"Description", 0>>))

WARNING: Only approximate count is given in multi-threaded context.
*)
TLCCnt(i, multiplier) ==    
    /\ TLCSet(i, [TLCGet(i) EXCEPT ![2] = @ + 1])
    /\ (TLCGet(i)[2] % multiplier = 0) => PrintT(TLCGet(i))
=============================================================================
