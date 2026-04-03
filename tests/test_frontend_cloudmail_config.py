import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SETTINGS_PAGE = ROOT / "frontend" / "src" / "pages" / "Settings.tsx"
REGISTER_PAGE = ROOT / "frontend" / "src" / "pages" / "RegisterTaskPage.tsx"


class FrontendCloudMailConfigTests(unittest.TestCase):
    def test_settings_page_exposes_standard_cloudmail_option_and_fields(self):
        content = SETTINGS_PAGE.read_text(encoding="utf-8")

        self.assertIn("value: 'cloudmail'", content)
        self.assertIn("label: 'CloudMail（标准版）'", content)
        self.assertIn("title: 'CloudMail'", content)
        self.assertIn("key: 'cloudmail_base_url'", content)
        self.assertIn("key: 'cloudmail_admin_email'", content)
        self.assertIn("key: 'cloudmail_admin_password'", content)
        self.assertIn("key: 'cloudmail_domain'", content)
        self.assertIn("key: 'cloudmail_subdomain'", content)
        self.assertIn("key: 'cloudmail_subdomains'", content)

    def test_register_page_exposes_standard_cloudmail_option_and_payload(self):
        content = REGISTER_PAGE.read_text(encoding="utf-8")

        self.assertIn("value: 'cloudmail'", content)
        self.assertIn("label: 'CloudMail'", content)
        self.assertIn("cloudmail_base_url: values.cloudmail_base_url", content)
        self.assertIn("cloudmail_admin_email: values.cloudmail_admin_email", content)
        self.assertIn("cloudmail_admin_password: values.cloudmail_admin_password", content)
        self.assertIn("cloudmail_domain: values.cloudmail_domain", content)
        self.assertIn("cloudmail_subdomain: values.cloudmail_subdomain", content)
        self.assertIn("cloudmail_subdomains: values.cloudmail_subdomains", content)
        self.assertIn("mailProvider === 'cloudmail'", content)


if __name__ == "__main__":
    unittest.main()
