# from playwright.async_api import async_playwright
# import playwright_async_cotestpilot
# import asyncio
# from playwright_async_cotestpilot import configure_logging, LogLevel

# # Configure logging and settings
# configure_logging(
#     level="DEBUG",
#     console_verbosity=LogLevel.VERBOSE,
#     config={
#         'api_rate_limit': 0.25,        # API calls per second
#         'screenshot_retention_days': 7,  # Screenshot retention period
#         'max_retries': 5                # API call retry attempts
#     }
# )

# async def main():
#     # Initialize Playwright and navigate to a page
#     async with async_playwright() as p:
#         browser = await p.chromium.launch()
#         page = await browser.new_page()
#         await page.goto('https://www,playwright.dev/')

#         # Basic AI check with additional options
#         result = await page.ai_check(
#             console_verbosity=LogLevel.BASIC,  # Control logging for this check
#             save_to_file=True,                 # Save results to JSON file
#             output_dir="ai_check_results"      # Directory for results
#         )
#         print(f"Found {len(result.bugs)} issues")

#         # Generate HTML report
#         report_path = await page.ai_report(output_dir="ai_check_results")
#         print(f"Report generated at: {report_path}")

# # Run the async function
# asyncio.run(main())

"""
How to run these tests:
1. From command line:
   python -m unittest test.py

Requirements:
- playwright >= 1.41.0
- playwright-cotestpilot >= 0.1.0

Note: Before running, ensure browsers are installed:
    playwright install chromium
"""

import unittest
import asyncio
from unittest import skipIf
from playwright.async_api import async_playwright, Page, Browser, BrowserContext, Playwright
import time
import playwright_async_cotestpilot
import json
import os
import logging

# Add logging configuration
logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

class TestPlaywrightPage(unittest.IsolatedAsyncioTestCase):  # Changed base class
    page: Page
    async def asyncSetUp(self):  # Changed to async setup
        """Set up test environment before each test"""
        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.chromium.launch(headless=False)
        self.context = await self.browser.new_context()
        self.page:Page = await self.context.new_page()

    async def asyncTearDown(self):  # Changed to async teardown
        """Clean up after each test"""
        await self.context.close()
        await self.browser.close()
        await self.playwright.stop()

    async def test_automation_exercise(self):  # Made test async
 
        await self.page.goto('https://practice-automation.com/')
        await self.page.wait_for_load_state('networkidle')
        await self.page.ai_check(label='with_no_testers')
        # Generate HTML report
        await self.page.ai_report(output_dir="ai_check_results")
        await asyncio.sleep(1)


if __name__ == '__main__':
    # Create and run test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPlaywrightPage)
    runner = unittest.TextTestRunner()
    asyncio.run(runner.run(suite))