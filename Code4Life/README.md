# Code4Life by Roche

## Goal
Produce medicines and maximize your score by transporting items across a medical complex.

## Rules
Robots can transfer data and molecules.

Possible moves:
* Collect data from *DIAGNOSIS module*
* Gather molecules from *MOLECULES module*
* Produce medicine at the *Laboratory module*

## AI's

### Roche-Fort 1.

**State machine:**

<----------------- Start -------------->

* Did I want to connect to a module last step
  * "yes"
    * Initiate *Module_goto_connect: destination*
    * Restart
  * "no"
    * Can I make a medicine with the molecules I have?
      * "yes"
        * Go the *Module_goto_connect: Laboratory module*
        * Make the medicine
        * Restart
      * "no"
        * Do I have data slots open?
          * "yes"
            * are there recipes in the cloud with a higher rating than mine?
              * "yes"
                * Initiate *DIAGNOSIS_berserk*
                * Restart
          * "no"
            * Do I have enough molecules the make a medicine?
              * "yes"
                * Initiate *LABORATORY_lazarus*
                * Restart
              * "no"
                * Initiate *MOLECULAR_madness*
                * Restart

    <------------------- end -------------->

**Protocols:**

*DIAGNOSIS_berserk*
* Go to the *DIAGNOSIS module*
* Fill up (max three) with the most valuable medicines available

*MOLECULAR_madness*
* Go to the *MOLECULES module*
  * Did I already start gathering for the second
    * "yes"
      * Get the molecules for that one
    * "no"
      * Are there medicines with the same score?
        * "yes"
          * Take the molecules for the medicine with the least amount required (compare to inventory)
        * "no"
          * Take the molecules for the medicine with the highest health
* if there are spots left, also part of the needed molecules for the second molecule
* Do I have molecules for two medicines?
  * "yes"
    * Initiate *LABORATORY_lazarus* twice
  * "no"
    * Did I start collecting for the second medicine?
      * "yes"
        * Tick the "Started hoarding for the second medicine"

*LABORATORY_lazarus*
* Make them medicines yo!

*Module_goto_connect*


## Ideas
Use an optimiser each timestep, that checks the possible outcomes given the current inventory and the the available data in the cloud
