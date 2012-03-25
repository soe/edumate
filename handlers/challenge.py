from handlers import AbstractHandler

#('/challenge/all', 'handlers.challenge.All'),
#('/challenge/sample', 'handlers.challenge.Sample'),
#('/challenge/edit', 'handlers.challenge.Edit'),
#('/challenge/judge', 'handlers.challenge.Judge'),

class All(AbstractHandler):

    def get(self):

        template_vars = {
            'header': 'Challenges',
        }
        self._output_template('challenge_all.html', **template_vars)
        
class Sample(AbstractHandler):

    def get(self):

        template_vars = {
            'header': 'A sample challenge',
        }
        self._output_template('challenge_sample.html', **template_vars)
        
class Edit(AbstractHandler):

    def get(self):

        template_vars = {
            'header': 'Challenge - create/edit page',
        }
        self._output_template('challenge_edit.html', **template_vars)
        
class Judge(AbstractHandler):

    def get(self):

        template_vars = {
            'header': 'Challenge - Judging scorecard',
        }
        self._output_template('challenge_judge.html', **template_vars)