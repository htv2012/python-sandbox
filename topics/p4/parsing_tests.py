import unittest

from parsing import get_views


class GetViewsTests(unittest.TestCase):
    longMessage = True

    def test_data_dev(self):
        client_json = {
            "Access": "2016/09/01 15:26:44",
            "Client": "hvu-mac-data-dev",
            "Description": "Created by hvu.\n",
            "Host": "hvu-mac",
            "LineEnd": "unix",
            "Options": "noallwrite noclobber nocompress unlocked nomodtime rmdir",
            "Owner": "hvu",
            "Root": "/Volumes/dev/data-dev",
            "SubmitOptions": "revertunchanged",
            "Update": "2016/02/23 14:44:59",
            "View0": "//depot/teams/data-dev/... //hvu-mac-data-dev/...",
            "View1": "//depot/private/hvu/... //hvu-mac-data-dev/private/...",
            "View2": "//depot/infrastructure/pycentral/... //hvu-mac-data-dev/pycentral/...",
            "code": "stat",
        }
        actual = get_views(client_json)
        expected = [
            ["//depot/teams/data-dev/...", "//hvu-mac-data-dev/..."],
            ["//depot/private/hvu/...", "//hvu-mac-data-dev/private/..."],
            [
                "//depot/infrastructure/pycentral/...",
                "//hvu-mac-data-dev/pycentral/...",
            ],
        ]
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
