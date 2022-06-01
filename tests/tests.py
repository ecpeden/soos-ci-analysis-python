import pathlib
import subprocess
import unittest

test_complete_success = "Analysis Completed Successfully"
test_complete_fail = "Analysis complete - Failures reported"


def vulnerabilities(x):
    return f"Vulnerabilities: {x}"


def violations(x):
    return f"Violations: {x}"


class GemfileTestCases(unittest.TestCase):
    def test_gemfile(self):
        print("testing gemfile")
        process = subprocess.run([pathlib.Path("./manifests/gemfile/script.sh").resolve()], shell=True, capture_output=True, text=True)

        print(process.stdout)
        self.assertEqual(process.returncode, 1, "Invalid return code.")
        self.assertEqual(process.stdout.count(test_complete_fail), 1, "Invalid completion message.")
        # self.assertEqual(process.stdout.count(vulnerabilities(4)), 1)
        # self.assertEqual(process.stdout.count(violations(4)), 1)


class DartTestCases(unittest.TestCase):
    def test_dart(self):
        print("testing dart")
        process = subprocess.run([pathlib.Path("./manifests/dart/script.sh").resolve()], shell=True, capture_output=True, text=True)

        print(process.stdout)
        self.assertEqual(process.returncode, 0, "Invalid return code.")
        self.assertEqual(process.stdout.count(test_complete_success), 1, "Invalid completion message.")
        # self.assertEqual(process.stdout.count(vulnerabilities(2)), 1)
        # self.assertEqual(process.stdout.count(violations(5)), 1)


class GradleTestCases(unittest.TestCase):
    def test_gradle(self):
        print("testing gradle")
        process = subprocess.run([pathlib.Path("./manifests/gradle/script.sh").resolve()], shell=True, capture_output=True, text=True)

        print(process.stdout)
        self.assertEqual(process.returncode, 1, "Invalid return code.")
        self.assertEqual(process.stdout.count(test_complete_fail), 1, "Invalid completion message.")
        # self.assertEqual(process.stdout.count(vulnerabilities(59)), 1)
        # self.assertEqual(process.stdout.count(violations(5)), 1)


class RustTestCases(unittest.TestCase):
    def test_rust(self):
        print("testing rust")
        process = subprocess.run([pathlib.Path("./manifests/rust/script.sh").resolve()], shell=True, capture_output=True, text=True)

        print(process.stdout)
        self.assertEqual(process.returncode, 1, "Invalid return code.")
        self.assertEqual(process.stdout.count(test_complete_fail), 1, "Invalid completion message.")
        # self.assertEqual(process.stdout.count(vulnerabilities(7)), 1)
        # self.assertEqual(process.stdout.count(violations(5)), 1)


class NugetTestCases(unittest.TestCase):
    def test_nuget(self):
        print("testing nuget")
        process = subprocess.run([pathlib.Path("./manifests/nuget/script.sh").resolve()], shell=True, capture_output=True, text=True)

        print(process.stdout)
        self.assertEqual(process.returncode, 1, "Invalid return code.")
        self.assertEqual(process.stdout.count(test_complete_fail), 1, "Invalid completion message.")
        # self.assertEqual(process.stdout.count(vulnerabilities(1)), 1)
        # self.assertEqual(process.stdout.count(violations(5)), 1)


# class MavenTestCases(unittest.TestCase):
#     def test_maven(self):
#         print("testing maven")
#         process = subprocess.run([pathlib.Path("./manifests/maven/script.sh").resolve()], shell=True, capture_output=True, text=True)

#         self.assertEqual(process.returncode, 0)


class ComposerTestCases(unittest.TestCase):
    def test_composer(self):
        print("testing composer")
        process = subprocess.run([pathlib.Path("./manifests/composer/script.sh").resolve()], shell=True, capture_output=True, text=True)

        print(process.stdout)
        self.assertEqual(process.returncode, 0, "Invalid return code.")
        self.assertEqual(process.stdout.count(test_complete_success), 1, "Invalid completion message.")


class NPMTestCases(unittest.TestCase):
    def test_with_issues(self):
        print("testing with issues")
        process = subprocess.run([pathlib.Path("./manifests/with_issues/script.sh").resolve()], shell=True, capture_output=True, text=True)

        print(process.stdout)
        self.assertEqual(process.returncode, 1, "Invalid return code.")
        self.assertEqual(process.stdout.count(test_complete_fail), 1, "Invalid completion message.")

    def test_no_issues(self):
        print("testing without issues")
        process = subprocess.run([pathlib.Path("./manifests/no_issues/script.sh").resolve()], shell=True, capture_output=True, text=True)

        print(process.stdout)
        self.assertEqual(process.returncode, 0, "Invalid return code.")
        self.assertEqual(process.stdout.count(test_complete_success), 1, "Invalid completion message.")


class ExcludeTestCases(unittest.TestCase):
    def test_exclude_files(self):
        print("testing exclude files")
        process = subprocess.run([pathlib.Path("./manifests/exclude_files/script.sh").resolve()], shell=True, capture_output=True, text=True)

        print(process.stdout)
        self.assertEqual(process.returncode, 1, "Invalid return code.")
        files_to_exclude = "pubspec.yaml, *composer.json, cargo* "
        expected_text = f"FILES_TO_EXCLUDE: {files_to_exclude.strip()}"
        self.assertEqual(process.stdout.count(expected_text), 1)
        self.assertEqual(process.stdout.count('Skipping file due to files_to_exclude:'), 4)
        self.assertEqual(process.stdout.count('manifests/exclude_files/pubspec.yaml'), 1)
        self.assertEqual(process.stdout.count('manifests/exclude_files/composer.json'), 1)
        self.assertEqual(process.stdout.count('manifests/exclude_files/cargo.toml'), 1)
        self.assertEqual(process.stdout.count('manifests/exclude_files/cargo.lock'), 1)
        self.assertEqual(process.stdout.count('Found manifest file:'), 2)
        self.assertEqual(process.stdout.count(test_complete_fail), 1, "Invalid completion message.")

    def test_exclude_dirs(self):
        print("testing exclude dirs")
        process = subprocess.run([pathlib.Path("./manifests/exclude_dirs/script.sh").resolve()], shell=True, capture_output=True, text=True)

        print(process.stdout)
        self.assertEqual(process.returncode, 1, "Invalid return code.")
        self.assertEqual(process.stdout.count('Skipping file due to dirs_to_exclude:'), 3)
        self.assertEqual(process.stdout.count('manifests/exclude_dirs/exclude/composer.json'), 1)
        self.assertEqual(process.stdout.count('manifests/exclude_dirs/exclude/cargo.toml'), 1)
        self.assertEqual(process.stdout.count('manifests/exclude_dirs/exclude/cargo.lock'), 1)
        self.assertEqual(process.stdout.count('Found manifest file:'), 3)
        self.assertEqual(process.stdout.count(test_complete_fail), 1, "Invalid completion message.")


# class SarifTestCases(unittest.TestCase):
#     def test_sarif(self):
#         print("testing sarif")
#         process = subprocess.run([pathlib.Path("./manifests/sarif/script.sh").resolve()], shell=True, capture_output=True, text=True)

#         print(process.stdout)
#         self.assertEqual(process.returncode, 0)
#         self.assertEqual(process.stdout.count(test_complete_success), 1)
