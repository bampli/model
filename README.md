[![Build Status](https://api.travis-ci.org/bampli/model.svg?branch=master)](https://travis-ci.org/bampli/model)

# bAmpli model

The goals are:

 * develop bAmpli specs
 * run bAmpli tests
 * develop actionwords

System under test
------------------

The SUT is (being transformed from) a simple coffee machine. You start it, you ask for a coffee and you get it, sometimes. But most of times you have to add water or beans, empty the grounds. You have an automatic expresso machine at work or at home? So you know how it goes :-)

Update tests
-------------

To update the tests:

    hiptest-publisher -c behave.conf --only=features,step_definitions

The tests are generated in the [``features``](https://github.com/hiptest/hps-behave/tree/master/features) directory.

Run tests
---------

To build the project and run the tests, use the following command:

    behave --junit --junit-directory results

The SUT implementation can be seen in [``src/coffee_machine.py``](https://github.com/hiptest/hps-behave/blob/master/src/coffee_machine.py)

The test report is generated in ```results/```

Note: Hiptest publisher with Behave: tests generated in Behave format from [Hiptest](https://hiptest.com), using [Hiptest publisher](https://github.com/hiptest/hiptest-publisher).

