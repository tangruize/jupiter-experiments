----------------------- MODULE CJupiterImplAbsJupiter -----------------------
EXTENDS CJupiter
-----------------------------------------------------------------------------
AbsJ == INSTANCE AbsJupiter
            WITH copss <- [r \in Replica |-> {e.cop: e \in css[r].edge}]

THEOREM Spec => AbsJ!Spec
=============================================================================
