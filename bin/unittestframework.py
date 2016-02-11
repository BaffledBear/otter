class UnitTestFramework:

    successCount = 0
    failCount = 0
    passedTests = []
    failedTests = []


    def __init__(self):
        pass


    def assertTrue(self, statusBool, testCase):
        if statusBool:
            self.successCount += 1
            self.logSuccess(testCase)
        else:
            self.failCount += 1
            self.logFail(testCase)


    def logSuccess(self, testCase):
        self.passedTests.append(testCase)


    def logFail(self, testCase):
        self.failedTests.append(testCase)


    def printResults(self):
        print("Number of Successes: {}".format(self.successCount))
        for case in self.passedTests:
            print("\t{}".format(case))
        print("")
        print("Number of Failures:  {}".format(self.failCount))
        for case in self.failedTests:
            print("\t{}".format(case))
