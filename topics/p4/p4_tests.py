import os
import unittest

from p4 import Perforce


class TestBase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        root = "sandbox"
        os.chdir("/Users/haiv/projects/p4/{}".format(root))
        cls.enlistment = "//{}".format(root)

    def setUp(self):
        self.p4 = Perforce()
        self.contents = {}
        self.temp_files = []

    def tearDown(self):
        os.system("p4 revert *")
        for f in self.temp_files:
            os.remove(f)

    # ==================================================================
    # Helpers
    # ==================================================================
    def file_to_enlistment(self, filename):
        return os.path.join(self.enlistment, filename)

    def checkout(self, filename, modify_contents=False):
        expected = [self.file_to_enlistment(filename)]
        actual = self.p4.edit([filename])
        self.assertEqual(expected, actual)

        if modify_contents:
            with open(filename, "a") as f:
                f.write("\nModified\n")

    def create_temp_file(self, filename):
        self.temp_files.append(filename)
        with open(filename, "wb") as f:
            f.write("# New file")

    def revert_checkout(self, filename):
        self.p4.revert(filename)

    def save_contents(self, filename):
        self.contents[filename] = open(filename).read()

    def verify_contents_unchanged(self, filename):
        new_contents = open(filename).read()
        self.assertEqual(
            new_contents,
            self.contents[filename],
            "Contents changed for {}".format(filename),
        )

    def verify_contents_changed(self, filename):
        new_contents = open(filename).read()
        self.assertNotEqual(
            new_contents,
            self.contents[filename],
            "Contents changed for {}".format(filename),
        )

    def verify_checkedout(self, filename):
        expected = [self.file_to_enlistment(filename)]
        actual = self.p4.opened(filename)
        self.assertEqual(expected, actual, "File not checked out: {}".format(filename))

    def verify_not_checkedout(self, filename):
        expected = [self.file_to_enlistment(filename)]
        actual = self.p4.opened(filename)
        self.assertNotEqual(
            expected, actual, "File not checked out: {}".format(filename)
        )


class AddTest(TestBase):
    def test_add(self):
        filename = "new_file.py"
        self.create_temp_file(filename)
        self.p4.add(filename)
        self.verify_checkedout(filename)

    def test_add_existing(self):
        filename = "hello.py"
        self.assertIsNone(self.p4.add(filename))


class CreateChangeListTests(TestBase):
    def test_create_simple_change_list(self):
        pass


class EditTests(TestBase):
    def test_single_file(self):
        filename = "hello.py"
        expected = [self.file_to_enlistment(filename)]
        actual = self.p4.edit(filename)
        self.assertEqual(expected, actual)

    def test_multiple_files(self):
        expected = ["//sandbox/hello.py", "//sandbox/basetest.py"]
        actual = self.p4.edit(["hello.py", "basetest.py"])
        self.assertEqual(expected, actual)

    def test_non_existing_file(self):
        self.assertIsNone(self.p4.edit(["foobar"]))


class OpenedTests(TestBase):
    def test_check_out_single_file(self):
        filename = "hello.py"
        self.p4.edit(filename)
        expected = [self.file_to_enlistment(filename)]
        actual = self.p4.opened(filename)
        self.assertEqual(expected, actual, "File not checked out: {}".format(filename))

    def test_check_out_multiple_files(self):
        filenames = ["hello.py", "basetest.py"]
        self.p4.edit(filenames)
        expected = [self.file_to_enlistment(f) for f in filenames]
        actual = self.p4.opened(filenames)
        self.assertEqual(expected, actual)

    def test_opened_without_filenames(self):
        filename = "hello.py"
        self.p4.edit(filename)
        expected = [self.file_to_enlistment(filename)]
        actual = self.p4.opened()
        self.assertEqual(expected, actual, "File not checked out: {}".format(filename))


class ScenarioTests(TestBase):
    def test_edit_change_revert(self):
        filename = "hello.py"
        self.save_contents(filename)
        self.checkout(filename, modify_contents=True)
        self.revert_checkout(filename)
        self.verify_contents_unchanged(filename)

    def test_revert_unchanged(self):
        unmodified = "basetest.py"
        modified = "hello.py"

        self.save_contents(unmodified)
        self.save_contents(modified)

        self.checkout(modified, modify_contents=True)
        self.verify_contents_changed(modified)

        self.checkout(unmodified)
        self.verify_contents_unchanged(unmodified)

        self.p4.revert_unchanged([unmodified, modified])
        self.verify_contents_unchanged(unmodified)
        self.verify_contents_changed(modified)

        self.verify_checkedout(modified)
        self.verify_not_checkedout(unmodified)


if __name__ == "__main__":
    unittest.main()
