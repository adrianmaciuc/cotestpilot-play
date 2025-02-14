

from playwright.async_api import async_playwright, Page # type: ignore
import time, json, os, logging, playwright_async_cotestpilot, unittest

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
        # Generate and verify report
        report_path = await self.page.ai_report(output_dir="ai_check_results_academy")
        
        # Verify report was created
        self.assertTrue(os.path.exists(report_path), f"Report file not found at {report_path}")

        """Clean up after each test"""
        await self.context.close()
        await self.browser.close()
        await self.playwright.stop()

    async def test_academy_home(self):
        await self.page.goto('https://academybugs.com/find-bugs/')
        await self.page.wait_for_load_state('networkidle')
        
        # Run AI check
        await self.page.ai_check(
            testers=['Adriano'],
            label='academy_bugs',
            save_to_file=True,
            output_dir="ai_check_results_academy"
        )
        

    async def test_academy_yellow_shoe(self):
        await self.page.goto('https://academybugs.com/store/dnk-yellow-shoes/')
        await self.page.wait_for_load_state('networkidle')
        
        # Run AI check
        await self.page.ai_check(
            label='academy_bugs',
            save_to_file=True,
            output_dir="ai_check_results_academy"
        )
        
    

if __name__ == '__main__':
    unittest.main()