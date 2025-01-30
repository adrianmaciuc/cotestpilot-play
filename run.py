from playwright.async_api import async_playwright
import playwright_async_cotestpilot
import asyncio
from playwright_async_cotestpilot import configure_logging, LogLevel

# Configure logging and settings
configure_logging(
    level="DEBUG",
    console_verbosity=LogLevel.VERBOSE,
    config={
        'api_rate_limit': 0.25,        # API calls per second
        'screenshot_retention_days': 7,  # Screenshot retention period
        'max_retries': 5                # API call retry attempts
    }
)

async def main():
    # Initialize Playwright and navigate to a page
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto('https://z.martioli.com')

        # Basic AI check with additional options
        result = await page.ai_check(
            console_verbosity=LogLevel.BASIC,  # Control logging for this check
            save_to_file=True,                 # Save results to JSON file
            output_dir="ai_check_results"      # Directory for results
        )
        print(f"Found {len(result.bugs)} issues")

        # Generate HTML report
        report_path = await page.ai_report(output_dir="ai_check_results")
        print(f"Report generated at: {report_path}")

# Run the async function
asyncio.run(main())