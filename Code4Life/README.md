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

* Are there tasks left in queue?
  * "yes"
    * Complete residual task
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
            * are there recipes in the cloud with a higher health rating than mine?
              * "yes"
                * Initiate *Module_goto_connect: diagnosis module*
                * Restart
          * "no"
            * Initiate  *Module_goto_connect: molecular module*
            * Restart

<------------------- end -------------->

**Protocols:**

*DIAGNOSIS_berserk*
* Fill up with the most recipe available
* Add task to queue to fill up with recipes

*MOLECULAR_madness2.0*
* rank the available recipes from high to low
* check the needed molecules for the first one
* is there room for more ?
* check the needed molecules for the second one

*MOLECULAR_madness1.0*
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
* **Difficulty unknown:** there is a need to query based on the recipe IDs
* **Medium:** make the queuing system more elegant
* **Simple:** start from a location based state Machine, starting pount of cascade is dependent on the location of the robot, it makes sense to fill up on recipes if the robot is at the diagnosis module
* **Hard:** Use an optimiser each timestep, that checks the possible outcomes given the current inventory and the the available data in the cloud
