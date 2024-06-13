# Virtual Wallet

## Project Description

Virtual Wallet is a web application that enables you to manage your budget. Every user can send and receive money (user to user) and put money in their Virtual Wallet (bank to app).

## Functional Requirements

### Entities:

#### Users:

- Users can be regular users and admins. Each user must have a username, password, email, and phone number. They can also have a photo. The username for regular users cannot be amended.
- Regular users must also have credit/debit cards.
- Regular users must be able to register/login, view their credit information, transfer money between own credit/debit cards, transfer money to other users, and confirm, deny, or view their transactions.
- Admins can authorize regular users' registrations, deactivate access for users, and block accounts. The admin role comes with predefined log-in details where only the password can be amended.

#### Credit/Debit Card:

- A credit/debit card must have a number, expiration date, cardholder, and a check number (CVV).
- A user must be able to register multiple credit and/or debit cards, from which to transfer funds to and from their account.
- Each card should have a personalized design.
- Users should be able to set up recurring transactions. When creating a transaction, the user has the option to select an interval of time on which the transaction is repeated automatically. Users have a page where they can view all their recurring transactions and cancel them. Users should be notified if their transactions fail for some reason.
- In addition to searching through all the application users, a user should be able to create a contacts list. A user can add another user to their contacts list and remove users from the list.
- When creating a transaction, a user should be able to select a category for the transfer (Rent, Utilities, Eating out, etc.). They can add, edit, or delete categories and see reports for each category for a certain period.

### Public Part

Accessible without authentication (for anonymous users):

- Anonymous users must be able to register and login. The username must be unique and between 2 and 20 symbols. The password must be at least 8 symbols and should contain a capital letter, digit, and special symbol (+, -, *, &, ^, …). The email must be valid and unique in the system. The phone number must be 10 digits and unique in the system.
- Anonymous users must see detailed information about Virtual Wallet and its features.

## Endpoints for Registered Users

Accessible only if the user is authenticated:

- Users must be able to login/logout.
- Users must be able to view and update their profile (except the username).
- Regular users can review their account and credit/debit cards, category list, contact list, and transaction history for their account (info page).
- Users must be able to register/delete a credit/debit card. The card number must be unique and have 16 digits. The cardholder must be between 2 and 30 symbols. The check number must be 3 digits.
- Users can create and add other users to their contacts list.
- Users can search through their contacts list and transfer money to other accounts. Users can search by phone number, username, or email to select the recipient user for the transfer, but when viewing recipient users, only the username must be displayed.
- Users should be able to make recurring transactions and access a list of all their recurring transactions.
- Users should be able to create categories and link different transactions to these categories.
- Each transfer must go through a confirmation step which displays the transfer details and allows either confirming it or editing it.
- The receiver of the money must be able to accept or decline the transaction.
- Users must be able to withdraw money from their account.
- Users should be able to view a list of their transactions filtered by period, recipient, and direction (incoming or outgoing) and sort them by amount and date. The transaction list should support pagination.

## Administrative Part

Accessible to users with administrative privileges:

- Admin users can approve registrations for regular users (via email).
- Admin users can see the list of all users and search them by phone number, username, or email and block or unblock them. The user list should support pagination. A blocked user can do everything a normal user can, except make transactions.
- Admin users can view a list of all user transactions filtered by period, sender, recipient, and direction (incoming or outgoing) and sort them by amount and date. The transaction list should support pagination.
- Admin users can deny pending transactions.

### Optional Features

- Search endpoints should support pagination and sorting.
- Email Verification for the users could be implemented. For the registration to be completed, the user must verify their email by clicking on a link sent to their email by the application. Before verifying their email, users cannot make transactions.
- Email notifications could be supported (e.g., using a third-party service like [Mailjet](https://dev.mailjet.com/email/guides/send-api-v31/)).
- Add Easter eggs whenever possible. Creativity is always welcome and appreciated. Find a way to add something fun and/or interesting, maybe an Easter egg or two to your project to add some variety.

## REST API - Summary

To provide other developers with your service, you need to develop a REST API. It should leverage HTTP as a transport protocol and clear text JSON for the request and response payloads.

A great API is nothing without great documentation. You must use Swagger to document yours.

The REST API provides the following capabilities:

1. **Users**
   - CRUD Operations
   - Add/view/update/delete profile and credit/debit card
   - Search for users, accounts, transactions
   - Block/unblock user

2. **Transactions**
   - Add money to wallet
   - Make transactions
   - Approve/decline transactions
   - List transactions
   - Filter by date, sender, recipient, and direction (in/out)
   - Sort by date or amount
   - Withdraw

## Technical Requirements

### General

- Follow KISS, SOLID, and DRY principles when coding.
- Follow REST API design best practices when designing the REST API.
- Use a tiered project structure (separate the application into layers).
- The service layer (i.e., "business" functionality) must have at least 60% unit test code coverage.
- Implement proper exception handling and propagation.
- Think ahead. When developing something, think – “How hard would it be to change/modify this later?”

### Database

The data of the application must be stored in a relational database. You need to identify the core domain objects and model their relationships accordingly. Database structure should avoid data duplication and empty data (normalize your database).

Your repository must include two scripts – one to create the database and one to fill it with data.

### Git

Commits in the GitHub repository should give a good overview of how the project was developed, which features were created first, and the people who contributed. Contributions from all team members must be evident through the git commit history. The repository must contain the complete application source code and any scripts (database scripts, for example).

Provide a link to a GitHub repository with the following information in the README.md file:

- Project description
- Link to the Swagger documentation
- Link to the hosted project (if hosted online)
- Instructions on how to setup and run the project locally
- Description of the project structure
- Technologies that are used, e.g., framework, RDBMS
- Images of the database relations

### Optional Requirements

- Use branching while working with Git.
- Integrate your app with a Continuous Integration server (e.g., GitHub’s own) and configure your unit tests to run on each commit to the master branch.
- Host your application’s backend in a public hosting provider of your choice (e.g., AWS, Azure, Heroku).

## Teamwork Guidelines

Please see the Teamwork Guidelines document.

## Appendix

- Guidelines for designing good REST API
- Guidelines for URL encoding
- [Git commits – an effective style guide](https://www.vojtechruzicka.com/field-dependency-injection-considered-harmful/)

## Legend

- **Must** – implement these first.
- **Should** – if you have time left, try to implement these.
- **Could** – implement if you have extra time and want to add additional features.
