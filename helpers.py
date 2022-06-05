import yaml


def get_test_cases(problem: str) -> dict:
    with open("enjoy-coding/" + problem + "/test-cases.yaml", "r") as stream:
        try:
            data = yaml.safe_load(stream)
            return data['test_cases']
        except yaml.YAMLError as exc:
            print(exc)
