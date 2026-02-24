# OktaSnapshot PDF Fields

This document lists the entities (sections) and the fields extracted for the OktaSnapshot PDF report.

## Organization Settings
- Address1
- Address2
- City
- Company Name
- Country
- End User Support Help URL
- Phone Number
- Postal Code
- State
- Support Phone Number
- Website
- Subdomain
- Billing Contact Email
- Technical Contact Email

## Security General Settings
- Setting
- Value

Settings included:
- Security notification emails
- New sign-on notification email
- Password changed notification email
- Authenticator enrolled notification email
- Authenticator reset notification email
- Report suspicious activity via email
- CAPTCHA integration
- CAPTCHA type
- User enumeration prevention
- Enable for Authentication
- Enable for Recovery
- Require verification with unknown device
- Protect against password-based attacks
- Require possession factor before password during MFA
- Block suspicious password attempts from unknown devices
- Okta ThreatInsight settings
- Action
- Exempt Zones
- Data Collection Enabled

## Groups
- Group Name
- Description

## Group Rules
- Rule Name
- Status
- If
- Then
- Except

## Network Zones
- Name
- Status
- Gateways
- Proxies
- Usage

## Identity Providers
Common fields:
- Name
- Type
- Protocol Type
- Status
- Policy Max Clock Skew
- Policy Account Link Action
- Policy Username Template
- Policy Provisioning Action

OIDC-specific fields:
- Endpoints (authorization, token, jwks)
- Settings
- Issuer
- Provisioning Groups To Sync

SAML/other protocol fields:
- SSO URL
- Trust Issuer
- Trust Audience
- Signing Key ID

## Authenticators
Common fields:
- Name
- Key
- Type
- Status

Email-specific fields:
- Allowed For
- Token Lifetime (Minutes)

Phone-specific fields:
- User can verify with

Security Question fields:
- Usage

Okta Verify fields:
- Compliance FIPS
- Channel Binding Style
- Channel Binding Required
- User Verification
- Enrollment Security Level
- User Verification Methods

## Authorization Servers - Settings
- ID
- Name
- Status
- Description
- Audiences
- Issuer
- Credentials Rotation Mode

## Authorization Server Claims
- Authorization Server
- Claim Name
- Status
- Claim Type
- Value Type
- Value
- Include In Token Type

## Authorization Server Scopes
- Authorization Server
- Scope Name
- Display Name
- Description
- System
- Consent

## Authorization Servers - Access Policies (Policies and Rules Combined)
Fields included for policy entries:
- Authorization Server
- Policy ID
- Policy Name
- Status
- Description
- Priority
- Conditions

Fields included for rule entries:
- Authorization Server
- Policy Name
- Rule ID
- Rule Name
- Status
- Priority
- Conditions
- Actions

Combined fields:
- Entry Type (Policy or Rule)

## Applications
Common fields:
- Name
- Status
- Type
- Groups

Non-bookmark fields:
- Okta Internal Name
- Username Format
- Logo
- Features
- Access Policy Name

Bookmark settings:
- Bookmark URL
- App Links
- Username Template

SAML 2.0 settings:
- Single Sign-On URL
- IdP Issuer
- Audience
- Recipient
- Destination
- Subject Name ID Template
- Subject Name ID Format
- Response Signed
- Assertion Signed
- Signature Algorithm
- Digest Algorithm
- Honor Force Authn
- Authentication Context Class
- Request Compressed
- Signed Request Enabled
- Allow Multiple ACS Endpoints
- ACS Endpoints
- Single Logout Enabled
- Attribute Statements
- Audience Override
- Default Relay State
- Recipient Override
- Destination Override
- SSO ACS URL Override

OIDC settings:
- Client ID
- Token Endpoint Auth Method
- PKCE Required
- Redirect URIs
- Post Logout Redirect URIs
- Grant Types
- Response Types
- Application Type
- Initiate Login URI
- Consent Method
- Issuer Mode
- Wildcard Redirect
- DPoP Bound Access Tokens
- Client URI
- Logo URI

Okta Org2Org (okta_org2org) settings:
- ACS URL
- Audience Restriction
- Base URL
- IdP ID

## Password Policies (Policies and Rules Combined)
Fields included for policy entries:
- ID
- Status
- Name
- Description
- Priority
- Provider
- Complexity Settings
- Age Settings
- Lockout Settings
- Breached Protection Settings
- Rules

Fields included for rule entries:
- Policy ID
- Policy Name
- Rule ID
- Rule Name
- Status
- Priority
- Conditions People
- Conditions Network
- Actions

Combined fields:
- Entry Type (Policy or Rule)

## Global Session Policies (Policies and Rules Combined)
Fields included for policy entries:
- ID
- Status
- Name
- Description
- Priority
- Conditions
- Rules

Fields included for rule entries:
- Policy ID
- Policy Name
- Rule ID
- Rule Name
- Status
- Priority
- Conditions People
- Conditions Network
- Conditions AuthContext
- Conditions Risk
- Conditions RiskScore
- Conditions IdentityProvider
- Actions

Combined fields:
- Entry Type (Policy or Rule)

## Authentication Policies (Policies and Rules Combined)
Fields included for policy entries:
- ID
- Status
- Name
- Description
- Priority
- Conditions
- Rules

Fields included for rule entries:
- Policy ID
- Policy Name
- Rule ID
- Rule Name
- Status
- Priority
- Conditions People
- Conditions Network
- Conditions AuthContext
- Conditions Risk
- Conditions RiskScore
- Conditions IdentityProvider
- Actions

Combined fields:
- Entry Type (Policy or Rule)

## MFA Enrollment Policies (Policies and Rules Combined)
Fields included for policy entries:
- ID
- Status
- Name
- Priority
- Conditions
- Settings

Fields included for rule entries:
- Policy ID
- Policy Name
- Rule ID
- Rule Name
- Status
- Priority
- Conditions People
- Conditions Network
- Conditions AuthContext
- Conditions Risk
- Conditions RiskScore
- Conditions IdentityProvider
- Actions

Combined fields:
- Entry Type (Policy or Rule)

## IDP Discovery Policies (Policies and Rules Combined)
Fields included for policy entries:
- Policy ID
- Policy Name
- Status
- Priority
- Description
- Conditions

Fields included for rule entries:
- Policy Name
- Rule ID
- Rule Name
- Status
- Priority
- Conditions
- Actions

Combined fields:
- Entry Type (Policy or Rule)

## Profile Enrollment Policies (Policies and Rules Combined)
Fields included for policy entries:
- Policy ID
- Policy Name
- Status
- Priority
- Description
- Conditions
- Settings

Fields included for rule entries:
- Policy Name
- Rule ID
- Rule Name
- Status
- Priority
- Conditions
- Actions

Combined fields:
- Entry Type (Policy or Rule)

## Brand Settings
- Brand Name
- Remove Powered By Okta
- Custom Privacy Policy URL
- Agree To Custom Privacy Policy
- Is Default
- Logo
- Favicon
- Background Image
- Primary Color Hex
- Primary Color Contrast Hex
- Secondary Color Hex
- Secondary Color Contrast Hex
- Sign-In Page Variant
- Error Page Variant
- Loading Page Variant
- Email Template Variant
- End User Dashboard Variant

## Brand Pages
- Brand Name
- Page Type
- Page Content
- Widget Version
- Widget Customizations

## Brand Email Templates
- Brand Name
- Template Name
- Subject
- Body

## Custom Admin Roles
- Role ID
- Label
- Description
- Is Cloneable
- Created
- Last Updated

## Resource Sets (Sets, Resources, and Bindings Combined)
Fields included for resource set entries:
- Label
- Description

Fields included for resource entries:
- Resource Set
- Resource Type
- Resource ID
- Resource Name

Fields included for binding entries:
- Resource Set
- Binding ID
- Binding Label
- Role

Combined fields:
- Entry Type (Resource Set, Resource, or Binding)

## Admin Assignments - Users
- User ID
- Display Name
- Email
- Login
- Admin Roles

## Admin Assignments - Groups
- Group ID
- Group Name
- Admin Roles

## Admin Assignments - Apps
- Client ID
- Display Name
- App Name
- App Instance ID

## API Tokens
- Token ID
- Name
- User ID
- Client Name
- Network
- Created
- Last Updated
- Expires At

## Realms
- Realm ID
- Name
- Description
- Status

## Realm Assignments
- Assignment ID
- Name
- Status
- Is Default
- Priority
- Domains
- Conditions
- Actions

## Profile Schema - User
- Attribute
- Title
- Type
- Required
- Mutability
- Scope
- Validation Type
- Settings

## Profile Mappings
- Mapping ID
- Source Name
- Target Name
- Properties

## Trusted Origins
- Origin ID
- Name
- Origin
- Status
- Scopes
