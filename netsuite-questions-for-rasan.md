# NetSuite Questions, for Rasan

Robin, this is the note I mentioned. Feel free to forward it to Rasan as-is.

## Context

Innovive has HubSpot in place as the CRM. Because the e-commerce site runs on NetSuite, the customer and order history that would make HubSpot useful to the sales team already lives in NetSuite. We want to connect the two.

HubSpot publishes a native NetSuite connector that is included on all HubSpot plans. If it fits, this is quick and inexpensive. If it does not fit, the alternative is integration middleware, which is a real project with real cost. Five questions decide which one we are looking at, and only someone inside the NetSuite account can answer them.

## The questions

**1. Is this NetSuite OneWorld, and if so how many subsidiaries are active?**
This is the big one. HubSpot's native connector syncs to a single subsidiary and cannot run separate syncs for the same record type across several. If Innovive, Innocycle, InnoPlus, and Nextbeam are separate subsidiaries in one OneWorld account, the native connector will not cover it and we need a different approach.

**2. Can you enable these in NetSuite, and are there any policy reasons not to?**
- REST Web Services
- OAuth 2.0 and token-based authentication
- Server-side RESTlets (SuiteScript)
- SuiteAnalytics Workbook

These require Administrator rights, and the setup also installs a bundle. This is not something we can do from our side.

**3. Is the storefront SuiteCommerce, SuiteCommerce Advanced, or something else?**
We want to understand where orders originate and which record they land on.

**4. Are you using custom records or heavily customized sales order flows?**
The native connector does not support NetSuite custom records, and it can struggle with complex sales order creation. If either is central to how Innovive operates, that changes the recommendation.

**5. How do you want customer records to work between the two systems?**
Specifically: should NetSuite stay the system of record for customers and Innovive's sales team simply read that history in HubSpot, or do you want records created in HubSpot to flow back into NetSuite? Both are possible. The first is much simpler and is usually the right starting point.

One related note: the native connector maps HubSpot Contacts to NetSuite Contacts and skips the NetSuite Lead stage. If Lead status matters to your process, tell us and we will plan around it.

## What happens next

Once we have these answers we will come back with a recommendation and a cost. We are deliberately not quoting anything until we understand the account, because the honest range here runs from "essentially free" to a five-figure integration project depending entirely on the answers above.

Happy to get on a call instead if that is easier.

Collin Wood
collin@voladolabs.com
