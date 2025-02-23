from playwright.async_api import async_playwright, Page # type: ignore
import time, json, os, logging, playwright_async_cotestpilot, unittest, asyncio

# Add logging configuration
logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

class TestPlaywrightPage(unittest.IsolatedAsyncioTestCase):  # Changed base class
    async def asyncSetUp(self):  # Changed to async setup
        """Set up test environment before each test"""
        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.chromium.launch(headless=False)
        self.context = await self.browser.new_context()
        self.page = await self.context.new_page()

    async def asyncTearDown(self):  # Changed to async teardown
        await self.page.ai_report(output_dir="ai_check_results")
        """Clean up after each test"""
        await self.context.close()
        await self.browser.close()
        await self.playwright.stop()

    async def test_playwright_navigation(self):  # Made test async
 
        await self.page.goto('https://www.playwright.dev/')
        await self.page.ai_check(label='with_no_testers')
        # Generate HTML report
        await self.page.ai_report(output_dir="ai_check_results")
        await asyncio.sleep(1)

    async def test_ai_check_with_testers(self):  # Made test async
        await self.page.goto('https://www.playwright.dev/')
        
        await self.page.ai_check(
            testers=['Jason', 'Alice'],
            label='with_testers'
        )

    async def test_ai_check_with_custom_rules(self):  # Made test async
        await self.page.goto('https://www.google.com')
        await self.page.wait_for_load_state('networkidle')
        
        await self.page.ai_check(
            custom_rules={
                'check_contrast': True,
                'min_font_size': 12
            },
            custom_prompt="Pay special attention to accessibility issues"
        )
        

if __name__ == '__main__':
    unittest.main()