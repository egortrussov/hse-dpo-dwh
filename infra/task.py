import datetime as dt

class Task:

    def __init__(self, client, runner_function):
        self.client = client
        self.runner_function = runner_function

    def configure_deps(self, inputs, outputs):
        self._dependencies = {
            "inputs": inputs,
            "outputs": outputs,
        }


    def get_depencencies(self):
        return self._dependencies


    def run(self, task_date = None, **kwargs):
        if task_date is None:
            task_date = dt.datetime.now()

        self.runner_function(
            self.client,
            self.get_depencencies()["inputs"],
            self.get_depencencies()["outputs"],
            task_date=task_date,
            **kwargs,
        )


