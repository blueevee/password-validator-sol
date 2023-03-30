import re
from api.Errors import VerifyError
from api.Helpers import minDigit, minSize, minLowercase, \
    minSpecialChars, minUppercase, noRepeted
    

def verify_resolver(self, info, password, rules):

    def is_rule_valid(rule):
        func = globals()[rule['rule']]
        return func(password, rule['value'])
    print(info)
    only_rules_status = list(map(is_rule_valid, rules))
    all_rules = list(map(lambda rule: rule["rule"], rules))
    rules_status = list(zip(all_rules, only_rules_status))
    invalid_rules = [rule[0] for rule in rules_status if not rule[1]]

    if len(invalid_rules):
        error_payload = {
            'verify': False,
            'noMatch': invalid_rules
        }
        return error_payload

    payload = {
            'verify': True,
            'noMatch': invalid_rules
        }
    return payload
