#
# The change of the unittestframework class to the otterassert class
# happened in GitHub. I haven't updated this file to make that association yet.
# My test runner is very basic at this point because my intent is to set up 
# @test decorator that will be used to determine test cases and all I wanted
# to do at this point was verify the asserTrue() call worked properly.
# In addition, I will be breaking up some of the otterassert features
# and adding them to this file.
#

from unittestframework import UnitTestFramework

class Runner:

    testCases = [
                    { "condition": True, "description": "case 1" },
                    { "condition": False, "description": "case 2" },
                    { "condition": True, "description": "case 3" },
                ]

    def __init__(self):
        pass


    def run(self):
        utf = UnitTestFramework()
        for case in self.testCases:
            # print(case)
            # print(value)
            utf.assertTrue(case["condition"], case["description"])
        utf.printResults()


test = Runner()
test.run()
