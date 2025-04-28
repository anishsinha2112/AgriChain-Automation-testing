# AgriChain-Automation-testing

agrichain_test_framework/
│
├── tests/
│   └── test_longest_substring.py         # Test scenarios
│
├── pages/
│   ├── home_page.py                       # HomePage object (input box, submit button)
│   └── result_page.py                     # ResultPage object (output text locator)
│
├── fixtures/
│   └── conftest.py                        # Browser setup, teardown
│
├── utils/
│   └── config.py                          # Base URL, Test Data
│
├── requirements.txt                       # Dependencies (selenium, pytest, etc.)
├── README.md
└── pytest.ini                             # Test run configs
