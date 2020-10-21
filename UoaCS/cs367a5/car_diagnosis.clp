;;;=========================================================
;;;   Car Diagnosis System
;;;
;;;   This expert system diagnoses why a car will not start.
;;;
;;;   This program is adapted from auto.clp
;;;=========================================================

;;*************************************
;;* DEFFUNCTIONS FOR QUESTIONS *
;;*************************************

(deffunction ask-question (?question $?allowed-values)
   (printout t ?question)
   (bind ?answer (read))
   (if (lexemep ?answer)
       then (bind ?answer (lowcase ?answer)))
   (while (not (member$ ?answer ?allowed-values)) do
      (printout t ?question)
      (bind ?answer (read))
      (if (lexemep ?answer)
          then (bind ?answer (lowcase ?answer))))
   ?answer)

(deffunction yes-or-no-p (?question)
   (bind ?response (ask-question ?question yes no y n))
   (if (or (eq ?response yes) (eq ?response y))
       then yes
       else no))

;;;********************************
;;;* STARTING BANNER *
;;;********************************

(defrule system-banner ""
  (declare (salience 10))
  =>
  (printout t crlf crlf)
  (printout t "The Car Diagnosis Expert System")
  (printout t crlf crlf))

;;;*************************************
;;;* DECISION TREE NODES *
;;;*************************************

(defrule determine-car-state ""
   (not (car-starts ?))
   (not (outcome ?))
   =>
   (assert (car-starts (yes-or-no-p "Does the car start (yes/no)? "))))

(defrule starts-normally ""
   (car-starts yes)
   (not (outcome ?))
   =>
   (assert (outcome "Sorry, only do non-starting")))

(defrule determine-motor-state ""
   (car-starts no)
   (not (outcome ?))
   =>
   (assert (motor-turns (yes-or-no-p "Does the starter motor turn (yes/no)? "))))

(defrule determine-headlight-state ""
   (motor-turns no)
   (not (outcome ?))
   =>
   (assert (headlights-work (yes-or-no-p "Do the headlights work (yes/no)? "))))

(defrule flat-battery ""
   (headlights-work no)
   (not (outcome ?))
   =>
   (assert (outcome "Flat Battery")))

(defrule determine-motor-problem ""
   (headlights-work yes)
   (not (outcome ?))
   =>
   (assert (outcome "Starter motor problem")))

(defrule determine-petrol-state ""
   (motor-turns yes)
   (not (outcome ?))
   =>
   (assert (got-petrol (yes-or-no-p "Is there petrol (yes/no)? "))))

(defrule fill-petrol-tank ""
   (got-petrol no)
   (not (outcome ?))
   =>
   (assert (outcome "Fill petrol tank")))

(defrule determine-plugs-state ""
   (got-petrol yes)
   (not (outcome ?))
   =>
   (assert (plugs-spark (yes-or-no-p "Is there spark at plugs (yes/no)? "))))

(defrule determine-fuel-reaching-plugs-state ""
   (plugs-spark yes)
   (not (outcome ?))
   =>
   (assert (fuel-reaching-plugs (yes-or-no-p "Is fuel reaching plugs (yes/no)? "))))

(defrule determine-coil-spark-state ""
   (plugs-spark no)
   (not (outcome ?))
   =>
   (assert (coil-spark (yes-or-no-p "Is there spark at coil (yes/no)? "))))

(defrule fault-in-LT-circuit ""
   (coil-spark yes)
   (not (outcome ?))
   =>
   (assert (outcome "Fault in LT circuit")))

(defrule fault-in-HT-circuit ""
   (coil-spark no)
   (not (outcome ?))
   =>
   (assert (outcome "Fault in HT circuit")))

(defrule determine-fuel-reaching-carburetor-state ""
   (fuel-reaching-plugs yes)
   (not (outcome ?))
   =>
   (assert (fuel-reaching-carburetor (yes-or-no-p "Is fuel reaching carburetor (yes/no)? "))))

(defrule problem-with-timing ""
   (fuel-reaching-plugs no)
   (not (outcome ?))
   =>
   (assert (outcome "Problem with timing")))

(defrule carburetor-problem ""
   (fuel-reaching-carburetor yes)
   (not (outcome ?))
   =>
   (assert (outcome "Carburetor Problem")))

 (defrule fuel-line-blockage ""
   (fuel-reaching-carburetor no)
   (not (outcome ?))
   =>
   (assert (outcome "Blockage in fuel line")))

;;;********************************
;;;* FINAL OUTCOME *
;;;********************************
(defrule print-repair ""
  (declare (salience 10))
  (outcome ?item)
  =>
  (printout t crlf crlf)
  (printout t "Suggested problem with the car:")
  (printout t crlf crlf)
  (format t " %s%n%n%n" ?item))
