---
uid: "404669"
title: 'Create a new Multi-Tenant Application'
seealso:
- linkId: "404670"
---

# Create a new Multi-Tenant Application

## Use XAF Application Builder to Create a New Application

In [Template Kit](xref:405447), select the **Multi-Tenant / SaaS-ready Application** option and proceed to create project.

![Template Kit - Multi-tenant Option](~/images/template-kit/template-kit-multi-tenant.png)

Note that not all application configurations support multi-tenancy. See [Limitations](xref:404436#best-practices-and-limitations) for more information.

>[!Tip]
> You can find the example of a multi-tenant application in our [Outlook Inspired Demo](xref:113577#net-winforms--blazor-outlook-inspired-demo-multi-tenancysaas-readyxref404669).

## Create and Initialize the Host Database

Follow the steps below to create and initialize the [Host Database](xref:404436#glossary).

If required, change the `ConnectionString` setting in the application configuration file (_appsettings.json_ in Blazor and _App.config_ in WinForms).

Run the application in _Debug_ mode and log in as _Admin_ with a blank password. The framework executes the following tasks:

- Creates the Host Database.
- Creates the [Super Administrator](xref:404436#glossary) user with the login `"Admin"` and a blank password.
- Switches the application to Host UI mode.

XAF [Template Kit](xref:405447) generates [Module Updater](xref:DevExpress.ExpressApp.Updating.ModuleUpdater) code that creates an Admin user with a blank password. For security reasons, this user is not available if the application is compiled in _Release_ configuration.

After you log in to the Host UI for the first time, we recommend that you change the Super Administrator's password. You can also create additional Super Administrator accounts. These accounts must be assigned the  _Administrators_ role.

![Change Password](~/images/create-multitenant-app-change-password.png)

## Create and Initialize Tenants

Follow the steps below to create a new tenant (named `"company1.com"` in this example).

In the Host UI, switch to the _Tenants_ List View and add a new Tenant record. Specify the tenant name and a connection string for a new [Tenant Database](xref:404436#glossary).

![Add Tenant](~/images/create-multitenant-app-add-tenant.png)

Log out from the Host UI and log in as the new tenant's administrator (`"admin@company1.com"`) with a blank password. The framework executes the following tasks:

- Creates a database for tenant _company1.com_.
- In this database, creates the following two users: `"admin@company1.com"` with the _Administrators_ role and `"user@company1.com"` with the _Users_ role.

![New Tenant](~/images/create-multitenant-app-new-tenant.png)

Take the following additional considerations into account:

- Ensure that none of the tenants share their databases with other tenants. A Tenant Database must also never be the same as the Host Database.
- An application does not immediately create a Tenant Database when the tenant is created. Instead, the database is created when a user logs in to this tenant for the first time.
- A tenant name must be unique.
- XAF Template Kit generates [Module Updater](xref:DevExpress.ExpressApp.Updating.ModuleUpdater) code that creates the Admin@_tenant\_name_ and Usern@_tenant\_name_ users with blank passwords. For security reasons, these users are not available if the application is compiled in _Release_ configuration.
- After the first login to the Tenant User Interface, it is recommended that you change passwords for all automatically created users.

## Create Tenant Users and Manage Access Permissions

Tenant users and their access permissions are managed in the [Tennant User Interface](xref:404436#glossary) independently from other tenants and from the Host User Interface. Each tenant has its own independent list of users, roles, and security permissions.

To create a new Tenant User in a _company1.com_ tenant, you need to:

1. Log in with a tenant administrator account (`admin@company1.com`).
2. Create a user with the standard user editing interface (the same as in a single-tenant XAF application).

![Create Users](~/images/create-multitenant-app-create-user.png)

When you create tenant users, we recommend that you pay special attention to how you specify user logins. For example, if you use [`TenantByEmailResolver`](xreF:404667#tenantbyemailresolver) or a [`TenantByUserNameResolver`](xref:404667#tenantbyusernameresolver) descendant to determine user tenants, a user's login must be specified in accordance with the exact name and format of their tenant. Otherwise, the system will not be able to identify the tenant on the user's login attempt, which will make the user unable to log in.