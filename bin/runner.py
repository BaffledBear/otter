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
