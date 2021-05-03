from django.test import SimpleTestCase
from courses.forms import CreateClassForm,CreateLectureForm
from unittest import mock
from django.core.files import File
from unittest.mock import MagicMock
class TestForms(SimpleTestCase):
    def test_create_class_form_with_valid_data(self):
        form =CreateClassForm(data={
            'title':'class1',
            'description':'description'
        })
        self.assertTrue(form.is_valid())
    def test_create_class_form_with_no_data(self):
        form =CreateClassForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)
    
    def test_create_lecture_form_with_valid_data(self):
        file_mock = mock.MagicMock(spec=File, name='FileMock')
        form =CreateLectureForm(data={
            'name':'Lecture1',
            'position':1,
            'description':'description',
            'video': file_mock,
            'ppt':file_mock,
            'notes':file_mock
        })
        self.assertTrue(form.is_valid())
    
    def test_create_lecture_form_with_no_data(self):
        form =CreateClassForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)
      
