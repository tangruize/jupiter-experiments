----------------------------- MODULE GraphsUtil -----------------------------
(*
A digraph is a pair of a set of nodes
and a set of directed edges, each of which is a pair of nodes.
*)
IsGraph(G) == \* Represented by a record with node field and edge field. 
    /\ G = [node |-> G.node, edge |-> G.edge] 

EmptyGraph == [node |-> {{}}, edge |-> {}]

g (+) h == \* A union (in terms of set) of two graphs g and h.
    [node |-> g.node \cup h.node, edge |-> g.edge \cup h.edge]
=============================================================================
