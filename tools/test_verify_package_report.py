import copy
import unittest

from verify_package_report import qualify


class QualificationTests(unittest.TestCase):
    def setUp(self):
        self.report = {"commit": "a" * 40, "app_version": "0.1.2~ynh1", "architecture": "amd64", "yunohost_version": "12.1.41.2", "level": 0,
            "tests": [{"test_type": kind, "test_arg": "", "main_result": "success"} for kind in
                ("TEST_PACKAGE_LINTER", "TEST_INSTALL", "TEST_BACKUP_RESTORE", "TEST_UPGRADE", "TEST_CHANGE_URL")]}
        self.report["tests"].append({"test_type": "TEST_UPGRADE", "test_arg": "old-release", "main_result": "success"})
        self.linter = {"error": ["AppCatalog.state_is_working"], "critical": ["AppCatalog.is_in_catalog"], "warning": []}

    def test_distinguishes_arcenal_evidence_from_unchanged_official_grade(self):
        original = copy.deepcopy(self.report)
        result = qualify([self.report], self.linter, "old-release")
        self.assertEqual(result["arcenal_technical_level"], 5)
        self.assertEqual(result["evidence"][0]["level"], 0)
        self.assertEqual(self.report, original)

    def test_failed_upgrade_never_gets_a_working_grade(self):
        self.report["tests"][-1]["main_result"] = "failure"
        with self.assertRaises(ValueError):
            qualify([self.report], self.linter, "old-release")

    def test_missing_old_version_upgrade_is_rejected(self):
        self.report["tests"].pop()
        with self.assertRaises(ValueError):
            qualify([self.report], self.linter, "old-release")

    def test_real_linter_error_is_not_dismissed_as_catalog_metadata(self):
        self.linter["error"].append("Scripts.invalid_helper")
        with self.assertRaises(ValueError):
            qualify([self.report], self.linter, "old-release")

    def test_empty_report_is_not_a_success(self):
        with self.assertRaises(ValueError):
            qualify([], self.linter, "old-release")


if __name__ == "__main__":
    unittest.main()
