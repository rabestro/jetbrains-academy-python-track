from typing import List

from hstest.check_result import CheckResult
from hstest.stage_test import StageTest
from hstest.test_case import TestCase


class TestStage2(StageTest):

    def generate(self) -> List[TestCase]:
        list_tests = [
            TestCase(stdin='42', attach=['42', '4200']),
            TestCase(stdin='75', attach=['75', '7500'])

        ]

        return list_tests

    def check(self, reply: str, attach) -> CheckResult:
        reply_parsed = reply.strip().splitlines()
        if len(reply_parsed) != 3:
            return CheckResult.wrong("Check your output")
        first_parsed = reply_parsed[0].split()
        if len(first_parsed) != 4:
            return CheckResult.wrong("Check your first line")
        try:
            amount = int(first_parsed[2])
        except ValueError:
            return CheckResult.wrong("Format your output"
                                     "according to the example")
        if amount != int(attach[0]):
            return CheckResult.wrong("The amount of money is wrong")
        second_parsed = reply_parsed[1].split()
        if len(second_parsed) != 5:
            return CheckResult.wrong("Check your second line")
        try:
            amount = int(second_parsed[0])
            dollars = int(second_parsed[3])
        except ValueError:
            return CheckResult.wrong("Format your output"
                                     "according to the example")
        if amount != int(attach[0]) or dollars != int(attach[1]):
            return CheckResult.wrong("The amount of monet is wrong")
        if "i am rich" not in reply_parsed[2].lower():
            return CheckResult.wrong("Your output differs from the example")

        return CheckResult.correct()


if __name__ == '__main__':
    TestStage2("cconverter.cconverter").run_tests()
