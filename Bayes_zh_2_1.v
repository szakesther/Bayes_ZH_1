(*feladat 2.1. Lemma Probléma*)
Lemma problem_1 : forall A B C : Prop, A /\ (B \/ C) -> (A /\ B) \/ (A /\ C).
Proof.
  (*Itt vannak az állítások: A, B, C*)
  (*premissza (A /\ (B \/ C)) szétszedjük két részre:*)
  (*HA: A igaz, HBC: B vagy C igaz*)
  intros A B C [HA HBC].
  (*HBC egy 'vagy', ezért két esetet kell megvizsgálnunk*)
  destruct HBC as [HB | HC].
  (*első: B igaz*)
  - left.
    (*A és B is igaz*)
    split; assumption.
  (*második eset: C igaz*)
  - right.
    (*A és C is igaz*)
    split; assumption.
Qed.
