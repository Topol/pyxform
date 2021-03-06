from unittest import TestCase
from pyxform.builder import create_survey_from_path
from pyxform.xls2json import SurveyReader
import utils


class SettingsTests(TestCase):

    def setUp(self):
        self.path = utils.path_to_text_fixture("settings.xls")

    def test_survey_reader(self):
        survey_reader = SurveyReader(self.path)
        expected_dict = {
            u'id_string': u'new_id',
            u'default_language': u'default',
            u'name': u'settings',
            u'title': u'My Survey',
            u'type': u'survey',
            u'children': [
                {
                    u'name': u'your_name',
                    u'text': {u'english': u'What is your name?'},
                    u'type': u'text'
                    },
                {
                    u'name': u'your_age',
                    u'text': {u'english': u'How many years old are you?'},
                    u'type': u'integer'
                    }
                ],
            }
        self.assertEqual(survey_reader.to_json_dict(), expected_dict)

    def test_settings(self):
        survey = create_survey_from_path(self.path)
        self.assertEqual(survey.id_string, "new_id")
        self.assertEqual(survey.title, "My Survey")
