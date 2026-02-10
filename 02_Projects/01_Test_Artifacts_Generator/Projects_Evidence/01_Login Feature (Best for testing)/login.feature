Feature: Login Feature
User login functionality

Scenario: Successful login
Given the user has a valid email and password
When the user attempts to login
Then the user should be logged in successfully

Scenario: Invalid credentials
Given the user has an invalid email or password
When the user attempts to login
Then an error message should be displayed

Scenario: Account lock after 5 failed attempts
Given the user has attempted to login 5 times with invalid credentials
When the user attempts to login again
Then the account should be locked

Scenario: Forgot password
Given the user has forgotten their password
When the user requests a password reset
Then an OTP should be sent to the user's email

Scenario: Password reset using OTP
Given the user has received the OTP
When the user enters the correct OTP and new password
Then the password should be reset successfully