from typing import List

import ast
import json
import requests
from hstest.check_result import CheckResult
from hstest.stage_test import StageTest
from hstest.test_case import TestCase


class TestStage5(StageTest):

    def generate(self) -> List[TestCase]:
        list_tests = [
            TestCase(stdin='HNL', attach='HNL'),
            TestCase(stdin='ILS', attach='ILS')

        ]

        return list_tests

    def check(self, reply: str, attach) -> CheckResult:
        reply_parsed = [i for i in reply.split('\n') if i]
        json_to_be = requests.get(f"http://www.floatrates.com/daily/{attach}.json").text
        usd_json = json.loads(json_to_be)['usd']
        eur_json = json.loads(json_to_be)['eur']
        he = {}
        jsons = [usd_json, eur_json]
        if len(reply_parsed) != 2:
            return CheckResult.wrong("Your output is incorrect")
        for i, repl in enumerate(reply_parsed):
            try:
                repl = ast.literal_eval(repl)
            except ValueError:
                return CheckResult.wrong("The format of the data is incorrect")
            if type(repl) != dict:
                return CheckResult.wrong("Your output should contain a dictionary.\n"
                                         "Make sure the format of your output is correct.")
            for key in repl.keys():
                try:
                    if repl[key] != jsons[i][key]:
                        return CheckResult.wrong("Make sure your output is right")
                except KeyError:
                    return CheckResult.wrong("The key needed is absent in your data")

        return CheckResult.correct()


if __name__ == '__main__':
    TestStage5("cconverter.cconverter").run_tests()
