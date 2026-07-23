# examples/few_shot_examples.py

FEW_SHOT_EXAMPLES = {

    "order_status": """
Example 1

Customer:
Where is my order?

Support:
I'd be happy to help!
Could you please provide your Order ID so I can check its current status?

---------------------------------------

Example 2

Customer:
Track my package.

Support:
Sure!
Please share your Order ID, and I'll help you track your shipment.
""",

    "refund": """
Example 1

Customer:
I want a refund.

Support:
I'm sorry to hear that.

I'd be happy to assist you.

Could you please provide your Order ID so I can verify your purchase before proceeding?

---------------------------------------

Example 2

Customer:
Return my product.

Support:
Certainly!

Please provide your Order ID so I can guide you through the return and refund process.
""",

    "billing": """
Example 1

Customer:
I was charged twice.

Support:
I'm sorry for the inconvenience.

Could you please provide your transaction ID or Order ID so I can investigate the duplicate charge?

---------------------------------------

Example 2

Customer:
Payment failed.

Support:
Could you let me know which payment method you used and whether any amount was deducted?
""",

    "technical": """
Example 1

Customer:
The app keeps crashing.

Support:
I'm sorry you're experiencing this issue.

Please try restarting the application and ensure you're using the latest version.

If the issue continues, I'll help you with further troubleshooting.

---------------------------------------

Example 2

Customer:
The website won't load.

Support:
Please check your internet connection and try refreshing the page.

If the problem persists, let me know the browser and device you're using.
""",

    "account": """
Example 1

Customer:
I forgot my password.

Support:
No problem!

Click the 'Forgot Password' option on the login page and follow the instructions sent to your registered email.

---------------------------------------

Example 2

Customer:
I can't log into my account.

Support:
Please confirm whether you're receiving an error message and whether you've recently changed your password.
""",

    "faq": """
Example

Customer:
What are your business hours?

Support:
Our support team is available Monday through Friday from 9:00 AM to 6:00 PM.
"""
}
