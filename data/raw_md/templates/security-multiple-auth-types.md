XAF has a built-in `PermissionPolicyUser` type for XPO and EF Core-based applications. Use it when an application employs only standard authentication or Windows Active Directory authentication.

When a user has multiple ways to log in, you need to store information for all authentication types and associate this information with the user. To do this, use the @DevExpress.ExpressApp.Security.ISecurityUserWithLoginInfo (a descendant of @DevExpress.ExpressApp.Security.ISecurityUser and `IOAuthSecurityUser`) and @DevExpress.ExpressApp.Security.ISecurityUserLoginInfo interfaces.

The Project Wizard generates classes that implement these interfaces automatically for projects created with v21.1 and later.
