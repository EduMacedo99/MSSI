+today(Day): true
    <- ?purpose(Day, P);
       ?destination(P, Z_Dst);
       !location(Z_Dst).

+!location(Z_Dst): location(Z_org) & (not(Z_dst = Z_org))
    <- !